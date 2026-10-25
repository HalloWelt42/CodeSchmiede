"""Pruefer für `task_type: ausgabe_sprint` (Spiel Ausgabe-Sprint).

Ein Sprint-Level ist eine Kategorie (Sprache und Stufe) mit einem Vorrat
an Schnipseln. Eine Runde zieht daraus Fragen und mischt die Antworten;
das läuft über spiel/sprint.py, darum ist der Abgabeweg "runde" und eine
direkte Abgabe wird abgelehnt. Hier stehen das Format der Level-Datei und
die Wertung einer Runde.

Im Frontmatter:
  sprint:
    fragen: 10                 je Runde
    sekunden: 90
    sterne: [6, 8, 10]         richtige Antworten für einen, zwei, drei Sterne
    schnipsel:
      - code: 'print(3 * "ab")'
        optionen: ["ababab", "ab3", "3ab", "Fehler"]
        richtig: 0
        warum: Ein Text mal einer Zahl wiederholt den Text.
Der ganze Vorrat bleibt im Backend; der Browser bekommt nur die Fragen
einer Runde und die richtige Antwort erst nach seiner Wahl.
"""

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, Wertung
from .registry import registriere

# Antworttext für Schnipsel, die mit einem Fehler abbrechen
FEHLER = "Fehler"


class Schnipsel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1)
    optionen: list[str] = Field(min_length=2, max_length=6)
    richtig: int = Field(ge=0)
    warum: str = Field(min_length=1)

    @model_validator(mode="after")
    def _richtig_vorhanden(self) -> "Schnipsel":
        if self.richtig >= len(self.optionen):
            raise ValueError("richtig zeigt auf keine Option")
        if len(set(self.optionen)) != len(self.optionen):
            raise ValueError("Optionen doppelt")
        return self


class SprintLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fragen: int = Field(default=10, ge=1)
    sekunden: int = Field(default=90, ge=10)
    sterne: tuple[int, int, int]
    schnipsel: list[Schnipsel]

    @model_validator(mode="after")
    def _stimmig(self) -> "SprintLevel":
        if len(self.schnipsel) < self.fragen:
            raise ValueError(f"nur {len(self.schnipsel)} Schnipsel für {self.fragen} Fragen")
        if not (0 < self.sterne[0] <= self.sterne[1] <= self.sterne[2] <= self.fragen):
            raise ValueError("sterne steigen von eins bis höchstens zur Zahl der Fragen")
        return self


def level_von(aufgabe: Aufgabe) -> SprintLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return SprintLevel.model_validate(extra.get("sprint"))


def wertung(level: SprintLevel, treffer: int) -> Wertung:
    kriterien = [
        SternKriterium(text=f"mindestens {schwelle} von {level.fragen} richtig", erreicht=treffer >= schwelle)
        for schwelle in level.sterne
    ]
    return Wertung(
        sterne=sum(1 for k in kriterien if k.erreicht),
        kriterien=kriterien,
        kennwerte=Kennwerte(treffer=treffer, fragen=level.fragen),
    )


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level_von(aufgabe)
    except ValidationError as fehler:
        return [f"sprint: {e['loc']} {e['msg']}" for e in fehler.errors()]
    return []


@registriere(
    "ausgabe_sprint",
    verbirgt=("sprint.schnipsel",),
    abgabe="runde",
    zaehle_versteckt=lambda aufgabe: 0,
    vergleicht_zeichen=False,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    raise ValueError("Ein Sprint wird über seine Runde abgegeben")
