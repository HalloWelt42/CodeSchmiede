"""Turingmaschine: Übergangstabelle lesen und auf einem Band laufen lassen.

Das Programm ist Text, eine Regel je Zeile, Kommentare mit #:

  plus 1 -> 0 L plus
  plus _ -> 1 N fertig

Zustand und gelesenes Zeichen links, rechts was geschrieben wird, wohin der Kopf geht (L, R, N) und der nächste
Zustand. `_` ist das leere Feld. Die Oberfläche zeigt denselben Text als Tabelle; was gilt, steht hier.
Gerechnet wird im Backend, ganz ohne Sandbox: eine Tabelle ist Daten, kein Code.
"""

import re
from dataclasses import dataclass, field

LEER = "_"
RICHTUNGEN = {"L": -1, "R": 1, "N": 0}
ZEILE = re.compile(r"^(\S+)\s+(\S)\s*->\s*(\S)\s+([LRN])\s+(\S+)$")
NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_äöüÄÖÜß]*$")


@dataclass(frozen=True)
class Regel:
    zeile: int
    zustand: str
    liest: str
    schreibt: str
    geht: str
    danach: str


@dataclass
class Tabelle:
    regeln: list[Regel]
    fehler: list[str] = field(default_factory=list)

    def zustaende(self, ende: set[str]) -> set[str]:
        """Zustände, die nicht Endzustände sind."""
        return {r.zustand for r in self.regeln} | {r.danach for r in self.regeln if r.danach not in ende}

    def regel(self, zustand: str, liest: str) -> Regel | None:
        for r in self.regeln:
            if r.zustand == zustand and r.liest == liest:
                return r
        return None


def lies(text: str, zeichen: set[str]) -> Tabelle:
    """Liest die Tabelle; meldet Zeilen, die nicht passen, unbekannte Zeichen und doppelte Regeln."""
    regeln: list[Regel] = []
    fehler: list[str] = []
    erlaubt = zeichen | {LEER}
    for nr, roh in enumerate(text.splitlines(), start=1):
        zeile = roh.split("#", 1)[0].strip()
        if not zeile:
            continue
        treffer = ZEILE.match(zeile)
        if not treffer:
            fehler.append(f"Zeile {nr}: so geht es: Zustand liest -> schreibt geht danach, etwa plus 1 -> 0 L plus")
            continue
        zustand, liest_z, schreibt, geht, danach = treffer.groups()
        for name in (zustand, danach):
            if not NAME.match(name):
                fehler.append(f"Zeile {nr}: {name} ist kein Name für einen Zustand")
        for z in (liest_z, schreibt):
            if z not in erlaubt:
                fehler.append(f"Zeile {nr}: das Zeichen {z} gibt es hier nicht, nur {' '.join(sorted(erlaubt))}")
        regel = Regel(nr, zustand, liest_z, schreibt, geht, danach)
        doppelt = next((r for r in regeln if r.zustand == zustand and r.liest == liest_z), None)
        if doppelt:
            fehler.append(f"Zeile {nr}: für {zustand} und {liest_z} gibt es schon Zeile {doppelt.zeile}")
        regeln.append(regel)
    return Tabelle(regeln, fehler)


@dataclass
class Schritt:
    """Ein Bild des Laufs: Band (ab Feld `von`), Kopf, Zustand und die Regel, die eben galt."""

    band: str
    von: int
    kopf: int
    zustand: str
    regel: int | None


@dataclass
class Lauf:
    schritte: list[Schritt]
    gehalten: bool
    zustand: str
    band: str
    grund: str | None = None


def band_text(zellen: dict[int, str]) -> tuple[str, int]:
    belegt = [i for i, z in zellen.items() if z != LEER]
    if not belegt:
        return "", 0
    von, bis = min(belegt), max(belegt)
    return "".join(zellen.get(i, LEER) for i in range(von, bis + 1)), von


def laufe(tabelle: Tabelle, band: str, kopf: int, start: str, ende: set[str], hoechstens: int,
          aufzeichnen: bool = True) -> Lauf:
    """Lässt die Maschine laufen, bis sie in einem Endzustand ist, keine Regel passt oder die Grenze erreicht ist."""
    zellen = {i: z for i, z in enumerate(band)}
    zustand = start
    schritte: list[Schritt] = []

    def bild(regel: int | None) -> None:
        if aufzeichnen:
            text, von = band_text(zellen)
            schritte.append(Schritt(text, von, kopf, zustand, regel))

    bild(None)
    for _ in range(hoechstens):
        if zustand in ende:
            text, _von = band_text(zellen)
            return Lauf(schritte, True, zustand, text)
        liest = zellen.get(kopf, LEER)
        regel = tabelle.regel(zustand, liest)
        if regel is None:
            text, _von = band_text(zellen)
            return Lauf(schritte, False, zustand, text, f"in {zustand} gibt es keine Regel für {liest}")
        zellen[kopf] = regel.schreibt
        kopf += RICHTUNGEN[regel.geht]
        zustand = regel.danach
        bild(regel.zeile)
    text, _von = band_text(zellen)
    if zustand in ende:
        return Lauf(schritte, True, zustand, text)
    return Lauf(schritte, False, zustand, text, f"nach {hoechstens} Schritten noch nicht fertig")
