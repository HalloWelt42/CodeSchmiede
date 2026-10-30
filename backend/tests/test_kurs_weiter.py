"""Wo es im Kurs weitergeht: allein aus der echten Kursdatei und dem Erledigten, im selben Kapitel, dann im nächsten
Kapitel desselben Kurses, am Ende zurück zur Übersicht; nie in einen fremden Kurs (früher landete "Guten Morgen" nach
"Hallo, Welt" auf einer CSS-Aufgabe). "Weiter hier" eines Kapitels und der Schritt nach einer Aufgabe folgen derselben
Regel (früher zeigte "Weiter hier" bei fertiger Einführung weiter auf sie, obwohl Übungen offen waren, und das
Kapitelende führte ins noch gesperrte nächste Kapitel)."""

from pathlib import Path

import pytest

from codeschmiede.kurs.einlesen import Kursinhalt, lade
from codeschmiede.kurs.weiter import Erledigt, kapitel_fertig, naechster_schritt, offener_schritt

KURS = Path(__file__).resolve().parents[2] / "kurs"
AUSGABE = ["k011-hallo-welt", "k012-guten-morgen", "k013-pinguin-sagt", "k014-zahlen", "k015-drei-namen",
           "k016-eisbude", "k017-gedicht", "k019-notenbuch-kopf"]


@pytest.fixture(scope="module")
def inhalt() -> Kursinhalt:
    return lade(KURS)


def kapitel(inhalt: Kursinhalt, eid: str):
    return next(k for kurs in inhalt.kurse.values() for k in kurs.kapitel() if k.einfuehrung == eid)


def erledigt(aufgaben=(), einfuehrungen=(), uebersprungen=()) -> Erledigt:
    return Erledigt(aufgaben=frozenset(aufgaben), einfuehrungen=frozenset(einfuehrungen), uebersprungen=frozenset(uebersprungen))


def test_python_kapitel_eins_bis_ins_zweite_kapitel(inhalt):
    for nr, (aktuell, erwartet) in enumerate(zip(AUSGABE, AUSGABE[1:])):
        schritt = naechster_schritt(inhalt, aktuell, erledigt(AUSGABE[:nr + 1], ["py-ausgabe"]), "py-ausgabe")
        assert (schritt.art, schritt.einfuehrung, schritt.aufgabe_id) == ("aufgabe", "py-ausgabe", erwartet)
    am_ende = naechster_schritt(inhalt, "k019-notenbuch-kopf", erledigt(AUSGABE, ["py-ausgabe"]), "py-ausgabe")
    assert (am_ende.art, am_ende.einfuehrung) == ("kapitel", "py-variablen")


def test_ohne_kontext_gilt_das_kapitel_der_aufgabe(inhalt):
    schritt = naechster_schritt(inhalt, "k011-hallo-welt", erledigt(["k011-hallo-welt"], ["py-ausgabe"]))
    assert (schritt.art, schritt.einfuehrung, schritt.aufgabe_id) == ("aufgabe", "py-ausgabe", "k012-guten-morgen")


def test_nie_in_einen_fremden_kurs(inhalt):
    python = inhalt.kurse["python"]
    python_aufgaben = {aid for k in python.kapitel() for aid in (*k.uebungen, *k.projekt)}
    python_kapitel = {k.einfuehrung for k in python.kapitel()}
    for kap in python.kapitel():
        for aid in (*kap.uebungen, *kap.projekt):
            schritt = naechster_schritt(inhalt, aid, erledigt([aid]), kap.einfuehrung)
            assert schritt.art in ("aufgabe", "kapitel", "kurs")
            assert schritt.aufgabe_id is None or schritt.aufgabe_id in python_aufgaben
            assert schritt.einfuehrung is None or schritt.einfuehrung in python_kapitel


def test_kursende_fuehrt_zur_uebersicht(inhalt):
    kapitel_liste = [k for k in inhalt.kurse["python"].kapitel() if k.einfuehrung in inhalt.einfuehrungen]
    alles = erledigt([aid for k in kapitel_liste for aid in (*k.uebungen, *k.projekt)], [k.einfuehrung for k in kapitel_liste])
    letztes = kapitel_liste[-1]
    assert naechster_schritt(inhalt, [*letztes.uebungen, *letztes.projekt][-1], alles, letztes.einfuehrung).art == "kurs"


def test_vertiefung_fuehrt_zurueck_ins_kapitel_und_fremde_aufgabe_ist_keiner(inhalt):
    assert naechster_schritt(inhalt, "fremd-123", erledigt(), "py-ausgabe").model_dump(exclude_none=True) == {
        "art": "kapitel", "einfuehrung": "py-ausgabe"}
    assert naechster_schritt(inhalt, "fremd-123", erledigt()).art == "keiner"


# Stand aus HELF-33: Einführung "Werte und Variablen" ganz gelesen, drei der sieben Übungen gelöst
VARIABLEN = erledigt([*AUSGABE, "k021-erster-name", "k022-lieblingsfisch", "k023-wohnort"], ["py-ausgabe", "py-variablen"])


def test_weiter_hier_zeigt_auf_die_erste_offene_uebung_statt_auf_die_fertige_einfuehrung(inhalt):
    kap = kapitel(inhalt, "py-variablen")
    assert not kapitel_fertig(kap, VARIABLEN)
    schritt = offener_schritt(kap, VARIABLEN)
    assert (schritt.art, schritt.aufgabe_id) == ("aufgabe", "k024-punkte-steigen")
    assert offener_schritt(kap, erledigt(einfuehrungen=["py-ausgabe"])).art == "kapitel"
    assert offener_schritt(kapitel(inhalt, "py-ausgabe"), VARIABLEN) is None


def test_kapitelende_mit_offener_uebung_bleibt_im_kapitel(inhalt):
    bis_projekt = erledigt([*VARIABLEN.aufgaben, "k025-wer-ist-wer", "k026-dreimal", "k027-tauschen", "k029-notenbuch-namen"],
                           VARIABLEN.einfuehrungen)
    schritt = naechster_schritt(inhalt, "k029-notenbuch-namen", bis_projekt, "py-variablen")
    assert (schritt.art, schritt.einfuehrung, schritt.aufgabe_id) == ("aufgabe", "py-variablen", "k024-punkte-steigen")


def test_nur_die_eigene_aufgabe_offen_fuehrt_ins_eigene_kapitel(inhalt):
    kap = kapitel(inhalt, "py-variablen")
    alle_ausser = erledigt([*AUSGABE, *kap.uebungen[1:], *kap.projekt], ["py-ausgabe", "py-variablen"])
    schritt = naechster_schritt(inhalt, kap.uebungen[0], alle_ausser, "py-variablen")
    assert (schritt.art, schritt.einfuehrung) == ("kapitel", "py-variablen")


def test_nach_dem_kapitel_zum_ersten_offenen_element_des_naechsten(inhalt):
    variablen, rechnen = kapitel(inhalt, "py-variablen"), kapitel(inhalt, "py-rechnen")
    fertig = [*AUSGABE, *variablen.uebungen, *variablen.projekt]
    schritt = naechster_schritt(inhalt, variablen.projekt[-1], erledigt([*fertig, rechnen.uebungen[0]], ["py-ausgabe", "py-variablen", "py-rechnen"]),
                                "py-variablen")
    assert (schritt.art, schritt.aufgabe_id) == ("aufgabe", rechnen.uebungen[1])
    # übersprungenes Kapitel (Kurztest) gilt als erledigt, es geht dahinter weiter
    schritt = naechster_schritt(inhalt, variablen.projekt[-1], erledigt(fertig, ["py-ausgabe", "py-variablen"], ["py-rechnen"]), "py-variablen")
    assert (schritt.art, schritt.einfuehrung) == ("kapitel", "py-text")
