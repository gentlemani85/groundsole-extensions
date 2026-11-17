---
name: office-inspector
description: Schnelles, deterministisches Auslesen und Prüfen von Office-Dateien (Word .docx, Excel .xlsx, PDF, CSV, TXT) ohne Token-Overhead. Läuft dezentral und plattformunabhängig auf macOS, Windows und Linux.
---

# Office Inspector - Skill

Dieser Skill ermöglicht das blitzschnelle Einlesen, Scannen und Prüfen von Office-Dokumenten (Word, Excel, PDF) ohne zeitraubende Multi-Turn-Erkundungen oder Halluzinationen.

## 🚀 Dezentrale Ausführung (Plattformunabhängig)

Das Skript liegt direkt innerhalb dieses Skills unter `scripts/inspect_office.py`.

### 1. Ausführung ermitteln
Führe das Skript immer mit dem aktuell aktiven Python-Interpreter der Umgebung aus (z. B. im lokalen venv oder systemweit):

```bash
# macOS / Linux:
python3 scripts/inspect_office.py [BEFEHL]

# Windows (PowerShell / CMD):
python scripts\inspect_office.py [BEFEHL]
```
*(Hinweis: Befindet sich der Agent in einem anderen Arbeitsverzeichnis, kann der Pfad zum Skill relativ oder über `~/.agents/skills/office-inspector/scripts/inspect_office.py` bzw. `%USERPROFILE%\.agents\skills\office-inspector\scripts\inspect_office.py` referenziert werden).* <!-- pfad-check: ok -->

---

### 2. Die Befehle im Überblick

#### A. Gesamtüberblick über einen Ordner (1 Schritt)
Scannt alle Word-, Excel-, PDF- und Textdateien rekursiv und liefert Dateinamen, Tabellenblätter und Textausschnitte:
```bash
python3 scripts/inspect_office.py scan [ORDNER_PFAD]
```

#### B. Gezieltes Einlesen einer Datei
Gibt Word-Dokumente (.docx), Excel-Tabellen (.xlsx) oder PDFs als sauberen Text bzw. Markdown-Tabelle aus:
```bash
# Word (.docx)
python3 scripts/inspect_office.py read "pfad/zu/dokument.docx"

# Excel (.xlsx)
python3 scripts/inspect_office.py read "pfad/zu/tabelle.xlsx"

# Bestimmtes Tabellenblatt
python3 scripts/inspect_office.py read "pfad/zu/tabelle.xlsx" --sheet "Eingangsrechnungen"
```

#### C. Buchhaltungs- & Rechnungs-Audit (Sofort-Prüfung)
Prüft alle Excel-Dateien im Ordner automatisch auf doppelte Belegnummern, fehlerhafte Steuerangaben (0% USt), Dummy-IBANs und unfertige Entwürfe:
```bash
python3 scripts/inspect_office.py audit [ORDNER_PFAD]
```

---

## ⚙️ Technische Plattform-Architektur (Zero-Lock-in)

- **Word (.docx):**
  - **macOS:** Nutzt automatisch das native Apple-Systemtool `textutil` (ultraschnell im RAM, ~0,02 s Latenz).
  - **Windows & Linux:** Fallback auf `python-docx` (falls installiert) bzw. direkter Fallback auf reines **Python Standard-Library XML-Parsing** (`zipfile` + `xml.etree`). Funktioniert somit auf jedem Windows-PC komplett ohne zusätzliche pip-Pakete!
- **Excel (.xlsx):**
  - Nutzt `openpyxl` mit `data_only=True`, um berechnete Werte statt roher Formeln zu erhalten.
- **Bearbeiten von Excel/Word:**
  - Niemals string-basierte Edit-Tools (wie find/replace) auf `.docx` oder `.xlsx` anwenden, da dies das komprimierte ZIP-XML-Format beschädigt. Änderungen immer programmatisch über `openpyxl` mit anschließendem `wb.save()` durchführen.
