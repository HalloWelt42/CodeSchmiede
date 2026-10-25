"""Datenmodelle des Ausgabe-Sprints: was der Browser von einer Runde sieht
und was die Runde im Backend festhält."""

from datetime import datetime

from pydantic import BaseModel

from .progress import Progress
from .spiel import Belohnung


class SprintFrage(BaseModel):
    code: str
    optionen: list[str]


class SprintRunde(BaseModel):
    """Eine neue Runde, ohne richtige Antworten."""

    id: str
    aufgabe_id: str
    sekunden: int
    fragen: list[SprintFrage]


class SprintRueckmeldung(BaseModel):
    richtig: bool
    # Stelle der richtigen Antwort in der gezeigten Reihenfolge
    richtige_wahl: int


class SprintAuswertung(BaseModel):
    code: str
    optionen: list[str]
    gewaehlt: int | None
    richtig: int
    warum: str


class SprintAbschluss(BaseModel):
    bestanden: bool
    sterne: int
    treffer: int
    fragen: int
    laengste_kette: int
    sekunden: float
    auswertung: list[SprintAuswertung]
    progress: Progress
    belohnung: Belohnung | None = None


class GestellteFrage(BaseModel):
    """Eine Frage der Runde: Schnipsel im Vorrat und gezeigte Reihenfolge der
    Optionen (Stelle -> Index der Option im Schnipsel)."""

    schnipsel: int
    reihenfolge: list[int]


class GespeicherteRunde(BaseModel):
    id: str
    aufgabe_id: str
    aufgabe_revision: int
    fragen: list[GestellteFrage]
    antworten: list[int | None]
    gestartet: datetime
    frist: datetime
    abgeschlossen: bool = False
