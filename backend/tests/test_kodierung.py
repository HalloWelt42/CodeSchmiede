import math

from codeschmiede.pruefung.kodierung import UNDEFINIERT, Unbekannt, anzeigen, dekodiere, gleich


def test_typen_bleiben_erhalten():
    roh = {"__d": [[{"__t": [1, 2]}, {"__s": [3, 4]}], ["a", [1, {"__f": "inf"}]]]}
    wert = dekodiere(roh)
    assert wert == {(1, 2): {3, 4}, "a": [1, math.inf]}


def test_tupel_ist_keine_liste():
    assert not gleich(dekodiere({"__t": [1, 2]}), [1, 2])
    assert gleich(dekodiere([1, 2]), [1, 2])


def test_undefined_ist_nicht_none():
    assert not gleich(dekodiere({"__u": 1}), None)
    assert dekodiere({"__u": 1}) is UNDEFINIERT


def test_unbekanntes_ist_nie_gleich():
    wert = dekodiere({"__r": "Trick: <immer gleich>"})
    assert isinstance(wert, Unbekannt)
    assert not gleich(wert, wert)
    assert not gleich(wert, 1)


def test_anzeige_ist_json_tauglich():
    wert = dekodiere({"__d": [[{"__t": [1]}, {"__s": [2, 1]}], ["n", {"__f": "nan"}]]})
    assert anzeigen(wert) == {"(1,)": [1, 2], "n": "nan"}
