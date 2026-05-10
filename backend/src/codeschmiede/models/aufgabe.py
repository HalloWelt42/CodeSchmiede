"""Datenmodelle für Aufgaben.

Ein Aufgabenfile besteht aus YAML-Frontmatter und Markdown-Beschreibung.
`Frontmatter` modelliert die Metadaten, `Aufgabe` ist Frontmatter plus
Beschreibung und Datei-Info (Pfad, Hash). Für die API werden
schmalere Sichten daraus abgeleitet.

Schwierigkeit ist ein freier String -- die gültigen IDs werden
zur Laufzeit gegen die `_konfig.yml` validiert (oder nur dort gepflegt).
Frontmatter erlaubt zusätzliche Felder (`extra="allow"`), damit neue
Aufgabentypen (z.B. `output_quiz` mit `quiz`-Feld) ohne Schema-
Erweiterung funktionieren.
"""

from datetime import date
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


# Schwierigkeit ist ein freier String. Welche IDs erlaubt sind, steht in
# `_konfig.yml` -- nicht im Code.
Schwierigkeit = str


class Quelle(BaseModel):
    url: str | None = None
    notiz: str | None = None


class Hint(BaseModel):
    kosten: int = Field(ge=0)
    text: str


class TestFall(BaseModel):
    """Ein einzelner Test: positionale Argumente und erwartetes Ergebnis."""

    input: list[Any] = Field(default_factory=list)
    expected: Any = None


class Frontmatter(BaseModel):
    """Schema des YAML-Frontmatter-Blocks am Anfang jeder Aufgabe-Datei.

    `extra="allow"` erlaubt zusätzliche Felder pro Aufgabentyp -- z.B.
    `quiz` für `task_type=output_quiz`. Diese landen im `extra`-Dict des
    Pydantic-Models und werden vom jeweiligen Pruefer interpretiert.
    """

    model_config = ConfigDict(extra="allow")

    schema_version: int = 1
    id: str
    revision: int = 1
    titel: str
    sprache: str
    task_type: str = "code_schreiben"
    runner_type: str = "docker_python"
    schwierigkeit: Schwierigkeit
    schwierigkeit_score: int = Field(ge=1, le=100)
    schaetz_minuten: int = Field(ge=1)
    tags: list[str] = Field(default_factory=list)
    pfade: list[str] = Field(default_factory=list)
    voraussetzungen: list[str] = Field(default_factory=list)
    quelle: Quelle = Field(default_factory=Quelle)
    lizenz: str = "eigen"
    autor: str | None = None
    erstellt_am: date | None = None
    zeitlimit_sekunden: int = Field(default=5, ge=1, le=60)
    funktion: str | None = None
    hints: list[Hint] = Field(default_factory=list)
    tests_sichtbar: list[TestFall] = Field(default_factory=list)
    tests_versteckt: list[TestFall] = Field(default_factory=list)
    starter_code: str = ""


class Aufgabe(Frontmatter):
    """Vollständige Aufgabe: Frontmatter + Markdown-Beschreibung + Datei-Info."""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="allow")

    beschreibung_md: str
    dateipfad: Path
    hash: str  # SHA1 über den gesamten Datei-Inhalt


class AufgabeKurz(BaseModel):
    """Listen-Sicht. Bewusst schmal, damit `GET /api/aufgaben` schnell bleibt.

    Enthält das berechnete Feld `gesperrt` plus die offenen
    Voraussetzungen, sodass die Liste direkt anzeigen kann, was noch
    fehlt.
    """

    id: str
    titel: str
    sprache: str
    schwierigkeit: Schwierigkeit
    schwierigkeit_score: int
    schaetz_minuten: int
    tags: list[str]
    pfade: list[str]
    revision: int
    voraussetzungen: list[str] = Field(default_factory=list)
    voraussetzungen_offen: list[str] = Field(default_factory=list)
    gesperrt: bool = False


class AufgabeDetail(BaseModel):
    """Detail-Sicht. Enthält sichtbare Tests, aber nie `tests_versteckt`.

    `extra` enthält Aufgabentyp-spezifische Zusatzfelder aus dem
    Frontmatter (z.B. `quiz` für Output-Quiz-Aufgaben).
    """

    schema_version: int
    id: str
    revision: int
    titel: str
    sprache: str
    task_type: str
    runner_type: str
    schwierigkeit: Schwierigkeit
    schwierigkeit_score: int
    schaetz_minuten: int
    tags: list[str]
    pfade: list[str]
    voraussetzungen: list[str]
    voraussetzungen_offen: list[str] = Field(default_factory=list)
    gesperrt: bool = False
    quelle: Quelle
    lizenz: str
    autor: str | None
    erstellt_am: date | None
    zeitlimit_sekunden: int
    funktion: str | None
    hints: list[Hint]
    tests_sichtbar: list[TestFall]
    starter_code: str
    beschreibung_md: str
    anzahl_versteckte_tests: int
    extra: dict[str, Any] = Field(default_factory=dict)
