"""Pruefer für `task_type: roboter` (Spiel Roboter-Parcours).

Das Python-Programm steuert einen Roboter mit gehe(), links(), rechts(),
nimm() und fragt wand_vorne(), kristall(), am_ziel(). Es läuft in der
Sandbox einmal je Welt: in der sichtbaren und in den versteckten, die
dieselbe Aufgabe in anderer Gestalt stellen. Wer nur die eine Welt
abläuft, scheitert dort; wer eine Schleife schreibt, besteht.

Aus der Sandbox kommt je Welt nur die Folge der Befehle mit ihrer Zeile
(und ein Programmfehler, etwa ein Tippfehler im Namen). Den Weg und ob er
gelingt, rechnet das Backend nach (roboter_welt.nachspielen).

Sterne: einer, wenn alle Welten gelingen; zwei, wenn die sichtbare Welt
höchstens so viele Schritte braucht wie angegeben; drei, wenn dazu der
Code höchstens so viele Zeichen hat (ohne Leerraum und Kommentare).

Im Frontmatter:
  roboter:
    welt: |                   sichtbare Welt, Zeichen siehe roboter_welt.py
      ########
      #>..K.Z#
      ########
    versteckt: [|..., |...]   weitere Welten, gehen nie an den Browser
    sterne: {schritte: 18, zeichen: 140}
"""

import io
import json
import tokenize

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from ..models.aufgabe import Aufgabe
from ..progress.submissions import codelaenge
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .testlauf import hinweise, lies_block, neue_marke
from .roboter_welt import Aktion, RoboterLauf, Welt, nachspielen

# mehr Befehle je Welt gelten als Endlosschleife
HOECHSTENS = 1000

# Läuft in der Sandbox. _DATEN und _MARKE stehen davor (siehe skript()).
LAUF = r'''
import json as _j, sys as _s
_RICHTUNGEN = ((1, 0), (0, -1), (-1, 0), (0, 1))


class _Halt(BaseException):
    pass


def _lauf(karte):
    breite, hoehe = len(karte[0]), len(karte)
    lage = {}
    for y, zeile in enumerate(karte):
        for x, z in enumerate(zeile):
            if z in ">^<v":
                lage.update(x=x, y=y, r=">^<v".index(z))
    kristalle = {(x, y) for y, zeile in enumerate(karte) for x, z in enumerate(zeile) if z == "K"}
    ziel = next((x, y) for y, zeile in enumerate(karte) for x, z in enumerate(zeile) if z == "Z")
    aktionen = []

    def frei(x, y):
        return 0 <= x < breite and 0 <= y < hoehe and karte[y][x] != "#"

    def zeile():
        f = _s._getframe(2)
        while f is not None and f.f_code.co_filename != "<programm>":
            f = f.f_back
        return f.f_lineno if f is not None else 0

    def befehl(art):
        if len(aktionen) >= _DATEN["hoechstens"]:
            raise _Halt("Mehr als %d Schritte; läuft eine Schleife endlos?" % _DATEN["hoechstens"])
        aktionen.append([art, zeile()])

    def vorne():
        dx, dy = _RICHTUNGEN[lage["r"]]
        return lage["x"] + dx, lage["y"] + dy

    def gehe():
        befehl("gehe")
        x, y = vorne()
        if not frei(x, y):
            raise _Halt("")
        lage.update(x=x, y=y)

    def links():
        befehl("links")
        lage["r"] = (lage["r"] + 1) % 4

    def rechts():
        befehl("rechts")
        lage["r"] = (lage["r"] + 3) % 4

    def nimm():
        befehl("nimm")
        if (lage["x"], lage["y"]) not in kristalle:
            raise _Halt("")
        kristalle.discard((lage["x"], lage["y"]))

    def wand_vorne():
        return not frei(*vorne())

    def kristall():
        return (lage["x"], lage["y"]) in kristalle

    def am_ziel():
        return (lage["x"], lage["y"]) == ziel

    namen = dict(gehe=gehe, links=links, rechts=rechts, nimm=nimm, wand_vorne=wand_vorne,
                 kristall=kristall, am_ziel=am_ziel, __name__="__main__")
    fehler = None
    try:
        exec(compile(_DATEN["code"], "<programm>", "exec"), namen)
    except _Halt as halt:
        # Absturz und leere Hände rechnet das Backend nach; nur die Endlosschleife meldet sich selbst
        fehler = str(halt) or None
    except SyntaxError as e:
        fehler = "SyntaxError: %s (Zeile %s)" % (e.msg, e.lineno)
    except Exception as e:
        tb, nr = e.__traceback__, 0
        while tb is not None:
            if tb.tb_frame.f_code.co_filename == "<programm>":
                nr = tb.tb_lineno
            tb = tb.tb_next
        fehler = "%s: %s (Zeile %d)" % (type(e).__name__, e, nr)
    return {"aktionen": aktionen, "fehler": fehler}


_ergebnis = [_lauf(w) for w in _DATEN["welten"]]
_s.stdout.flush()
_s.stdout.write("\n" + _MARKE + _j.dumps(_ergebnis) + "\n")
'''


class RoboterSterne(BaseModel):
    schritte: int = Field(ge=1)
    zeichen: int = Field(ge=1)


class RoboterLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    welt: Welt
    versteckt: list[Welt] = Field(default_factory=list)
    sterne: RoboterSterne

    def welten(self) -> list[Welt]:
        return [self.welt, *self.versteckt]


class WeltLauf(BaseModel):
    """Was die Sandbox je Welt meldet."""

    aktionen: list[tuple[str, int]]
    fehler: str | None = None


def level_von(aufgabe: Aufgabe) -> RoboterLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return RoboterLevel.model_validate(extra.get("roboter"))


def skript(code: str, welten: list[Welt], marke: str) -> str:
    daten = {"code": code, "welten": [w.karte for w in welten], "hoechstens": HOECHSTENS}
    return f"_DATEN = __import__('json').loads({json.dumps(daten)!r})\n_MARKE = {marke!r}\n{LAUF}"


def zeichen_code(code: str) -> int:
    """Zeichen ohne Leerraum und ohne Kommentare: Kommentare kosten keine Sterne.
    Lässt sich der Code nicht zerlegen, zählt alles (wie codelaenge)."""
    leer = {tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}
    try:
        teile = [t.string for t in tokenize.generate_tokens(io.StringIO(code).readline) if t.type not in leer]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return codelaenge(code)
    return codelaenge("".join(teile))


def zeilen_code(code: str) -> int:
    """Zeilen, die etwas tun: ohne leere und ohne reine Kommentare."""
    return sum(1 for z in code.splitlines() if z.strip() and not z.strip().startswith("#"))


class Laeufe(BaseModel):
    laeufe: list[RoboterLauf] | None
    stdout: str
    stderr: str
    laufzeit_ms: float
    timeout: bool


def laufe(code: str, welten: list[Welt], runner: Runner, sekunden: int) -> Laeufe:
    """Lässt das Programm in allen Welten laufen und spielt jede nach."""
    marke = neue_marke()
    erg = runner.run_code(skript(code, welten, marke), "python", RunLimits(timeout_sekunden=sekunden))
    stdout, block = lies_block(erg, marke)
    laeufe = None
    if isinstance(block, list) and len(block) == len(welten):
        try:
            gemeldet = [WeltLauf.model_validate(b) for b in block]
            laeufe = [
                nachspielen(welt, [Aktion(befehl=a, zeile=z) for a, z in g.aktionen], g.fehler)
                for welt, g in zip(welten, gemeldet)
            ]
        except ValidationError:
            laeufe = None
    return Laeufe(laeufe=laeufe, stdout=stdout, stderr=hinweise(erg), laufzeit_ms=erg.laufzeit_ms, timeout=erg.timeout)


def lauf_sichtbar(aufgabe: Aufgabe, code: str, runner: Runner) -> Laeufe:
    """Probelauf: nur die sichtbare Welt, ohne Wertung."""
    return laufe(code, [level_von(aufgabe).welt], runner, aufgabe.zeitlimit_sekunden)


def kriterien(level: RoboterLevel, geschafft: bool, schritte: int, zeichen: int) -> list[SternKriterium]:
    kurz = geschafft and schritte <= level.sterne.schritte
    return [
        SternKriterium(text="Ziel erreicht, Kristalle genommen, in allen Welten", erreicht=geschafft),
        SternKriterium(text=f"höchstens {level.sterne.schritte} Schritte in der sichtbaren Welt", erreicht=kurz),
        SternKriterium(text=f"dazu höchstens {level.sterne.zeichen} Zeichen Code", erreicht=kurz and zeichen <= level.sterne.zeichen),
    ]


def _anzahl_versteckt(aufgabe: Aufgabe) -> int:
    try:
        return len(level_von(aufgabe).versteckt)
    except ValidationError:
        return 0  # meldet die Bestandsprüfung


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level_von(aufgabe)
    except ValidationError as fehler:
        return [f"roboter: {e['loc']} {e['msg']}" for e in fehler.errors()]
    return [] if aufgabe.sprache == "python" else ["Roboter-Parcours läuft mit Python: sprache python"]


@registriere(
    "roboter",
    verbirgt=("roboter.versteckt",),
    zaehle_versteckt=_anzahl_versteckt,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level.welten(), runner, aufgabe.zeitlimit_sekunden)
    zeichen = zeichen_code(code)
    if ergebnis.laeufe is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=["sichtbare Welt"], fehler="Programm lief nicht bis zum Ende")],
            versteckt_pass=0,
            versteckt_fail=len(level.versteckt),
            laufzeit_ms=ergebnis.laufzeit_ms,
            stdout=ergebnis.stdout,
            stderr=ergebnis.stderr,
            timeout=ergebnis.timeout,
            wertung=Wertung(sterne=0, kriterien=kriterien(level, False, 0, zeichen)),
        )

    sichtbar, *versteckt = ergebnis.laeufe
    geschafft = all(lauf.geschafft for lauf in ergebnis.laeufe)
    k = kriterien(level, geschafft, len(sichtbar.schritte), zeichen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(
            index=0,
            bestanden=sichtbar.geschafft,
            eingabe=["sichtbare Welt"],
            erwartet="Ziel erreicht, alle Kristalle genommen",
            tatsaechlich=sichtbar.model_dump(),
            fehler=sichtbar.fehler,
        )],
        versteckt_pass=sum(1 for lauf in versteckt if lauf.geschafft),
        versteckt_fail=sum(1 for lauf in versteckt if not lauf.geschafft),
        laufzeit_ms=ergebnis.laufzeit_ms,
        stdout=ergebnis.stdout,
        stderr=ergebnis.stderr,
        timeout=ergebnis.timeout,
        wertung=Wertung(
            sterne=sum(1 for x in k if x.erreicht),
            kriterien=k,
            kennwerte=Kennwerte(schritte=len(sichtbar.schritte), zeilen=zeilen_code(code)),
        ),
    )
