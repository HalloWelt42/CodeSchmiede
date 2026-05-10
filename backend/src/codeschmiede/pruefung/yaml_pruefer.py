"""YAML-Pruefer: prueft eine Aufgabe gegen die im Frontmatter definierten
input/expected-Tests (sichtbare + versteckte).

Strategie:
- Baue ein Skript, das den Nutzer-Code uebernimmt und im Anschluss alle
  Tests gegen die `funktion` aus dem Frontmatter ausfuehrt.
- Die Test-Ergebnisse werden als JSON nach einem Marker auf stdout
  geschrieben, alles davor ist Nutzer-Output.
- DockerRunner fuehrt das Skript in der Sandbox aus.
- Anschliessend wird die Ausgabe geparst, mit den erwarteten Werten
  verglichen, getrennt nach sichtbar / versteckt.
"""

import json

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, TestErgebnis
from .registry import registriere


MARKER = "===CODESCHMIEDE_TESTS===\n"


@registriere("code_schreiben")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    if not aufgabe.funktion:
        raise ValueError(
            f"Aufgabe {aufgabe.id}: Feld 'funktion' fehlt im Frontmatter"
        )

    alle_tests = aufgabe.tests_sichtbar + aufgabe.tests_versteckt
    sichtbar_anz = len(aufgabe.tests_sichtbar)
    test_inputs = [{"input": t.input, "expected": t.expected} for t in alle_tests]

    skript = _baue_skript(code, aufgabe.funktion, test_inputs)
    limits = RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden)
    erg = runner.run_code(skript, limits=limits)

    if MARKER not in erg.stdout:
        return _crash_ergebnis(aufgabe, erg.stdout, erg.stderr, erg.laufzeit_ms, erg.timeout)

    nutzer_stdout, _, json_teil = erg.stdout.partition(MARKER)
    try:
        roh = json.loads(json_teil.strip())
    except json.JSONDecodeError:
        return _crash_ergebnis(
            aufgabe,
            nutzer_stdout,
            (erg.stderr or "") + "\nTest-Ausgabe konnte nicht geparst werden.",
            erg.laufzeit_ms,
            erg.timeout,
        )

    sichtbar_ergebnisse: list[TestErgebnis] = []
    versteckt_pass = 0
    versteckt_fail = 0

    for i, r in enumerate(roh):
        if i < sichtbar_anz:
            sichtbar_ergebnisse.append(
                TestErgebnis(
                    index=i,
                    bestanden=r["ok"],
                    eingabe=alle_tests[i].input,
                    erwartet=alle_tests[i].expected,
                    tatsaechlich=r.get("actual"),
                    fehler=r.get("err"),
                )
            )
        else:
            if r["ok"]:
                versteckt_pass += 1
            else:
                versteckt_fail += 1

    bestanden = (
        all(t.bestanden for t in sichtbar_ergebnisse)
        and versteckt_fail == 0
        and len(roh) == len(alle_tests)
    )

    return PruefErgebnis(
        bestanden=bestanden,
        sichtbar=sichtbar_ergebnisse,
        versteckt_pass=versteckt_pass,
        versteckt_fail=versteckt_fail,
        laufzeit_ms=erg.laufzeit_ms,
        stdout=nutzer_stdout,
        stderr=erg.stderr,
        timeout=erg.timeout,
    )


def _crash_ergebnis(
    aufgabe: Aufgabe, stdout: str, stderr: str, laufzeit_ms: float, timeout: bool
) -> PruefErgebnis:
    """Skript ist vor dem Test-Block gecrasht (Syntax, Timeout, Crash)."""
    return PruefErgebnis(
        bestanden=False,
        sichtbar=[
            TestErgebnis(
                index=i,
                bestanden=False,
                eingabe=t.input,
                erwartet=t.expected,
                tatsaechlich=None,
                fehler="Code wurde nicht vollstaendig ausgefuehrt",
            )
            for i, t in enumerate(aufgabe.tests_sichtbar)
        ],
        versteckt_pass=0,
        versteckt_fail=len(aufgabe.tests_versteckt),
        laufzeit_ms=laufzeit_ms,
        stdout=stdout,
        stderr=stderr,
        timeout=timeout,
    )


def _baue_skript(code: str, funktion: str, tests: list[dict]) -> str:
    """Wrapper-Skript: Nutzer-Code + Test-Runner + JSON-Marker auf stdout."""
    tests_json = json.dumps(tests)
    return (
        f"{code}\n\n"
        "# === codeschmiede test runner (auto generated) ===\n"
        "import json as _json\n"
        "import sys as _sys\n"
        f"_tests = {tests_json}\n"
        "_ergebnisse = []\n"
        "for _i, _t in enumerate(_tests):\n"
        "    try:\n"
        f"        _actual = {funktion}(*_t['input'])\n"
        "        _ergebnisse.append({\n"
        "            'i': _i,\n"
        "            'ok': _actual == _t['expected'],\n"
        "            'actual': _actual,\n"
        "            'err': None,\n"
        "        })\n"
        "    except Exception as _e:\n"
        "        _ergebnisse.append({\n"
        "            'i': _i,\n"
        "            'ok': False,\n"
        "            'actual': None,\n"
        "            'err': type(_e).__name__ + ': ' + str(_e),\n"
        "        })\n"
        f"_sys.stdout.write({MARKER!r})\n"
        "_sys.stdout.write(_json.dumps(_ergebnisse, default=str))\n"
        "_sys.stdout.flush()\n"
    )
