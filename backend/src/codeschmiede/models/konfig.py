"""Konfigurations-Modelle. Werden aus `aufgaben/_konfig.yml` gelesen.

Damit lassen sich Schwierigkeitsstufen, Sprachen und Aufgabentypen
deklarativ definieren -- ohne Code-Aenderung. Frontend zieht die Konfig
ueber `/api/admin/konfig` und nutzt sie reaktiv.
"""

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
    runner_type: str  # Backend-Runner, der diese Sprache ausführt


class AufgabentypKonfig(BaseModel):
    """Ein Aufgabentyp -- bestimmt UI-View und Pruefer."""

    id: str  # z.B. "code_schreiben", "output_quiz"
    titel: str
    view: str  # Frontend-View-Schlüssel (Komponenten-Registry)
    beschreibung: str = ""


class Konfiguration(BaseModel):
    """Gesamte Konfiguration. Wird beim Backend-Start geladen."""

    schwierigkeiten: list[SchwierigkeitsStufe] = []
    sprachen: list[SprachKonfig] = []
    aufgabentypen: list[AufgabentypKonfig] = []

    def schwierigkeit_ids(self) -> set[str]:
        return {s.id for s in self.schwierigkeiten}

    def sprache_ids(self) -> set[str]:
        return {s.id for s in self.sprachen}

    def aufgabentyp_ids(self) -> set[str]:
        return {t.id for t in self.aufgabentypen}
