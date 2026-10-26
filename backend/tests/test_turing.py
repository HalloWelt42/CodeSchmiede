"""Turingmaschine: Tabelle lesen, laufen lassen und die echten Levels (ohne Sandbox, eine Tabelle ist Daten)."""

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung.orchestrator import oeffentliches_extra, pruefe, pruefer_fuer
from codeschmiede.steuerung import turing

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "maschine").glob("t0*/aufgabe.md"))

PLUS = """# plus eins
plus 1 -> 0 L plus
plus 0 -> 1 N fertig   # fertig
plus _ -> 1 N fertig
"""


def test_tabelle_lesen():
    t = turing.lies(PLUS, {"0", "1"})
    assert t.fehler == [] and len(t.regeln) == 3 and t.zustaende({"fertig"}) == {"plus"}
    assert t.regel("plus", "_").schreibt == "1"


def test_fehler_mit_zeile():
    t = turing.lies("plus 1 -> 0 L\nplus 2 -> 0 L plus\nplus 1 -> 1 R plus\n", {"0", "1"})
    assert t.fehler[0].startswith("Zeile 1:")
    assert any("Zeichen 2" in f for f in t.fehler)


def test_doppelte_regel():
    t = turing.lies("plus 1 -> 0 L plus\nplus 1 -> 1 R plus\n", {"0", "1"})
    assert any("schon Zeile 1" in f for f in t.fehler)


def test_laufen_bis_zum_ende_und_grenze():
    t = turing.lies(PLUS, {"0", "1"})
    lauf = turing.laufe(t, "111", 2, "plus", {"fertig"}, 100)
    assert lauf.gehalten and lauf.band == "1000" and len(lauf.schritte) == 5
    endlos = turing.lies("a _ -> _ R a\n", {"0"})
    lauf = turing.laufe(endlos, "", 0, "a", {"fertig"}, 50)
    assert not lauf.gehalten and "50 Schritten" in lauf.grund
    lauf = turing.laufe(t, "2", 0, "plus", {"fertig"}, 50)
    assert not lauf.gehalten and "keine Regel" in lauf.grund


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def test_sieben_levels():
    assert len(LEVELS) == 7 and LEVELS[0] == "t001-bits-tauschen" and LEVELS[-1] == "t007-kopieren"


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / aid / "aufgabe.md")
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], None)
    assert erg.bestanden and erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    start = pruefe(aufgabe, aufgabe.starter_code, None)
    assert not start.bestanden and not start.sichtbar[0].tatsaechlich["teilschritte"][0]["erfuellt"]


def test_falsches_ergebnis_wird_benannt(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / "t002-plus-eins" / "aufgabe.md")
    erg = pruefe(aufgabe, "plus 1 -> 0 L plus\nplus 0 -> 1 N fertig\n", None)
    staende = erg.sichtbar[0].tatsaechlich["teilschritte"]
    assert staende[0]["erfuellt"] and staende[1]["erfuellt"] and not staende[2]["erfuellt"]
    assert "keine Regel" in staende[2]["befunde"][0]


def test_versteckte_baender_bleiben_verborgen(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "maschine" / "t005-klammern" / "aufgabe.md")
    assert "versteckt" not in oeffentliches_extra(aufgabe)["turing"]
