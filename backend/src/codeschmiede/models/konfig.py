"""Konfigurations-Modelle. Werden aus `aufgaben/_konfig.yml` gelesen.

Damit lassen sich Schwierigkeitsstufen, Sprachen und Aufgabentypen
deklarativ definieren -- ohne Code-Aenderung. Frontend zieht die Konfig
ueber `/api/admin/konfig` und nutzt sie reaktiv.
"""

from typing import Literal

from pydantic import BaseModel, Field


class SchwierigkeitsStufe(BaseModel):
    """Eine Schwierigkeitsstufe."""

    id: str  # ASCII-Slug, z.B. "anfaenger"
    titel: str  # angezeigter Name, darf Umlaute haben
    farbe: str = "accent"  # Farb-Schluessel: green, orange, red, accent, info_blue, grau, oder beliebiger CSS-Wert
    score_max: int = Field(default=100, ge=1, le=1000)


class SprachKonfig(BaseModel):
    """Eine unterstützte Programmiersprache."""

    id: str  # z.B. "python"
    titel: str  # z.B. "Python"
    editor_lang: str  # CodeMirror-Sprach-Plugin-Schlüssel
    endung: str  # Dateiendung der Musterlösungen, z.B. "py"
    runner_type: str  # Wo der Code läuft (docker_python, docker_javascript, iframe_css, ...)


class AufgabentypKonfig(BaseModel):
    """Ein Aufgabentyp -- bestimmt UI-View und Pruefer."""

    id: str  # z.B. "code_schreiben", "output_quiz"
    titel: str
    view: str  # Frontend-View-Schlüssel (Komponenten-Registry)
    beschreibung: str = ""


class SpielKonfig(BaseModel):
    """Ein Spiel im Spielebereich. Seine Levels sind Aufgaben des
    Aufgabentyps; die Reihenfolge geben die Pfade vor."""

    id: str
    titel: str
    icon: str  # Font-Awesome-Klasse, z. B. "fa-crosshairs"
    beschreibung: str = ""
    aufgabentyp: str
    pfade: list[str] = Field(default_factory=list)
    # "stufen": Levels nacheinander (Leiste); "auswahl": gleichrangige Kategorien zum Wählen
    levels_als: Literal["stufen", "auswahl"] = "stufen"
    # wie ein Level heißt, etwa "Kapitel" im Krimi
    level_wort: str = "Level"


class Raenge(BaseModel):
    """Anteil der erreichbaren Punkte, ab dem ein Rang gilt."""

    bronze: float = Field(default=0.25, gt=0, le=1)
    silber: float = Field(default=0.5, gt=0, le=1)
    gold: float = Field(default=0.8, gt=0, le=1)


class SpielRegeln(BaseModel):
    """Schwellen der Spielmechanik (docs/SPIELE.md)."""

    # Stufe k gilt ab stufe_basis * k * k Punkten, die erste Stufe ab 0
    stufe_basis: int = Field(default=25, ge=1)
    # alle `titel_alle` Stufen der nächste Titel
    titel: list[str] = Field(
        default_factory=lambda: ["Lehrling", "Geselle", "Schmied", "Meister", "Großmeister"],
        min_length=1,
    )
    titel_alle: int = Field(default=5, ge=1)
    raenge: Raenge = Field(default_factory=Raenge)
    # je so viele Tage Serie ein Schutzschild, der einen verpassten Tag auffängt
    schild_alle_tage: int = Field(default=7, ge=1)
    schilde_max: int = Field(default=3, ge=0)
    auftrag_bonus: int = Field(default=10, ge=0)
    # ein schnellerer Lauf zählt als Bestwert erst ab diesem Anteil der alten Laufzeit
    bestwert_laufzeit_anteil: float = Field(default=0.8, gt=0, lt=1)


class Konfiguration(BaseModel):
    """Gesamte Konfiguration. Wird beim Backend-Start geladen."""

    schwierigkeiten: list[SchwierigkeitsStufe] = []
    sprachen: list[SprachKonfig] = []
    aufgabentypen: list[AufgabentypKonfig] = []
    spiele: list[SpielKonfig] = []
    spiel: SpielRegeln = Field(default_factory=SpielRegeln)

    def schwierigkeit_ids(self) -> set[str]:
        return {s.id for s in self.schwierigkeiten}

    def sprache_ids(self) -> set[str]:
        return {s.id for s in self.sprachen}

    def aufgabentyp_ids(self) -> set[str]:
        return {t.id for t in self.aufgabentypen}

    def spieltypen(self) -> set[str]:
        """Aufgabentypen, deren Aufgaben Levels eines Spiels sind."""
        return {s.aufgabentyp for s in self.spiele}
