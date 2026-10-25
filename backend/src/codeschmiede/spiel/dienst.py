"""Spieldienst - rechnet den Spielstand aus Abgaben, Fortschritt und
Gutschriften und verbucht Abgaben samt Belohnung.

Eine Abgabe verbuchen heißt: Abgabe speichern, Fortschritt fortschreiben,
einen erledigten Tagesauftrag gutschreiben und aus dem Stand vorher und
nachher die Belohnung ablesen. Die Regeln selbst stehen in den
Nachbarmodulen und sind reine Funktionen.
"""

from dataclasses import dataclass
from datetime import date

from ..aufgaben.repository import AufgabenRepository
from ..models.aufgabe import Aufgabe
from ..models.konfig import SpielRegeln
from ..models.progress import Progress
from ..models.spiel import (
    Belohnung,
    Bestwert,
    ErfolgsListe,
    LevelStand,
    SerienStand,
    SpielUebersicht,
    Spielstand,
    StufenStand,
    Tagesauftrag,
)
from ..progress.repository import ProgressRepository
from ..progress.submissions import (
    BestandeneAbgabe,
    Bestwerte,
    SubmissionRepository,
    codelaenge,
)
from ..pruefung.ergebnis import Kennwerte, PruefErgebnis
from ..pruefung.registry import hole
from .auftrag import tagesauftrag
from .bestand import Bestand
from .erfolge import Kennzahlen, erfolge, neu_erreicht
from .gutschriften import GutschriftRepository
from .meisterschaft import meisterschaft
from .serie import serie_aus_tagen
from .stufe import stufe_aus_punkten


@dataclass(frozen=True)
class Lage:
    """Spielstand eines Augenblicks; Grundlage für Anzeige und Belohnung."""

    punkte: int
    stufe: StufenStand
    serie: SerienStand
    auftrag: Tagesauftrag
    erfolge: ErfolgsListe
    progress: list[Progress]


@dataclass(frozen=True)
class Verbuchung:
    submission_id: int
    progress: Progress
    # nur bei bestandenen Abgaben
    belohnung: Belohnung | None


def neue_bestwerte(
    alt: Bestwerte, zeichen: int | None, laufzeit_ms: float, sterne: int | None, regeln: SpielRegeln
) -> list[Bestwert]:
    """Was dieser Versuch besser macht als alle bestandenen davor."""
    neu: list[Bestwert] = []
    if zeichen is not None and alt.zeichen is not None and zeichen < alt.zeichen:
        neu.append(Bestwert(art="zeichen", neu=zeichen, vorher=alt.zeichen))
    if alt.laufzeit_ms and 0 < laufzeit_ms < alt.laufzeit_ms * regeln.bestwert_laufzeit_anteil:
        neu.append(Bestwert(art="laufzeit", neu=laufzeit_ms, vorher=alt.laufzeit_ms))
    if sterne is not None and alt.sterne is not None and sterne > alt.sterne:
        neu.append(Bestwert(art="sterne", neu=sterne, vorher=alt.sterne))
    return neu


class Spieldienst:
    def __init__(
        self,
        progress: ProgressRepository,
        submissions: SubmissionRepository,
        gutschriften: GutschriftRepository,
        aufgaben: AufgabenRepository,
    ):
        self.progress = progress
        self.submissions = submissions
        self.gutschriften = gutschriften
        self.aufgaben = aufgaben

    def stand(self, bestand: Bestand, heute: date | None = None) -> Spielstand:
        lage = self._lage(bestand, heute or date.today())
        return Spielstand(
            punkte=lage.punkte,
            stufe=lage.stufe,
            serie=lage.serie,
            auftrag=lage.auftrag,
            meisterschaft=meisterschaft(bestand, lage.progress),
        )

    def erfolge(self, bestand: Bestand, heute: date | None = None) -> ErfolgsListe:
        return self._lage(bestand, heute or date.today()).erfolge

    def spiele(self, bestand: Bestand) -> list[SpielUebersicht]:
        progress = {p.aufgabe_id: p for p in self.progress.hole_alle_progress()}
        heute = self.submissions.heute_je_aufgabe()
        uebersicht = []
        for spiel in bestand.konfig.spiele:
            levels = []
            for nummer, aufgabe in enumerate(bestand.levels(spiel), start=1):
                p = progress.get(aufgabe.id)
                levels.append(LevelStand(
                    id=aufgabe.id,
                    titel=aufgabe.titel,
                    nummer=nummer,
                    geloest=p is not None and p.status == "geloest",
                    sterne=p.sterne if p else None,
                ))
            punkte = sum(progress[lv.id].punkte_erreicht for lv in levels if lv.id in progress)
            uebersicht.append(SpielUebersicht(
                id=spiel.id,
                titel=spiel.titel,
                icon=spiel.icon,
                beschreibung=spiel.beschreibung,
                aufgabentyp=spiel.aufgabentyp,
                levels_als=spiel.levels_als,
                levels=levels,
                geschafft=sum(1 for lv in levels if lv.geloest),
                sterne=sum(lv.sterne or 0 for lv in levels),
                sterne_moeglich=3 * len(levels),
                punkte=punkte,
                moeglich=sum(bestand.aufgaben[lv.id].schwierigkeit_score for lv in levels),
                versuche_heute=sum(heute.get(lv.id, 0) for lv in levels),
                naechstes=next((lv for lv in levels if not lv.geloest), None),
            ))
        return uebersicht

    def verbuche(
        self, bestand: Bestand, aufgabe: Aufgabe, code: str, ergebnis: PruefErgebnis, heute: date | None = None
    ) -> Verbuchung:
        heute = heute or date.today()
        regeln = bestand.konfig.spiel
        pruefer = hole(aufgabe.task_type)
        vergleicht_zeichen = pruefer.vergleicht_zeichen if pruefer else True

        vorher = self._lage(bestand, heute)
        bisher = self.progress.hole_progress(aufgabe.id) or Progress(aufgabe_id=aufgabe.id, status="neu")
        wertung = ergebnis.wertung
        sterne = wertung.sterne if wertung else None
        kennwerte = wertung.kennwerte.model_copy() if wertung else Kennwerte()
        zeichen = codelaenge(code) if vergleicht_zeichen else None
        if ergebnis.bestanden and zeichen is not None:
            muster = self.aufgaben.kuerzeste_musterloesung(aufgabe.id)
            if muster is not None:
                kennwerte.kuerzer_als_muster = zeichen < muster
        bisherige_bestwerte = self.submissions.bestwerte(aufgabe.id)

        submission_id = self.submissions.speichere(
            aufgabe,
            code,
            ergebnis.bestanden,
            ergebnis.laufzeit_ms,
            ohne_hilfe=bisher.hints_genutzt == 0 and not bisher.aufgegeben,
            sterne=sterne,
            kennwerte=kennwerte,
        )
        progress = self.progress.aktualisiere_nach_submission(aufgabe, ergebnis.bestanden, sterne, heute)
        if not ergebnis.bestanden:
            return Verbuchung(submission_id, progress, None)

        nachher = self._lage(bestand, heute)
        bonus = 0
        if nachher.auftrag.erledigt and not nachher.auftrag.gutgeschrieben:
            if self.gutschriften.schreibe(heute, regeln.auftrag_bonus):
                bonus = regeln.auftrag_bonus
            nachher = self._lage(bestand, heute)

        belohnung = Belohnung(
            punkte=progress.punkte_erreicht - bisher.punkte_erreicht,
            punkte_versuch=0 if bisher.aufgegeben
            else self.progress.berechne_punkte(aufgabe, bisher.hints_genutzt, sterne),
            punkte_moeglich=aufgabe.schwierigkeit_score,
            hinweise=bisher.hints_genutzt,
            aufgegeben=bisher.aufgegeben,
            wiederholung=bisher.status == "geloest",
            erster_versuch=bisher.versuche == 0,
            sterne=sterne,
            stufe_vorher=vorher.stufe.stufe,
            stufe=nachher.stufe,
            neue_erfolge=neu_erreicht(vorher.erfolge, nachher.erfolge),
            bestwerte=neue_bestwerte(bisherige_bestwerte, zeichen, ergebnis.laufzeit_ms, sterne, regeln),
            auftrag_bonus=bonus,
            auftrag=nachher.auftrag,
        )
        return Verbuchung(submission_id, progress, belohnung)

    # --- Stand ------------------------------------------------------------

    def _lage(self, bestand: Bestand, heute: date) -> Lage:
        regeln = bestand.konfig.spiel
        abgaben = self.submissions.bestandene_abgaben()
        progress = self.progress.hole_alle_progress()
        gutschriften = self.gutschriften.alle()

        punkte = sum(p.punkte_erreicht for p in progress) + sum(gutschriften.values())
        serie = serie_aus_tagen((a.tag for a in abgaben), heute, regeln)
        auftrag = tagesauftrag(
            heute,
            [a for a in abgaben if a.tag == heute],
            bestand,
            regeln.auftrag_bonus,
            heute in gutschriften,
        )
        kennzahlen = self._kennzahlen(bestand, abgaben, progress, serie, len(gutschriften))
        return Lage(
            punkte=punkte,
            stufe=stufe_aus_punkten(punkte, regeln),
            serie=serie,
            auftrag=auftrag,
            erfolge=erfolge(kennzahlen),
            progress=progress,
        )

    def _kennzahlen(
        self,
        bestand: Bestand,
        abgaben: list[BestandeneAbgabe],
        progress: list[Progress],
        serie: SerienStand,
        auftraege: int,
    ) -> Kennzahlen:
        geloest = {p.aufgabe_id for p in progress if p.status == "geloest" and p.aufgabe_id in bestand.aufgaben}
        return Kennzahlen(
            geloest=len(geloest),
            ohne_hilfe=len({a.aufgabe_id for a in abgaben if a.ohne_hilfe}),
            erster_versuch=self.submissions.erste_versuche_bestanden(),
            kuerzer_als_muster=len({a.aufgabe_id for a in abgaben if a.kennwerte.kuerzer_als_muster}),
            sprachen_geloest=len({bestand.aufgaben[a].sprache for a in geloest}),
            sprachen_gesamt=len({a.sprache for a in bestand.aufgaben.values()}),
            pfade_komplett=sum(
                1 for p in bestand.pfade if p.reihenfolge and all(a in geloest for a in p.reihenfolge)
            ),
            pfade_gesamt=sum(1 for p in bestand.pfade if p.reihenfolge),
            serie_laengste=serie.laengste,
            auftraege=auftraege,
            levels_je_typ=self._zaehle_je_typ(bestand, bestand.aufgaben),
            drei_sterne_je_typ=self._zaehle_je_typ(bestand, {p.aufgabe_id for p in progress if p.sterne == 3}),
            volle_runden=sum(
                1 for a in abgaben if a.kennwerte.treffer is not None and a.kennwerte.treffer == a.kennwerte.fragen
            ),
        )

    @staticmethod
    def _zaehle_je_typ(bestand: Bestand, ids) -> dict[str, int]:
        zahlen: dict[str, int] = {}
        for aid in ids:
            aufgabe = bestand.aufgaben.get(aid)
            if aufgabe is not None and aufgabe.task_type in bestand.spieltypen:
                zahlen[aufgabe.task_type] = zahlen.get(aufgabe.task_type, 0) + 1
        return zahlen
