"""Der nächste Schritt nach einer Aufgabe im Kurs, allein aus der Kursdatei (kurs/<sprache>.yml) bestimmt.

Reihenfolge: die Übungen des Kapitels, dann das Stück des Kapitelprojekts, dann die Einführung des nächsten Kapitels
desselben Kurses; nach dem letzten Kapitel zurück zur Kursübersicht. Über Kursgrenzen geht es nie.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .einlesen import Kursinhalt
from .modelle import Kapitel

KursSchrittArt = Literal["aufgabe", "kapitel", "kurs", "keiner"]


class KursWeiter(BaseModel):
    art: KursSchrittArt
    """aufgabe: nächste Aufgabe im Kapitel; kapitel: Einführung eines Kapitels (das nächste, oder das eigene, wenn die
    Aufgabe dort nur Vertiefung ist); kurs: Kurs zu Ende, zurück zur Übersicht; keiner: die Aufgabe gehört zu keinem
    Kapitel, es gilt der allgemeine Vorschlag."""
    einfuehrung: str | None = None
    """Kapitel (Kennung seiner Einführung), in dem es weitergeht."""
    aufgabe_id: str | None = None


def _folge(kap: Kapitel) -> list[str]:
    return [*kap.uebungen, *kap.projekt]


def naechster_schritt(inhalt: Kursinhalt, aufgabe_id: str, einfuehrung: str | None = None) -> KursWeiter:
    """Ohne `einfuehrung` gilt das Kapitel, dessen Übungen oder Projekt die Aufgabe enthält."""
    for kurs in inhalt.kurse.values():
        kapitel = [k for k in kurs.kapitel() if k.einfuehrung in inhalt.einfuehrungen]
        for stelle, kap in enumerate(kapitel):
            folge = _folge(kap)
            gemeint = kap.einfuehrung == einfuehrung if einfuehrung is not None else aufgabe_id in folge
            if not gemeint:
                continue
            if aufgabe_id not in folge:
                return KursWeiter(art="kapitel", einfuehrung=kap.einfuehrung)
            nr = folge.index(aufgabe_id)
            if nr + 1 < len(folge):
                return KursWeiter(art="aufgabe", einfuehrung=kap.einfuehrung, aufgabe_id=folge[nr + 1])
            if stelle + 1 < len(kapitel):
                return KursWeiter(art="kapitel", einfuehrung=kapitel[stelle + 1].einfuehrung)
            return KursWeiter(art="kurs")
    return KursWeiter(art="keiner")
