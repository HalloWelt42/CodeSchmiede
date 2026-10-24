"""Code-Pruefer: prüft eine Funktion gegen die im Frontmatter definierten
input/expected-Tests (sichtbare + versteckte).

Ablauf:
- Der Testlauf ruft die Funktion in der Sandbox mit allen Eingaben auf
  und liefert die Rückgaben typgetreu zurück (Python und JavaScript).
- Verglichen wird hier im Backend; die erwarteten Werte gelangen nie in
  die Sandbox. Ein manipuliertes `__eq__` oder eine gefälschte Ausgabe
  im Nutzercode bringt deshalb nichts.
"""

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, TestErgebnis
from .kodierung import anzeigen, gleich
from .registry import registriere
from .testlauf import fuehre_aus


@registriere("code_schreiben")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    if not aufgabe.funktion:
        raise ValueError(f"Aufgabe {aufgabe.id}: Feld 'funktion' fehlt im Frontmatter")

    tests = aufgabe.tests_sichtbar + aufgabe.tests_versteckt
    lauf = fuehre_aus(
        runner,
        aufgabe.sprache,
        code,
        aufgabe.funktion,
        [t.input for t in tests],
        RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
    )

    if lauf.aufrufe is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[
                TestErgebnis(
                    index=i,
                    bestanden=False,
                    eingabe=t.input,
                    erwartet=t.expected,
                    fehler="Code wurde nicht vollständig ausgeführt",
                )
                for i, t in enumerate(aufgabe.tests_sichtbar)
            ],
            versteckt_pass=0,
            versteckt_fail=len(aufgabe.tests_versteckt),
            laufzeit_ms=lauf.laufzeit_ms,
            stdout=lauf.nutzer_stdout,
            stderr=lauf.stderr,
            timeout=lauf.timeout,
        )

    sichtbar: list[TestErgebnis] = []
    versteckt_pass = 0
    versteckt_fail = 0
    for i, (test, aufruf) in enumerate(zip(tests, lauf.aufrufe)):
        ok = aufruf.ok and gleich(aufruf.wert, test.expected)
        if i < len(aufgabe.tests_sichtbar):
            sichtbar.append(
                TestErgebnis(
                    index=i,
                    bestanden=ok,
                    eingabe=test.input,
                    erwartet=test.expected,
                    tatsaechlich=anzeigen(aufruf.wert) if aufruf.ok else None,
                    fehler=aufruf.fehler,
                )
            )
        elif ok:
            versteckt_pass += 1
        else:
            versteckt_fail += 1

    return PruefErgebnis(
        bestanden=all(t.bestanden for t in sichtbar) and versteckt_fail == 0,
        sichtbar=sichtbar,
        versteckt_pass=versteckt_pass,
        versteckt_fail=versteckt_fail,
        laufzeit_ms=lauf.laufzeit_ms,
        stdout=lauf.nutzer_stdout,
        stderr=lauf.stderr,
        timeout=lauf.timeout,
    )
