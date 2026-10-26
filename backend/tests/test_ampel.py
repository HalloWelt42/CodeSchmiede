"""Ampelschule: Welt, Regeln, Teilschritte und die echten Levels.

Die Welt und die Regeln laufen ohne Sandbox. Die Levels aus aufgaben/ prüft ein Lauf mit dem lokalen Python (nur
eigene Musterlösungen und kleine Gegenproben); ein Level läuft zusätzlich in der echten Sandbox.
"""

import subprocess
import sys
import time

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung import ampel_pruefer
from codeschmiede.pruefung.orchestrator import pruefe, pruefer_fuer
from codeschmiede.sandbox.result import RunResult
from codeschmiede.steuerung import ampel_anlage, ampel_welt
from codeschmiede.steuerung.ampel_regeln import AmpelLauf, Feindlich, Gelb, Raeumzeit, Rotgelb
from codeschmiede.steuerung.teilschritte import ablauf_mengen

from .conftest import braucht_sandbox

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "python").glob("v0*/aufgabe.md"))


class LokalerRunner:
    """Führt das Skript mit dem Python der Tests aus, wie die Sandbox es täte (ohne Grenzen)."""

    def run_code(self, code, sprache, limits=None):
        start = time.perf_counter()
        p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=120)
        return RunResult(stdout=p.stdout, stderr=p.stderr, exit_code=p.returncode,
                         laufzeit_ms=(time.perf_counter() - start) * 1000)


def ueberweg():
    return ampel_anlage.baue(ampel_anlage.UeberwegVorgabe(vorlage="ueberweg"))


def ablauf(ankuenfte, dauer=30):
    return {"name": "Probe", "dauer": dauer, "ankuenfte": ankuenfte, "nacht": [], "stoerung": None}


# --- Anlage und Welt -----------------------------------------------------------


def test_ueberweg_kreuzt_jede_fahrbahn_mit_beiden_gehrichtungen():
    anlage = ueberweg()
    paare = {(a, b) for a, _, _, b, _, _ in anlage.konflikte}
    assert paare == {("west_gerade", "ueberweg_mitte_a"), ("west_gerade", "ueberweg_mitte_b"),
                     ("ost_gerade", "ueberweg_mitte_a"), ("ost_gerade", "ueberweg_mitte_b")}
    welt = ampel_welt.Welt(anlage.fuer_welt(), ablauf([]))
    assert welt.feindlich == {"auto": {"fuss"}, "fuss": {"auto"}}


def test_kreuzende_wege_einer_gruppe_sind_ein_befund():
    vorgabe = ampel_anlage.KreuzungVorgabe.model_validate({
        "vorlage": "kreuzung",
        "zufahrten": {"nord": {"spuren": [{"wege": ["gerade", "links"], "gruppe": "ns"}]},
                      "sued": {"spuren": [{"wege": ["gerade"], "gruppe": "ns"}]}},
    })
    assert any("nord_links" in b and "sued_gerade" in b for b in ampel_anlage.befunde(vorgabe))


def test_auto_haelt_bei_rot_und_faehrt_bei_gruen():
    anlage = ueberweg().fuer_welt()
    signale = [{"auto": "rot", "fuss": "rot"}] * 8 + [{"auto": "gruen", "fuss": "rot"}] * 10
    welt, _ = ampel_welt.nachspielen(anlage, ablauf([{"t": 0, "weg": "west_gerade", "art": "auto"}], 18), signale)
    auto = welt.alle[0]
    halt = next(w for w in anlage["wege"] if w["id"] == "west_gerade")["halt"]
    stand = [s for _, teilnehmer in welt.bilder[:32] for i, s in teilnehmer if i == 0]
    assert max(stand) <= halt and auto.warten > 3
    assert auto.fertig or auto.s > halt


def test_gruen_fuer_beide_ueberfaehrt_den_fussgaenger():
    anlage = ueberweg().fuer_welt()
    # das Auto erreicht den Überweg nach gut 3 s, der Fußgänger von Süden ist dann gerade auf seiner Spur
    ankuenfte = [{"t": 0, "weg": "west_gerade", "art": "auto"}, {"t": 2.8, "weg": "ueberweg_mitte_b", "art": "fuss"}]
    welt, _ = ampel_welt.nachspielen(anlage, ablauf(ankuenfte, 12), [{"auto": "gruen", "fuss": "gruen"}] * 12)
    assert [u["art"] for u in welt.unfaelle] == ["fuss"]


def test_signale_werden_geprueft():
    gruppen = {"auto": {"art": "auto"}, "fuss": {"art": "fuss"}}
    assert "kein Signal für fuss" in ampel_welt.signale_pruefen(gruppen, {"auto": "rot"})
    assert "gibt es nicht" in ampel_welt.signale_pruefen(gruppen, {"auto": "lila", "fuss": "rot"})
    assert "gibt es nicht" in ampel_welt.signale_pruefen(gruppen, {"auto": "rot", "fuss": "gelb"})
    assert ampel_welt.signale_pruefen(gruppen, {"fuss": "rot", "auto": "gruen"}) == {"auto": "gruen", "fuss": "rot"}


# --- Regeln und Teilschritte ---------------------------------------------------


def lauf(folge):
    """Ein Lauf aus einer Folge (auto, fuss) je Sekunde, ohne Verkehr."""
    signale = [{"auto": a, "fuss": f} for a, f in folge]
    verlauf = [{"bedarf": {"auto": False, "fuss": False}, "nacht": False, "einsatz": None, "stoerung": None}] * len(signale)
    return AmpelLauf(name="Probe", sichtbar=True, dauer=len(signale), arten={"auto": "auto", "fuss": "fuss"},
                     feindlich={"auto": {"fuss"}, "fuss": {"auto"}}, signale=signale, verlauf=verlauf,
                     teilnehmer=[], unfaelle=[])


def test_regeln_finden_die_stelle():
    hart = lauf([("gruen", "rot")] * 3 + [("rot", "gruen")] * 3)
    assert Gelb(art="gelb").pruefe(hart)[0].sekunde == 3
    assert Raeumzeit(art="raeumzeit").pruefe(hart)[0].text.startswith("fuss öffnet 0 s nach auto")
    assert Feindlich(art="feindlich").pruefe(lauf([("gelb", "gruen")]))
    sauber = lauf([("gruen", "rot")] * 2 + [("gelb", "rot")] * 3 + [("rot", "rot")] * 2 + [("rot", "gruen")] * 4
                  + [("rot", "rot")] * 3 + [("rotgelb", "rot"), ("gruen", "rot")])
    for regel in (Gelb(art="gelb"), Rotgelb(art="rotgelb"), Raeumzeit(art="raeumzeit"), Feindlich(art="feindlich")):
        assert regel.pruefe(sauber) == []


def test_ablaeufe_der_teilschritte_wachsen():
    class Schritt:
        def __init__(self, ablaeufe):
            self.titel = self.text = "x"
            self.regeln = []
            self.ablaeufe = ablaeufe

    mengen = ablauf_mengen([Schritt(None), Schritt(["Nacht"]), Schritt(None), Schritt("alle")],
                           ["Alltag", "Nacht", "Geheim"], "Alltag")
    assert mengen == [{"Alltag"}, {"Alltag", "Nacht"}, {"Alltag", "Nacht"}, {"Alltag", "Nacht", "Geheim"}]


# --- die echten Levels ---------------------------------------------------------


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def test_acht_levels(loader):
    assert LEVELS == [f"v00{i}-{n}" for i, n in enumerate(
        ["fester-takt", "knopfdruck", "zwei-strassen", "kontaktschleifen", "fussgaenger-ringsum",
         "linksabbieger", "grosse-kreuzung", "sonderfaelle"], start=1)]


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / aid / "aufgabe.md")
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    runner = LokalerRunner()
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], runner)
    assert erg.bestanden, erg.sichtbar[0].tatsaechlich and [t["befunde"] for t in erg.sichtbar[0].tatsaechlich["teilschritte"]]
    assert erg.wertung.sterne == 3, [k.text for k in erg.wertung.kriterien if not k.erreicht]
    start = pruefe(aufgabe, aufgabe.starter_code, runner)
    assert not start.bestanden and not start.sichtbar[0].tatsaechlich["teilschritte"][0]["erfuellt"]


def test_ohne_blick_auf_frei_kracht_es_im_lieferverkehr(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "v002-knopfdruck" / "aufgabe.md")
    (muster,) = loader.lade_musterloesungen("v002-knopfdruck")
    erg = pruefe(aufgabe, muster["code"].replace('lage.frei["fuss"]', "True"), LokalerRunner())
    auswertung = erg.sichtbar[0].tatsaechlich
    liefer = next(a for a in auswertung["ablaeufe"] if a["name"] == "Lieferverkehr")
    assert not erg.bestanden and liefer["kennzahlen"]["unfaelle"] > 0
    # der misslungene versteckte Ablauf lässt sich abspielen
    assert [w["name"] for w in auswertung["wiedergaben"]] == ["Feierabend", "Lieferverkehr"]


def test_versteckte_ablaeufe_bleiben_verborgen(loader):
    from codeschmiede.pruefung.orchestrator import oeffentliches_extra

    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "v002-knopfdruck" / "aufgabe.md")
    assert "versteckt" not in oeffentliches_extra(aufgabe)["ampel"]


def test_programmfehler_mit_zeile(loader):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "v001-fester-takt" / "aufgabe.md")
    erg = ampel_pruefer.lauf_sichtbar(aufgabe, "def takt(lage):\n    return {'auto': 'gruen', 'fuss': rot}\n",
                                      LokalerRunner())
    fehler = erg.auswertung.ablaeufe[0].erster_befund
    assert "NameError" in fehler and "Zeile 2" in fehler


@braucht_sandbox
def test_level_in_der_sandbox(loader, docker_runner):
    aufgabe = loader.lade_aufgabe(AUFGABEN / "python" / "v002-knopfdruck" / "aufgabe.md")
    (muster,) = loader.lade_musterloesungen("v002-knopfdruck")
    erg = pruefe(aufgabe, muster["code"], docker_runner)
    assert erg.bestanden and erg.wertung.sterne == 3
