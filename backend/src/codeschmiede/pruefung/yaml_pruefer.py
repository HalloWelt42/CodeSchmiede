"""YAML-Pruefer: prueft eine Aufgabe gegen die im Frontmatter definierten
input/expected-Tests (sichtbare + versteckte).

Strategie:
- Baue ein Skript, das den Nutzer-Code übernimmt und im Anschluss alle
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
                fehler="Code wurde nicht vollständig ausgeführt",
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
    """Wrapper-Skript: Nutzer-Code + Test-Runner + JSON-Marker auf stdout.

    Tests werden als JSON-String an den Container uebergeben und dort per
    `json.loads` geparst -- so klappt es auch für Booleans, None, und
    Sonderzeichen, die in Python-Syntax anders aussehen (true vs True).

    Der gesamte Test-Runner laeuft in einer eigenen Funktion. So
    koennen Hilfsvariablen des Runners (i, t, actual, ...) nicht mit
    Helfern aus dem Nutzer-Code kollidieren -- die leben im Modul-
    Scope, der Runner in einem Funktions-Scope.
    """
    tests_json = json.dumps(tests)
    return (
        f"{code}\n\n"
        "# === codeschmiede test runner (auto generated) ===\n"
        "def __cs_run_tests():\n"
        "    import json as __cs_json\n"
        "    import sys as __cs_sys\n"
        f"    __cs_tests = __cs_json.loads({tests_json!r})\n"
        "    __cs_ergebnisse = []\n"
        "    for __cs_i, __cs_t in enumerate(__cs_tests):\n"
        "        try:\n"
        f"            __cs_actual = {funktion}(*__cs_t['input'])\n"
        "            __cs_ergebnisse.append({\n"
        "                'i': __cs_i,\n"
        "                'ok': __cs_actual == __cs_t['expected'],\n"
        "                'actual': __cs_actual,\n"
        "                'err': None,\n"
        "            })\n"
        "        except Exception as __cs_e:\n"
        "            __cs_ergebnisse.append({\n"
        "                'i': __cs_i,\n"
        "                'ok': False,\n"
        "                'actual': None,\n"
        "                'err': type(__cs_e).__name__ + ': ' + str(__cs_e),\n"
        "            })\n"
        f"    __cs_sys.stdout.write({MARKER!r})\n"
        "    __cs_sys.stdout.write(__cs_json.dumps(__cs_ergebnisse, default=str))\n"
        "    __cs_sys.stdout.flush()\n"
        "\n"
        "__cs_run_tests()\n"
    )
