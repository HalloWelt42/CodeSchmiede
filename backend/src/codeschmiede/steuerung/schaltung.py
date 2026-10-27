"""Digitale Schaltungen: Schaltplan lesen und die ganze Wahrheitstabelle ausrechnen.

Der Schaltplan ist Text, ein Baustein oder Ausgang je Zeile, Kommentare mit #:

  x1 = XOR(A, B) @ 230,54
  u1 = UND(A, B) @ 230,184
  S = x1
  C = u1

Links der Name, rechts die Art mit ihren Eingängen (Eingänge der Schaltung, andere Bausteine oder die festen Werte
0 und 1); hinter `@` steht, wo der Baustein im Plan liegt (nur für die Zeichnung). Ausgänge der Schaltung bekommen
ein Signal. `?` ist ein noch nicht verbundener Eingang. Gerechnet wird im Backend ohne Sandbox: ein Schaltplan ist Daten, kein Code.

Schaltungen mit Takt haben dazu Flipflops (`f0 = FF(d0)`): beim Takt übernimmt ein Flipflop, was an seinem Eingang D
anliegt, und zeigt es bis zum nächsten Takt als sein Signal. Alle beginnen bei 0, alle hängen am selben Takt. Ein
Kreis ist erlaubt, wenn auf ihm ein Flipflop sitzt; ein Kreis nur aus Gattern bliebe nicht berechenbar.
"""

import re
from dataclasses import dataclass, field
from itertools import product

ARTEN = {
    "UND": (2, lambda a, b: a & b),
    "ODER": (2, lambda a, b: a | b),
    "XOR": (2, lambda a, b: a ^ b),
    "NAND": (2, lambda a, b: 1 - (a & b)),
    "NOR": (2, lambda a, b: 1 - (a | b)),
    "NICHT": (1, lambda a: 1 - a),
}
# Flipflop: ein Eingang D, gerechnet wird er nicht zwischen den Gattern, sondern beim Takt (siehe takte)
SPEICHER = "FF"
EINGAENGE = {**{art: n for art, (n, _) in ARTEN.items()}, SPEICHER: 1}
OFFEN = "?"
FEST = {"0": 0, "1": 1}
NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
BAUSTEIN = re.compile(r"^(\w+)\s*=\s*([A-Z]+)\s*\(([^)]*)\)\s*(?:@\s*(-?\d+)\s*,\s*(-?\d+))?$")
AUSGANG = re.compile(r"^(\w+)\s*=\s*(\S+)$")


@dataclass
class Baustein:
    zeile: int
    name: str
    art: str
    eingaenge: list[str]
    x: int | None = None
    y: int | None = None


@dataclass
class Plan:
    bausteine: list[Baustein]
    ausgaenge: dict[str, str]
    fehler: list[str] = field(default_factory=list)


def lies(text: str, eingaenge: list[str], ausgaenge: list[str], erlaubt: list[str]) -> Plan:
    """Liest den Plan und meldet, was nicht stimmt: unbekannte Arten und Signale, falsche Zahl an Eingängen,
    offene Eingänge, doppelte Namen, fehlende Ausgänge und Kreise."""
    bausteine: list[Baustein] = []
    belegt: dict[str, str] = {}
    fehler: list[str] = []
    for nr, roh in enumerate(text.splitlines(), start=1):
        zeile = roh.split("#", 1)[0].strip()
        if not zeile:
            continue
        b = BAUSTEIN.match(zeile)
        if b:
            name, art, roh_ein, x, y = b.groups()
            ein = [e.strip() for e in roh_ein.split(",")] if roh_ein.strip() else []
            if art not in EINGAENGE:
                fehler.append(f"Zeile {nr}: einen Baustein {art} gibt es nicht")
                continue
            if art not in erlaubt:
                fehler.append(f"Zeile {nr}: {art} ist hier nicht erlaubt, nur {', '.join(erlaubt)}")
            if len(ein) != EINGAENGE[art]:
                fehler.append(f"Zeile {nr}: {art} hat {EINGAENGE[art]} {'Eingang' if EINGAENGE[art] == 1 else 'Eingänge'}, nicht {len(ein)}")
            if name in eingaenge or name in ausgaenge or any(x.name == name for x in bausteine):
                fehler.append(f"Zeile {nr}: der Name {name} ist schon vergeben")
            bausteine.append(Baustein(nr, name, art, ein, int(x) if x else None, int(y) if y else None))
            continue
        a = AUSGANG.match(zeile)
        if a and a.group(1) in ausgaenge:
            if a.group(1) in belegt:
                fehler.append(f"Zeile {nr}: der Ausgang {a.group(1)} ist schon belegt")
            belegt[a.group(1)] = a.group(2)
            continue
        fehler.append(f"Zeile {nr}: so geht es: name = ART(Eingang, Eingang) oder Ausgang = Signal")
    signale = set(eingaenge) | set(FEST) | {b.name for b in bausteine}
    for b in bausteine:
        for i, e in enumerate(b.eingaenge, start=1):
            if e == OFFEN:
                fehler.append(f"{b.name}: Eingang {i} ist nicht verbunden")
            elif e not in signale:
                fehler.append(f"{b.name}: das Signal {e} gibt es nicht")
    for name in ausgaenge:
        quelle = belegt.get(name)
        if quelle is None or quelle == OFFEN:
            fehler.append(f"Ausgang {name} ist nicht verbunden")
        elif quelle not in signale:
            fehler.append(f"Ausgang {name}: das Signal {quelle} gibt es nicht")
    plan = Plan(bausteine, belegt, fehler)
    if not fehler and reihenfolge(plan, eingaenge) is None:
        nur = " ohne Flipflop" if SPEICHER in erlaubt else ""
        fehler.append(f"Die Schaltung hat einen Kreis{nur}: ein Baustein hängt von sich selbst ab")
    return plan


def flipflops(plan: Plan) -> list[Baustein]:
    return [b for b in plan.bausteine if b.art == SPEICHER]


def reihenfolge(plan: Plan, eingaenge: list[str]) -> list[Baustein] | None:
    """Die Gatter so geordnet, dass jedes nach seinen Eingängen kommt; None bei einem Kreis. Flipflops zählen als
    Quelle wie ein Eingang: ihr Signal steht zu Beginn des Takts schon fest."""
    fertig = set(eingaenge) | set(FEST) | {b.name for b in flipflops(plan)}
    rest = [b for b in plan.bausteine if b.art != SPEICHER]
    folge = []
    while rest:
        bereit = [b for b in rest if all(e in fertig for e in b.eingaenge)]
        if not bereit:
            return None
        for b in bereit:
            folge.append(b)
            fertig.add(b.name)
            rest.remove(b)
    return folge


def tiefe(plan: Plan, eingaenge: list[str]) -> int:
    """Längster Weg in Gattern von einem Eingang oder Flipflop zu einem Ausgang oder dem Eingang eines Flipflops."""
    ff = flipflops(plan)
    stufe = {e: 0 for e in [*eingaenge, *FEST, *(b.name for b in ff)]}
    for b in reihenfolge(plan, eingaenge) or []:
        stufe[b.name] = 1 + max((stufe[e] for e in b.eingaenge), default=0)
    ziele = [*plan.ausgaenge.values(), *(b.eingaenge[0] for b in ff)]
    return max((stufe.get(q, 0) for q in ziele), default=0)


def _rechne(folge: list[Baustein], plan: Plan, signal: dict[str, int]) -> dict[str, int]:
    for b in folge:
        signal[b.name] = ARTEN[b.art][1](*(signal[e] for e in b.eingaenge))
    for name, quelle in plan.ausgaenge.items():
        signal[name] = signal[quelle]
    return signal


def wahrheitstabelle(plan: Plan, eingaenge: list[str]) -> list[dict[str, int]]:
    """Je Belegung der Eingänge (der erste Eingang ist die höchste Stelle) die Werte aller Signale und Ausgänge."""
    folge = reihenfolge(plan, eingaenge) or []
    return [_rechne(folge, plan, {**FEST, **dict(zip(eingaenge, werte))})
            for werte in product((0, 1), repeat=len(eingaenge))]


def takte(plan: Plan, eingaenge: list[str], eingaben: list[dict[str, int]]) -> list[dict[str, int]]:
    """Je Takt die Werte aller Signale und Ausgänge, wie sie bis zum Takt anliegen: die Flipflops zeigen, was sie beim
    vorigen Takt übernommen haben (zu Beginn 0), die Gatter rechnen damit und mit den Eingängen dieses Takts. Beim Takt
    übernehmen dann alle Flipflops zugleich ihren Eingang D."""
    ff = flipflops(plan)
    folge = reihenfolge(plan, eingaenge) or []
    stand = {b.name: 0 for b in ff}
    verlauf = []
    for werte in eingaben:
        signal = _rechne(folge, plan, {**FEST, **werte, **stand})
        verlauf.append(signal)
        stand = {b.name: signal[b.eingaenge[0]] for b in ff}
    return verlauf
