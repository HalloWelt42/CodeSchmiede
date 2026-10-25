"""Sicht der Spielmechanik auf den Aufgabenbestand."""

from dataclasses import dataclass, field

from ..models.aufgabe import Aufgabe
from ..models.konfig import Konfiguration
from ..models.pfad import Pfad


@dataclass(frozen=True)
class Bestand:
    aufgaben: dict[str, Aufgabe]
    pfade: list[Pfad]
    konfig: Konfiguration
    spieltypen: frozenset[str] = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "spieltypen", frozenset(self.konfig.spieltypen()))

    @classmethod
    def aus(cls, aufgaben: list[Aufgabe], pfade: list[Pfad], konfig: Konfiguration) -> "Bestand":
        return cls({a.id: a for a in aufgaben}, pfade, konfig)

    def ist_spiel(self, aufgabe_id: str) -> bool:
        aufgabe = self.aufgaben.get(aufgabe_id)
        return aufgabe is not None and aufgabe.task_type in self.spieltypen

    def hat_spiele(self) -> bool:
        return any(a.task_type in self.spieltypen for a in self.aufgaben.values())

    def hat_aufgaben(self) -> bool:
        return any(a.task_type not in self.spieltypen for a in self.aufgaben.values())
