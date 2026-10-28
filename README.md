# Groundsole Extensions

> **Curated & Proven Community Skills for the Groundsole Personal AI Coprocessor.**

This repository contains modular, application-level extensions and specialized tools that extend the core [Groundsole](https://github.com/gentlemani85/groundsole) framework.

---

## 📦 Included Extensions

| Extension / Skill | Description | Requirements |
| :--- | :--- | :--- |
| **`document-export`** | Generates formatted Microsoft Word (`.docx`) documents and print-ready PDFs from Markdown notes. | Headless Chrome / Pandoc |
| **`presentation-deck`** | Self-contained, interactive 16:9 HTML presentations with Markdown SSOT and live keyboard navigation. | Modern Browser |
| **`space-sync`** | Autonomous cognitive hub synchronizer for shared local folders (extracts facts from incoming PDFs/spreadsheets). | None (Plaintext / Python) |
| **`mail-manager`** | Checks incoming emails and drafts/sends messages via standard IMAP/SMTP (Gmail, Outlook). | Python IMAP/SMTP |
| **`youtube-transcript`** | Deterministically fetches and analyzes full transcripts from YouTube URLs via local CLI. | YouTube API / yt-dlp |

---

## 🚀 How to Install an Extension

To install an extension into your Groundsole workspace (e.g. `presentation-deck`):

```bash
# In your workspace root:
mkdir -p .agents/skills/presentation-deck
cp -R path/to/groundsole-extensions/skills/presentation-deck/* .agents/skills/presentation-deck/
```

Or simply prompt your Groundsole coprocessor:
> *"Install the `presentation-deck` extension from https://github.com/gentlemani85/groundsole-extensions."*

---

## 📄 License

MIT License (c) 2026 Emanuel Gössler.
