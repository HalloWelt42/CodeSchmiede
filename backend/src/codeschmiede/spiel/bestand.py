"""Sicht der Spielmechanik auf den Aufgabenbestand."""

from dataclasses import dataclass, field

from ..models.aufgabe import Aufgabe
from ..models.konfig import Konfiguration, SpielKonfig
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

    def levels(self, spiel: SpielKonfig) -> list[Aufgabe]:
        """Levels eines Spiels: in der Reihenfolge seiner Pfade, übrige nach ID."""
        vom_typ = {a.id: a for a in self.aufgaben.values() if a.task_type == spiel.aufgabentyp}
        pfade = {p.id: p for p in self.pfade}
        reihenfolge: list[str] = []
        for pid in spiel.pfade:
            if pid in pfade:
                reihenfolge += [aid for aid in pfade[pid].reihenfolge if aid in vom_typ and aid not in reihenfolge]
        reihenfolge += sorted(aid for aid in vom_typ if aid not in reihenfolge)
        return [vom_typ[aid] for aid in reihenfolge]
