"""Vorgaben der Aufzugsteuerung aus der Level-Datei: das Haus und die Abläufe (wer wann wohin will).

Fahrgäste stehen knapp in der Level-Datei: feste Zeiten, Takt oder Zufall je Sekunde, Start und Ziel als Etage oder
"zufall". `ausbreiten` macht daraus die Liste, die Welt und Sandbox lesen. Der Zufall hat einen festen Startwert aus
dem Namen des Ablaufs: derselbe Ablauf bringt immer dieselben Fahrgäste.
"""

import random
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .aufzug_welt import GEWICHT

Zufall = Literal["zufall"]


class Haus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    etagen: int = Field(ge=2, le=12)
    aufzuege: list[str] = Field(default_factory=lambda: ["a"], min_length=1, max_length=3)
    plaetze: int = Field(default=6, ge=1, le=20)
    # Höchstlast in Kilogramm; ohne Angabe passen so viele Fahrgäste mit Normalgewicht, wie es Plätze gibt
    last: int | None = Field(default=None, ge=GEWICHT)
    start: int = Field(default=0, ge=0)

    @model_validator(mode="after")
    def _stimmig(self) -> "Haus":
        if self.start >= self.etagen:
            raise ValueError("start liegt über dem Haus")
        if len(set(self.aufzuege)) != len(self.aufzuege):
            raise ValueError("Aufzüge brauchen verschiedene Namen")
        return self

    def namen(self) -> list[str]:
        return ["EG", *[str(e) for e in range(1, self.etagen)]]

    def fuer_welt(self) -> dict:
        return {"etagen": self.etagen, "aufzuege": list(self.aufzuege), "plaetze": self.plaetze,
                "last": self.last or self.plaetze * GEWICHT, "start": self.start}


class Fahrt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    von: int | Zufall
    nach: int | list[int] | Zufall
    um: list[float] = Field(default_factory=list)
    alle: float | None = Field(default=None, gt=0)
    zufall: float | None = Field(default=None, gt=0, le=1)
    ab: float = Field(default=0, ge=0)
    bis: float | None = None
    gewicht: int = Field(default=GEWICHT, ge=10, le=1000)

    @model_validator(mode="after")
    def _zeiten(self) -> "Fahrt":
        if not self.um and self.alle is None and self.zufall is None:
            raise ValueError("um, alle oder zufall angeben")
        return self


class Ablauf(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    dauer: int = Field(ge=10, le=600)
    fahrgaeste: list[Fahrt] = Field(min_length=1)
    # ab dieser Sekunde Feueralarm
    feuer: int | None = Field(default=None, ge=0)


def befunde(ablauf: Ablauf, haus: Haus) -> list[str]:
    meldungen = []
    for f in ablauf.fahrgaeste:
        etagen = [f.von] if isinstance(f.von, int) else []
        etagen += f.nach if isinstance(f.nach, list) else [f.nach] if isinstance(f.nach, int) else []
        meldungen += [f"{ablauf.name}: Etage {e} gibt es nicht" for e in etagen if not 0 <= e < haus.etagen]
        if isinstance(f.von, int) and f.nach == f.von:
            meldungen.append(f"{ablauf.name}: Fahrt von {f.von} nach {f.nach} führt nirgends hin")
    return meldungen


def ausbreiten(ablauf: Ablauf, haus: Haus) -> dict:
    """Die Fahrgäste eines Ablaufs, nach Zeit geordnet, so wie Welt und Sandbox sie lesen."""
    zufall = random.Random(f"aufzug:{ablauf.name}")
    fahrgaeste = []
    for f in ablauf.fahrgaeste:
        ende = min(f.bis if f.bis is not None else ablauf.dauer, ablauf.dauer)
        zeiten = [t for t in f.um if t < ablauf.dauer]
        if f.alle is not None:
            t = f.ab
            while t < ende:
                zeiten.append(t)
                t += f.alle
        if f.zufall is not None:
            for sekunde in range(int(f.ab), int(ende)):
                if zufall.random() < f.zufall:
                    zeiten.append(sekunde + zufall.randrange(4) * 0.25)
        for t in zeiten:
            von = f.von if isinstance(f.von, int) else zufall.randrange(haus.etagen)
            if isinstance(f.nach, int):
                nach = f.nach
            else:
                moeglich = [e for e in (f.nach if isinstance(f.nach, list) else range(haus.etagen)) if e != von]
                nach = zufall.choice(moeglich)
            if nach != von:
                fahrgaeste.append({"t": round(t, 2), "von": von, "nach": nach, "gewicht": f.gewicht})
    fahrgaeste.sort(key=lambda g: (g["t"], g["von"], g["nach"]))
    return {"name": ablauf.name, "dauer": ablauf.dauer, "fahrgaeste": fahrgaeste, "feuer": ablauf.feuer}
