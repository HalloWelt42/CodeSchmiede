"""Ausgabe-Sprint: Runden ohne Sandbox, mit gestellter Uhr."""

import random
import textwrap
from datetime import datetime, timedelta, timezone

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.pruefung.orchestrator import oeffentliches_extra

from .conftest import schreibe_aufgabe

SCHNIPSEL = "".join(
    f'      - {{code: "print({i})", optionen: ["{i}", "x{i}", "y{i}"], richtig: 0, warum: "Zahl {i}"}}\n'
    for i in range(12)
)
LEVEL = "sprint:\n  fragen: 5\n  sekunden: 60\n  sterne: [3, 4, 5]\n  schnipsel:\n" + textwrap.indent(SCHNIPSEL, "")


class Uhr:
    def __init__(self):
        self.jetzt = datetime(2026, 10, 25, 12, 0, tzinfo=timezone.utc)

    def __call__(self):
        return self.jetzt


def richtige_wahl(frage):
    # die richtige Option ist die Zahl selbst
    zahl = frage["code"][len("print("):-1]
    return frage["optionen"].index(zahl)


def test_vorrat_bleibt_im_backend(settings, bestand):
    from codeschmiede.state import AppState

    schreibe_aufgabe(bestand, "python", "a900-probe", "ausgabe_sprint", LEVEL.replace("\n      -", "\n    -"))
    st = AppState(settings, runner=object())
    assert st.befunde == []
    extra = oeffentliches_extra(st.aufgaben.aufgabe("a900-probe"))
    assert "schnipsel" not in extra["sprint"] and extra["sprint"]["fragen"] == 5


@pytest.fixture
def ablauf(settings, bestand):
    from codeschmiede.state import AppState

    schreibe_aufgabe(bestand, "python", "a900-probe", "ausgabe_sprint", LEVEL.replace("\n      -", "\n    -"))
    st = AppState(settings, runner=object())
    uhr = Uhr()
    st.sprint.uhr = uhr
    st.sprint.zufall = random.Random(1)
    return st, uhr


def test_runde_der_reihe_nach(ablauf):
    st, uhr = ablauf
    runde = st.sprint.neue_runde(st.aufgaben.aufgabe("a900-probe"))
    assert len(runde.fragen) == 5 and runde.sekunden == 60
    from codeschmiede.spiel.sprint import FalscheAntwort, RundeVorbei

    with pytest.raises(FalscheAntwort):
        st.sprint.antworte(runde.id, 1, 0, st.bestand())
    r = st.sprint.antworte(runde.id, 0, richtige_wahl(runde.fragen[0].model_dump()), st.bestand())
    assert r.richtig
    with pytest.raises(RundeVorbei):
        st.sprint.antworte(runde.id, 0, 0, st.bestand())
    with pytest.raises(FalscheAntwort):
        st.sprint.abschliessen(runde.id, st.bestand())


def test_volle_runde_bringt_sterne_und_punkte(ablauf):
    st, uhr = ablauf
    runde = st.sprint.neue_runde(st.aufgaben.aufgabe("a900-probe"))
    for i, frage in enumerate(runde.fragen):
        wahl = richtige_wahl(frage.model_dump()) if i != 2 else (richtige_wahl(frage.model_dump()) + 1) % 3
        st.sprint.antworte(runde.id, i, wahl, st.bestand())
        uhr.jetzt += timedelta(seconds=5)
    ende = st.sprint.abschliessen(runde.id, st.bestand())
    assert (ende.treffer, ende.sterne, ende.laengste_kette) == (4, 2, 2)
    assert ende.bestanden and ende.belohnung.punkte == round(10 * 2 / 3)
    assert ende.auswertung[2].gewaehlt != ende.auswertung[2].richtig and ende.auswertung[2].warum
    assert st.progress.hole_progress("a900-probe").sterne == 2


def test_nach_der_frist_zaehlen_offene_fragen_als_falsch(ablauf):
    st, uhr = ablauf
    runde = st.sprint.neue_runde(st.aufgaben.aufgabe("a900-probe"))
    st.sprint.antworte(runde.id, 0, richtige_wahl(runde.fragen[0].model_dump()), st.bestand())
    uhr.jetzt += timedelta(seconds=64)
    from codeschmiede.spiel.sprint import RundeVorbei

    with pytest.raises(RundeVorbei):
        st.sprint.antworte(runde.id, 1, 0, st.bestand())
    ende = st.sprint.abschliessen(runde.id, st.bestand())
    assert (ende.treffer, ende.sterne, ende.bestanden, ende.sekunden) == (1, 0, False, 60)
    with pytest.raises(RundeVorbei):
        st.sprint.abschliessen(runde.id, st.bestand())


def test_routen(settings, bestand):
    schreibe_aufgabe(bestand, "python", "a900-probe", "ausgabe_sprint", LEVEL.replace("\n      -", "\n    -"))
    client = TestClient(app_bauen(settings, runner=object()))
    assert client.post("/api/submissions", json={"aufgabe_id": "a900-probe", "code": "x"}).status_code == 400
    assert client.post("/api/spiel/sprint/001-verdoppeln/runde").status_code == 404
    runde = client.post("/api/spiel/sprint/a900-probe/runde").json()
    assert "richtig" not in runde["fragen"][0]
    antwort = client.post(f"/api/spiel/sprint/runde/{runde['id']}/antwort", json={"frage": 0, "wahl": 0})
    assert antwort.status_code == 200 and "richtige_wahl" in antwort.json()
    assert client.post(f"/api/spiel/sprint/runde/{runde['id']}/antwort", json={"frage": 0, "wahl": 0}).status_code == 409
    assert client.post(f"/api/spiel/sprint/runde/{runde['id']}/abschluss").status_code == 422
    assert client.post("/api/spiel/sprint/runde/gibt-es-nicht/abschluss").status_code == 404
