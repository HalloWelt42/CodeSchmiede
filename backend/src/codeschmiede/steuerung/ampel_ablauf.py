"""Abläufe der Ampelschule: wer wann ankommt, wann Nacht ist, was ausfällt.

In der Level-Datei steht der Verkehr knapp (feste Zeiten, Takt oder Zufall je Sekunde, für einen Weg, eine Zufahrt
oder einen Überweg). `ausbreiten` macht daraus die Liste der Ankünfte, die Welt und Sandbox bekommen. Der Zufall hat
einen festen Startwert aus dem Namen des Ablaufs: derselbe Ablauf bringt immer denselben Verkehr.
"""

import random
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .ampel_anlage import Anlage


class Verkehr(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # genau eins: ein Weg, alle Wege einer Zufahrt (gemischt) oder ein Überweg (beide Gehrichtungen gemischt)
    weg: str | None = None
    zufahrt: str | None = None
    ueberweg: str | None = None
    art: Literal["auto", "lkw", "einsatz"] = "auto"
    um: list[float] = Field(default_factory=list)
    alle: float | None = Field(default=None, gt=0)
    zufall: float | None = Field(default=None, gt=0, le=1)
    ab: float = Field(default=0, ge=0)
    bis: float | None = None

    @model_validator(mode="after")
    def _eindeutig(self) -> "Verkehr":
        if sum(x is not None for x in (self.weg, self.zufahrt, self.ueberweg)) != 1:
            raise ValueError("genau eins von weg, zufahrt, ueberweg")
        if not self.um and self.alle is None and self.zufall is None:
            raise ValueError("um, alle oder zufall angeben")
        return self


class Stoerung(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # die Kontaktschleife dieser Gruppe meldet ab dann nichts mehr
    gruppe: str
    ab: int = Field(ge=0)


class Ablauf(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    dauer: int = Field(ge=10, le=600)
    verkehr: list[Verkehr] = Field(min_length=1)
    nacht: list[tuple[int, int]] = Field(default_factory=list)
    stoerung: Stoerung | None = None


def befunde(ablauf: Ablauf, anlage: Anlage) -> list[str]:
    """Verweise auf Wege, Zufahrten und Gruppen, die es in der Anlage nicht gibt."""
    wege = {w.id for w in anlage.wege}
    gruppen = {g.name for g in anlage.gruppen}
    meldungen = []
    for v in ablauf.verkehr:
        if v.weg is not None and v.weg not in wege:
            meldungen.append(f"{ablauf.name}: Weg {v.weg} gibt es nicht")
        if v.zufahrt is not None and not anlage.zufahrt_wege(v.zufahrt):
            meldungen.append(f"{ablauf.name}: Zufahrt {v.zufahrt} gibt es nicht")
        if v.ueberweg is not None and not anlage.ueberweg_wege(v.ueberweg):
            meldungen.append(f"{ablauf.name}: Überweg {v.ueberweg} gibt es nicht")
    if ablauf.stoerung is not None and ablauf.stoerung.gruppe not in gruppen:
        meldungen.append(f"{ablauf.name}: Störung für unbekannte Gruppe {ablauf.stoerung.gruppe}")
    return meldungen


def ausbreiten(ablauf: Ablauf, anlage: Anlage) -> dict:
    """Die Ankünfte eines Ablaufs, nach Zeit geordnet, so wie Welt und Sandbox sie lesen."""
    zufall = random.Random(f"ampel:{ablauf.name}")
    ankuenfte = []
    for v in ablauf.verkehr:
        if v.ueberweg is not None:
            wege, art = anlage.ueberweg_wege(v.ueberweg), "fuss"
        elif v.zufahrt is not None:
            wege, art = anlage.zufahrt_wege(v.zufahrt), v.art
        else:
            wege, art = [v.weg], v.art
        ende = min(v.bis if v.bis is not None else ablauf.dauer, ablauf.dauer)
        zeiten = [t for t in v.um if t < ablauf.dauer]
        if v.alle is not None:
            t = v.ab
            while t < ende:
                zeiten.append(t)
                t += v.alle
        if v.zufall is not None:
            for sekunde in range(int(v.ab), int(ende)):
                if zufall.random() < v.zufall:
                    zeiten.append(sekunde + zufall.randrange(4) * 0.25)
        for t in zeiten:
            ankuenfte.append({"t": round(t, 2), "weg": zufall.choice(wege), "art": art})
    ankuenfte.sort(key=lambda a: (a["t"], a["weg"]))
    return {
        "name": ablauf.name,
        "dauer": ablauf.dauer,
        "ankuenfte": ankuenfte,
        "nacht": [list(n) for n in ablauf.nacht],
        "stoerung": ablauf.stoerung.model_dump() if ablauf.stoerung else None,
    }
