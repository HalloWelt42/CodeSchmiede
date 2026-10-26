"""Aufzugsteuerung: Welt, Regeln und die echten Levels.

Die Welt läuft ohne Sandbox. Die Levels aus aufgaben/ prüft ein Lauf mit dem lokalen Python (nur eigene
Musterlösungen und kleine Gegenproben); ein Level läuft zusätzlich in der echten Sandbox.
"""

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung.orchestrator import oeffentliches_extra, pruefe, pruefer_fuer
from codeschmiede.steuerung import aufzug_welt
from codeschmiede.steuerung.sandbox_lauf import nachspielen

from .conftest import braucht_sandbox
from .test_ampel import LokalerRunner

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "python").glob("e0*/aufgabe.md"))
HAUS = {"etagen": 3, "aufzuege": ["a"], "plaetze": 2, "last": 150, "start": 0}


def welt(fahrgaeste, dauer=40, **haus):
    return aufzug_welt.Welt({**HAUS, **haus}, {"name": "Probe", "dauer": dauer, "fahrgaeste": fahrgaeste,
                                              "feuer": None}, aufzeichnen=True)


def verstoesse(w):
    return [e["grund"] for e in w.ereignisse if e["art"] == "verstoss"]


def test_abholen_und_hinbringen():
    w = nachspielen(welt([{"t": 0, "von": 0, "nach": 2}]),
                    ["auf", "warten", "warten", "zu", "hoch", "hoch", "auf", "warten", "warten", "zu"] + ["warten"] * 30)
    (f,) = w.bilanz()
    assert f["angekommen"] is not None and f["warten"] < 2 and verstoesse(w) == []


def test_fahren_mit_offener_tuer_und_einklemmen_werden_nicht_ausgefuehrt():
    w = nachspielen(welt([{"t": 0, "von": 0, "nach": 1}]), ["auf", "zu", "hoch"] + ["warten"] * 40)
    assert verstoesse(w) == ["einklemmen", "offen_fahren"]
    assert w.aufzuege[0].etage == 0


def test_ueberlast_der_letzte_steigt_wieder_aus():
    fahrgaeste = [{"t": 0, "von": 0, "nach": 1}, {"t": 0.1, "von": 0, "nach": 1, "gewicht": 120}]
    w = welt(fahrgaeste)
    gesehen = False
    while w.laeuft():
        for wer in w.bereit():
            lage = w.lage(wer)
            if lage.ueberlast and not lage.lichtschranke and not gesehen:
                gesehen = True
                w.befehl(wer, "zu")  # verboten: die Tür bleibt offen
            else:
                w.befehl(wer, "auf" if lage.sekunde == 0 else "warten")
        w.schritt()
    assert gesehen and "ueberlast" in verstoesse(w)
    a = w.aufzuege[0]
    assert len(a.fahrgaeste) == 1 and a.fahrgaeste[0].gewicht == 75
    # der Abgewiesene ruft erst wieder, wenn die Kabine weiterfährt
    assert w.rufe()[1] == set()


def test_befehle_werden_geprueft():
    w = welt([])
    assert w.befehl_pruefen("hoch") == ("hoch", None)
    befehl, fehler = w.befehl_pruefen("fliegen")
    assert befehl is None and "hoch" in fehler


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def test_sieben_levels():
    assert len(LEVELS) == 7 and LEVELS[0] == "e001-zwei-etagen" and LEVELS[-1] == "e007-sonderfaelle"


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / aid / "aufgabe.md")
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    runner = LokalerRunner()
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], runner)
    assert erg.bestanden, [t["befunde"] for t in erg.sichtbar[0].tatsaechlich["teilschritte"]]
    assert erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    start = pruefe(aufgabe, aufgabe.starter_code, runner)
    assert not start.bestanden and not start.sichtbar[0].tatsaechlich["teilschritte"][0]["erfuellt"]


@pytest.mark.parametrize(("aid", "vorher"), [
    ("e002-rufe-sammeln", "e001-zwei-etagen"),
    ("e003-volle-kabine", "e002-rufe-sammeln"),
    ("e006-stosszeit", "e005-zwei-aufzuege"),
    ("e007-sonderfaelle", "e003-volle-kabine"),
])
def test_das_vorige_programm_reicht_nicht(loader, aid, vorher):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / aid / "aufgabe.md")
    (muster,) = loader.lade_musterloesungen(vorher)
    assert not pruefe(aufgabe, muster["code"], LokalerRunner()).bestanden


def test_versteckte_ablaeufe_bleiben_verborgen(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "e002-rufe-sammeln" / "aufgabe.md")
    assert "versteckt" not in oeffentliches_extra(aufgabe)["aufzug"]


@braucht_sandbox
def test_level_in_der_sandbox(loader, docker_runner):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "e005-zwei-aufzuege" / "aufgabe.md")
    (muster,) = loader.lade_musterloesungen("e005-zwei-aufzuege")
    erg = pruefe(aufgabe, muster["code"], docker_runner)
    assert erg.bestanden and erg.wertung.sterne == 3
