"""Pruefer für `task_type: output_quiz`.

Eine Quiz-Aufgabe enthält im Frontmatter ein `quiz`-Feld mit:
  - `code`: das Code-Schnipsel, dessen Output zu erraten ist
  - `optionen`: Liste der angezeigten Antwort-Optionen
  - `richtig_index`: 0-basierter Index der korrekten Option

Die Antwort des Nutzers ist der gewählte Index als String. Kein
Sandbox-Lauf nötig -- reine Index-Vergleichs-Logik.
"""

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis
from .registry import registriere


@registriere("output_quiz")
def pruefe(aufgabe: Aufgabe, antwort: str, runner: Runner) -> PruefErgebnis:
    quiz = (getattr(aufgabe, "model_extra", {}) or {}).get("quiz", {})
    richtig_index = quiz.get("richtig_index")
    if richtig_index is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[],
            versteckt_pass=0,
            versteckt_fail=0,
            laufzeit_ms=0,
            stderr="Quiz-Definition fehlerhaft -- richtig_index fehlt",
        )

    try:
        gewaehlt = int(antwort.strip())
    except (ValueError, AttributeError):
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[],
            versteckt_pass=0,
            versteckt_fail=0,
            laufzeit_ms=0,
            stderr=f"Ungültige Antwort: {antwort!r}",
        )

    bestanden = gewaehlt == richtig_index
    return PruefErgebnis(
        bestanden=bestanden,
        sichtbar=[],
        versteckt_pass=1 if bestanden else 0,
        versteckt_fail=0 if bestanden else 1,
        laufzeit_ms=0,
        stdout="",
        stderr="" if bestanden else f"Richtig wäre Option {richtig_index} gewesen.",
    )
