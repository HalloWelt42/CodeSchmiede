"""Tagesauftrag: drei kleine Ziele je Tag; alle erledigt geben den Bonus.

Ein Ziel, für das der Bestand nichts hergibt (ein Spiel-Level ohne
Spiele), entfällt.
"""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date

from ..models.spiel import AuftragsZiel, Tagesauftrag
from ..progress.submissions import BestandeneAbgabe
from .bestand import Bestand


@dataclass(frozen=True)
class Ziel:
    id: str
    text: str
    erfuellt_von: Callable[[BestandeneAbgabe, Bestand], bool]
    verfuegbar: Callable[[Bestand], bool]


ZIELE: tuple[Ziel, ...] = (
    Ziel(
        "aufgabe",
        "Eine Aufgabe oder Wiederholung lösen",
        lambda abgabe, bestand: not bestand.ist_spiel(abgabe.aufgabe_id),
        Bestand.hat_aufgaben,
    ),
    Ziel(
        "spiel",
        "Ein Spiel-Level schaffen",
        lambda abgabe, bestand: bestand.ist_spiel(abgabe.aufgabe_id),
        Bestand.hat_spiele,
    ),
    Ziel(
        "ohne_hilfe",
        "Eine Aufgabe ohne Hinweis bestehen",
        lambda abgabe, bestand: abgabe.ohne_hilfe is True,
        lambda bestand: bool(bestand.aufgaben),
    ),
)


def tagesauftrag(
    datum: date, abgaben_des_tages: list[BestandeneAbgabe], bestand: Bestand, bonus: int, gutgeschrieben: bool
) -> Tagesauftrag:
    ziele = [
        AuftragsZiel(
            id=z.id,
            text=z.text,
            erledigt=any(z.erfuellt_von(a, bestand) for a in abgaben_des_tages),
        )
        for z in ZIELE
        if z.verfuegbar(bestand)
    ]
    return Tagesauftrag(
        datum=datum,
        ziele=ziele,
        erledigt=bool(ziele) and all(z.erledigt for z in ziele),
        bonus=bonus,
        gutgeschrieben=gutgeschrieben,
    )
