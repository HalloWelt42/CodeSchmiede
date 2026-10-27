"""Codes knacken: Verfahren, Urteil und die echten Levels.

Die Levels aus aufgaben/ prüft ein Lauf mit dem lokalen Python (nur eigene Musterlösungen und kleine Gegenproben);
ein Level läuft zusätzlich in der echten Sandbox.
"""

import subprocess
import sys
import time

import pytest

from codeschmiede.aufgaben.loader import AufgabenLoader
from codeschmiede.config import PROJEKT_WURZEL
from codeschmiede.pruefung import codes_pruefer
from codeschmiede.pruefung.orchestrator import oeffentliches_extra, pruefe, pruefer_fuer
from codeschmiede.sandbox.result import RunResult
from codeschmiede.steuerung import codes

from .conftest import braucht_sandbox

AUFGABEN = PROJEKT_WURZEL / "aufgaben"
LEVELS = sorted(p.parent.name for p in (AUFGABEN / "python").glob("c0*/aufgabe.md"))


class LokalerRunner:
    """Führt das Skript mit dem Python der Tests aus, wie die Sandbox es täte (ohne Grenzen), und merkt es sich."""

    def __init__(self):
        self.skripte = []

    def run_code(self, code, sprache, limits=None):
        self.skripte.append(code)
        start = time.perf_counter()
        p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=120)
        return RunResult(stdout=p.stdout, stderr=p.stderr, exit_code=p.returncode,
                         laufzeit_ms=(time.perf_counter() - start) * 1000)


# --- Verfahren -------------------------------------------------------------------


def test_caesar_laesst_alles_ausser_a_bis_z_stehen():
    assert codes.verschluessele("caesar", "ZEBRA, ÄRGER!", 3) == "CHEUD, ÄUJHU!"
    assert codes.schiebe(codes.schiebe("HALLO WELT", 7), -7) == "HALLO WELT"


def test_ersetzung_mit_mischung_oder_startwert():
    mischung = "QWERTZUIOPASDFGHJKLYXCVBNM"
    assert codes.verschluessele("ersetzung", "ABC XYZ", mischung) == "QWE BNM"
    assert codes.verschluessele("ersetzung", "ABC", 5) == codes.ersetze("ABC", codes.mischung(5))
    assert sorted(codes.mischung(5)) == list(codes.ALPHABET)


def test_vigenere_zaehlt_nur_buchstaben():
    # das Leerzeichen und das Ä schieben den Schlüssel nicht weiter
    assert codes.verschluessele("vigenere", "AA ÄAA", "BC") == "BC ÄBC"


def test_xor_schichten_und_pin():
    geheim = codes.verschluessele("xor", "Grüße", "ab")
    assert bytes(b ^ b"ab"[i % 2] for i, b in enumerate(bytes.fromhex(geheim))).decode() == "Grüße"
    assert codes.verschluessele("schichten", "ABC", ["caesar:1", "hex"]) == "424344"
    assert codes.verschluessele("pin", "0042", None) == codes.pruefwert("0042")


@pytest.mark.parametrize(("verfahren", "klar", "schluessel", "erwartet"), [
    ("caesar", "ABC", 0, "zwischen 1 und 25"),
    ("caesar", "abc", 3, "nur Großbuchstaben"),
    ("ersetzung", "ABC", "ABC", "genau einmal"),
    ("vigenere", "ABC", "kat", "Wort aus A bis Z"),
    ("schichten", "ABC", ["rot13"], "rot13 gibt es nicht"),
    ("pin", "12345", None, "vier Ziffern"),
])
def test_falsche_schluessel_werden_benannt(verfahren, klar, schluessel, erwartet):
    assert any(erwartet in f for f in codes.schluessel_fehler(verfahren, klar, schluessel))


def test_anteil_zaehlt_nur_buchstaben():
    # Leerzeichen und Satzzeichen bleiben beim Verschlüsseln stehen und zählen nicht mit
    assert codes.anteil_gleich("HALLO WELT!", "HALLO WELT!") == 1.0
    assert codes.anteil_gleich("HXLLO WELT!", "HALLO WELT!") == pytest.approx(8 / 9)
    assert codes.anteil_gleich("HALLO", "HALLO WELT") == pytest.approx(5 / 9)
    assert codes.anteil_gleich("1234", "1235") == pytest.approx(3 / 4)


def test_haeufigkeiten_sind_deutsch():
    assert max(codes.DEUTSCH, key=codes.DEUTSCH.get) == "E"
    assert sum(codes.DEUTSCH.values()) == pytest.approx(100, abs=0.5)
    assert codes.PAARE["CH"] > codes.PAARE.get("QX", 0) and "_D" in codes.PAARE


# --- Levels ----------------------------------------------------------------------


@pytest.fixture(scope="module")
def loader():
    return AufgabenLoader(AUFGABEN)


def lade(loader, aid):
    return loader.lade_aufgabe(AUFGABEN / "python" / aid / "aufgabe.md")


def test_sechs_levels():
    assert LEVELS == ["c001-caesar", "c002-ersetzung", "c003-vigenere", "c004-xor", "c005-schichten", "c006-pin"]


@pytest.mark.parametrize("aid", LEVELS)
def test_level_aufbau_und_musterloesung(loader, aid):
    aufgabe = lade(loader, aid)
    assert pruefer_fuer(aufgabe).pruefe_aufbau(aufgabe) == []
    (muster,) = loader.lade_musterloesungen(aid)
    erg = pruefe(aufgabe, muster["code"], LokalerRunner())
    k = erg.wertung.kriterien
    assert erg.bestanden and k[0].erreicht, erg.sichtbar[0].tatsaechlich
    level = codes_pruefer.level_von(aufgabe)
    # die Zeit hängt an der Last der Maschine; die Zeichen nicht
    assert codes_pruefer.zeichen_code(muster["code"]) <= level.sterne.zeichen
    if erg.laufzeit_ms <= level.sterne.ms:
        assert erg.wertung.sterne == 3
    assert not pruefe(aufgabe, aufgabe.starter_code, LokalerRunner()).bestanden


def test_klartexte_gehen_nie_in_die_sandbox(loader):
    aufgabe = lade(loader, "c003-vigenere")
    level = codes_pruefer.level_von(aufgabe)
    runner = LokalerRunner()
    pruefe(aufgabe, "def knacke(geheim):\n    return geheim\n", runner)
    (skript,) = runner.skripte
    assert all(n.klar[:30] not in skript for n in level.nachrichten())
    assert "versteckt" not in oeffentliches_extra(aufgabe)["codes"]


def test_teilschritte_folgen_den_nachrichten(loader):
    aufgabe = lade(loader, "c001-caesar")
    code = (
        'ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\n'
        "def schiebe(text, n):\n"
        '    return "".join(ABC[(ABC.index(c) + n) % 26] if c in ABC else c for c in text)\n'
        "def knacke(geheim):\n"
        "    return schiebe(geheim, -7)\n"
    )
    erg = pruefe(aufgabe, code, LokalerRunner())
    staende = erg.sichtbar[0].tatsaechlich["teilschritte"]
    assert [s["erfuellt"] for s in staende] == [True, False, False]
    assert staende[1]["befunde"][0].startswith("Nachricht 2: ergibt")
    assert not erg.bestanden and erg.versteckt_fail == 3


@pytest.mark.parametrize(("code", "erwartet"), [
    ("def schiebe(t, n):\n    return t\n", "Es fehlt die Funktion knacke()."),
    ("def schiebe(t, n):\n    return t\ndef knacke(g):\n    return 7\n", "knacke() gibt int zurück, keinen Text"),
    ("def schiebe(t, n):\n    return t\ndef knacke(g):\n    return g[99999]\n", "IndexError: string index out of range (Zeile 4)"),
    ("def knacke(g)\n", "SyntaxError"),
])
def test_fehler_werden_benannt(loader, code, erwartet):
    aufgabe = lade(loader, "c001-caesar")
    erg = pruefe(aufgabe, code, LokalerRunner())
    befunde = [b for s in erg.sichtbar[0].tatsaechlich["teilschritte"] for b in s["befunde"]]
    assert any(erwartet in b for b in befunde), befunde


def test_die_uhr_laesst_sich_nicht_verstellen(loader):
    aufgabe = lade(loader, "c006-pin")
    code = (
        "import hashlib, time\n"
        "time.perf_counter = lambda: 0.0\n"
        "def pruefwert(pin):\n"
        "    return hashlib.sha256(pin.encode()).hexdigest()\n"
        "def knacke(geheim):\n"
        "    time.sleep(0.03)\n"
        "    return next(p for p in (f'{z:04d}' for z in range(10000)) if pruefwert(p) == geheim)\n"
    )
    erg = pruefe(aufgabe, code, LokalerRunner())
    assert erg.bestanden and erg.laufzeit_ms >= 6 * 25


def test_probelauf_nur_mit_sichtbaren_nachrichten(loader):
    aufgabe = lade(loader, "c006-pin")
    (muster,) = loader.lade_musterloesungen("c006-pin")
    lauf = codes_pruefer.lauf_sichtbar(aufgabe, muster["code"], LokalerRunner())
    assert [a.name for a in lauf.auswertung.ablaeufe] == ["Probe", "Fahrradschloss", "Haustür"]
    assert lauf.auswertung.teilschritte[-1].geprueft is False
    probe = lauf.auswertung.wiedergaben[0]
    assert probe.aufruf == "pruefwert(klar)" and probe.eingabe == "1234" and probe.ergebnis == codes.pruefwert("1234")


@braucht_sandbox
def test_level_in_der_sandbox(loader, docker_runner):
    aufgabe = lade(loader, "c005-schichten")
    (muster,) = loader.lade_musterloesungen("c005-schichten")
    erg = pruefe(aufgabe, muster["code"], docker_runner)
    assert erg.bestanden and erg.wertung.kriterien[0].erreicht
