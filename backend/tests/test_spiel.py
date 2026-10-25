"""Spielmechanik: Regeln als reine Funktionen und die Verbuchung einer
Abgabe samt Belohnung. Ohne Sandbox: die Prüfergebnisse sind vorgegeben."""

from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.models.konfig import SpielKonfig, SpielRegeln
from codeschmiede.pruefung.ergebnis import Kennwerte, PruefErgebnis, Wertung
from codeschmiede.spiel.bestand import Bestand
from codeschmiede.spiel.erfolge import ErfolgDefinition, bewerte, bis_hoechstens
from codeschmiede.spiel.serie import serie_aus_tagen
from codeschmiede.spiel.stufe import stufe_aus_punkten
from codeschmiede.state import AppState

REGELN = SpielRegeln()
HEUTE = date(2026, 10, 25)


def tage(*abstaende: int) -> list[date]:
    """Tage relativ zu HEUTE, 0 ist heute, 1 gestern."""
    return [HEUTE - timedelta(days=a) for a in abstaende]


# --- Stufe ----------------------------------------------------------------


def test_stufe_beginnt_bei_eins():
    s = stufe_aus_punkten(0, REGELN)
    assert (s.stufe, s.titel, s.ab, s.bis) == (1, "Lehrling", 0, 100)
    assert (s.naechster_titel, s.naechster_titel_ab_stufe) == ("Geselle", 5)


def test_stufe_k_ab_25_k_quadrat():
    s = stufe_aus_punkten(1284, REGELN)
    assert (s.stufe, s.titel, s.ab, s.bis) == (7, "Geselle", 1225, 1600)
    assert (s.naechster_titel, s.naechster_titel_ab_stufe) == ("Schmied", 10)
    assert stufe_aus_punkten(1599, REGELN).stufe == 7
    assert stufe_aus_punkten(1600, REGELN).stufe == 8


def test_letzter_titel_bleibt():
    s = stufe_aus_punkten(25 * 30 * 30, REGELN)
    assert (s.stufe, s.titel, s.naechster_titel) == (30, "Großmeister", None)


# --- Serie ----------------------------------------------------------------


def test_serie_zaehlt_tage_am_stueck():
    s = serie_aus_tagen(tage(0, 1, 2), HEUTE, REGELN)
    assert (s.aktuell, s.laengste, s.heute_geuebt) == (3, 3, True)


def test_heute_noch_offen_reisst_nichts():
    s = serie_aus_tagen(tage(1, 2), HEUTE, REGELN)
    assert (s.aktuell, s.heute_geuebt) == (2, False)


def test_verpasster_tag_ohne_schild_reisst():
    s = serie_aus_tagen(tage(0, 2, 3, 4), HEUTE, REGELN)
    assert (s.aktuell, s.laengste) == (1, 3)


def test_schild_faengt_einen_tag_auf():
    # sieben Tage geübt (8 bis 14 zurück) geben einen Schild, Tag 7 fehlt
    geuebt = tage(*range(8, 15), *range(0, 7))
    s = serie_aus_tagen(geuebt, HEUTE, REGELN)
    assert s.aktuell == 14
    assert s.schilde == 1  # einer verbraucht, einer nach den nächsten sieben Tagen neu


def test_zwei_luecken_mit_einem_schild_reissen():
    geuebt = tage(*range(9, 16), *range(0, 7))
    s = serie_aus_tagen(geuebt, HEUTE, REGELN)
    assert s.aktuell == 7 and s.laengste == 7


def test_hoechstens_drei_schilde():
    s = serie_aus_tagen(tage(*range(0, 40)), HEUTE, REGELN)
    assert (s.aktuell, s.schilde, s.naechster_schild_in) == (40, 3, None)
    s = serie_aus_tagen(tage(*range(0, 9)), HEUTE, REGELN)
    assert (s.schilde, s.naechster_schild_in) == (1, 5)


def test_ohne_abgaben_keine_serie():
    s = serie_aus_tagen([], HEUTE, REGELN)
    assert (s.aktuell, s.laengste, s.schilde, s.naechster_schild_in) == (0, 0, 0, 7)


# --- Erfolge --------------------------------------------------------------


def erfolg(wert: int, schwellen: tuple[int, ...]) -> ErfolgDefinition:
    return ErfolgDefinition(
        "probe", "meilensteine", "fa-flag", wert, schwellen,
        ("Zehn gelöst", "Fünfzig gelöst", "Zweihundert gelöst"),
        lambda n: f"{n} Aufgaben gelöst",
    )


def test_erfolg_in_drei_stufen():
    offen = bewerte(erfolg(6, (10, 50, 200)))
    assert (offen.erreicht, offen.rang, offen.titel, offen.ziel) == (False, None, "Zehn gelöst", 10)
    assert offen.beschreibung == "10 Aufgaben gelöst (6 / 10)"
    silber = bewerte(erfolg(56, (10, 50, 200)))
    assert (silber.rang, silber.titel, silber.ziel) == ("silber", "Fünfzig gelöst", 200)
    assert silber.beschreibung == "Silber: 50 Aufgaben gelöst; Gold bei 200"
    gold = bewerte(erfolg(250, (10, 50, 200)))
    assert (gold.rang, gold.beschreibung) == ("gold", "Gold: 200 Aufgaben gelöst")


def test_einstufiger_erfolg_ist_gold():
    e = bewerte(erfolg(1, (1,)))
    assert (e.rang, e.beschreibung) == ("gold", "1 Aufgaben gelöst")


def test_schwellen_nur_so_hoch_wie_der_bestand():
    assert bis_hoechstens((1, 5, 15), 34) == (1, 5, 15)
    assert bis_hoechstens((1, 5, 15), 3) == (1, 3)
    assert bis_hoechstens((1, 5, 15), 1) == (1,)


# --- Verbuchung -----------------------------------------------------------


@pytest.fixture
def state(settings) -> AppState:
    return AppState(settings, runner=object())


def bestanden(sterne: int | None = None, **kennwerte) -> PruefErgebnis:
    wertung = None if sterne is None else Wertung(sterne=sterne, kennwerte=Kennwerte(**kennwerte))
    return PruefErgebnis(
        bestanden=True, sichtbar=[], versteckt_pass=0, versteckt_fail=0, laufzeit_ms=12.0, wertung=wertung
    )


def durchgefallen() -> PruefErgebnis:
    return PruefErgebnis(bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=1, laufzeit_ms=5.0)


def verbuche(state: AppState, aufgabe_id: str, code: str, ergebnis: PruefErgebnis, bestand: Bestand | None = None):
    return state.spiel.verbuche(bestand or state.bestand(), state.aufgaben.aufgabe(aufgabe_id), code, ergebnis)


def test_erste_loesung_bringt_punkte_auftrag_und_serie(state):
    v = verbuche(state, "001-verdoppeln", "def verdoppeln(x):\n    return x + x\n", bestanden())
    b = v.belohnung
    assert (b.punkte, b.punkte_versuch, b.punkte_moeglich) == (10, 10, 10)
    assert b.erster_versuch and not b.wiederholung and b.hinweise == 0
    # der Testbestand hat keine Spiele: der Auftrag hat zwei Ziele, beide erledigt
    assert [z.id for z in b.auftrag.ziele] == ["aufgabe", "ohne_hilfe"]
    assert b.auftrag.erledigt and b.auftrag.gutgeschrieben and b.auftrag_bonus == 10
    stand = state.spiel.stand(state.bestand())
    assert stand.punkte == 20
    assert (stand.serie.aktuell, stand.serie.heute_geuebt) == (1, True)


def test_bonus_nur_einmal_am_tag(state):
    verbuche(state, "001-verdoppeln", "def verdoppeln(x): return 2*x", bestanden())
    b = verbuche(state, "002-paar", "def paar(a, b): return [a, b]", bestanden()).belohnung
    assert b.auftrag_bonus == 0 and b.punkte == 10
    assert state.spiel.stand(state.bestand()).punkte == 30


def test_durchgefallen_ohne_belohnung(state):
    v = verbuche(state, "001-verdoppeln", "def verdoppeln(x): return x", durchgefallen())
    assert v.belohnung is None and v.progress.status == "in_arbeit"
    assert state.spiel.stand(state.bestand()).serie.aktuell == 0


def test_hinweis_kostet_punkte_und_das_ziel_ohne_hilfe(state):
    state.progress.markiere_hint_gesehen("001-verdoppeln", 0)
    b = verbuche(state, "001-verdoppeln", "def verdoppeln(x): return 2*x", bestanden()).belohnung
    assert (b.punkte, b.hinweise) == (7, 1)
    ziele = {z.id: z.erledigt for z in b.auftrag.ziele}
    assert ziele == {"aufgabe": True, "ohne_hilfe": False}
    assert b.auftrag_bonus == 0


def test_kuerzer_als_die_musterloesung_und_bestwert(state):
    verbuche(state, "001-verdoppeln", "def verdoppeln(x):\n    return x * 2  # lang\n", bestanden())
    b = verbuche(state, "001-verdoppeln", "verdoppeln=lambda x:2*x", bestanden()).belohnung
    assert b.wiederholung and b.punkte == 0
    assert [(w.art, w.neu) for w in b.bestwerte] == [("zeichen", 22)]
    assert [e.id for e in b.neue_erfolge] == ["kuerzer"]


def test_sterne_teilen_die_punkte(state):
    b = verbuche(state, "c005-knopf", "b{color:red}", bestanden(sterne=2)).belohnung
    assert (b.punkte, b.sterne) == (7, 2)
    b = verbuche(state, "c005-knopf", "b{color:red}", bestanden(sterne=3)).belohnung
    assert b.punkte == 3
    assert [(w.art, w.vorher, w.neu) for w in b.bestwerte] == [("sterne", 2, 3)]
    assert state.progress.hole_progress("c005-knopf").sterne == 3


def test_spiel_level_erfuellt_das_spielziel(state):
    konfig = state.konfig.model_copy(deep=True)
    konfig.spiele = [SpielKonfig(id="probe", titel="Probe", icon="fa-flag", aufgabentyp="css_klon")]
    bestand = Bestand.aus(state.aufgaben.alle_aufgaben(), state.aufgaben.alle_pfade(), konfig)
    b = verbuche(state, "c005-knopf", "b{color:red}", bestanden(sterne=1), bestand).belohnung
    ziele = {z.id: z.erledigt for z in b.auftrag.ziele}
    assert ziele == {"aufgabe": False, "spiel": True, "ohne_hilfe": True}
    bereiche = {m.id: m for m in state.spiel.stand(bestand).meisterschaft}
    assert "css" not in bereiche and bereiche["spiele"].punkte == 3


def test_meisterschaft_je_sprache(state):
    verbuche(state, "001-verdoppeln", "def verdoppeln(x): return 2*x", bestanden())
    verbuche(state, "002-paar", "def paar(a, b): return [a, b]", bestanden())
    bereiche = {m.id: m for m in state.spiel.stand(state.bestand()).meisterschaft}
    # Python hat drei Aufgaben zu je 10 Punkten
    assert (bereiche["python"].punkte, bereiche["python"].moeglich, bereiche["python"].rang) == (20, 30, "silber")
    assert bereiche["sql"].rang is None


def test_pfad_und_reset(state):
    verbuche(state, "001-verdoppeln", "def verdoppeln(x): return 2*x", bestanden())
    verbuche(state, "002-paar", "def paar(a, b): return [a, b]", bestanden())
    erfolge = {e.id: e for e in state.spiel.erfolge(state.bestand()).eintraege}
    assert erfolge["pfade"].erreicht and erfolge["pfade"].ziel == 1
    state.progress.reset_alles()
    stand = state.spiel.stand(state.bestand())
    assert (stand.punkte, stand.serie.aktuell, stand.auftrag.gutgeschrieben) == (0, 0, False)


def test_routen_liefern_stand_und_erfolge(settings):
    client = TestClient(app_bauen(settings, runner=object()))
    antwort = client.post("/api/submissions/lokal", json={
        "aufgabe_id": "c005-knopf",
        "code": "b{color:red}",
        "pruefung": bestanden(sterne=3).model_dump(),
    })
    assert antwort.status_code == 200
    assert antwort.json()["belohnung"]["punkte"] == 10
    stand = client.get("/api/spiel/stand").json()
    assert stand["stufe"]["stufe"] == 1 and stand["serie"]["aktuell"] == 1
    erfolge = client.get("/api/spiel/erfolge").json()
    assert erfolge["gesamt"] == len(erfolge["eintraege"]) > 0
