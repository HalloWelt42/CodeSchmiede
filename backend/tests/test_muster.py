"""Muster-Jagd: Prüfer gegen die echte JavaScript-Sandbox."""

import textwrap

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.pruefung.orchestrator import anzahl_versteckt, oeffentliches_extra, pruefe

from .conftest import braucht_sandbox, schreibe_aufgabe

LEVEL = """\
    zeitlimit_sekunden: 2
    muster:
      treffer: ["PLZ 70173", "10115 Berlin"]
      nieten: ["Tel. 0711123456", "1234"]
      treffer_versteckt: ["(20095)"]
      nieten_versteckt: ["123456"]
      sterne: {zwei: 12, drei: 9}
    """


@pytest.fixture
def level(tmp_path):
    ordner = schreibe_aufgabe(tmp_path, "javascript", "m900-plz", "muster_jagd", textwrap.dedent(LEVEL))
    return AufgabenLoader(tmp_path).lade_aufgabe(ordner / "aufgabe.md")


def test_versteckte_zeilen_bleiben_verborgen(level):
    extra = oeffentliches_extra(level)["muster"]
    assert "treffer_versteckt" not in extra and "nieten_versteckt" not in extra
    assert extra["sterne"] == {"zwei": 12, "drei": 9}
    assert anzahl_versteckt(level) == 2


@braucht_sandbox
def test_kurzes_muster_drei_sterne(level, docker_runner):
    erg = pruefe(level, r"\b\d{5}\b", docker_runner)
    assert erg.bestanden and erg.versteckt_pass == 2
    assert erg.wertung.sterne == 3
    assert [t.tatsaechlich for t in erg.sichtbar] == [True, True, False, False]


@braucht_sandbox
def test_langes_muster_weniger_sterne(level, docker_runner):
    erg = pruefe(level, r"\b[0-9]{5}\b", docker_runner)
    assert erg.bestanden and erg.wertung.sterne == 2
    erg = pruefe(level, r"(?<!\d)[0-9]{5}(?!\d)", docker_runner)
    assert erg.bestanden and erg.wertung.sterne == 1


@braucht_sandbox
def test_falsches_muster_zeigt_die_zeilen(level, docker_runner):
    erg = pruefe(level, r"\d{5}", docker_runner)
    assert not erg.bestanden and erg.wertung.sterne == 0
    assert [t.bestanden for t in erg.sichtbar] == [True, True, False, True]
    assert erg.versteckt_fail == 1


@braucht_sandbox
def test_ungueltiges_muster(level, docker_runner):
    erg = pruefe(level, r"(\d", docker_runner)
    assert not erg.bestanden and "Invalid regular expression" in erg.stderr


@braucht_sandbox
def test_gieriges_muster_laeuft_in_die_zeitgrenze(tmp_path, docker_runner):
    ordner = schreibe_aufgabe(tmp_path, "javascript", "m901-gierig", "muster_jagd", textwrap.dedent("""\
        zeitlimit_sekunden: 1
        muster:
          treffer: ["aaa"]
          nieten: ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
          sterne: {zwei: 10, drei: 5}
        """))
    aufgabe = AufgabenLoader(tmp_path).lade_aufgabe(ordner / "aufgabe.md")
    erg = pruefe(aufgabe, "^(a+)+$", docker_runner)
    assert not erg.bestanden and erg.timeout and "zu lange" in erg.stderr


def test_leeres_muster(level):
    erg = pruefe(level, "\n", runner=None)
    assert not erg.bestanden and "leer" in erg.stderr
