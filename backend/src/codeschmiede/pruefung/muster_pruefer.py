"""Pruefer für `task_type: muster_jagd` (Spiel Muster-Jagd).

Ein Level gibt Zeilen vor, die das Muster treffen muss (Treffer), und
Zeilen, die es nicht treffen darf (Nieten), jeweils sichtbare und
versteckte. Abgegeben wird nur das Muster selbst, ohne Schrägstriche;
die Flags legt das Level fest.

Geprüft wird in der JavaScript-Sandbox, mit derselben Ausdrucksart wie
die Vorschau im Browser und mit Zeitgrenze gegen zu gierige Muster. In
die Sandbox gehen Muster und Zeilen, ob eine Zeile treffen soll, bleibt
im Backend. Eine Zeile gilt als getroffen, wenn das Muster darin eine
nicht leere Stelle findet.

Sterne: einer fürs Bestehen, zwei und drei für Muster mit höchstens so
vielen Zeichen, wie das Level unter `sterne` angibt.

Im Frontmatter:
  muster:
    treffer: [...]              sichtbar, müssen passen
    nieten: [...]               sichtbar, dürfen nicht passen
    treffer_versteckt: [...]
    nieten_versteckt: [...]
    flags: "i"                  optional, ohne g und y
    sterne: {zwei: 24, drei: 18}
    spickzettel: [["\\d", "eine Ziffer"], ...]
"""

import json

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .testlauf import fuehre_aus

FUNKTION = "trifft"
LAENGSTES_MUSTER = 500


class SternSchwellen(BaseModel):
    """Höchstens so viele Zeichen für zwei und für drei Sterne."""

    zwei: int = Field(ge=1)
    drei: int = Field(ge=1)

    @model_validator(mode="after")
    def _drei_strenger(self) -> "SternSchwellen":
        if self.drei > self.zwei:
            raise ValueError("drei Sterne brauchen höchstens so viele Zeichen wie zwei")
        return self


class MusterLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    treffer: list[str] = Field(min_length=1)
    nieten: list[str] = Field(min_length=1)
    treffer_versteckt: list[str] = Field(default_factory=list)
    nieten_versteckt: list[str] = Field(default_factory=list)
    flags: str = Field(default="", pattern=r"^[imsu]*$")
    sterne: SternSchwellen
    spickzettel: list[tuple[str, str]] = Field(default_factory=list)

    def zeilen(self) -> list[tuple[str, bool]]:
        """Alle Zeilen mit Soll, sichtbare zuerst."""
        return (
            [(z, True) for z in self.treffer]
            + [(z, False) for z in self.nieten]
            + [(z, True) for z in self.treffer_versteckt]
            + [(z, False) for z in self.nieten_versteckt]
        )

    def anzahl_sichtbar(self) -> int:
        return len(self.treffer) + len(self.nieten)


def level_von(aufgabe: Aufgabe) -> MusterLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return MusterLevel.model_validate(extra.get("muster"))


def lauf_code(muster: str, flags: str) -> str:
    """JavaScript, das `trifft(text)` bereitstellt. Muster und Flags stehen
    als JSON-Zeichenketten darin, der Code selbst ist fest."""
    return (
        f"const __muster = new RegExp({json.dumps(muster)}, {json.dumps(flags + 'g')});\n"
        f"function {FUNKTION}(text) {{\n"
        "  for (const m of text.matchAll(__muster)) if (m[0] !== '') return true;\n"
        "  return false;\n"
        "}\n"
    )


def kriterien(level: MusterLevel, bestanden: bool, laenge: int) -> list[SternKriterium]:
    return [
        SternKriterium(text="alle Treffer, keine Niete, auch versteckte", erreicht=bestanden),
        SternKriterium(text=f"höchstens {level.sterne.zwei} Zeichen", erreicht=bestanden and laenge <= level.sterne.zwei),
        SternKriterium(text=f"höchstens {level.sterne.drei} Zeichen", erreicht=bestanden and laenge <= level.sterne.drei),
    ]


def _durchgefallen(level: MusterLevel, laenge: int, **felder) -> PruefErgebnis:
    zeilen = level.zeilen()
    sichtbar = zeilen[: level.anzahl_sichtbar()]
    k = kriterien(level, False, laenge)
    return PruefErgebnis(
        bestanden=False,
        sichtbar=[
            TestErgebnis(index=i, bestanden=False, eingabe=[text], erwartet=soll)
            for i, (text, soll) in enumerate(sichtbar)
        ],
        versteckt_pass=0,
        versteckt_fail=len(zeilen) - len(sichtbar),
        wertung=Wertung(sterne=0, kriterien=k),
        **felder,
    )


def _anzahl_versteckt(aufgabe: Aufgabe) -> int:
    try:
        level = level_von(aufgabe)
    except ValidationError:
        return 0  # meldet die Bestandsprüfung
    return len(level.treffer_versteckt) + len(level.nieten_versteckt)


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level_von(aufgabe)
    except ValidationError as fehler:
        return [f"muster: {e['loc']} {e['msg']}" for e in fehler.errors()]
    return [] if aufgabe.sprache == "javascript" else ["Muster-Jagd prüft mit JavaScript: sprache javascript"]


@registriere(
    "muster_jagd",
    verbirgt=("muster.treffer_versteckt", "muster.nieten_versteckt"),
    zaehle_versteckt=_anzahl_versteckt,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    muster = code.rstrip("\r\n")
    laenge = len(muster)
    if not muster:
        return _durchgefallen(level, laenge, laufzeit_ms=0, stderr="Das Muster ist leer.")
    if laenge > LAENGSTES_MUSTER:
        return _durchgefallen(level, laenge, laufzeit_ms=0, stderr=f"Das Muster ist länger als {LAENGSTES_MUSTER} Zeichen.")

    zeilen = level.zeilen()
    lauf = fuehre_aus(
        runner,
        "javascript",
        lauf_code(muster, level.flags),
        FUNKTION,
        [[text] for text, _ in zeilen],
        RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
    )
    if lauf.aufrufe is None:
        hinweis = "Das Muster braucht zu lange; vermutlich probiert es zu viele Wege durch." if lauf.timeout else lauf.stderr
        return _durchgefallen(level, laenge, laufzeit_ms=lauf.laufzeit_ms, stderr=hinweis, timeout=lauf.timeout)

    sichtbar: list[TestErgebnis] = []
    versteckt_pass = versteckt_fail = 0
    for i, ((text, soll), aufruf) in enumerate(zip(zeilen, lauf.aufrufe)):
        getroffen = aufruf.ok and aufruf.wert is True
        ok = aufruf.ok and getroffen == soll
        if i < level.anzahl_sichtbar():
            sichtbar.append(TestErgebnis(
                index=i, bestanden=ok, eingabe=[text], erwartet=soll,
                tatsaechlich=getroffen if aufruf.ok else None, fehler=aufruf.fehler,
            ))
        elif ok:
            versteckt_pass += 1
        else:
            versteckt_fail += 1

    bestanden = all(t.bestanden for t in sichtbar) and versteckt_fail == 0
    k = kriterien(level, bestanden, laenge)
    return PruefErgebnis(
        bestanden=bestanden,
        sichtbar=sichtbar,
        versteckt_pass=versteckt_pass,
        versteckt_fail=versteckt_fail,
        laufzeit_ms=lauf.laufzeit_ms,
        stderr=lauf.stderr,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k),
    )
