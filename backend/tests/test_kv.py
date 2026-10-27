"""KV-Werkstatt: Formeln lesen, Primblöcke, kleinste Lösung, Teilschritte und die echten Levels (ohne Sandbox)."""

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung.orchestrator import pruefe, pruefer_fuer
from codeschmiede.steuerung import kv

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "maschine").glob("b0*/aufgabe.md"))
ABCD = list("ABCD")
# Segment e der 7-Segment-Anzeige für die Ziffern 0 bis 9, 10 bis 15 egal
SEGMENT_E = "1010001010xxxxxx"


def test_formel_lesen():
    f = kv.lies("# Kommentar\ne = !B !D + C*!D\n", ABCD, ["e"])
    assert f.fehler == []
    assert [b.text(ABCD) for b in f.bloecke["e"]] == ["!B !D", "C !D"]
    assert f.bloecke["e"][0].felder(4) == {0, 2, 8, 10}


@pytest.mark.parametrize(("text", "erwartet"), [
    ("e = Q", "Q ist kein Eingang"),
    ("e = A !A", "zugleich 0 und 1"),
    ("x = A", "so geht es"),
    ("", "Für e fehlt die Zeile"),
])
def test_fehler_werden_benannt(text, erwartet):
    assert any(erwartet in f for f in kv.lies(text, ABCD, ["e"]).fehler)


def test_eins_und_null():
    f = kv.lies("e = 1\n", list("AB"), ["e"])
    assert [kv.wert(f.bloecke["e"], x, 2) for x in range(4)] == [1, 1, 1, 1]
    assert kv.lies("e = 0\n", list("AB"), ["e"]).bloecke["e"] == []


def test_primbloecke_und_kleinste_loesung():
    assert sorted(b.text(ABCD) for b in kv.primbloecke(SEGMENT_E, 4)) == ["!B !D", "A !D", "C !D"]
    assert kv.kleinste_abdeckung(SEGMENT_E, 4) == (2, 4)
    # Schachbrett: nichts lässt sich zusammenfassen
    assert kv.kleinste_abdeckung("01101001", 3) == (4, 12)


def test_vergroesserbar_nennt_den_eingang():
    block = kv.lies("e = !A C !D", ABCD, ["e"]).bloecke["e"][0]
    assert kv.vergroesserbar(block, SEGMENT_E, 4) == 0
    assert kv.vergroesserbar(kv.lies("e = C !D", ABCD, ["e"]).bloecke["e"][0], SEGMENT_E, 4) is None


def test_schaltplan_teilt_gleiche_bloecke():
    f = kv.lies("a = !B !D + C\nd = !B !D\n", ABCD, ["a", "d"])
    text, bausteine, tiefe = kv.schaltplan(f, ABCD, ["a", "d"])
    # zwei NICHT, ein UND für !B !D (für beide Ausgänge), ein ODER
    assert bausteine == 4 and tiefe == 3
    assert text.count("UND(") == 1 and "d = und1" in text


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def lade(loader, aid):
    return loader.lade_aufgabe(AUFGABEN / "maschine" / aid / "aufgabe.md")


def test_sieben_levels():
    assert len(LEVELS) == 7 and LEVELS[0] == "b001-zwei-eingaenge" and LEVELS[-1] == "b007-vom-block-zum-schaltplan"


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = lade(loader, aid)
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], None)
    assert erg.bestanden and erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    assert not pruefe(aufgabe, aufgabe.starter_code, None).bestanden


def befunde(loader, aid, code):
    erg = pruefe(lade(loader, aid), code, None)
    return erg, [(s["titel"], s["erfuellt"], s["befunde"]) for s in erg.sichtbar[0].tatsaechlich["teilschritte"]]


def test_zu_kleiner_block_wie_im_entwurf(loader):
    erg, staende = befunde(loader, "b005-egal-felder", "e = !B !D + !A C !D")
    assert [s[1] for s in staende] == [True, True, False, False]
    assert staende[2][2] == ["Block !A C !D lässt sich verdoppeln: ohne A erwischt er noch keine 0"]
    assert not erg.bestanden


def test_null_erwischt_und_ueberfluessiger_block(loader):
    _, staende = befunde(loader, "b002-mehrheit", "M = A B + A C + B C + A")
    assert staende[1][2] == ["Block A erwischt die 0 bei 100"]
    _, staende = befunde(loader, "b002-mehrheit", "M = A B + A C + B C + A B C")
    assert staende[2][1] is False  # A B C geht größer
    assert any("lässt sich weglassen" in b for b in staende[3][2])


def test_offene_eins_nennt_den_namen(loader):
    _, staende = befunde(loader, "b005-egal-felder", "e = !B !D")
    assert staende[0][2] == ["die 1 bei 6 (0110) liegt in keinem Block"]


def test_mehrere_ausgaenge_nennen_den_ausgang(loader):
    _, staende = befunde(loader, "b007-vom-block-zum-schaltplan",
                         "S = !A !B C + !A B !C + A !B !C + A B C\nCo = A B + A C")
    assert staende[0][2] == ["Co: die 1 bei 011 liegt in keinem Block"]
