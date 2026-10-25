"""Datenmodelle der Spielmechanik (docs/SPIELE.md).

Alles hier ist abgeleitet: Stufe aus den Punkten, Serie und Tagesauftrag
aus den bestandenen Abgaben, Meisterschaft aus den Punkten je Bereich,
Erfolge aus Kennzahlen. Gespeichert werden nur die Abgaben, der beste
Versuch je Aufgabe und die Gutschriften erledigter Tagesaufträge.
"""

from datetime import date
from typing import Literal

from pydantic import BaseModel

Rang = Literal["bronze", "silber", "gold"]
ErfolgsGruppe = Literal["meilensteine", "serie", "technik", "spiele"]
BestwertArt = Literal["zeichen", "laufzeit", "sterne"]


class StufenStand(BaseModel):
    stufe: int
    titel: str
    punkte: int
    # Punkte, ab denen die Stufe gilt, und ab denen die nächste gilt
    ab: int
    bis: int
    naechster_titel: str | None = None
    naechster_titel_ab_stufe: int | None = None


class SerienStand(BaseModel):
    aktuell: int = 0
    laengste: int = 0
    heute_geuebt: bool = False
    schilde: int = 0
    schilde_max: int = 0
    # Tage Serie bis zum nächsten Schutzschild; None, wenn alle Schilde da sind
    naechster_schild_in: int | None = None


class AuftragsZiel(BaseModel):
    id: str
    text: str
    erledigt: bool


class Tagesauftrag(BaseModel):
    datum: date
    ziele: list[AuftragsZiel]
    erledigt: bool
    bonus: int
    gutgeschrieben: bool


class BereichStand(BaseModel):
    """Meisterschaft eines Bereichs: eine Sprache oder die Spiele."""

    id: str
    titel: str
    punkte: int
    moeglich: int
    anteil: float
    rang: Rang | None = None


class ErfolgStand(BaseModel):
    id: str
    gruppe: ErfolgsGruppe
    # Titel der erreichten Stufe, vorher der ersten
    titel: str
    beschreibung: str
    icon: str
    rang: Rang | None = None
    wert: int
    # Schwelle der nächsten Stufe, nach der letzten deren Schwelle
    ziel: int
    erreicht: bool


class ErfolgsListe(BaseModel):
    eintraege: list[ErfolgStand]
    erreicht: int
    gesamt: int


class Spielstand(BaseModel):
    """Was Kopf und Startseite zeigen."""

    punkte: int
    stufe: StufenStand
    serie: SerienStand
    auftrag: Tagesauftrag
    meisterschaft: list[BereichStand]


class Bestwert(BaseModel):
    art: BestwertArt
    neu: float
    vorher: float


class Belohnung(BaseModel):
    """Was ein bestandener Versuch eingebracht hat (Belohnungsband)."""

    # Zuwachs der Aufgabe (bester Versuch zählt), was dieser Versuch für sich
    # bringt und was die Aufgabe höchstens bringt; der Tagesauftrag kommt dazu
    punkte: int
    punkte_versuch: int
    punkte_moeglich: int
    hinweise: int
    aufgegeben: bool
    wiederholung: bool
    erster_versuch: bool
    sterne: int | None = None
    stufe_vorher: int
    stufe: StufenStand
    neue_erfolge: list[ErfolgStand]
    bestwerte: list[Bestwert]
    auftrag_bonus: int
    auftrag: Tagesauftrag
