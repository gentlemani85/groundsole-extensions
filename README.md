# Groundsole Extensions

> **Curated & Proven Community Skills for the Groundsole Personal AI Coprocessor.**
> 🇩🇪 [Deutsche Version (README_DE.md)](./README_DE.md)

This repository contains modular, application-level extensions and curated references to proven open-source projects that extend the core [Groundsole](https://github.com/gentlemani85/groundsole) framework.

---

## 📦 Included Extensions (Built for Groundsole)

| Extension / Skill | Description | Requirements |
| :--- | :--- | :--- |
| **`document-export`** | Generates formatted Microsoft Word (`.docx`) documents and print-ready PDFs from Markdown notes. | Headless Chrome / Pandoc |
| **`presentation-deck`** | Self-contained, interactive 16:9 HTML presentations with Markdown SSOT and live keyboard navigation. | Modern Browser |
| **`space-sync`** | Autonomous cognitive hub synchronizer for shared local folders (extracts facts from incoming PDFs/spreadsheets). | None (Plaintext / Python) |
| **`mail-manager`** | Checks incoming emails and drafts/sends messages via standard IMAP/SMTP (Gmail, Outlook). | Python IMAP/SMTP |
| **`youtube-transcript`** | Deterministically fetches and analyzes full transcripts from YouTube URLs via local CLI. | YouTube API / yt-dlp |

---

## 🌐 Curated External Projects (Proven Open-Source Tools)

Groundsole Extensions does not reinvent everything from scratch. Alongside our own skills, we curate proven open-source GitHub projects by linking directly to the original repository and explaining in plain, non-technical language how they work.

| Project | Original Source | How It Works (Plain Language) | Guide |
| :--- | :--- | :--- | :--- |
| **`agent-browser`** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | A remote-controlled web browser for AI assistants. Instead of taking heavy screenshots at every step, it reads a page like a clean list of buttons and input fields (`@e1`, `@e2`, …) and clicks or types directly—making web tasks, form tests, and software manuals fast and cheap. | [Non-Technical Guide](./curated/agent-browser.md) |

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
