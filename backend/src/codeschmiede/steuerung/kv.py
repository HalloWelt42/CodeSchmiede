"""KV-Werkstatt: Formeln aus Blöcken lesen und prüfen, wie gut sie eine Funktion abdecken.

Eine Funktion hat 2 bis 4 Eingänge (A, B, C, D in der Reihenfolge der Level) und je Belegung einen Wert 0, 1 oder x
(egal); Belegungen sind binär gezählt, der erste Eingang ist die höchste Stelle. Abgegeben wird je Ausgang eine Zeile

  e = !B !D + C !D

Jeder Term ist ein Block im KV-Diagramm: ein Buchstabe heißt "der Eingang ist 1", `!` davor "der Eingang ist 0";
fehlt ein Eingang, darf er beides sein. `1` ist das ganze Raster, `0` (oder nichts) kein Block. Kommentare mit #.
Gerechnet wird im Backend ohne Sandbox: eine Formel ist Daten.

Begriffe: ein Block ist "so groß wie möglich" (ein Primblock), wenn kein Buchstabe wegfallen kann, ohne dass er eine
0 erwischt; ein Block ist "überflüssig", wenn alle seine Einsen auch in anderen Blöcken liegen.
"""

import re
from dataclasses import dataclass, field
from itertools import combinations, product

ZEILE = re.compile(r"^(\w+)\s*=\s*(.*)$")
LITERAL = re.compile(r"^(!?)([A-Za-z]\w*)$")


@dataclass(frozen=True)
class Block:
    """Ein Term: je Eingang 1, 0 oder None (egal)."""

    stellen: tuple[int | None, ...]

    def enthaelt(self, belegung: int, n: int) -> bool:
        return all(s is None or ((belegung >> (n - 1 - i)) & 1) == s for i, s in enumerate(self.stellen))

    def felder(self, n: int) -> set[int]:
        return {b for b in range(2 ** n) if self.enthaelt(b, n)}

    def buchstaben(self) -> int:
        return sum(1 for s in self.stellen if s is not None)

    def text(self, eingaenge: list[str]) -> str:
        teile = [("" if s else "!") + e for e, s in zip(eingaenge, self.stellen) if s is not None]
        return " ".join(teile) or "1"


@dataclass
class Formel:
    """Je Ausgang die Blöcke; Fehler beim Lesen als Text."""

    bloecke: dict[str, list[Block]] = field(default_factory=dict)
    fehler: list[str] = field(default_factory=list)


def lies(text: str, eingaenge: list[str], ausgaenge: list[str]) -> Formel:
    formel = Formel()
    for nr, roh in enumerate(text.splitlines(), start=1):
        zeile = roh.split("#", 1)[0].strip()
        if not zeile:
            continue
        m = ZEILE.match(zeile)
        if not m or m.group(1) not in ausgaenge:
            formel.fehler.append(f"Zeile {nr}: so geht es: {ausgaenge[0]} = A !B + C")
            continue
        name, rechts = m.groups()
        if name in formel.bloecke:
            formel.fehler.append(f"Zeile {nr}: {name} steht schon in einer Zeile davor")
            continue
        bloecke = []
        for term in [t.strip() for t in rechts.split("+")]:
            if term in ("", "0"):
                continue
            if term == "1":
                bloecke.append(Block(tuple(None for _ in eingaenge)))
                continue
            stellen: list[int | None] = [None] * len(eingaenge)
            for roh_lit in term.replace("*", " ").replace("·", " ").split():
                lit = LITERAL.match(roh_lit)
                if not lit or lit.group(2) not in eingaenge:
                    formel.fehler.append(f"Zeile {nr}: {roh_lit} ist kein Eingang (es gibt {', '.join(eingaenge)})")
                    continue
                i = eingaenge.index(lit.group(2))
                wert = 0 if lit.group(1) else 1
                if stellen[i] is not None and stellen[i] != wert:
                    formel.fehler.append(f"Zeile {nr}: {term} will {lit.group(2)} zugleich 0 und 1, der Block ist leer")
                stellen[i] = wert
            bloecke.append(Block(tuple(stellen)))
        formel.bloecke[name] = bloecke
    for name in ausgaenge:
        if name not in formel.bloecke:
            formel.fehler.append(f"Für {name} fehlt die Zeile {name} = ...")
    return formel


def wert(bloecke: list[Block], belegung: int, n: int) -> int:
    return int(any(b.enthaelt(belegung, n) for b in bloecke))


def primbloecke(werte: str, n: int) -> list[Block]:
    """Alle Blöcke, die keine 0 erwischen und nicht größer gehen (für Sterne und Hinweise)."""
    erlaubt = [b for b in product((0, 1, None), repeat=n)
               if all(werte[x] != "0" for x in Block(b).felder(n))]
    bloecke = [Block(b) for b in erlaubt]
    return [b for b in bloecke if not any(b != c and b.felder(n) < c.felder(n) for c in bloecke)
            and any(werte[x] == "1" for x in b.felder(n))]


def kleinste_abdeckung(werte: str, n: int) -> tuple[int, int]:
    """(Blöcke, Buchstaben) der kleinsten Abdeckung aller Einsen aus Primblöcken: erst wenige Blöcke, dann wenige
    Buchstaben. Bei höchstens 4 Eingängen reicht Durchprobieren."""
    einsen = {x for x, w in enumerate(werte) if w == "1"}
    if not einsen:
        return 0, 0
    prim = primbloecke(werte, n)
    for k in range(1, len(prim) + 1):
        passend = [c for c in combinations(prim, k) if einsen <= set().union(*(b.felder(n) for b in c))]
        if passend:
            return k, min(sum(b.buchstaben() for b in c) for c in passend)
    return len(prim), sum(b.buchstaben() for b in prim)


def vergroesserbar(block: Block, werte: str, n: int) -> int | None:
    """Ein Eingang, der aus dem Block wegfallen kann, ohne dass er eine 0 erwischt (sonst None)."""
    for i, s in enumerate(block.stellen):
        if s is None:
            continue
        groesser = Block(block.stellen[:i] + (None,) + block.stellen[i + 1:])
        if all(werte[x] != "0" for x in groesser.felder(n)):
            return i
    return None


def schaltplan(formel: Formel, eingaenge: list[str], ausgaenge: list[str]) -> tuple[str, int, int]:
    """Die Formel als Schaltplan aus Bausteinen mit zwei Eingängen (wie im Spiel Digitale Schaltungen): ein NICHT je
    verneintem Eingang, eine UND-Kette je Block (derselbe Block in mehreren Ausgängen nur einmal), eine ODER-Kette je
    Ausgang. Liefert (Text, Bausteine, Tiefe)."""
    zeilen: list[str] = []
    tiefe: dict[str, int] = {e: 0 for e in [*eingaenge, "0", "1"]}
    zaehler: dict[str, int] = {}

    def baustein(art: str, *ein: str) -> str:
        zaehler[art] = zaehler.get(art, 0) + 1
        name = f"{art.lower()}{zaehler[art]}"
        zeilen.append(f"{name} = {art}({', '.join(ein)})")
        tiefe[name] = 1 + max(tiefe[e] for e in ein)
        return name

    def kette(art: str, signale: list[str]) -> str:
        while len(signale) > 1:
            # die beiden flachsten zuerst, damit der Weg kurz bleibt
            signale.sort(key=lambda s: tiefe[s])
            signale = [baustein(art, signale[0], signale[1]), *signale[2:]]
        return signale[0]

    nicht: dict[str, str] = {}
    gebaut: dict[Block, str] = {}
    for name in ausgaenge:
        terme = []
        for b in formel.bloecke.get(name, []):
            literale = []
            for e, s in zip(eingaenge, b.stellen):
                if s == 1:
                    literale.append(e)
                elif s == 0:
                    if e not in nicht:
                        nicht[e] = baustein("NICHT", e)
                    literale.append(nicht[e])
            if b not in gebaut:
                gebaut[b] = kette("UND", literale) if literale else "1"
            terme.append(gebaut[b])
        zeilen.append(f"{name} = {kette('ODER', terme) if terme else '0'}")
    gatter = sum(zaehler.values())
    weg = max((tiefe.get(z.split(" = ")[1], 0) for z in zeilen if z.split(" = ")[0] in ausgaenge), default=0)
    return "\n".join(zeilen) + "\n", gatter, weg
