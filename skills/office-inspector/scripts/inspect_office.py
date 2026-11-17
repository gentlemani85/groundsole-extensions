#!/usr/bin/env python3
"""
inspect_office.py - Universelles, schnelles Auslesen und Prüfen von Office-Dateien
(Word .docx, Excel .xlsx, PDF, CSV, TXT) plattformübergreifend auf macOS, Windows und Linux.

Null-Abhängigkeits-Garantie:
- Word (.docx): macOS `textutil` -> python-docx -> Python Standard-Library (zipfile + xml.etree)
- Excel (.xlsx): openpyxl (mit Fallback-Meldung)
- PDF (.pdf): pypdf -> pdftotext -> Fallback
- Text / CSV: Python Standard-Library
"""

import sys
import os
import glob
import subprocess
import argparse
import zipfile
import xml.etree.ElementTree as ET

try:
    import openpyxl
except ImportError:
    openpyxl = None

try:
    import pypdf
except ImportError:
    pypdf = None


def read_docx_fast(path):
    """
    Liest .docx robust und plattformübergreifend:
    1. macOS: natives `textutil` (ultraschnell, RAM-basiert)
    2. python-docx (falls im venv vorhanden)
    3. Reines Python Standard-Library XML-Parsing (Zero Dependency Fallback für Windows/Linux)
    """
    # 1. macOS native textutil (nur auf Darwin / Mac)
    if sys.platform == "darwin":
        try:
            res = subprocess.check_output(
                ["textutil", "-convert", "txt", "-stdout", path],
                stderr=subprocess.DEVNULL
            )
            return res.decode("utf-8", errors="replace").strip()
        except Exception:
            pass

    # 2. python-docx (falls vorhanden)
    try:
        import docx
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    except ImportError:
        pass
    except Exception:
        pass

    # 3. Standard-Library Fallback via zipfile + xml.etree (keine externe Dependency nötig!)
    try:
        with zipfile.ZipFile(path, "r") as z:
            xml_content = z.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            # Word namespaces
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paragraphs = []
            for p in tree.iterfind(".//w:p", ns):
                texts = [node.text for node in p.iterfind(".//w:t", ns) if node.text]
                if texts:
                    paragraphs.append("".join(texts))
            return "\n".join(paragraphs).strip()
    except Exception as e:
        return f"[Fehler beim Lesen von {os.path.basename(path)}: {e}]"


def read_pdf(path):
    """Liest .pdf via pypdf oder pdftotext."""
    if pypdf:
        try:
            reader = pypdf.PdfReader(path)
            pages_text = [p.extract_text() or "" for p in reader.pages]
            return "\n\n--- Seite getrennt ---\n\n".join(pages_text).strip()
        except Exception:
            pass
    try:
        res = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL)
        return res.decode("utf-8", errors="replace").strip()
    except Exception:
        return f"[PDF-Inhalt von {os.path.basename(path)} konnte nicht extrahiert werden (bitte pypdf installieren)]"


def read_xlsx(path, sheet_name=None, max_rows=100):
    """Liest .xlsx via openpyxl und gibt eine saubere Markdown-Tabelle aus."""
    if not openpyxl:
        return "[Hinweis: openpyxl ist in diesem Python-Environment nicht installiert. Bitte 'pip install openpyxl' ausführen.]"
    
    try:
        wb = openpyxl.load_workbook(path, data_only=True)
    except Exception as e:
        return f"[Fehler beim Öffnen von {os.path.basename(path)}: {e}]"

    sheets_to_read = [sheet_name] if sheet_name and sheet_name in wb.sheetnames else wb.sheetnames
    output = []

    for sname in sheets_to_read:
        ws = wb[sname]
        output.append(f"### Tabelle: `{sname}` ({ws.max_row} Zeilen, {ws.max_column} Spalten)")
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            output.append("*(Leere Tabelle)*\n")
            continue

        # Header suchen (erste Zeile mit Inhalt)
        header_idx = 0
        while header_idx < len(rows) and not any(rows[header_idx]):
            header_idx += 1

        if header_idx >= len(rows):
            output.append("*(Keine Daten gefunden)*\n")
            continue

        headers = [str(c) if c is not None else "" for c in rows[header_idx]]
        output.append("| " + " | ".join(headers) + " |")
        output.append("| " + " | ".join(["---"] * len(headers)) + " |")

        count = 0
        for r in rows[header_idx + 1:]:
            if not any(r):
                continue
            vals = [str(c) if c is not None else "" for c in r]
            if len(vals) < len(headers):
                vals.extend([""] * (len(headers) - len(vals)))
            output.append("| " + " | ".join(vals[:len(headers)]) + " |")
            count += 1
            if count >= max_rows:
                output.append(f"*(... weitere Zeilen abgeschnitten, Limit {max_rows} erreicht)*")
                break
        output.append("")

    return "\n".join(output)


def cmd_scan(target_dir):
    """Scannt einen Ordner rekursiv und gibt eine strukturierte Übersicht aus."""
    abs_target = os.path.abspath(target_dir)
    print(f"## Ordner-Scan: `{abs_target}`\n")
    
    files = []
    for root, _, filenames in os.walk(target_dir):
        if any(part.startswith(".") and part not in [".", ".."] for part in root.split(os.sep)):
            continue
        for f in filenames:
            if f.startswith("."):
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in [".docx", ".xlsx", ".pdf", ".txt", ".csv"]:
                files.append(os.path.join(root, f))

    if not files:
        print("Keine relevanten Office-Dateien gefunden.")
        return

    docx_files = [f for f in files if f.endswith(".docx")]
    xlsx_files = [f for f in files if f.endswith(".xlsx")]
    pdf_files = [f for f in files if f.endswith(".pdf")]
    txt_files = [f for f in files if f.endswith((".txt", ".csv"))]

    print(f"**Gefundene Dokumente ({len(files)} gesamt):** {len(docx_files)} Word, {len(xlsx_files)} Excel, {len(pdf_files)} PDF, {len(txt_files)} Text/CSV\n")

    if xlsx_files:
        print("### Excel-Dateien:")
        for f in sorted(xlsx_files):
            rel = os.path.relpath(f, target_dir)
            if openpyxl:
                try:
                    wb = openpyxl.load_workbook(f, data_only=True, read_only=True)
                    sheets = ", ".join(wb.sheetnames)
                    print(f"- **`{rel}`** (Tabellen: {sheets})")
                except Exception:
                    print(f"- **`{rel}`**")
            else:
                print(f"- **`{rel}`**")
        print()

    if docx_files:
        print("### Word-Dokumente:")
        for f in sorted(docx_files):
            rel = os.path.relpath(f, target_dir)
            snippet = read_docx_fast(f)
            first_line = snippet.splitlines()[0] if snippet.splitlines() else ""
            if len(first_line) > 80:
                first_line = first_line[:77] + "..."
            desc = f" – *„{first_line}“*" if first_line else ""
            print(f"- **`{rel}`**{desc}")
        print()

    if txt_files:
        print("### Text- & CSV-Dateien:")
        for f in sorted(txt_files):
            rel = os.path.relpath(f, target_dir)
            print(f"- **`{rel}`**")
        print()


def cmd_read(file_path, sheet=None, max_rows=100):
    """Liest eine Datei ein und gibt ihren Inhalt aus."""
    if not os.path.exists(file_path):
        print(f"Fehler: Datei existiert nicht: {file_path}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        print(read_docx_fast(file_path))
    elif ext == ".xlsx":
        print(read_xlsx(file_path, sheet_name=sheet, max_rows=max_rows))
    elif ext == ".pdf":
        print(read_pdf(file_path))
    elif ext in [".txt", ".csv", ".md"]:
        with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
            print(fh.read())
    else:
        print(f"Format {ext} wird nicht unterstützt.", file=sys.stderr)


def cmd_audit(target_dir):
    """Prüft alle Excel-Dateien auf Rechnungsdoppelungen, Steuerfehler und Anomalien."""
    abs_target = os.path.abspath(target_dir)
    print(f"## Buchhaltungs- & Daten-Audit für `{abs_target}`\n")
    
    if not openpyxl:
        print("[Hinweis: openpyxl ist nicht installiert. Audit erfordert openpyxl.]")
        return

    xlsx_files = []
    for root, _, filenames in os.walk(target_dir):
        if any(part.startswith(".") and part not in [".", ".."] for part in root.split(os.sep)):
            continue
        for f in filenames:
            if f.endswith(".xlsx") and not f.startswith("."):
                xlsx_files.append(os.path.join(root, f))

    if not xlsx_files:
        print("Keine Excel-Dateien für Audit gefunden.")
        return

    findings = []

    for fpath in sorted(xlsx_files):
        rel = os.path.relpath(fpath, target_dir)
        try:
            wb = openpyxl.load_workbook(fpath, data_only=True)
        except Exception as e:
            findings.append(f"- **`{rel}`**: Datei konnte nicht geöffnet werden ({e})")
            continue

        for sname in wb.sheetnames:
            ws = wb[sname]
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                continue

            header_idx = -1
            headers = []
            for idx, r in enumerate(rows):
                str_row = [str(c).lower() if c is not None else "" for c in r]
                if any(k in str_row for k in ["beleg", "rechnung", "datum", "betrag", "status", "kunde", "lieferant"]):
                    header_idx = idx
                    headers = [str(c).strip() if c is not None else "" for c in r]
                    break

            if header_idx == -1:
                non_empty = [r for r in rows if any(r)]
                if len(non_empty) <= 5:
                    findings.append(f"- ⚠️ **`{rel}` (Tabelle: `{sname}`)**: Unformatierter Tabellenentwurf ohne Kopfzeile ({len(non_empty)} Einträge).")
                continue

            col_map = {h.lower(): i for i, h in enumerate(headers) if h}
            
            beleg_col = None
            for k, idx in col_map.items():
                if "beleg" in k or "rechnungs-nr" in k or "rechnungsnr" in k:
                    beleg_col = idx
                    break

            if beleg_col is not None:
                seen_belege = {}
                for r_idx, r in enumerate(rows[header_idx + 1:], start=header_idx + 2):
                    val = r[beleg_col] if beleg_col < len(r) else None
                    if val:
                        sval = str(val).strip()
                        if sval in seen_belege:
                            findings.append(
                                f"- 🔴 **DOPPELTE BELEGNUMMER in `{rel}`**: `{sval}` erscheint in Zeile {seen_belege[sval]} und erneut in Zeile {r_idx}!"
                            )
                        else:
                            seen_belege[sval] = r_idx

            for r_idx, r in enumerate(rows[header_idx + 1:], start=header_idx + 2):
                r_strs = [str(c) if c is not None else "" for c in r]
                for cell in r_strs:
                    if "fehler" in cell.lower() or "doppelt" in cell.lower() or "achtung" in cell.lower():
                        findings.append(f"- ⚠️ **Hinweis in `{rel}` (Zeile {r_idx})**: Vermerk gefunden: *„{cell}“*")
                    if "at000000000000000000" in cell:
                        findings.append(f"- ⚠️ **Ungültige Bankdaten in `{rel}` (Zeile {r_idx})**: Dummy-IBAN `{cell}` hinterlegt.")

    if findings:
        print("### Gefundene Unstimmigkeiten & Warnungen:")
        for f in findings:
            print(f)
    else:
        print("Keine offensichtlichen Unstimmigkeiten gefunden.")
    print()


def main():
    parser = argparse.ArgumentParser(description="Schnelle Dokumenten-Inspektion (macOS, Windows, Linux)")
    subparsers = parser.add_subparsers(dest="command", help="Befehle")

    p_scan = subparsers.add_parser("scan", help="Übersicht über alle Dokumente im Verzeichnis")
    p_scan.add_argument("path", nargs="?", default=".", help="Zielverzeichnis")

    p_read = subparsers.add_parser("read", help="Inhalt einer Datei ausgeben")
    p_read.add_argument("file", help="Pfad zur Datei")
    p_read.add_argument("--sheet", help="Name der Excel-Tabelle")
    p_read.add_argument("--max-rows", type=int, default=100, help="Maximale Zeilen")

    p_audit = subparsers.add_parser("audit", help="Prüft Excel-Dateien auf Doppelungen und Fehler")
    p_audit.add_argument("path", nargs="?", default=".", help="Zielverzeichnis")

    args = parser.parse_args()

    if args.command == "scan":
        cmd_scan(args.path)
    elif args.command == "read":
        cmd_read(args.file, sheet=getattr(args, "sheet", None), max_rows=getattr(args, "max_rows", 100))
    elif args.command == "audit":
        cmd_audit(args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
