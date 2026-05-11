---
schema_version: 1
id: 122-flash-karten
revision: 1
titel: Flash-Karten - SM-2 Update
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [zahlen, lernen, sm2, dict]
pfade: [python_algorithmen2]
voraussetzungen: []
quelle:
  url: https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm
  notiz: Vereinfachte Version vom SM-2-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: sm2_update
hints:
  - kosten: 0
    text: |
      SM-2 ist der Lern-Algorithmus hinter Anki, SuperMemo und unserem
      eigenen Wiederholungs-System. Eingabe: aktueller `ease` (>=1.3),
      `intervall_tage`, `wiederholungen` und `bewertung` (0-5).
      Liefere neuen Zustand als Dict.
  - kosten: 25
    text: |
      Bewertung < 3: zurück auf wiederholungen=0, intervall=1, ease bleibt.
      Bewertung >= 3: 
        - wenn wiederholungen==0: intervall=1
        - wenn wiederholungen==1: intervall=6
        - sonst: intervall = round(intervall * ease)
        - wiederholungen += 1
        - ease = max(1.3, ease + 0.1 - (5-bewertung)*(0.08 + (5-bewertung)*0.02))
tests_sichtbar:
  - input: [2.5, 0, 0, 5]
    expected: { "ease": 2.6, "intervall_tage": 1, "wiederholungen": 1 }
  - input: [2.5, 1, 1, 5]
    expected: { "ease": 2.6, "intervall_tage": 6, "wiederholungen": 2 }
  - input: [2.5, 6, 2, 5]
    expected: { "ease": 2.6, "intervall_tage": 16, "wiederholungen": 3 }
  - input: [2.5, 6, 2, 2]
    expected: { "ease": 2.5, "intervall_tage": 1, "wiederholungen": 0 }
tests_versteckt:
  - input: [2.5, 0, 0, 0]
    expected: { "ease": 2.5, "intervall_tage": 1, "wiederholungen": 0 }
  - input: [2.5, 0, 0, 3]
    expected: { "ease": 2.36, "intervall_tage": 1, "wiederholungen": 1 }
  - input: [1.3, 6, 2, 0]
    expected: { "ease": 1.3, "intervall_tage": 1, "wiederholungen": 0 }
  - input: [2.5, 1, 1, 4]
    expected: { "ease": 2.5, "intervall_tage": 6, "wiederholungen": 2 }
starter_code: |
  def sm2_update(ease: float, intervall_tage: int, wiederholungen: int, bewertung: int) -> dict:
      # Deine Lösung hier -- SM-2-Algorithmus.
      # Ease >= 1.3. Bewertung < 3: Reset. Sonst: Folgeformel.
      pass
---

# Flash-Karten - SM-2 Update

Schreibe eine Funktion `sm2_update(ease, intervall_tage, wiederholungen, bewertung)`,
die den **neuen Zustand** einer Lern-Karte nach dem SM-2-Algorithmus
berechnet.

## Bewertung

| Bewertung | Bedeutung                |
|-----------|--------------------------|
| 0         | komplett falsch          |
| 1         | falsch, aber Begriff bekannt |
| 2         | falsch, aber leicht zu merken |
| 3         | richtig, mit Mühe        |
| 4         | richtig, kleine Pause    |
| 5         | richtig, sofort          |

## Regeln

- **Bewertung < 3**: Karte zurücksetzen. `wiederholungen=0`, `intervall_tage=1`, `ease` bleibt.
- **Bewertung >= 3**:
  - Erste Wiederholung (`wiederholungen=0`): Intervall = 1 Tag
  - Zweite (`wiederholungen=1`): Intervall = 6 Tage
  - Sonst: Intervall = round(altes Intervall * ease)
  - `wiederholungen` += 1
  - `ease` aktualisieren mit Formel:

$$
e' = \max(1.3, e + 0.1 - (5-b)(0.08 + (5-b) \cdot 0.02))
$$

## Beispiele

| ease | intervall | wdh | bew | → ease | intervall | wdh |
|------|-----------|-----|-----|--------|-----------|-----|
| 2.5  | 0         | 0   | 5   | 2.6    | 1         | 1   |
| 2.5  | 1         | 1   | 5   | 2.6    | 6         | 2   |
| 2.5  | 6         | 2   | 5   | 2.6    | 16        | 3   |
| 2.5  | 6         | 2   | 2   | 2.5    | 1         | 0   |

## Hintergrund

SM-2 ist der **Algorithmus hinter Anki**. Genau diesen verwenden
wir auch in der Codeschmiede für die Wiederholungs-Logik. Die
Aufgabe selbst zu lösen heisst auch: zu verstehen wie Anki tickt.
