"""Datenmodelle für Fortschritts-Tracking und Streak."""

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


Status = Literal["neu", "in_arbeit", "geloest"]


class Progress(BaseModel):
    """Fortschritt pro Aufgabe (eine Zeile in der `progress`-Tabelle)."""

    aufgabe_id: str
    status: Status
    versuche: int = 0
    hints_genutzt: int = 0
    punkte_erreicht: int = 0
    geloest_am: datetime | None = None
    ease: float = 2.5
    intervall_tage: int = 0
    faellig_am: date | None = None
    letzte_wiederholung: datetime | None = None


class Streak(BaseModel):
    """Aktuelle und laengste Tagesserie. Persistiert in `kv_state`."""

    aktuell: int = 0
    laengster: int = 0
    letzter_tag: date | None = None


class GesamtFortschritt(BaseModel):
    """Aggregat für das Dashboard."""

    aufgaben_gesamt: int
    aufgaben_geloest: int
    aufgaben_in_arbeit: int
    aufgaben_neu: int
    submissions_gesamt: int
    bestandene_submissions: int
    punkte_gesamt: int = 0
    punkte_maximal: int = 0


class Tagesziel(BaseModel):
    """Was steht heute an? Antwort für `GET /api/progress/heute`."""

    datum: date
    faellige_wiederholungen: list[str]
    vorgeschlagene_neue: str | None = None
    letzte_aufgabe: str | None = None
    streak_aktiv: bool = False
    aktueller_streak: int = 0
    laengster_streak: int = 0


class WeiterVorschlag(BaseModel):
    """Vorschlag für die nächste Aufgabe, ausgehend von einer aktuellen.
    Bevorzugt eine offene Aufgabe im selben Pfad, sonst global nächste
    nach Schwierigkeitsscore.
    """

    naechste_id: str | None = None
    quelle: Literal["pfad", "global", "keine"] = "keine"
    pfad_id: str | None = None
