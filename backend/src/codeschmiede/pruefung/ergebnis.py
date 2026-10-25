"""Ergebnis-Modelle einer Pruefung.

`TestErgebnis` ist ein einzelner sichtbarer Test. `PruefErgebnis` ist
die Antwort an das Frontend: aggregiert + Nutzerausgabe + Laufzeit.
Versteckte Tests werden nur als Anzahl durchgereicht (Anti-Hardcoding).
"""

from typing import Any, Literal

from pydantic import BaseModel, Field


class TestErgebnis(BaseModel):
    index: int
    bestanden: bool
    eingabe: list[Any] = []
    erwartet: Any = None
    tatsaechlich: Any = None
    fehler: str | None = None


class Kennwerte(BaseModel):
    """Messwerte eines Versuchs über das Bestehen hinaus, je Aufgabentyp
    gefüllt. Sie stehen mit der Abgabe in der Datenbank; Bestwerte und
    Erfolge leiten sich daraus ab."""

    # CSS: Anteil der Bildpunkte, die mit dem Ziel übereinstimmen, 0 bis 1
    deckung: float | None = Field(default=None, ge=0, le=1)
    # Roboter: Schritte in der sichtbaren Welt und Zeilen Code
    schritte: int | None = Field(default=None, ge=0)
    zeilen: int | None = Field(default=None, ge=0)
    # Sprint: richtige Antworten und Fragen der Runde
    treffer: int | None = Field(default=None, ge=0)
    fragen: int | None = Field(default=None, ge=0)
    # setzt die Verbuchung: weniger Zeichen als die kürzeste Musterlösung
    kuerzer_als_muster: bool | None = None


class SternKriterium(BaseModel):
    """Ein Stern und wofür er steht. "ergebnis" entscheidet der Prüfer;
    "ohne_hinweis" und "versuche" hängen vom Verlauf der Aufgabe ab und
    entscheidet die Verbuchung (spiel/dienst.py)."""

    text: str
    erreicht: bool
    art: Literal["ergebnis", "ohne_hinweis", "versuche"] = "ergebnis"
    # bei "versuche": höchstens so viele Prüfversuche
    grenze: int | None = None


class Wertung(BaseModel):
    """Sterne eines Levels: einer fürs Bestehen, zwei und drei für Güte
    nach den Schwellen der Level-Datei."""

    sterne: int = Field(ge=0, le=3)
    kriterien: list[SternKriterium] = Field(default_factory=list)
    kennwerte: Kennwerte = Field(default_factory=Kennwerte)


class PruefErgebnis(BaseModel):
    bestanden: bool
    sichtbar: list[TestErgebnis]
    versteckt_pass: int
    versteckt_fail: int
    laufzeit_ms: float
    stdout: str = ""
    stderr: str = ""
    timeout: bool = False
    # nur bei Aufgabentypen mit Sternen (Spiele, CSS)
    wertung: Wertung | None = None
