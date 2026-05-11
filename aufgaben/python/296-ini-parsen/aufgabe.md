---
schema_version: 1
id: 296-ini-parsen
revision: 1
titel: INI-Datei zu verschachteltem Dict
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [strings, parsing, ini, dict]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Konfig-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ini_parse
hints:
  - kosten: 0
    text: |
      Parse einen INI-String zu Dict {sektion: {key: value}}.
      Sektionen: [name]. Eintraege: key=value (mit/ohne Whitespace).
      Leere Zeilen und Zeilen die mit ; oder # anfangen IGNORIEREN.
      Keys/Values werden gestrippt. Eintraege ohne aktive Sektion → ignorieren.
  - kosten: 25
    text: |
      Zeile fuer Zeile durchgehen, Sektion merken,
      Key/Value bei "=" splitten und strippen.
tests_sichtbar:
  - input: ["[a]\nx=1\ny=2"]
    expected: {"a": {"x": "1", "y": "2"}}
  - input: [""]
    expected: {}
  - input: ["[s]\nk=v"]
    expected: {"s": {"k": "v"}}
  - input: ["[a]\n[b]"]
    expected: {"a": {}, "b": {}}
tests_versteckt:
  - input: ["[server]\nhost=localhost\nport=8080"]
    expected: {"server": {"host": "localhost", "port": "8080"}}
  - input: ["[a]\nx = 1\n[b]\ny = 2"]
    expected: {"a": {"x": "1"}, "b": {"y": "2"}}
  - input: ["; comment\n[s]\n# auch comment\nk=v"]
    expected: {"s": {"k": "v"}}
  - input: ["k=v"]
    expected: {}
  - input: ["[s]\nleer=\nklasse=test"]
    expected: {"s": {"leer": "", "klasse": "test"}}
  - input: ["[db]\nhost=db.example\nuser=admin\npass=secret\n[cache]\nttl=300"]
    expected: {"db": {"host": "db.example", "user": "admin", "pass": "secret"}, "cache": {"ttl": "300"}}
starter_code: |
  def ini_parse(s: str) -> dict:
      # Deine Lösung hier -- per Hand parsen
      pass
---

# INI-Datei zu verschachteltem Dict

Schreibe `ini_parse(s)`, die einen INI-String in ein verschachteltes
Dict `{sektion: {key: value}}` umwandelt.

INI-Format:
- **Sektionen**: `[name]` -- alle folgenden Eintraege gehoeren zur Sektion
- **Eintraege**: `key=value` -- Whitespace um `=` wird ignoriert
- **Kommentare**: Zeilen die mit `;` oder `#` anfangen werden uebersprungen
- **Leere Zeilen** werden uebersprungen
- **Eintraege vor der ersten Sektion** werden ignoriert

## Beispiele

```ini
[server]
host=localhost
port=8080

[db]
host=db.example
user=admin
```

→ `{"server": {"host": "localhost", "port": "8080"}, "db": {"host": "db.example", "user": "admin"}}`

| Eingabe                              | Ergebnis                                    |
|--------------------------------------|----------------------------------------------|
| `"[a]\nx=1\ny=2"`                    | `{"a": {"x": "1", "y": "2"}}`               |
| `"[a]\nx = 1\n[b]\ny = 2"`           | `{"a": {"x": "1"}, "b": {"y": "2"}}`        |
| `"; comment\n[s]\n# auch comment\nk=v"` | `{"s": {"k": "v"}}`                       |
| `"k=v"`                              | `{}` (kein Sektion vorher)                  |

## Idee

```python
def ini_parse(s):
    out = {}
    aktuelle_sektion = None
    for zeile in s.splitlines():
        z = zeile.strip()
        if not z or z.startswith(";") or z.startswith("#"):
            continue
        if z.startswith("[") and z.endswith("]"):
            aktuelle_sektion = z[1:-1].strip()
            out.setdefault(aktuelle_sektion, {})
        elif "=" in z and aktuelle_sektion is not None:
            k, v = z.split("=", 1)
            out[aktuelle_sektion][k.strip()] = v.strip()
    return out
```

## Variante -- mit `configparser`

```python
import configparser
from io import StringIO

def ini_parse(s):
    parser = configparser.ConfigParser()
    parser.read_file(StringIO(s))
    return {sec: dict(parser[sec]) for sec in parser.sections()}
```

Pythons eingebauter Parser ist robuster (multi-line values,
Interpolation, etc.) -- aber komplexer in der Pruefung. Hier
implementieren wir es selbst.

## Anwendung

INI-Files sind klassisch fuer Konfiguration: Wine, Git-Config,
Setuptools `setup.cfg`, viele Datenbank-Tools.
