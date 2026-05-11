---
schema_version: 1
id: 189-html-escape
revision: 1
titel: HTML-Sonderzeichen escapen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, html, sicherheit, replace]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Web-Sicherheits-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: html_escape
hints:
  - kosten: 0
    text: |
      Ersetze die HTML-Sonderzeichen so, dass beliebiger Text sicher
      in HTML eingebettet werden kann:
      &  →  &amp;        muss als ERSTES ersetzt werden!
      <  →  &lt;
      >  →  &gt;
      "  →  &quot;
      '  →  &#39;
  - kosten: 8
    text: |
      Wichtig: & zuerst ersetzen, sonst wird "&lt;" zu "&amp;lt;".
      Reihenfolge der replace-Aufrufe ist sicherheitsrelevant.
tests_sichtbar:
  - input: [""]
    expected: ""
  - input: ["Hallo Welt"]
    expected: "Hallo Welt"
  - input: ["<b>fett</b>"]
    expected: "&lt;b&gt;fett&lt;/b&gt;"
  - input: ["a & b"]
    expected: "a &amp; b"
tests_versteckt:
  - input: ["\"hi\""]
    expected: "&quot;hi&quot;"
  - input: ["it's"]
    expected: "it&#39;s"
  - input: ["1 < 2 && 2 > 1"]
    expected: "1 &lt; 2 &amp;&amp; 2 &gt; 1"
  - input: ["<script>alert(1)</script>"]
    expected: "&lt;script&gt;alert(1)&lt;/script&gt;"
  - input: ["&amp;"]
    expected: "&amp;amp;"
  - input: ["<a href=\"x\">y</a>"]
    expected: "&lt;a href=&quot;x&quot;&gt;y&lt;/a&gt;"
starter_code: |
  def html_escape(s: str) -> str:
      # Deine Lösung hier -- & zuerst!
      pass
---

# HTML-Sonderzeichen escapen

Schreibe `html_escape(s)`, die einen String so umwandelt, dass er
**sicher in HTML eingebettet** werden kann -- ohne dass enthaltene
Sonderzeichen als HTML interpretiert werden.

## Ersetzungs-Tabelle

| Original | Escape   |
|----------|----------|
| `&`      | `&amp;`  |
| `<`      | `&lt;`   |
| `>`      | `&gt;`   |
| `"`      | `&quot;` |
| `'`      | `&#39;`  |

**Wichtig**: `&` muss **zuerst** ersetzt werden, sonst wird `&lt;`
zu `&amp;lt;`.

## Beispiele

| Eingabe                    | Escaped                                         |
|----------------------------|-------------------------------------------------|
| `"Hallo Welt"`             | `"Hallo Welt"`                                  |
| `"<b>fett</b>"`            | `"&lt;b&gt;fett&lt;/b&gt;"`                     |
| `"a & b"`                  | `"a &amp; b"`                                   |
| `"<script>alert(1)</script>"` | `"&lt;script&gt;alert(1)&lt;/script&gt;"`    |

## Sicherheitskontext -- XSS

Diese Funktion ist die Grundlage zur Verhinderung von **XSS**
(Cross-Site Scripting) -- der häufigsten Webschwachstelle bis heute.
Wer User-Eingaben unescaped ins HTML rendert, öffnet Angreifern
die Tür für `<script>`-Injection.

In Python gibt's `html.escape` aus der Standard-Library, das genau
das tut. Aber es lohnt zu verstehen, **was** dahinter passiert.
