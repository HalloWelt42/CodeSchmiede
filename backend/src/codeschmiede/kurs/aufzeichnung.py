"""Aufzeichnung eines Python-Laufs: je ausgeführter Zeile des eigenen Codes der Speicher danach.

Daraus entstehen im Kurs Ablauf und Speicherbild eines Beispiels, später im Debugger das Vor- und Zurückspulen.
Aufgezeichnet wird in der Sandbox wie jeder andere Lauf: das Skript besteht aus einem kleinen Aufzeichner und dem
Code des Nutzers als Zeichenkette, die der Aufzeichner unter dem Dateinamen BEISPIEL ausführt. Nur Zeilen aus dieser
Datei zählen, Bibliotheken und der Aufzeichner selbst bleiben unsichtbar (kein Tiefendebugger).

Grenzen halten die Aufzeichnung klein: höchstens MAX_SCHRITTE Schritte, Werte bis zur Tiefe MAX_TIEFE mit höchstens
MAX_ELEMENTE Elementen, Darstellungen bis MAX_ZEICHEN Zeichen. Wird eine Grenze erreicht, läuft der Code trotzdem zu
Ende, nur die Aufzeichnung endet (`gekuerzt`).
"""

from __future__ import annotations

import json
from typing import Literal

from pydantic import BaseModel, Field

from ..pruefung.testlauf import hinweise, lies_block, neue_marke
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner

BEISPIEL = "<beispiel>"
MAX_SCHRITTE = 400
MAX_TIEFE = 3
MAX_ELEMENTE = 20
MAX_ZEICHEN = 80

Wertart = Literal["zahl", "text", "wahrheit", "nichts", "liste", "tupel", "menge", "woerterbuch", "funktion", "klasse", "objekt", "sonst"]


class Wert(BaseModel):
    """Ein Wert im Speicherbild. `kennung` ist gleich, wenn zwei Namen auf dasselbe Objekt zeigen (Pfeil)."""

    art: Wertart
    darstellung: str
    kennung: int | None = None
    elemente: list[Wert] | None = None
    paare: list[tuple[Wert, Wert]] | None = None
    attribute: dict[str, Wert] | None = None
    gekuerzt: bool = False


class Rahmen(BaseModel):
    """Ein Aufrufrahmen: das Modul oder eine laufende Funktion mit ihren Namen."""

    name: str
    variablen: dict[str, Wert]


class Schritt(BaseModel):
    zeile: int
    """Zeile, die gerade ausgeführt wurde; der Speicher ist der Zustand danach."""
    rahmen: list[Rahmen]
    """Vom Modul bis zur innersten laufenden Funktion."""
    ausgabe: str = ""
    """Was diese Zeile ausgegeben hat."""
    rueckgabe: Wert | None = None
    """Bei der letzten Zeile einer Funktion: ihr Rückgabewert."""


class Aufzeichnung(BaseModel):
    art: Literal["python"] = "python"
    schritte: list[Schritt] = Field(default_factory=list)
    ausgabe: str = ""
    fehler: str | None = None
    fehlerzeile: int | None = None
    gekuerzt: bool = False
    zeitueberschreitung: bool = False
    laufzeit_ms: float = 0


_AUFZEICHNER = r'''
import json as _j, sys as _s, io as _io, types as _t

_BEISPIEL = __BEISPIEL__
_MAX_SCHRITTE, _MAX_TIEFE, _MAX_ELEMENTE, _MAX_ZEICHEN = __GRENZEN__
_code = _j.loads(__CODE__)
_eingabe = _j.loads(__EINGABE__)

class _Mitschrift(_io.TextIOBase):
    def __init__(self):
        self.alles, self.neu = [], []
    def write(self, s):
        self.alles.append(s); self.neu.append(s); return len(s)
    def abholen(self):
        s = "".join(self.neu); self.neu.clear(); return s

def _kurz(s):
    return s if len(s) <= _MAX_ZEICHEN else s[:_MAX_ZEICHEN - 3] + "..."

def _wert(w, tiefe=0):
    if w is None:
        return {"art": "nichts", "darstellung": "None"}
    if isinstance(w, bool):
        return {"art": "wahrheit", "darstellung": repr(w)}
    if isinstance(w, (int, float, complex)):
        return {"art": "zahl", "darstellung": _kurz(repr(w))}
    if isinstance(w, str):
        return {"art": "text", "darstellung": _kurz(repr(w))}
    if isinstance(w, (_t.FunctionType, _t.BuiltinFunctionType, _t.MethodType)):
        return {"art": "funktion", "darstellung": getattr(w, "__name__", "Funktion"), "kennung": id(w)}
    if isinstance(w, type):
        return {"art": "klasse", "darstellung": w.__name__, "kennung": id(w)}
    art = {list: "liste", tuple: "tupel", set: "menge", frozenset: "menge", dict: "woerterbuch"}.get(type(w))
    try:
        darstellung = _kurz(repr(w))
    except Exception:
        darstellung = "<" + type(w).__name__ + ">"
    d = {"art": art or "objekt", "darstellung": darstellung, "kennung": id(w)}
    if tiefe >= _MAX_TIEFE:
        d["gekuerzt"] = True
        return d
    if art in ("liste", "tupel", "menge"):
        teile = list(w)
        if art == "menge":
            teile = sorted(teile, key=repr)
        d["elemente"] = [_wert(x, tiefe + 1) for x in teile[:_MAX_ELEMENTE]]
        d["gekuerzt"] = len(teile) > _MAX_ELEMENTE
    elif art == "woerterbuch":
        paare = list(w.items())
        d["paare"] = [[_wert(k, tiefe + 1), _wert(v, tiefe + 1)] for k, v in paare[:_MAX_ELEMENTE]]
        d["gekuerzt"] = len(paare) > _MAX_ELEMENTE
    elif art is None:
        attribute = getattr(w, "__dict__", None)
        if isinstance(attribute, dict):
            d["darstellung"] = type(w).__name__
            d["attribute"] = {k: _wert(v, tiefe + 1) for k, v in list(attribute.items())[:_MAX_ELEMENTE] if not k.startswith("__")}
        else:
            d["art"] = "sonst"
    return d

def _variablen(namen):
    return {k: _wert(v) for k, v in list(namen.items()) if not k.startswith("__") and not isinstance(v, _t.ModuleType)}

def _rahmen(frame):
    kette = []
    while frame is not None:
        if frame.f_code.co_filename == _BEISPIEL:
            name = "Modul" if frame.f_code.co_name == "<module>" else frame.f_code.co_name
            kette.append({"name": name, "variablen": _variablen(frame.f_locals)})
        frame = frame.f_back
    return kette[::-1]

_schritte, _mitschrift = [], _Mitschrift()
_stand = {"zeile": None, "gekuerzt": False}

def _festhalten(frame, rueckgabe=None, mit_rueckgabe=False):
    if _stand["zeile"] is None or _stand["gekuerzt"]:
        return
    if len(_schritte) >= _MAX_SCHRITTE:
        _stand["gekuerzt"] = True
        return
    s = {"zeile": _stand["zeile"], "rahmen": _rahmen(frame), "ausgabe": _mitschrift.abholen()}
    if mit_rueckgabe:
        s["rueckgabe"] = _wert(rueckgabe)
    _schritte.append(s)

def _verfolgen(frame, ereignis, arg):
    if frame.f_code.co_filename != _BEISPIEL:
        return None
    if ereignis == "line":
        _festhalten(frame)
        _stand["zeile"] = frame.f_lineno
    elif ereignis == "return":
        _festhalten(frame, arg, frame.f_code.co_name != "<module>")
        # zurück beim Aufrufer: dessen Zeile ist erst jetzt fertig (etwa die Zuweisung des Ergebnisses)
        aufrufer = frame.f_back
        _stand["zeile"] = aufrufer.f_lineno if aufrufer is not None and aufrufer.f_code.co_filename == _BEISPIEL else None
    return _verfolgen

_ergebnis = {"fehler": None, "fehlerzeile": None}
_echt = _s.stdout
_s.stdout = _mitschrift
_s.stdin = _io.StringIO("".join(z + "\n" for z in _eingabe))
_namen = {"__name__": "__main__"}
try:
    _uebersetzt = compile(_code, _BEISPIEL, "exec")
    _s.settrace(_verfolgen)
    try:
        exec(_uebersetzt, _namen)
    finally:
        _s.settrace(None)
except SyntaxError as e:
    _ergebnis["fehler"] = "SyntaxError: " + str(e.msg)
    _ergebnis["fehlerzeile"] = e.lineno
except BaseException as e:
    tb = e.__traceback__
    zeile = None
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == _BEISPIEL:
            zeile = tb.tb_lineno
        tb = tb.tb_next
    _ergebnis["fehler"] = type(e).__name__ + (": " + str(e) if str(e) else "")
    _ergebnis["fehlerzeile"] = zeile
finally:
    _s.stdout = _echt
_rest = _mitschrift.abholen()
if _rest and _schritte:
    _schritte[-1]["ausgabe"] += _rest
print(__MARKE__)
print(_j.dumps({"schritte": _schritte, "ausgabe": "".join(_mitschrift.alles), "gekuerzt": _stand["gekuerzt"], **_ergebnis}))
'''


def skript(code: str, marke: str, eingabe: list[str] | None = None) -> str:
    """Das Python-Skript für die Sandbox: Aufzeichner mit dem Nutzercode als Zeichenkette und den Zeilen für input()."""
    return (
        _AUFZEICHNER.replace("__BEISPIEL__", repr(BEISPIEL))
        .replace("__EINGABE__", repr(json.dumps(eingabe or [])))
        .replace("__GRENZEN__", repr((MAX_SCHRITTE, MAX_TIEFE, MAX_ELEMENTE, MAX_ZEICHEN)))
        .replace("__MARKE__", repr(marke))
        .replace("__CODE__", repr(json.dumps(code)))
    )


def aufzeichnen(runner: Runner, code: str, limits: RunLimits | None = None, eingabe: list[str] | None = None) -> Aufzeichnung:
    """Führt Python-Code in der Sandbox aus und liefert Ausgabe, Fehler und die Schritte mit dem Speicher; input()
    liest die Zeilen aus `eingabe`."""
    marke = neue_marke()
    erg = runner.run_code(skript(code, marke, eingabe), "python", limits or RunLimits())
    _, block = lies_block(erg, marke)
    if block is None:
        # Der Aufzeichner kam nicht bis zum Ende: Zeit, Speicher oder Ausgabeflut
        return Aufzeichnung(fehler=hinweise(erg).strip() or "Der Lauf brach ab.", zeitueberschreitung=erg.timeout,
                            gekuerzt=erg.gekuerzt, laufzeit_ms=erg.laufzeit_ms)
    return Aufzeichnung.model_validate({**block, "zeitueberschreitung": erg.timeout, "laufzeit_ms": erg.laufzeit_ms})
