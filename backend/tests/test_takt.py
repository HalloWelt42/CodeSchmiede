"""Schaltungen mit Takt: Flipflops, Takte, Tiefe und die echten Levels (ohne Sandbox)."""

import pytest
from pydantic import ValidationError

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung import takt_pruefer
from codeschmiede.pruefung.orchestrator import oeffentliches_extra, pruefe, pruefer_fuer
from codeschmiede.steuerung import schaltung

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "maschine").glob("f0*/aufgabe.md"))
ALLE = [*schaltung.ARTEN, schaltung.SPEICHER]

ZAEHLER = """# Zähler bis 3
n0 = NICHT(f0) @ 130,40
f0 = FF(n0)
x1 = XOR(f0, f1)
f1 = FF(x1)
Q0 = f0
Q1 = f1
"""
# der Fehler aus dem Entwurf: D1 hängt direkt an Q0
FALSCH = ZAEHLER.replace("f1 = FF(x1)", "f1 = FF(f0)")


def test_zaehler_zaehlt():
    plan = schaltung.lies(ZAEHLER, [], ["Q1", "Q0"], ALLE)
    assert plan.fehler == []
    verlauf = schaltung.takte(plan, [], [{}] * 6)
    assert [(v["Q1"], v["Q0"]) for v in verlauf] == [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (0, 1)]
    assert schaltung.tiefe(plan, []) == 1


def test_flipflop_reicht_den_eingang_einen_takt_spaeter_weiter():
    plan = schaltung.lies("q = FF(E)\nQ = q\n", ["E"], ["Q"], ALLE)
    verlauf = schaltung.takte(plan, ["E"], [{"E": e} for e in (1, 0, 1, 1)])
    assert [v["Q"] for v in verlauf] == [0, 1, 0, 1]


def test_kreis_nur_ueber_ein_flipflop():
    plan = schaltung.lies("a = NICHT(b)\nb = NICHT(a)\nQ = a\n", [], ["Q"], ALLE)
    assert any("Kreis ohne Flipflop" in f for f in plan.fehler)
    ohne = schaltung.lies("a = NICHT(b)\nb = NICHT(a)\nQ = a\n", [], ["Q"], list(schaltung.ARTEN))
    assert any("Kreis:" in f for f in ohne.fehler)


def test_flipflop_nur_wo_erlaubt_und_mit_einem_eingang():
    plan = schaltung.lies("q = FF(E, E)\nQ = q\n", ["E"], ["Q"], list(schaltung.ARTEN))
    assert any("FF ist hier nicht erlaubt" in f for f in plan.fehler)
    assert any("hat 1 Eingang, nicht 2" in f for f in plan.fehler)


def test_tiefe_zaehlt_bis_zum_eingang_eines_flipflops():
    plan = schaltung.lies("a = UND(E, q)\nb = NICHT(a)\nq = FF(b)\nQ = q\n", ["E"], ["Q"], ALLE)
    assert schaltung.tiefe(plan, ["E"]) == 2


def test_falscher_eingang_im_ablauf_wird_gemeldet():
    with pytest.raises(ValidationError, match="Zeichen aus 0, 1 und x"):
        takt_pruefer.TaktLevel.model_validate({
            "ausgaenge": ["Q"], "bausteine": ["FF"], "sterne": {"bausteine": 0, "tiefe": 1},
            "sichtbar": [{"name": "A", "takte": 3, "soll": {"Q": "01"}}],
            "teilschritte": [{"titel": "t", "text": "t", "ausgaenge": "alle"}],
        })


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def lade(loader, aid):
    return loader.lade_aufgabe(AUFGABEN / "maschine" / aid / "aufgabe.md")


def test_sieben_levels():
    assert len(LEVELS) == 7 and LEVELS[0] == "f001-ein-bit-merken" and LEVELS[-1] == "f007-wuerfel"


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = lade(loader, aid)
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], None)
    assert erg.bestanden and erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    assert not pruefe(aufgabe, aufgabe.starter_code, None).bestanden


def test_befund_nennt_takt_und_ausgang(loader):
    aufgabe = lade(loader, "f003-zaehler-bis-3")
    erg = pruefe(aufgabe, FALSCH, None)
    a = erg.sichtbar[0].tatsaechlich
    staende = a["teilschritte"]
    assert [s["erfuellt"] for s in staende] == [True, False, False]
    assert staende[1]["befunde"] == ["Takt 3: Q1 ist 0, soll 1"]
    zaehlen = a["ablaeufe"][0]
    assert zaehlen["erste_stelle"] == 3 and zaehlen["kennzahlen"]["richtig"] == 5
    assert not erg.bestanden and erg.versteckt_fail == 1


def test_versteckte_ablaeufe_bleiben_verborgen(loader):
    aufgabe = lade(loader, "f001-ein-bit-merken")
    assert "versteckt" not in oeffentliches_extra(aufgabe)["takt"]
    (muster,) = loader.lade_musterloesungen("f001-ein-bit-merken")
    lauf = takt_pruefer.lauf_sichtbar(aufgabe, muster["code"])
    assert [a.name for a in lauf.auswertung.ablaeufe] == ["Durchreichen", "Halten"]
    assert lauf.auswertung.teilschritte[-1].geprueft is False


def test_wiedergabe_hat_eingaben_und_soll(loader):
    aufgabe = lade(loader, "f004-zaehler-bis-9")
    (muster,) = loader.lade_musterloesungen("f004-zaehler-bis-9")
    w = takt_pruefer.lauf_sichtbar(aufgabe, muster["code"]).auswertung.wiedergaben[0]
    # ohne Folge ist ein Eingang in jedem Takt 0
    assert w.eingaben == {"R": "0" * 12} and w.dauer == 12
    assert w.bilder[9][1]["Q3"] == 1 and w.bilder[10][1]["Q3"] == 0
