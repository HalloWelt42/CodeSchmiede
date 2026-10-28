"""Nächste Aufgabe im Kurs: allein aus der echten Kursdatei, im selben Kapitel, dann im nächsten Kapitel desselben
Kurses, am Ende zurück zur Übersicht; nie in einen fremden Kurs (früher landete "Guten Morgen" nach "Hallo, Welt" auf
einer CSS-Aufgabe)."""

from pathlib import Path

import pytest

from codeschmiede.kurs.einlesen import Kursinhalt, lade
from codeschmiede.kurs.weiter import naechster_schritt

KURS = Path(__file__).resolve().parents[2] / "kurs"


@pytest.fixture(scope="module")
def inhalt() -> Kursinhalt:
    return lade(KURS)


def test_python_kapitel_eins_bis_ins_zweite_kapitel(inhalt):
    weg = ["k011-hallo-welt", "k012-guten-morgen", "k013-pinguin-sagt", "k014-zahlen", "k015-drei-namen",
           "k016-eisbude", "k017-gedicht", "k019-notenbuch-kopf"]
    for aktuell, erwartet in zip(weg, weg[1:]):
        schritt = naechster_schritt(inhalt, aktuell, "py-ausgabe")
        assert (schritt.art, schritt.einfuehrung, schritt.aufgabe_id) == ("aufgabe", "py-ausgabe", erwartet)
    am_ende = naechster_schritt(inhalt, "k019-notenbuch-kopf", "py-ausgabe")
    assert (am_ende.art, am_ende.einfuehrung) == ("kapitel", "py-variablen")


def test_ohne_kontext_gilt_das_kapitel_der_aufgabe(inhalt):
    schritt = naechster_schritt(inhalt, "k011-hallo-welt")
    assert (schritt.art, schritt.einfuehrung, schritt.aufgabe_id) == ("aufgabe", "py-ausgabe", "k012-guten-morgen")


def test_nie_in_einen_fremden_kurs(inhalt):
    python = inhalt.kurse["python"]
    python_aufgaben = {aid for k in python.kapitel() for aid in (*k.uebungen, *k.projekt)}
    python_kapitel = {k.einfuehrung for k in python.kapitel()}
    for kap in python.kapitel():
        for aid in (*kap.uebungen, *kap.projekt):
            schritt = naechster_schritt(inhalt, aid, kap.einfuehrung)
            assert schritt.art in ("aufgabe", "kapitel", "kurs")
            assert schritt.aufgabe_id is None or schritt.aufgabe_id in python_aufgaben
            assert schritt.einfuehrung is None or schritt.einfuehrung in python_kapitel


def test_kursende_fuehrt_zur_uebersicht(inhalt):
    letztes = [k for k in inhalt.kurse["python"].kapitel() if k.einfuehrung in inhalt.einfuehrungen][-1]
    schritt = naechster_schritt(inhalt, [*letztes.uebungen, *letztes.projekt][-1], letztes.einfuehrung)
    assert schritt.art == "kurs"


def test_vertiefung_fuehrt_zurueck_ins_kapitel_und_fremde_aufgabe_ist_keiner(inhalt):
    assert naechster_schritt(inhalt, "fremd-123", "py-ausgabe").model_dump(exclude_none=True) == {
        "art": "kapitel", "einfuehrung": "py-ausgabe"}
    assert naechster_schritt(inhalt, "fremd-123").art == "keiner"
