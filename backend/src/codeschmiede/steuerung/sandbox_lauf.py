"""Gemeinsamer Lauf der Steuerungsspiele: das Programm in der Sandbox, das Nachspielen im Backend.

Jede Welt (ampel_welt, aufzug_welt) ist reines Python ohne Abhängigkeiten und hat dieselbe Schnittstelle:

  Welt(anlage, ablauf, aufzeichnen=False)
  welt.laeuft()              ob der Ablauf noch läuft
  welt.bereit()              wer jetzt eine Entscheidung braucht (Schlüssel, etwa None oder der Name eines Aufzugs)
  welt.lage(schluessel)      was das Programm in takt(lage) sieht
  welt.befehl_pruefen(wert)  (Befehl, None) oder (None, Fehlertext)
  welt.befehl(schluessel, befehl)
  welt.schritt()             einen Takt weiter
  welt.zeit                  Sekunden seit dem Start

In der Sandbox läuft die Quelle der Welt mit dem Programm; sie liefert nur die Sensoren, heraus kommt je Ablauf die
Folge der Befehle. Das Backend spielt dieselbe Folge mit derselben Welt nach und urteilt darauf; was das Programm in
der Sandbox an der Welt verändert hat, zählt so nicht.
"""

import json
from typing import Any

from pydantic import BaseModel, ValidationError

from ..pruefung.testlauf import hinweise, lies_block, neue_marke
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner

# Läuft in der Sandbox hinter der Welt. _DATEN und _MARKE stehen davor (siehe skript()).
LAUF = r'''
import json as _j, sys as _s


def _zeile(e):
    tb, nr = e.__traceback__, 0
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == "<programm>":
            nr = tb.tb_lineno
        tb = tb.tb_next
    return nr


def _lauf(ablauf):
    welt = Welt(_DATEN["anlage"], ablauf)
    namen = {"__name__": "__main__"}
    try:
        exec(compile(_DATEN["code"], "<programm>", "exec"), namen)
    except SyntaxError as e:
        return {"befehle": [], "fehler": "SyntaxError: %s (Zeile %s)" % (e.msg, e.lineno)}
    except Exception as e:
        return {"befehle": [], "fehler": "%s: %s (Zeile %d)" % (type(e).__name__, e, _zeile(e))}
    takt = namen.get("takt")
    if not callable(takt):
        return {"befehle": [], "fehler": "Es fehlt die Funktion takt(lage)."}
    befehle = []
    while welt.laeuft():
        for wer in welt.bereit():
            try:
                wert = takt(welt.lage(wer))
            except Exception as e:
                return {"befehle": befehle, "fehler": "Sekunde %d: %s: %s (Zeile %d)" % (
                    int(welt.zeit), type(e).__name__, e, _zeile(e))}
            befehl, fehler = welt.befehl_pruefen(wert)
            if fehler:
                return {"befehle": befehle, "fehler": "Sekunde %d: %s" % (int(welt.zeit), fehler)}
            befehle.append(befehl)
            welt.befehl(wer, befehl)
        welt.schritt()
    return {"befehle": befehle, "fehler": None}


_ergebnis = [_lauf(a) for a in _DATEN["ablaeufe"]]
_s.stdout.flush()
_s.stdout.write("\n" + _MARKE + _j.dumps(_ergebnis) + "\n")
'''


class Gemeldet(BaseModel):
    """Was die Sandbox je Ablauf meldet: die Befehle in der Reihenfolge der Entscheidungen."""

    befehle: list[Any]
    fehler: str | None = None


class SandboxLauf(BaseModel):
    gemeldet: list[Gemeldet] | None
    stdout: str
    stderr: str
    laufzeit_ms: float
    timeout: bool


def skript(welt_quelle: str, code: str, anlage: dict, ablaeufe: list[dict], marke: str) -> str:
    daten = {"code": code, "anlage": anlage, "ablaeufe": ablaeufe}
    return f"_DATEN = __import__('json').loads({json.dumps(daten)!r})\n_MARKE = {marke!r}\n{welt_quelle}\n{LAUF}"


def laufe(welt_quelle: str, code: str, anlage: dict, ablaeufe: list[dict], runner: Runner, sekunden: int) -> SandboxLauf:
    """Lässt das Programm in jedem Ablauf laufen und liefert je Ablauf die Befehle."""
    marke = neue_marke()
    erg = runner.run_code(skript(welt_quelle, code, anlage, ablaeufe, marke), "python",
                          RunLimits(timeout_sekunden=sekunden))
    stdout, block = lies_block(erg, marke)
    gemeldet = None
    if isinstance(block, list) and len(block) == len(ablaeufe):
        try:
            gemeldet = [Gemeldet.model_validate(b) for b in block]
        except ValidationError:
            gemeldet = None
    return SandboxLauf(gemeldet=gemeldet, stdout=stdout, stderr=hinweise(erg), laufzeit_ms=erg.laufzeit_ms,
                       timeout=erg.timeout)


def nachspielen(welt: Any, befehle: list[Any]) -> Any:
    """Spielt die Befehle mit der Welt nach. Brach das Programm ab, endet der Ablauf mit dem letzten Befehl."""
    rest = list(befehle)
    while welt.laeuft():
        for wer in welt.bereit():
            if not rest:
                return welt
            welt.befehl(wer, rest.pop(0))
        welt.schritt()
    return welt
