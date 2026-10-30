"""Aufbaukurs: Einlesen und Prüfung der Inhalte, Antworten nur auf dem Server, Freischaltung, Beispiele, Kurztest,
Merkblatt und der Programm-Prüfer für die Übungen."""

import json
import textwrap
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
from codeschmiede.kurs.einlesen import abschnitte, lade
from codeschmiede.kurs.modelle import Ordnungsfrage
from codeschmiede.pruefung.orchestrator import pruefe

from .conftest import braucht_sandbox, schreibe_aufgabe

BEGRIFFE = """\
sprache: python
begriffe:
  - {id: ausgabe, titel: Ausgabe mit print, erkennung: {aufrufe: [print]}}
  - {id: text, titel: Text, erkennung: {literale: [str]}}
  - {id: variable, titel: Variablen, erkennung: {knoten: [Assign]}}
  - {id: for_schleife, titel: for, erkennung: {knoten: [For]}}
"""

EINFUEHRUNG = '''\
---
id: py-ausgabe
sprache: python
titel: Hallo, Ausgabe
kurz: Text auf den Bildschirm bringen.
fuehrt_ein: [ausgabe, text]
lernziele: [Text mit print ausgeben]
karte: Ich bringe Text auf den Schirm
bilder:
  - {schluessel: karte_py_ausgabe, art: sammelkarte, sprache: python, motiv: Ein Papagei mit Megafon ruft laut}
---

## Hallo sagen

Mit `print` erscheint Text.

```beispiel
id: hallo
code: |
  print("Hallo")
vorhersage:
  art: auswahl
  optionen:
    - {text: "Hallo", richtig: true, erklaerung: "Genau, ohne Anführungszeichen."}
    - {text: "print(Hallo)", erklaerung: "Ausgegeben wird nur der Text."}
```

```merke
text: print gibt aus, was in den Klammern steht.
```

```frage
frageart: auswahl
id: was-macht-print
text: Was macht print?
optionen:
  - {text: Es gibt Text aus, richtig: true, erklaerung: Richtig.}
  - {text: Es rechnet, erklaerung: Rechnen kommt später.}
```

## Lücken füllen

```falle
titel: Anführungszeichen vergessen
text: Ohne Anführungszeichen hält Python den Text für einen Namen.
```

```frage
frageart: luecke
id: luecke-print
text: Ergänze die Zeile.
code: '___("Hi")'
antworten: [[print]]
erklaerung: Richtig, print.
hinweis: Gesucht ist das Wort zum Ausgeben.
```
'''

KURZTEST = """\
fragen:
  - frageart: ordnen
    id: test-ordnen
    text: Bring die Zeilen in Reihenfolge.
    zeilen: ['print("eins")', 'print("zwei")', 'print("drei")']
    erklaerung: Von oben nach unten.
    hinweis: Python liest von oben nach unten.
  - frageart: fehlerstelle
    id: test-fehler
    text: Wo ist der Fehler?
    code: |
      print("a")
      print(b)
    zeile: 2
    erklaerung: Ohne Anführungszeichen ist b ein Name.
    hinweis: Schau auf die Anführungszeichen.
uebung: 090-programm-hallo
"""


def baue_kurs(kurs: Path, aufgaben: Path, einfuehrung: str = EINFUEHRUNG) -> None:
    (kurs / "begriffe").mkdir(parents=True)
    (kurs / "begriffe" / "python.yml").write_text(BEGRIFFE, encoding="utf-8")
    ordner = kurs / "einfuehrungen" / "python" / "ausgabe"
    ordner.mkdir(parents=True)
    (ordner / "einfuehrung.md").write_text(einfuehrung, encoding="utf-8")
    (ordner / "kurztest.yml").write_text(KURZTEST, encoding="utf-8")
    (kurs / "python.yml").write_text(textwrap.dedent("""\
        sprache: python
        titel: Python
        bloecke:
          - titel: Erste Schritte
            kapitel:
              - {einfuehrung: py-ausgabe, uebungen: [090-programm-hallo]}
        """), encoding="utf-8")
    loesung = schreibe_aufgabe(aufgaben, "python", "090-programm-hallo", "programm", """\
        tests_sichtbar:
          - {input: [], expected: "Hallo Welt\\n"}
        tests_versteckt:
          - {input: [], expected: "Hallo Welt"}
        """)
    (loesung / "solution_idiomatic.py").write_text('print("Hallo Welt")\n')


@pytest.fixture
def kurs_settings(settings: Settings) -> Settings:
    baue_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    return settings


@pytest.fixture
def kurs_client(kurs_settings: Settings, docker_runner) -> TestClient:
    return TestClient(app_bauen(kurs_settings, runner=docker_runner))


def test_einlesen_zerlegt_abschnitte_und_bloecke(tmp_path):
    baue_kurs(tmp_path / "kurs", tmp_path / "aufgaben")
    inhalt = lade(tmp_path / "kurs")
    assert inhalt.ladefehler == []
    e = inhalt.einfuehrungen["py-ausgabe"]
    assert [a.titel for a in e.abschnitte] == ["Hallo sagen", "Lücken füllen"]
    assert [t.art for t in e.abschnitte[0].teile] == ["text", "beispiel", "merke", "frage"]
    assert inhalt.kurztests["py-ausgabe"].uebung == "090-programm-hallo"


def test_kaputte_bloecke_werden_gemeldet():
    with pytest.raises(ValueError, match="nicht geschlossen"):
        abschnitte("## A\n```merke\ntext: x\n")
    with pytest.raises(ValueError, match="vor dem ersten Abschnitt"):
        abschnitte("Text ohne Abschnitt\n## A\nx")


def test_unbekanntes_feld_ist_ladefehler(tmp_path):
    baue_kurs(tmp_path / "kurs", tmp_path / "aufgaben", EINFUEHRUNG.replace("karte: Ich", "karte_tippfehler: x\nkarte: Ich"))
    inhalt = lade(tmp_path / "kurs")
    assert "py-ausgabe" not in inhalt.einfuehrungen and "karte_tippfehler" in inhalt.ladefehler[0].meldung


def test_ordnen_mischt_fest_und_nie_richtig():
    f = Ordnungsfrage(frageart="ordnen", id="x", text="t", zeilen=["a", "b", "c"], erklaerung="e", hinweis="h")
    assert f.gemischt() == f.gemischt() and f.gemischt() != f.zeilen and sorted(f.gemischt()) == sorted(f.zeilen)


def test_befunde_ohne_fehler_und_mit_vorgriff(kurs_settings: Settings, docker_runner):
    state = app_bauen(kurs_settings, runner=docker_runner).state.codeschmiede
    meldungen = [b.meldung for b in state.kurs.befunde]
    assert not any("voraus" in m for m in meldungen), meldungen
    # eine Variable im Beispiel ist ein Vorgriff: Kapitel 1 führt sie nicht ein
    datei = kurs_settings.kurs_pfad / "einfuehrungen" / "python" / "ausgabe" / "einfuehrung.md"
    datei.write_text(EINFUEHRUNG.replace('  print("Hallo")', '  gruss = "Hallo"\n  print(gruss)'), encoding="utf-8")
    state.neu_einlesen()
    assert any("variable" in b.meldung and "Beispiel hallo" in b.ort for b in state.befunde)


def test_einfuehrung_verraet_keine_antworten(kurs_client):
    roh = kurs_client.get("/api/kurs/einfuehrung/py-ausgabe").text
    for geheim in ("richtig\": true", "erklaerung", "antworten", "Genau, ohne", "Richtig, print"):
        assert geheim not in roh
    daten = json.loads(roh)
    assert daten["abschnitte"][0]["teile"][1]["vorhersage"]["optionen"] == ["Hallo", "print(Hallo)"]


def test_kapitel_fortschritt_bis_fertig(kurs_client):
    kapitel = kurs_client.get("/api/kurs").json()[0]["bloecke"][0]["kapitel"][0]
    assert kapitel["stand"] == "aktuell" and not kapitel["uebungen_offen"] and kapitel["bild"]["url"] is None
    assert kapitel["offen"] == {"art": "kapitel", "einfuehrung": "py-ausgabe", "aufgabe_id": None}

    # Abschnitt erst nach richtiger Antwort fertig
    assert kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/abschnitt/1/fertig").status_code == 409
    falsch = kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/antwort", json={"element": "was-macht-print", "wahl": [1]}).json()
    assert not falsch["richtig"] and falsch["erklaerung"] == "Rechnen kommt später."
    richtig = kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/antwort", json={"element": "was-macht-print", "wahl": [0]}).json()
    assert richtig["richtig"] and richtig["abschnitt_bereit"]
    assert kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/abschnitt/1/fertig").status_code == 200

    luecke = kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/antwort", json={"element": "luecke-print", "luecken": [" print "]}).json()
    assert luecke["richtig"]
    e = kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/abschnitt/2/fertig").json()
    assert all(a["fertig"] for a in e["abschnitte"])

    kapitel = kurs_client.get("/api/kurs").json()[0]["bloecke"][0]["kapitel"][0]
    assert kapitel["uebungen_offen"] and kapitel["stand"] == "aktuell" and kapitel["abschnitte_fertig"] == 2
    # "Weiter hier" zeigt jetzt auf die offene Übung, nicht mehr auf die fertige Einführung
    assert kapitel["offen"] == {"art": "aufgabe", "einfuehrung": "py-ausgabe", "aufgabe_id": "090-programm-hallo"}


@braucht_sandbox
def test_ausfuehren_erst_nach_vorhersage(kurs_client):
    weg = "/api/kurs/einfuehrung/py-ausgabe/beispiel/hallo/ausfuehren"
    assert kurs_client.post(weg, json={}).status_code == 409
    urteil = kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/antwort", json={"element": "hallo", "wahl": [1]}).json()
    assert not urteil["richtig"]
    lauf = kurs_client.post(weg, json={}).json()
    assert lauf["ausgabe"] == "Hallo\n" and [s["zeile"] for s in lauf["schritte"]] == [1]
    veraendert = kurs_client.post(weg, json={"code": 'print("Tschüss")'}).json()
    assert veraendert["ausgabe"] == "Tschüss\n"


@braucht_sandbox
def test_kurztest_bestehen_ueberspringt_das_kapitel(kurs_client):
    test = kurs_client.get("/api/kurs/kurztest/py-ausgabe").json()
    ordnen = test["fragen"][0]
    reihenfolge = [ordnen["zeilen"].index(z) for z in ['print("eins")', 'print("zwei")', 'print("drei")']]
    assert kurs_client.post("/api/kurs/kurztest/py-ausgabe/antwort", json={"element": "test-ordnen", "reihenfolge": reihenfolge}).json()["richtig"]
    falsch = kurs_client.post("/api/kurs/kurztest/py-ausgabe/antwort", json={"element": "test-fehler", "zeile": 1}).json()
    assert not falsch["richtig"] and falsch["erklaerung"] == "Schau auf die Anführungszeichen."
    assert kurs_client.post("/api/kurs/kurztest/py-ausgabe/antwort", json={"element": "test-fehler", "zeile": 2}).json()["richtig"]
    assert not kurs_client.get("/api/kurs/kurztest/py-ausgabe").json()["bestanden"]     # Übung fehlt noch
    abgabe = kurs_client.post("/api/submissions", json={"aufgabe_id": "090-programm-hallo", "code": 'print("Hallo Welt")'}).json()
    assert abgabe["bestanden"]
    assert kurs_client.get("/api/kurs/kurztest/py-ausgabe").json()["bestanden"]
    assert kurs_client.get("/api/kurs").json()[0]["bloecke"][0]["kapitel"][0]["stand"] == "uebersprungen"


@braucht_sandbox
def test_merkblatt_sammelt_merke_fallen_und_beispiele(kurs_client):
    m = kurs_client.get("/api/kurs/merkblatt/py-ausgabe").json()
    assert m["merke"] == ["print gibt aus, was in den Klammern steht."]
    assert m["fallen"][0]["titel"] == "Anführungszeichen vergessen"
    assert m["beispiele"][0] == {"code": 'print("Hallo")\n', "html": None, "ausgabe": "Hallo\n"}
    assert m["begriffe"] == ["Ausgabe mit print", "Text"]


@braucht_sandbox
def test_programm_pruefer_mit_eingabe(kurs_settings, docker_runner):
    state = app_bauen(kurs_settings, runner=docker_runner).state.codeschmiede
    schreibe_aufgabe(kurs_settings.aufgaben_pfad, "python", "091-gruss", "programm", """\
        tests_sichtbar:
          - {input: [Anna], expected: "Wie heißt du? Hallo Anna!"}
        tests_versteckt:
          - {input: [Bo], expected: "Wie heißt du? Hallo Bo!"}
        """)
    state.neu_einlesen()
    aufgabe = state.aufgaben.aufgabe("091-gruss")
    gut = pruefe(aufgabe, 'name = input("Wie heißt du? ")\nprint("Hallo " + name + "!")\n', docker_runner)
    assert gut.bestanden and gut.versteckt_pass == 1
    schlecht = pruefe(aufgabe, 'print("Hallo Anna!")\n', docker_runner)
    assert not schlecht.bestanden and schlecht.versteckt_fail == 1
    kaputt = pruefe(aufgabe, 'print("Hallo"\n', docker_runner)
    assert not kaputt.bestanden and "SyntaxError" in (kaputt.sichtbar[0].fehler or "")


def test_abschnitt_bringt_erfahrung_und_zaehlt_zur_serie(kurs_client):
    vorher = kurs_client.get("/api/spiel/stand").json()
    kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/antwort", json={"element": "was-macht-print", "wahl": [0]})
    kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/abschnitt/1/fertig")
    kurs_client.post("/api/kurs/einfuehrung/py-ausgabe/abschnitt/1/fertig")   # zweimal fertig zählt einmal
    nachher = kurs_client.get("/api/spiel/stand").json()
    assert nachher["punkte"] == vorher["punkte"] + 5
    assert nachher["serie"]["heute_geuebt"] and not vorher["serie"]["heute_geuebt"]


@braucht_sandbox
def test_probelauf_eines_programms_mit_eingabe(kurs_settings, docker_runner):
    schreibe_aufgabe(kurs_settings.aufgaben_pfad, "python", "092-echo", "programm", """\
        tests_sichtbar:
          - {input: [a], expected: "a"}
        """)
    client = TestClient(app_bauen(kurs_settings, runner=docker_runner))
    antwort = client.post("/api/submissions/probelauf", json={"aufgabe_id": "092-echo", "code": "print(input() * 2)", "input": ["ab"]}).json()
    assert antwort["stdout"] == "abab\n" and antwort["fehler"] is None


def test_gesperrtes_kapitel_nur_per_kurztest(kurs_settings, docker_runner):
    zweite = kurs_settings.kurs_pfad / "einfuehrungen" / "python" / "zwei"
    zweite.mkdir(parents=True)
    (zweite / "einfuehrung.md").write_text(EINFUEHRUNG.replace("id: py-ausgabe", "id: py-zwei").replace("fuehrt_ein: [ausgabe, text]", "fuehrt_ein: [variable]"), encoding="utf-8")
    kurs = kurs_settings.kurs_pfad / "python.yml"
    kurs.write_text(kurs.read_text() + "      - {einfuehrung: py-zwei}\n", encoding="utf-8")
    client = TestClient(app_bauen(kurs_settings, runner=docker_runner))
    assert client.get("/api/kurs").json()[0]["bloecke"][0]["kapitel"][1]["stand"] == "zu"
    assert client.get("/api/kurs/einfuehrung/py-zwei").status_code == 409
    assert client.post("/api/kurs/einfuehrung/py-zwei/antwort", json={"element": "was-macht-print", "wahl": [0]}).status_code == 409
    assert client.get("/api/kurs/einfuehrung/py-ausgabe").status_code == 200
