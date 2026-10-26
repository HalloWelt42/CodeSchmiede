"""CSS-Nachbauten: der Browser misst die Deckung, der Server wertet."""

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.pruefung.css_klon_pruefer import werte
from codeschmiede.pruefung.ergebnis import Messung
from codeschmiede.pruefung.registry import registriere
from codeschmiede.state import AppState


@pytest.fixture
def state(settings) -> AppState:
    return AppState(settings, runner=object())


def gewertet(state, deckung: float, code: str = "b{color:red}", muster: int | None = 12):
    aufgabe = state.aufgaben.aufgabe("c005-knopf")
    return werte(aufgabe, code, Messung(deckung=deckung), muster)


def test_bestehen_erst_ab_95_prozent(state):
    knapp = gewertet(state, 0.949)
    assert not knapp.bestanden and knapp.wertung.sterne == 0
    erg = gewertet(state, 0.96)
    assert erg.bestanden and erg.wertung.sterne == 1
    assert erg.wertung.kennwerte.deckung == 0.96


def test_punkte_deckung_linear_ab_80_kuerze_erst_ab_99(state):
    w = gewertet(state, 0.96).wertung
    deckung, kuerze = w.teile
    assert deckung.anteil == pytest.approx(0.6 * 0.8) and kuerze.anteil == 0
    w = gewertet(state, 1.0).wertung
    assert w.punkteanteil == pytest.approx(1.0) and w.sterne == 3


def test_dritter_stern_nur_so_kurz_wie_die_musterloesung(state):
    lang = "b { color: red; font-weight: bold; }"  # 30 Zeichen ohne Leerraum
    w = gewertet(state, 0.995, code=lang).wertung
    assert w.sterne == 2 and not w.kriterien[2].erreicht
    assert w.teile[1].anteil == pytest.approx(0.4 * 12 / 30)
    assert gewertet(state, 0.995).wertung.sterne == 3


def test_ohne_musterloesung_zaehlt_kuerze_voll(state):
    w = gewertet(state, 0.99, code="b { color: red; font-weight: bold; }", muster=None).wertung
    assert w.sterne == 3 and w.teile[1].anteil == pytest.approx(0.4)


def test_browser_abgabe_braucht_wertung():
    with pytest.raises(ValueError):
        registriere("css_test", abgabe="browser")
    with pytest.raises(ValueError):
        registriere("code_test", werte=lambda *a: None)


def test_verlauf_punkte_und_pixelgenau(settings):
    client = TestClient(app_bauen(settings, runner=object()))
    lokal = "/api/submissions/lokal"
    erg = client.post(lokal, json={"aufgabe_id": "c005-knopf", "code": "b{color:red}", "messung": {"deckung": 0.96}}).json()
    # 10 Punkte, davon der Deckungsteil 0.6 * 0.8 = 48 %
    assert erg["belohnung"]["punkte"] == round(10 * 0.48)
    assert [t["text"] for t in erg["pruefung"]["wertung"]["teile"]] == ["Deckung", "Kürze"]
    erg = client.post(lokal, json={"aufgabe_id": "c005-knopf", "code": "b{color:red}", "messung": {"deckung": 1.0}}).json()
    assert erg["progress"]["punkte_erreicht"] == 10 and erg["progress"]["sterne"] == 3
    assert any(e["id"] == "pixelgenau" for e in erg["belohnung"]["neue_erfolge"])
    verlauf = client.get("/api/aufgaben/c005-knopf/submissions").json()
    assert [v["deckung"] for v in verlauf] == [1.0, 0.96]


def test_css_bestand_fuer_die_messung_im_browser(settings):
    client = TestClient(app_bauen(settings, runner=object()))
    bestand = client.get("/api/admin/css-bestand").json()
    assert bestand["voll"] == 0.9995 and bestand["bestehen"] == 0.95
    knopf = next(a for a in bestand["aufgaben"] if a["id"] == "c005-knopf")
    assert knopf["ziel_html"] and knopf["ziel_css"] and knopf["musterloesungen"][0]["code"]
    assert [a["id"] for a in bestand["aufgaben"]] == ["c005-knopf"]  # nur CSS-Nachbauten
