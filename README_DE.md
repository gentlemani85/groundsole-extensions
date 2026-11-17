# Groundsole Extensions (Deutsch)

> **Kuratierte Erweiterungen & bewährte Open-Source-Werkzeuge für den persönlichen KI-Koprozessor Groundsole.**
> 🇬🇧 [English Version (README.md)](./README.md)

Dieses Repository sammelt modulare Erweiterungen für das [Groundsole](https://github.com/gentlemani85/groundsole)-Framework. Es enthält sowohl eigene Skills als auch direkte Verweise auf bewährte Open-Source-Projekte auf GitHub – immer mit einer verständlichen Erklärung für Nicht-Techniker.

---

## 📦 Eigene Erweiterungen (Groundsole Skills)

| Erweiterung / Skill | Beschreibung | Voraussetzungen |
| :--- | :--- | :--- |
| **`document-export`** | Erstellt formatierte Microsoft-Word-Dokumente (`.docx`) und druckfertige PDFs aus Markdown-Notizen. | Headless Chrome / Pandoc |
| **`presentation-deck`** | Eigenständige, interaktive 16:9-HTML-Präsentationen mit Markdown als zentraler Quelle und Tastatur-Steuerung. | Moderner Browser |
| **`space-sync`** | Synchronisiert geteilte lokale Ordner automatisch und übernimmt Fakten aus PDFs und Tabellen ins Gedächtnis. | Keine (Plaintext / Python) |
| **`mail-manager`** | Prüft eingehende E-Mails und entwirft oder sendet Nachrichten über IMAP/SMTP (Gmail, Outlook usw.). | Python IMAP/SMTP |
| **`youtube-transcript`** | Lädt vollständige Transkripte von YouTube-Videos deterministisch über die lokale Kommandozeile. | YouTube API / yt-dlp |

---

## 🌐 Kuratierte externe Projekte (Verweise auf Originale)

Groundsole Extensions baut nicht alles neu, sondern verweist gezielt auf bewährte GitHub-Projekte im Original – jeweils mit einer Erklärung in Alltagssprache:

| Projekt | Original-Quelle | Wie es funktioniert (für Nicht-Techniker) | Beschreibung |
| :--- | :--- | :--- | :--- |
| **`agent-browser`** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Ein ferngesteuerter Webbrowser für den KI-Assistenten. Statt bei jedem Klick ein teures Bildschirmfoto an die KI zu schicken, liest das Werkzeug die Seite wie ein übersichtliches Inhaltsverzeichnis aller sichtbaren Knöpfe und Eingabefelder (`@e1`, `@e2`, …) und klickt oder tippt dort direkt. | [Anleitung & Erklärung](./curated/agent-browser.md) |

---

## 🚀 Erweiterung installieren

Um einen eigenen Skill in deinen Groundsole-Arbeitsbereich zu übernehmen (z. B. `presentation-deck`), gib deinem KI-Koprozessor einfach folgende Anweisung:
> *„Installiere die Erweiterung `presentation-deck` aus https://github.com/gentlemani85/groundsole-extensions.“*

Bei **kuratierten externen Projekten** wird direkt das Original-Projekt von GitHub installiert (siehe jeweilige Beschreibung unter `curated/`).

---

## 📄 Lizenz

MIT License (c) 2026 Emanuel Gössler.
