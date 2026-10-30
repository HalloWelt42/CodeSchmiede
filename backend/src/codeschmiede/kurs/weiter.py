"""Wo es im Kurs weitergeht, allein aus der Kursdatei (kurs/<sprache>.yml) und dem Erledigten bestimmt.

Eine Regel für beides: "Weiter hier" eines Kapitels (das erste offene Element) und der nächste Schritt nach einer
Aufgabe. Reihenfolge im Kapitel: die Einführung, die Übungen, dann das Stück des Kapitelprojekts. Ein Kapitel ist
fertig, wenn nichts davon mehr offen ist; erst dann geht es ins nächste Kapitel desselben Kurses, und zwar zu dessen
erstem offenen Element (ein schon fertiges Kapitel wird übersprungen). Nach dem letzten Kapitel zurück zur
Kursübersicht. Über Kursgrenzen geht es nie.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel

from .einlesen import Kursinhalt
from .modelle import Kapitel

KursSchrittArt = Literal["aufgabe", "kapitel", "kurs", "keiner"]


class KursWeiter(BaseModel):
    art: KursSchrittArt
    """aufgabe: eine Aufgabe im Kapitel; kapitel: Einführung eines Kapitels (das nächste, oder das eigene, wenn die
    Aufgabe dort nur Vertiefung ist oder nur sie selbst noch offen ist); kurs: Kurs zu Ende, zurück zur Übersicht;
    keiner: die Aufgabe gehört zu keinem Kapitel, es gilt der allgemeine Vorschlag."""
    einfuehrung: str | None = None
    """Kapitel (Kennung seiner Einführung), in dem es weitergeht."""
    aufgabe_id: str | None = None


@dataclass(frozen=True)
class Erledigt:
    """Was erledigt ist: gelöste Aufgaben, Einführungen mit allen Abschnitten fertig, Kapitel per Kurztest
    übersprungen (je Kennung der Einführung)."""

    aufgaben: frozenset[str]
    einfuehrungen: frozenset[str]
    uebersprungen: frozenset[str] = frozenset()


def _folge(kap: Kapitel) -> list[str]:
    return [*kap.uebungen, *kap.projekt]


def _offene_aufgabe(folge: list[str], erledigt: Erledigt, nach: str | None = None) -> str | None:
    """Erste ungelöste Aufgabe der Folge; mit `nach` zuerst die dahinter, dann die davor, `nach` selbst nicht."""
    if nach in folge:
        nr = folge.index(nach)
        folge = [*folge[nr + 1:], *folge[:nr]]
    return next((aid for aid in folge if aid not in erledigt.aufgaben), None)


def kapitel_fertig(kap: Kapitel, erledigt: Erledigt) -> bool:
    """Einführung fertig und jede Übung und jedes Projektstück gelöst."""
    return kap.einfuehrung in erledigt.einfuehrungen and _offene_aufgabe(_folge(kap), erledigt) is None


def offener_schritt(kap: Kapitel, erledigt: Erledigt) -> KursWeiter | None:
    """Erstes offenes Element des Kapitels ("Weiter hier"); None, wenn das Kapitel fertig oder per Kurztest
    übersprungen ist (beides öffnet das nächste Kapitel)."""
    if kapitel_fertig(kap, erledigt) or kap.einfuehrung in erledigt.uebersprungen:
        return None
    if kap.einfuehrung not in erledigt.einfuehrungen:
        return KursWeiter(art="kapitel", einfuehrung=kap.einfuehrung)
    aid = _offene_aufgabe(_folge(kap), erledigt)
    return KursWeiter(art="aufgabe", einfuehrung=kap.einfuehrung, aufgabe_id=aid) if aid else None


def _nach_dem_kapitel(kapitel: list[Kapitel], stelle: int, erledigt: Erledigt) -> KursWeiter:
    for kap in kapitel[stelle + 1:]:
        schritt = offener_schritt(kap, erledigt)
        if schritt is not None:
            return schritt
    return KursWeiter(art="kurs")


def naechster_schritt(inhalt: Kursinhalt, aufgabe_id: str, erledigt: Erledigt, einfuehrung: str | None = None) -> KursWeiter:
    """Nach `aufgabe_id`: die nächste offene Aufgabe des Kapitels, sonst das nächste Kapitel mit Offenem. Ohne
    `einfuehrung` gilt das Kapitel, dessen Übungen oder Projekt die Aufgabe enthält."""
    for kurs in inhalt.kurse.values():
        kapitel = [k for k in kurs.kapitel() if k.einfuehrung in inhalt.einfuehrungen]
        for stelle, kap in enumerate(kapitel):
            folge = _folge(kap)
            gemeint = kap.einfuehrung == einfuehrung if einfuehrung is not None else aufgabe_id in folge
            if not gemeint:
                continue
            if aufgabe_id not in folge:
                return KursWeiter(art="kapitel", einfuehrung=kap.einfuehrung)
            aid = _offene_aufgabe(folge, erledigt, nach=aufgabe_id)
            if aid is not None:
                return KursWeiter(art="aufgabe", einfuehrung=kap.einfuehrung, aufgabe_id=aid)
            if aufgabe_id not in erledigt.aufgaben:
                return KursWeiter(art="kapitel", einfuehrung=kap.einfuehrung)
            return offener_schritt(kap, erledigt) or _nach_dem_kapitel(kapitel, stelle, erledigt)
    return KursWeiter(art="keiner")
