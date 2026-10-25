"""SQL-Krimi: eindeutige Antwort, Sterne aus dem Verlauf, Prüfer in der Sandbox, Pinnwand."""

import textwrap

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.models.progress import Progress
from codeschmiede.pruefung.ergebnis import SternKriterium, Wertung
from codeschmiede.pruefung.krimi_pruefer import Ergebnistabelle, antwort_eindeutig
from codeschmiede.pruefung.orchestrator import oeffentliches_extra, pruefe
from codeschmiede.spiel.dienst import mit_verlauf
from codeschmiede.state import AppState

from .conftest import braucht_sandbox, schreibe_aufgabe

TATORT = """CREATE TABLE firmen (id INTEGER PRIMARY KEY, name TEXT, farbe TEXT, zeit TEXT);
INSERT INTO firmen VALUES (1, 'Schlüssel Sommer', 'blau', '21:22'), (2, 'Fix und Fertig', 'blau', '22:41'), (3, 'Rapid Schloss', 'rot', '21:31');
"""
GEGEN = """CREATE TABLE firmen (id INTEGER PRIMARY KEY, name TEXT, farbe TEXT, zeit TEXT);
INSERT INTO firmen VALUES (1, 'Schlüssel Sommer', 'blau', '20:15'), (2, 'Fix und Fertig', 'blau', '23:02'), (3, 'Rapid Schloss', 'blau', '21:31');
"""
KAPITEL = """\
    krimi:
      dataset: probe_tat
      gegenprobe: probe_gegen
      kapitel: 1
      frage: Welche blaue Firma war zwischen 21 und 22:30 Uhr unterwegs?
      antwort: Schlüssel Sommer
      antwort_gegen: Rapid Schloss
      notiz: "Schlüssel Sommer, 21:22"
      versuche: 1
    """
LOESUNG = "SELECT name, zeit FROM firmen WHERE farbe = 'blau' AND zeit BETWEEN '21:00' AND '22:30'"


@pytest.fixture
def mit_fall(bestand):
    datasets = bestand / "sql" / "datasets"
    (datasets / "probe_tat.sql").write_text(TATORT, encoding="utf-8")
    (datasets / "probe_gegen.sql").write_text(GEGEN, encoding="utf-8")
    ordner = schreibe_aufgabe(bestand, "sql", "k900-probe", "sql_krimi", textwrap.dedent(KAPITEL))
    (ordner / "solution_idiomatic.sql").write_text(LOESUNG + ";\n")
    (bestand / "pfade" / "fall.yml").write_text("id: fall\ntitel: Probefall\nreihenfolge: [k900-probe]\n", encoding="utf-8")
    return bestand


def tabelle(spalten, *zeilen):
    return Ergebnistabelle(spalten=spalten, zeilen=[list(z) for z in zeilen])


def test_antwort_eindeutig():
    assert antwort_eindeutig(tabelle(["name", "zeit"], ("Schlüssel Sommer", "21:22")), "schlüssel sommer")
    assert antwort_eindeutig(tabelle(["name"], ("Schlüssel Sommer",), ("Schlüssel Sommer",)), "Schlüssel Sommer")
    assert not antwort_eindeutig(tabelle(["name"], ("Schlüssel Sommer",), ("Fix und Fertig",)), "Schlüssel Sommer")
    assert not antwort_eindeutig(tabelle(["name"]), "Schlüssel Sommer")


def test_sterne_aus_dem_verlauf_der_reihe_nach():
    wertung = Wertung(sterne=1, kriterien=[
        SternKriterium(text="gefunden", erreicht=True),
        SternKriterium(text="ohne Hinweis", erreicht=False, art="ohne_hinweis"),
        SternKriterium(text="erster Versuch", erreicht=False, art="versuche", grenze=1),
    ])
    neu = Progress(aufgabe_id="x", status="neu")
    assert mit_verlauf(wertung, neu).sterne == 3
    assert mit_verlauf(wertung, neu.model_copy(update={"versuche": 2})).sterne == 2
    # mit Hinweis zählt der Stern für den ersten Versuch nicht mehr, Sterne gehen der Reihe nach
    assert mit_verlauf(wertung, neu.model_copy(update={"hints_genutzt": 1})).sterne == 1


def test_geheimes_bleibt_im_backend(settings, mit_fall):
    st = AppState(settings, runner=object())
    assert st.befunde == []
    extra = oeffentliches_extra(st.aufgaben.aufgabe("k900-probe"))["krimi"]
    assert not {"antwort", "antwort_gegen", "notiz"} & set(extra)
    client = TestClient(app_bauen(settings, runner=object()))
    assert client.get("/api/sql/datasets/probe_tat/vorschau").status_code == 200
    assert client.get("/api/sql/datasets/probe_gegen/vorschau").status_code == 404
    assert client.get("/api/spiel/krimi/k900-probe/pinnwand").json() == []


@braucht_sandbox
def test_pruefer(settings, mit_fall, docker_runner):
    st = AppState(settings, runner=docker_runner)
    kapitel = st.aufgaben.aufgabe("k900-probe")
    erg = pruefe(kapitel, LOESUNG, docker_runner)
    assert erg.bestanden and erg.versteckt_pass == 1 and erg.wertung.sterne == 1
    eingetippt = pruefe(kapitel, "SELECT 'Schlüssel Sommer'", docker_runner)
    assert eingetippt.sichtbar[0].bestanden and not eingetippt.bestanden and eingetippt.versteckt_fail == 1
    breit = pruefe(kapitel, "SELECT name FROM firmen WHERE farbe = 'blau'", docker_runner)
    assert not breit.bestanden and "eindeutig" in breit.sichtbar[0].fehler
    kaputt = pruefe(kapitel, "SELEKT name", docker_runner)
    assert not kaputt.bestanden


@braucht_sandbox
def test_verbuchung_und_pinnwand(settings, mit_fall, docker_runner):
    client = TestClient(app_bauen(settings, runner=docker_runner))
    falsch = client.post("/api/submissions", json={"aufgabe_id": "k900-probe", "code": "SELECT name FROM firmen"}).json()
    assert not falsch["bestanden"]
    richtig = client.post("/api/submissions", json={"aufgabe_id": "k900-probe", "code": LOESUNG}).json()
    # ohne Hinweis, aber im zweiten Versuch: zwei Sterne
    assert richtig["bestanden"] and richtig["pruefung"]["wertung"]["sterne"] == 2
    assert richtig["belohnung"]["sterne"] == 2
    assert client.get("/api/spiel/krimi/k900-probe/pinnwand").json() == [{"kapitel": 1, "titel": "k900-probe", "text": "Schlüssel Sommer, 21:22"}]
    lauf = client.post("/api/spiel/krimi/k900-probe/ausfuehren", json={"code": "SELECT COUNT(*) AS n FROM firmen"}).json()
    assert lauf["tabelle"]["zeilen"] == [[3]]
