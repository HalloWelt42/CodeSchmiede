"""Digitale Schaltungen: Schaltplan lesen, Wahrheitstabelle, Tiefe und die echten Levels (ohne Sandbox)."""

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung.orchestrator import pruefe, pruefer_fuer
from codeschmiede.steuerung import schaltung

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "maschine").glob("d0*/aufgabe.md"))
ALLE = list(schaltung.ARTEN)

HALB = """# Halbaddierer
x1 = XOR(A, B) @ 230,40
u1 = UND(A, B)
S = x1
C = u1
"""


def test_halbaddierer_rechnet():
    plan = schaltung.lies(HALB, ["A", "B"], ["S", "C"], ALLE)
    assert plan.fehler == []
    tabelle = schaltung.wahrheitstabelle(plan, ["A", "B"])
    assert [(z["S"], z["C"]) for z in tabelle] == [(0, 0), (1, 0), (1, 0), (0, 1)]
    assert schaltung.tiefe(plan, ["A", "B"]) == 1
    assert plan.bausteine[0].x == 230 and plan.bausteine[1].x is None


def test_feste_werte_und_eingang_direkt():
    plan = schaltung.lies("b = 1\ng = A\n", ["A"], ["b", "g"], ALLE)
    assert plan.fehler == [] and [(z["b"], z["g"]) for z in schaltung.wahrheitstabelle(plan, ["A"])] == [(1, 0), (1, 1)]


@pytest.mark.parametrize(("text", "erwartet"), [
    ("x = UND(A, ?)\nY = x\n", "Eingang 2 ist nicht verbunden"),
    ("x = UND(A)\nY = x\n", "hat 2 Eingänge"),
    ("x = FOO(A, A)\nY = x\n", "gibt es nicht"),
    ("x = UND(A, Q)\nY = x\n", "das Signal Q gibt es nicht"),
    ("x = UND(A, y)\ny = UND(x, A)\nY = x\n", "Kreis"),
    ("x = XOR(A, A)\nY = x\n", "nicht erlaubt"),
    ("x = UND(A, A)\n", "Ausgang Y ist nicht verbunden"),
])
def test_fehler_werden_benannt(text, erwartet):
    plan = schaltung.lies(text, ["A"], ["Y"], ["UND", "ODER", "NICHT"])
    assert any(erwartet in f for f in plan.fehler), plan.fehler


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def test_acht_levels():
    assert len(LEVELS) == 8 and LEVELS[0] == "d001-drei-gatter" and LEVELS[-1] == "d008-sieben-segment"


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / aid / "aufgabe.md")
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], None)
    assert erg.bestanden and erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    assert not pruefe(aufgabe, aufgabe.starter_code, None).bestanden


def test_beim_verdrahten_nur_die_vorgabe(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / "d003-halbaddierer" / "aufgabe.md")
    erg = pruefe(aufgabe, HALB.replace("u1 = UND(A, B)", "u1 = UND(A, B)\nu2 = UND(A, B)"), None)
    befunde = erg.sichtbar[0].tatsaechlich["teilschritte"][0]["befunde"]
    assert not erg.bestanden and "nur verdrahtet" in befunde[0] and "u2" in befunde[0]


def test_teilschritte_je_ausgang(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / "d003-halbaddierer" / "aufgabe.md")
    erg = pruefe(aufgabe, HALB.replace("C = u1", "C = x1"), None)
    staende = erg.sichtbar[0].tatsaechlich["teilschritte"]
    assert staende[0]["erfuellt"] and not staende[1]["erfuellt"]
    assert "C 0, soll 1" in staende[1]["befunde"][0] or "C 1, soll 0" in staende[1]["befunde"][0]
