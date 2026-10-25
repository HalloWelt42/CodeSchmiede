"""Erfolge: ein Katalog aus Kennzahlen, gestuft in Bronze, Silber, Gold.

Jeder Eintrag nennt seinen Wert und seine Schwellen; ein Erfolg, für
den der Bestand nichts hergibt, steht nicht im Katalog. Neue Erfolge
brauchen nur einen Eintrag in `katalog` und, wenn nötig, eine Kennzahl.
"""

from collections.abc import Callable
from dataclasses import dataclass

from pydantic import BaseModel

from ..models.spiel import ErfolgsGruppe, ErfolgsListe, ErfolgStand, Rang

RAENGE_JE_STUFENZAHL: dict[int, tuple[Rang, ...]] = {
    1: ("gold",),
    2: ("silber", "gold"),
    3: ("bronze", "silber", "gold"),
}
RANG_NAME: dict[Rang, str] = {"bronze": "Bronze", "silber": "Silber", "gold": "Gold"}


class Kennzahlen(BaseModel):
    """Was die Erfolge zählen; der Spieldienst rechnet sie aus Abgaben und Fortschritt."""

    geloest: int = 0
    ohne_hilfe: int = 0
    erster_versuch: int = 0
    kuerzer_als_muster: int = 0
    sprachen_geloest: int = 0
    sprachen_gesamt: int = 0
    pfade_komplett: int = 0
    pfade_gesamt: int = 0
    serie_laengste: int = 0
    auftraege: int = 0


@dataclass(frozen=True)
class ErfolgDefinition:
    id: str
    gruppe: ErfolgsGruppe
    icon: str
    wert: int
    schwellen: tuple[int, ...]
    # Titel je Stufe; einer gilt für alle
    titel: tuple[str, ...]
    # was eine Schwelle verlangt, als Text
    was: Callable[[int], str]

    def titel_fuer(self, stufe_index: int) -> str:
        return self.titel[min(stufe_index, len(self.titel) - 1)]


def anzahl(n: int, einzahl: str, mehrzahl: str) -> str:
    return einzahl if n == 1 else f"{n} {mehrzahl}"


def bis_hoechstens(schwellen: tuple[int, ...], hoechstens: int) -> tuple[int, ...]:
    """Schwellen, die der Bestand hergibt; die oberste wird höchstens alles."""
    unten = tuple(s for s in schwellen if s < hoechstens)
    return unten + (hoechstens,) if len(unten) < len(schwellen) else unten


def katalog(k: Kennzahlen) -> list[ErfolgDefinition]:
    eintraege = [
        ErfolgDefinition(
            "geloest", "meilensteine", "fa-flag-checkered", k.geloest, (10, 50, 200),
            ("Zehn gelöst", "Fünfzig gelöst", "Zweihundert gelöst"),
            lambda n: f"{anzahl(n, 'eine Aufgabe', 'Aufgaben')} gelöst",
        ),
        ErfolgDefinition(
            "ohne_hilfe", "meilensteine", "fa-feather", k.ohne_hilfe, (10, 50, 150),
            ("Ohne Hilfe",),
            lambda n: f"{anzahl(n, 'eine Aufgabe', 'Aufgaben')} ohne Hinweis",
        ),
    ]
    if k.sprachen_gesamt > 1:
        eintraege.append(ErfolgDefinition(
            "sprachen", "meilensteine", "fa-language", k.sprachen_geloest, (k.sprachen_gesamt,),
            ("Alle Sprachen",),
            lambda n: "in jeder Sprache eine Aufgabe gelöst",
        ))
    if k.pfade_gesamt:
        eintraege.append(ErfolgDefinition(
            "pfade", "meilensteine", "fa-route", k.pfade_komplett,
            bis_hoechstens((1, 5, 15), k.pfade_gesamt),
            ("Pfad gegangen", "Fünf Pfade gegangen", "Alle Pfade gegangen"),
            lambda n: f"{anzahl(n, 'einen Pfad', 'Pfade')} vollständig gelöst",
        ))
    eintraege += [
        ErfolgDefinition(
            "serie", "serie", "fa-fire", k.serie_laengste, (7, 30, 100),
            ("Eine Woche am Stück", "Ein Monat am Stück", "Hundert Tage am Stück"),
            lambda n: f"{n} Tage am Stück",
        ),
        ErfolgDefinition(
            "auftraege", "serie", "fa-calendar-check", k.auftraege, (10, 50, 150),
            ("Tagesaufträge",),
            lambda n: f"{anzahl(n, 'ein Tagesauftrag', 'Tagesaufträge')} ganz erledigt",
        ),
        ErfolgDefinition(
            "kuerzer", "technik", "fa-compress", k.kuerzer_als_muster, (1, 10, 50),
            ("Kürzer als die Musterlösung",),
            lambda n: f"{anzahl(n, 'eine Aufgabe', 'Aufgaben')} mit weniger Zeichen als die Musterlösung",
        ),
        ErfolgDefinition(
            "erster_versuch", "technik", "fa-bolt", k.erster_versuch, (5, 10, 25),
            ("Erster Versuch",),
            lambda n: f"{anzahl(n, 'eine Aufgabe', 'Aufgaben')} im ersten Versuch bestanden",
        ),
    ]
    return eintraege


def stufen_erreicht(d: ErfolgDefinition) -> int:
    return sum(1 for s in d.schwellen if d.wert >= s)


def bewerte(d: ErfolgDefinition) -> ErfolgStand:
    erreicht = stufen_erreicht(d)
    raenge = RAENGE_JE_STUFENZAHL[len(d.schwellen)]
    rang = raenge[erreicht - 1] if erreicht else None
    naechste = d.schwellen[erreicht] if erreicht < len(d.schwellen) else None
    ziel = naechste if naechste is not None else d.schwellen[-1]

    if rang is None:
        beschreibung = d.was(ziel) + (f" ({d.wert} / {ziel})" if ziel > 1 else "")
    elif len(d.schwellen) == 1:
        beschreibung = d.was(ziel)
    else:
        beschreibung = f"{RANG_NAME[rang]}: {d.was(d.schwellen[erreicht - 1])}"
        if naechste is not None:
            beschreibung += f"; {RANG_NAME[raenge[erreicht]]} bei {naechste}"

    return ErfolgStand(
        id=d.id,
        gruppe=d.gruppe,
        titel=d.titel_fuer(max(erreicht - 1, 0)),
        beschreibung=beschreibung,
        icon=d.icon,
        rang=rang,
        wert=d.wert,
        ziel=ziel,
        erreicht=rang is not None,
    )


def erfolge(k: Kennzahlen) -> ErfolgsListe:
    eintraege = [bewerte(d) for d in katalog(k)]
    return ErfolgsListe(
        eintraege=eintraege,
        erreicht=sum(1 for e in eintraege if e.erreicht),
        gesamt=len(eintraege),
    )


def neu_erreicht(vorher: ErfolgsListe, nachher: ErfolgsListe) -> list[ErfolgStand]:
    """Erfolge, die seit `vorher` einen höheren Rang haben."""
    stufe = {e.id: _stufe(e) for e in vorher.eintraege}
    return [e for e in nachher.eintraege if _stufe(e) > stufe.get(e.id, 0)]


def _stufe(e: ErfolgStand) -> int:
    return 0 if e.rang is None else ("bronze", "silber", "gold").index(e.rang) + 1
