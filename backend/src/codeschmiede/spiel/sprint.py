"""SprintDienst - Runden des Ausgabe-Sprints.

Eine Runde zieht Fragen aus dem Vorrat des Levels und mischt die
Antworten. Der Browser bekommt Code und Optionen, die richtige Antwort
erst nach seiner Wahl; gewählt wird der Reihe nach und nur bis zur Frist
(plus kurzer Nachfrist für die Leitung). Abgeschlossen wird, wenn alle
Fragen beantwortet sind oder die Zeit um ist; offene Fragen zählen als
falsch. Der Abschluss wird wie jede Abgabe verbucht (Punkte, Sterne,
Serie, Tagesauftrag), die Erklärungen kommen mit der Auswertung.
"""

import json
import random
import secrets
from collections.abc import Callable
from datetime import datetime, timedelta, timezone

from ..models.aufgabe import Aufgabe
from ..models.sprint import (
    GespeicherteRunde,
    GestellteFrage,
    SprintAbschluss,
    SprintAuswertung,
    SprintFrage,
    SprintRueckmeldung,
    SprintRunde,
)
from ..pruefung.ergebnis import PruefErgebnis, TestErgebnis
from ..pruefung.sprint_pruefer import SprintLevel, level_von, wertung
from .bestand import Bestand
from .dienst import Spieldienst
from .sprint_runden import SprintRundenRepository

NACHFRIST = timedelta(seconds=3)


class RundeNichtGefunden(LookupError):
    pass


class RundeVorbei(ValueError):
    """Die Runde nimmt nichts mehr an (ausgewertet, Zeit um, Level geändert)."""


class FalscheAntwort(ValueError):
    """Die Anfrage passt nicht zur Runde (Reihenfolge, Stelle)."""


def jetzt() -> datetime:
    return datetime.now(timezone.utc)


class SprintDienst:
    def __init__(
        self,
        runden: SprintRundenRepository,
        spiel: Spieldienst,
        zufall: random.Random | None = None,
        uhr: Callable[[], datetime] = jetzt,
    ):
        self.runden = runden
        self.spiel = spiel
        self.zufall = zufall or random.Random()
        self.uhr = uhr

    def neue_runde(self, aufgabe: Aufgabe) -> SprintRunde:
        level = level_von(aufgabe)
        fragen = []
        for i in self.zufall.sample(range(len(level.schnipsel)), level.fragen):
            reihenfolge = list(range(len(level.schnipsel[i].optionen)))
            self.zufall.shuffle(reihenfolge)
            fragen.append(GestellteFrage(schnipsel=i, reihenfolge=reihenfolge))
        start = self.uhr()
        runde = GespeicherteRunde(
            id=secrets.token_urlsafe(12),
            aufgabe_id=aufgabe.id,
            aufgabe_revision=aufgabe.revision,
            fragen=fragen,
            antworten=[None] * len(fragen),
            gestartet=start,
            frist=start + timedelta(seconds=level.sekunden),
        )
        self.runden.anlegen(runde)
        return SprintRunde(
            id=runde.id,
            aufgabe_id=aufgabe.id,
            sekunden=level.sekunden,
            fragen=[
                SprintFrage(
                    code=level.schnipsel[f.schnipsel].code,
                    optionen=[level.schnipsel[f.schnipsel].optionen[k] for k in f.reihenfolge],
                )
                for f in fragen
            ],
        )

    def antworte(self, runde_id: str, frage: int, wahl: int, bestand: Bestand) -> SprintRueckmeldung:
        runde, _, level = self._laden(runde_id, bestand)
        if runde.abgeschlossen:
            raise RundeVorbei("Die Runde ist schon ausgewertet")
        if self.uhr() > runde.frist + NACHFRIST:
            raise RundeVorbei("Die Zeit ist um")
        if 0 <= frage < len(runde.antworten) and runde.antworten[frage] is not None:
            raise RundeVorbei("Die Frage ist schon beantwortet")
        offen = next((i for i, a in enumerate(runde.antworten) if a is None), None)
        if frage != offen:
            raise FalscheAntwort("Die Fragen kommen der Reihe nach")
        gestellt = runde.fragen[frage]
        if not 0 <= wahl < len(gestellt.reihenfolge):
            raise FalscheAntwort("Diese Antwort gibt es nicht")
        if not self.runden.antworte(runde_id, frage, wahl):
            raise RundeVorbei("Die Frage ist schon beantwortet")
        richtige_wahl = gestellt.reihenfolge.index(level.schnipsel[gestellt.schnipsel].richtig)
        return SprintRueckmeldung(richtig=wahl == richtige_wahl, richtige_wahl=richtige_wahl)

    def abschliessen(self, runde_id: str, bestand: Bestand) -> SprintAbschluss:
        runde, aufgabe, level = self._laden(runde_id, bestand)
        ende = self.uhr()
        if None in runde.antworten and ende < runde.frist:
            raise FalscheAntwort("Die Runde läuft noch")
        if not self.runden.abschliessen(runde_id):
            raise RundeVorbei("Die Runde ist schon ausgewertet")

        auswertung = self._auswertung(runde, level)
        treffer = sum(1 for z in auswertung if z.gewaehlt == z.richtig)
        w = wertung(level, treffer)
        sekunden = (min(ende, runde.frist) - runde.gestartet).total_seconds()
        ergebnis = PruefErgebnis(
            bestanden=w.sterne >= 1,
            sichtbar=[
                TestErgebnis(
                    index=i,
                    bestanden=z.gewaehlt == z.richtig,
                    eingabe=[z.code],
                    erwartet=z.optionen[z.richtig],
                    tatsaechlich=None if z.gewaehlt is None else z.optionen[z.gewaehlt],
                )
                for i, z in enumerate(auswertung)
            ],
            versteckt_pass=0,
            versteckt_fail=0,
            laufzeit_ms=sekunden * 1000,
            wertung=w,
        )
        code = json.dumps({"treffer": treffer, "fragen": level.fragen, "antworten": runde.antworten})
        verbucht = self.spiel.verbuche(bestand, aufgabe, code, ergebnis)
        return SprintAbschluss(
            bestanden=ergebnis.bestanden,
            sterne=w.sterne,
            treffer=treffer,
            fragen=level.fragen,
            laengste_kette=laengste_kette([z.gewaehlt == z.richtig for z in auswertung]),
            sekunden=sekunden,
            auswertung=auswertung,
            progress=verbucht.progress,
            belohnung=verbucht.belohnung,
        )

    def _laden(self, runde_id: str, bestand: Bestand) -> tuple[GespeicherteRunde, Aufgabe, SprintLevel]:
        runde = self.runden.hole(runde_id)
        aufgabe = bestand.aufgaben.get(runde.aufgabe_id) if runde else None
        if runde is None or aufgabe is None:
            raise RundeNichtGefunden("Diese Runde gibt es nicht")
        if aufgabe.revision != runde.aufgabe_revision:
            raise RundeVorbei("Das Level wurde inzwischen geändert; bitte eine neue Runde starten")
        return runde, aufgabe, level_von(aufgabe)

    @staticmethod
    def _auswertung(runde: GespeicherteRunde, level: SprintLevel) -> list[SprintAuswertung]:
        zeilen = []
        for gestellt, gewaehlt in zip(runde.fragen, runde.antworten):
            s = level.schnipsel[gestellt.schnipsel]
            zeilen.append(SprintAuswertung(
                code=s.code,
                optionen=[s.optionen[k] for k in gestellt.reihenfolge],
                gewaehlt=gewaehlt,
                richtig=gestellt.reihenfolge.index(s.richtig),
                warum=s.warum,
            ))
        return zeilen


def laengste_kette(richtig: list[bool]) -> int:
    laengste = lauf = 0
    for ok in richtig:
        lauf = lauf + 1 if ok else 0
        laengste = max(laengste, lauf)
    return laengste
