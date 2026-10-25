---
schema_version: 1
id: c160-form-group
revision: 3
titel: "Form: Label + Input-Gruppe"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [form, label, flex-column, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="gruppe"><label class="lab">E-Mail</label><input class="inp" placeholder="dein@beispiel.de"></div>
ziel_css: |
  .gruppe {
    display: flex;
    flex-direction: column;
    gap: 6px;
    width: 280px;
  }
  .lab {
    color: #9ca3af;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .inp {
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
  }
hints:
  - kosten: 0
    text: |
      Gruppe als flex-column mit gap 6px. Label klein und uppercase über Input.
starter_code: |
  .gruppe {
    /* ... */
  }
  .lab {
    /* ... */
  }
  .inp {
    /* ... */
  }
---

# Form: Label + Input-Gruppe

Label über Input, vertikal gestapelt mit kleinem Abstand.
