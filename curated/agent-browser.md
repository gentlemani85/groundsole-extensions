# `agent-browser` (Vercel Labs)

- **Original-Projekt / Source:** [https://github.com/vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- **Lizenz / License:** Apache-2.0 (Original-Repository, keine Kopie in Groundsole)

---

## 🇩🇪 Wie das funktioniert (für Nicht-Techniker)

Stell dir vor, du möchtest, dass dein KI-Assistent eine Website liest, ein Kontaktformular ausfüllt oder Schritt für Schritt ein Handbuch für eine Web-Software erstellt.

Bei vielen bekannten Cloud-Lösungen (wie etwa dem Browser-Modus von ChatGPT) macht die KI bei jedem einzelnen Schritt ein komplettes Bildschirmfoto, schickt das Bild an ein teures Bild-Erkennungsmodell und rät dann, wo sie hinklicken muss. Das dauert lange und verbraucht das Tageskontingent extrem schnell.

**`agent-browser` löst das anders:**
1. **Eigener Test-Browser im Hintergrund:** Das Werkzeug öffnet auf deinem Rechner einen separaten, sauberen Chrome-Browser. Dein normaler Browser mit deinen privaten Passwörtern bleibt davon unberührt.
2. **Inhaltsverzeichnis statt Bildschirmfoto:** Statt ein schweres Bild zu übertragen, fragt `agent-browser` die geöffnete Webseite nach ihrem eingebauten „Inhaltsverzeichnis“ (der sogenannten Bedienstruktur). Die KI bekommt dadurch nur wenige Zeilen Text zurück – zum Beispiel: *„Knopf: Erstgespräch anfordern (`@e14`), Eingabefeld: Ihr Name (`@e30`)“*.
3. **Gezielte Steuerung:** Die KI sagt dem Browser einfach *„Schreibe den Namen in `@e30` und klicke auf `@e14`“*. Danach prüft sie wieder per Textliste, was sich auf der Seite geändert hat (z. B. ob *„Angekommen!“* erscheint).
4. **Screenshots nur auf Wunsch:** Ein echtes Bildschirmfoto wird nur dann gemacht, wenn du es ausdrücklich für ein Handbuch oder eine visuelle Kontrolle brauchst.

### Wofür es im Alltag besonders nützlich ist
- **Webseiten & Formulare testen:** Automatisch prüfen, ob Buttons, Links und Kontaktformulare auf der eigenen Seite funktionieren.
- **Software-Handbücher erstellen:** Sich durch eine Web-App klicken, die echten Button-Namen und Feldbezeichnungen exakt auslesen und an den wichtigen Stellen nummerierte Screenshots für ein Handbuch speichern.
- **Recherchen auf dynamischen Seiten:** Inhalte von modernen Webseiten einlesen, die erst nach dem Laden oder nach einem Klick sichtbar werden.

### Einrichtung (durch deinen KI-Koprozessor)
Da Groundsole Extensions nur auf das Original verweist, installierst du `agent-browser` direkt aus der offiziellen Quelle – oder sagst deinem KI-Koprozessor einfach:
> *„Installiere `https://github.com/vercel-labs/agent-browser` lokal und binde es als MCP-Server ein.“*

---

## 🇬🇧 How It Works (Plain Language)

Many cloud browser agents take a full-page screenshot at every single step and send it to a vision model to guess where to click. That is slow and burns through daily token limits very quickly.

**`agent-browser` works differently:**
1. **A clean background browser:** It runs a separate, clean Chrome instance on your machine, leaving your personal browser and logins untouched.
2. **A text outline instead of heavy images:** Instead of sending screenshots back and forth, `agent-browser` reads the page's built-in structure and hands the AI a compact list of visible buttons, links, and fields (`@e1`, `@e2`, …).
3. **Direct, fast actions:** The AI simply tells the browser *"type this into `@e30` and click `@e33`"* and reads the updated outline in seconds.
4. **Screenshots only when needed:** Visual screenshots are only captured when you explicitly need them (for example, to illustrate a step-by-step user manual).

### Installation
Install directly from the official upstream project ([vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)):
```bash
npm install -g agent-browser
agent-browser install
```
Or ask your Groundsole coprocessor to install and register `agent-browser` as an MCP server.
