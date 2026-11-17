# Genesis: office-inspector

- **Erstellt am:** 2026-10-30 (Plattformunabhängig erweitert: 2026-11-04)
- **Autor / Ersteller:** Emanuel Gössler
- **Geltungsbereich:** Dezentral (macOS, Windows, Linux) – Kanzleien, Gemeinden & ISN Praxis

---

## 1. Auslösender Schmerz & Reales Problem
Das Einlesen von Word (.docx), Excel (.xlsx) und PDF erzeugte in KI-Agenten (Goose, Hermes, Antigravity) oft enorme Token-Kosten, Fehlversuche und formatierte Tabellen unlesbar.

---

## 2. Kern-Mechanik & Plattformunabhängigkeit
- **macOS:** Ultraschnelles Auslesen via nativem `textutil`.
- **Windows & Linux:** Zero-Dependency XML-Extraktion (`zipfile` + `xml.etree`) für `.docx` sowie `openpyxl` / `pypdf`.
- **Kapselung:** Skripte liegen autark im Skill (`scripts/inspect_office.py`), keine fest verdrahteten absoluten Pfade auf Nutzer-Homeverzeichnisse.

---

## 3. Ausmusterungs-Kriterium (Sunset Rule)
Dauerhafter Ingestion-Standard für Office-Dateien im dezentralen Groundsole-Ökosystem.
