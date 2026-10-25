"""Meisterschaft: Anteil der erreichbaren Punkte je Sprache und für die
Spiele, mit Rang nach den Schwellen der Spielregeln."""

from ..models.konfig import Raenge
from ..models.progress import Progress
from ..models.spiel import BereichStand, Rang
from .bestand import Bestand

SPIELE = "spiele"


def rang_fuer(anteil: float, raenge: Raenge) -> Rang | None:
    if anteil >= raenge.gold:
        return "gold"
    if anteil >= raenge.silber:
        return "silber"
    if anteil >= raenge.bronze:
        return "bronze"
    return None


def bereich_von(aufgabe_id: str, bestand: Bestand) -> str | None:
    aufgabe = bestand.aufgaben.get(aufgabe_id)
    if aufgabe is None:
        return None
    return SPIELE if aufgabe.task_type in bestand.spieltypen else aufgabe.sprache


def meisterschaft(bestand: Bestand, progress: list[Progress]) -> list[BereichStand]:
    titel = {s.id: s.titel for s in bestand.konfig.sprachen} | {SPIELE: "Spiele"}
    moeglich: dict[str, int] = {}
    for aufgabe in bestand.aufgaben.values():
        bereich = bereich_von(aufgabe.id, bestand)
        if bereich is not None:
            moeglich[bereich] = moeglich.get(bereich, 0) + aufgabe.schwierigkeit_score
    erreicht: dict[str, int] = {}
    for p in progress:
        bereich = bereich_von(p.aufgabe_id, bestand)
        if bereich is not None:
            erreicht[bereich] = erreicht.get(bereich, 0) + p.punkte_erreicht

    reihenfolge = [s.id for s in bestand.konfig.sprachen] + [SPIELE]
    reihenfolge += sorted(b for b in moeglich if b not in reihenfolge)
    staende = []
    for bereich in reihenfolge:
        if not moeglich.get(bereich):
            continue
        punkte = min(erreicht.get(bereich, 0), moeglich[bereich])
        anteil = punkte / moeglich[bereich]
        staende.append(
            BereichStand(
                id=bereich,
                titel=titel.get(bereich, bereich),
                punkte=punkte,
                moeglich=moeglich[bereich],
                anteil=anteil,
                rang=rang_fuer(anteil, bestand.konfig.spiel.raenge),
            )
        )
    return staende
