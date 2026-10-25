"""Roboter-Parcours: Welt, Nachspielen und Prüfer (mit echter Sandbox)."""

import textwrap

import pytest
from pydantic import ValidationError

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.pruefung.orchestrator import anzahl_versteckt, oeffentliches_extra, pruefe
from codeschmiede.pruefung.roboter_pruefer import zeichen_code, zeilen_code
from codeschmiede.pruefung.roboter_welt import Aktion, Welt, nachspielen

from .conftest import braucht_sandbox, schreibe_aufgabe

GANG = """
#######
#>.K.Z#
#######
"""

LEVEL = """\
    roboter:
      welt: |
        #######
        #>.K.Z#
        #######
      versteckt:
        - |
          #########
          #>..K..Z#
          #########
      sterne: {schritte: 5, zeichen: 45}
    """

LOESUNG = "while not am_ziel():\n    gehe()\n    if kristall():\n        nimm()\n"


def aktionen(*befehle: str) -> list[Aktion]:
    return [Aktion(befehl=b, zeile=i + 1) for i, b in enumerate(befehle)]


def test_welt_aus_text_und_pruefung():
    welt = Welt.model_validate(GANG)
    assert (welt.breite, welt.hoehe, welt.start()) == (7, 3, (1, 1, 0))
    with pytest.raises(ValidationError):
        Welt.model_validate("#>.#\n#..")  # ungleich lang
    with pytest.raises(ValidationError):
        Welt.model_validate("#>..#")  # kein Ziel


def test_nachspielen():
    welt = Welt.model_validate(GANG)
    ok = nachspielen(welt, aktionen("gehe", "gehe", "nimm", "gehe", "gehe"))
    assert ok.geschafft and len(ok.schritte) == 5 and ok.schritte[-1].x == 5
    ohne = nachspielen(welt, aktionen("gehe", "gehe", "gehe", "gehe"))
    assert not ohne.geschafft and ohne.am_ziel and ohne.kristalle_offen == 1
    wand = nachspielen(welt, aktionen("links", "gehe"))
    assert not wand.geschafft and "Wand" in wand.fehler and "Zeile 2" in wand.fehler
    leer = nachspielen(welt, aktionen("nimm"))
    assert "kein Kristall" in leer.fehler


def test_zeichen_ohne_kommentare():
    assert zeichen_code("# Hinweis\nwhile not am_ziel():  # los\n    gehe()\n") == zeichen_code("while not am_ziel():\n    gehe()")
    assert zeilen_code("# x\n\ngehe()\n  # y\ngehe()\n") == 2


@pytest.fixture
def level(tmp_path):
    ordner = schreibe_aufgabe(tmp_path, "python", "r900-gang", "roboter", textwrap.dedent(LEVEL))
    return AufgabenLoader(tmp_path).lade_aufgabe(ordner / "aufgabe.md")


def test_versteckte_welten_bleiben_verborgen(level):
    extra = oeffentliches_extra(level)["roboter"]
    assert "versteckt" not in extra and "#>.K.Z#" in extra["welt"]
    assert anzahl_versteckt(level) == 1


@braucht_sandbox
def test_schleife_besteht_mit_drei_sternen(level, docker_runner):
    erg = pruefe(level, LOESUNG, docker_runner)
    assert erg.bestanden and erg.versteckt_pass == 1 and erg.wertung.sterne == 3
    lauf = erg.sichtbar[0].tatsaechlich
    assert [s["befehl"] for s in lauf["schritte"]] == ["gehe", "gehe", "nimm", "gehe", "gehe"]
    assert lauf["schritte"][2]["zeile"] == 4
    assert erg.wertung.kennwerte.schritte == 5 and erg.wertung.kennwerte.zeilen == 4


@braucht_sandbox
def test_abgezaehlt_scheitert_in_der_versteckten_welt(level, docker_runner):
    erg = pruefe(level, "gehe()\ngehe()\nnimm()\ngehe()\ngehe()\n", docker_runner)
    assert erg.sichtbar[0].bestanden and not erg.bestanden and erg.versteckt_fail == 1


@braucht_sandbox
def test_fehler_mit_zeile(level, docker_runner):
    erg = pruefe(level, "gehe()\ngeh()\n", docker_runner)
    assert not erg.bestanden and "NameError" in erg.sichtbar[0].fehler and "Zeile 2" in erg.sichtbar[0].fehler
    erg = pruefe(level, "while True:\n    links()\n", docker_runner)
    assert "Schleife endlos" in erg.sichtbar[0].fehler


@braucht_sandbox
def test_abgefangener_absturz_zaehlt_trotzdem(level, docker_runner):
    # wer den Absturz abfängt und weiterläuft, kommt nicht durch: das Backend spielt nach
    code = "links()\ntry:\n    gehe()\nexcept BaseException:\n    pass\nrechts()\nwhile not am_ziel():\n    gehe()\n    if kristall():\n        nimm()\n"
    erg = pruefe(level, code, docker_runner)
    assert not erg.bestanden and "Wand" in erg.sichtbar[0].fehler
