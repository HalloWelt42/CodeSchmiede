---
schema_version: 1
id: 298-deep-merge
revision: 1
titel: Deep-Merge zweier Dicts
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 45
schaetz_minuten: 15
tags: [dict, recursion, nested, merge]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Config-Merge
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: deep_merge
hints:
  - kosten: 0
    text: |
      Verschmelze zwei Dicts rekursiv. Bei Konflikten gewinnt b (rechts).
      Wenn beide Werte Dicts sind, werden sie WEITER verschmolzen.
      Sonst überschreibt der b-Wert direkt.
      Original-Dicts dürfen NICHT mutiert werden.
  - kosten: 25
    text: |
      Neue Dict bauen mit allen Keys. Wenn key in beiden UND beide
      Dicts → rekursiv. Sonst b[key] (falls da) sonst a[key].
tests_sichtbar:
  - input: [{"a": 1}, {"b": 2}]
    expected: {"a": 1, "b": 2}
  - input: [{"a": 1}, {"a": 2}]
    expected: {"a": 2}
  - input: [{}, {}]
    expected: {}
  - input: [{"a": {"x": 1}}, {"a": {"y": 2}}]
    expected: {"a": {"x": 1, "y": 2}}
tests_versteckt:
  - input: [{"a": {"x": 1, "y": 2}}, {"a": {"y": 99, "z": 3}}]
    expected: {"a": {"x": 1, "y": 99, "z": 3}}
  - input: [{"a": [1, 2]}, {"a": [3, 4]}]
    expected: {"a": [3, 4]}
  - input: [{"a": {"b": {"c": 1}}}, {"a": {"b": {"d": 2}}}]
    expected: {"a": {"b": {"c": 1, "d": 2}}}
  - input: [{"a": 1}, {"a": {"b": 2}}]
    expected: {"a": {"b": 2}}
  - input: [{"a": {"b": 1}}, {"a": "ueberschrieben"}]
    expected: {"a": "ueberschrieben"}
  - input: [{"shared": "a", "only_a": 1}, {"shared": "b", "only_b": 2}]
    expected: {"shared": "b", "only_a": 1, "only_b": 2}
starter_code: |
  def deep_merge(a: dict, b: dict) -> dict:
      # Deine Lösung hier -- rekursiv, b gewinnt bei Konflikt
      pass
---

# Deep-Merge zweier Dicts

Schreibe `deep_merge(a, b)`, die zwei Dicts **rekursiv** verschmelzt:

- Bei Schlüsseln nur in `a` oder nur in `b` → übernehmen.
- Bei Schlüsseln in **beiden**:
  - Wenn beide Werte Dicts sind → rekursiv verschmelzen.
  - Sonst → `b`-Wert überschreibt `a`-Wert.

Original-Dicts **nicht mutieren** -- neue Dicts bauen.

## Beispiele

| `a`                         | `b`                            | Merged                              |
|-----------------------------|---------------------------------|--------------------------------------|
| `{"a": 1}`                  | `{"b": 2}`                     | `{"a": 1, "b": 2}`                  |
| `{"a": 1}`                  | `{"a": 2}`                     | `{"a": 2}` (b gewinnt)              |
| `{"a": {"x": 1}}`           | `{"a": {"y": 2}}`              | `{"a": {"x": 1, "y": 2}}` (rekursiv) |
| `{"a": {"x": 1, "y": 2}}`   | `{"a": {"y": 99, "z": 3}}`     | `{"a": {"x": 1, "y": 99, "z": 3}}`  |
| `{"a": [1, 2]}`             | `{"a": [3, 4]}`                | `{"a": [3, 4]}` (Listen NICHT mergen) |
| `{"a": 1}`                  | `{"a": {"b": 2}}`              | `{"a": {"b": 2}}` (Typ-Wechsel)     |
| `{"a": {"b": 1}}`           | `{"a": "überschrieben"}`      | `{"a": "überschrieben"}`           |

## Idee -- Rekursion

`dict(a)` macht eine **flache Kopie** -- ändert nicht die innere
Dicts. Diese werden bei Bedarf rekursiv ersetzt.

## Stolperstein -- Listen mergen?

Es gibt zwei Konventionen für Listen:

1. **Komplett überschreiben** (b gewinnt) -- unsere Wahl.
2. **Konkatenieren** (a + b).

Wir nehmen Variante 1, weil sie konsistent mit dem "b gewinnt"-
Prinzip ist und einfacher zu merken.

## Anwendung

- **Config-Defaults + User-Overrides**: Defaults sind das `a`,
  User-Settings das `b`. Die Verschmelzung ergibt die finale Config.
- **API-Response-Merge** (z.B. partielle Updates).
- **Theme-Vererbung** in UI-Bibliotheken.
