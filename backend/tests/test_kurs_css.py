"""Aufbaukurs CSS: Beispiele mit Markup, Lauf für die Bühne ohne Sandbox und Begriffe über tinycss2 und html.parser."""

import textwrap
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
from codeschmiede.kurs.begriffe import merkmale_css
from codeschmiede.kurs.einlesen import lade
from codeschmiede.state import AppState

from .conftest import schreibe_aufgabe

BEGRIFFE = """\
sprache: css
begriffe:
  - {id: regel, titel: Regel, erkennung: {knoten: [regel], elemente: [p, h1]}}
  - {id: color, titel: Schriftfarbe, erkennung: {eigenschaften: [color]}}
  - {id: klasse, titel: Klassen, erkennung: {attribute: [class], knoten: [klasse]}}
  - {id: flex, titel: Flexbox, erkennung: {werte: [display:flex]}}
"""

EINFUEHRUNG = '''\
---
id: css-farbe
sprache: css
titel: Die erste Regel
kurz: Farbe ins Spiel.
fuehrt_ein: [regel, color]
lernziele: [eine Regel schreiben]
karte: Ich färbe
---

## Farbe

Text.

```beispiel
id: orange
html: |
  <h1>Fischwagen</h1>
  <p>Hering</p>
code: |
  p {
    color: orange;
  }
vorhersage:
  art: auswahl
  optionen:
    - {text: Der Absatz wird orange, richtig: true, erklaerung: Genau.}
    - {text: Alles wird orange, erklaerung: Nur p.}
```
'''


def baue_css_kurs(kurs: Path, aufgaben: Path, einfuehrung: str = EINFUEHRUNG, ziel_css: str = "p { color: gold; }") -> None:
    (kurs / "begriffe").mkdir(parents=True)
    (kurs / "begriffe" / "css.yml").write_text(BEGRIFFE, encoding="utf-8")
    ordner = kurs / "einfuehrungen" / "css" / "farbe"
    ordner.mkdir(parents=True)
    (ordner / "einfuehrung.md").write_text(einfuehrung, encoding="utf-8")
    (kurs / "css.yml").write_text(textwrap.dedent("""\
        sprache: css
        titel: CSS
        bloecke:
          - titel: Erste Schritte
            kapitel:
              - {einfuehrung: css-farbe, uebungen: [w011-gold]}
        """), encoding="utf-8")
    ordner = schreibe_aufgabe(aufgaben, "css", "w011-gold", "css_klon", f"""\
        ziel_html: "<p class=\\"x\\">Hering</p>"
        ziel_css: "{ziel_css}"
        starter_code: "p {{ }}"
        """)
    (ordner / "solution_idiomatic.css").write_text(ziel_css + "\n")


@pytest.fixture
def css_settings(settings: Settings) -> Settings:
    baue_css_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    return settings


def test_merkmale_aus_css_und_markup():
    m = merkmale_css("/* k */\n.karte > h2, #x::before, ul li:first-child, * {\n  margin: calc(1px + 2em) 50%;\n"
                     "  --farbe: #fff;\n  color: rgb(0 0 0 / .5);\n  display: flex;\n}\n@media (min-width: 500px) { p { color: blue; } }")
    assert m is not None
    assert {"kommentar", "klasse", "kind", "typ", "id", "gruppe", "nachfahre", "pseudoklasse", ":first-child",
            "pseudoelement", "::before", "universal", "eigene_eigenschaft", "@media", "regel"} <= m.knoten
    assert {"calc", "rgb"} <= m.aufrufe and {"px", "em", "%", "hex", "zahl"} <= m.literale
    assert {"margin", "color", "display"} <= m.eigenschaften and {"display:flex", "*:flex", "color:blue"} <= m.werte
    assert {"h2", "ul", "li", "p"} <= m.elemente
    html = merkmale_css('<div class="a" id="b"><!-- x --><p>Hering</p></div>')
    assert html is not None and html.elemente == {"div", "p"} and html.attribute == {"class", "id"} and html.knoten == {"kommentar"}
    assert merkmale_css("p { color }") is None


def test_css_beispiel_braucht_html_und_auswahl(tmp_path):
    ohne_html = EINFUEHRUNG.replace("html: |\n  <h1>Fischwagen</h1>\n  <p>Hering</p>\n", "")
    baue_css_kurs(tmp_path / "kurs", tmp_path / "aufgaben", ohne_html)
    inhalt = lade(tmp_path / "kurs")
    assert "css-farbe" not in inhalt.einfuehrungen
    assert any("brauchen html" in f.meldung for f in inhalt.ladefehler)


def test_vorgriff_im_markup_und_im_ziel(settings: Settings):
    baue_css_kurs(settings.kurs_pfad, settings.aufgaben_pfad, ziel_css="p { display: flex; }")
    befunde = [b.meldung for b in AppState(settings).befunde]
    # ziel_html benutzt die Klasse, ziel_css und Musterlösung Flexbox: beides ist in Kapitel 1 noch nicht eingeführt
    assert any("klasse" in m for m in befunde), befunde
    assert any("flex" in m for m in befunde), befunde


def test_css_lauf_erst_nach_der_vorhersage(css_settings: Settings):
    client = TestClient(app_bauen(css_settings))
    e = client.get("/api/kurs/einfuehrung/css-farbe").json()
    beispiel = e["abschnitte"][0]["teile"][1]
    assert beispiel["html"].startswith("<h1>") and not beispiel["ablauf"]
    weg = "/api/kurs/einfuehrung/css-farbe/beispiel/orange/ausfuehren"
    assert client.post(weg, json={}).status_code == 409
    assert client.post("/api/kurs/einfuehrung/css-farbe/antwort", json={"element": "orange", "wahl": [0]}).json()["richtig"]
    lauf = client.post(weg, json={}).json()
    assert lauf == {"art": "css", "html": "<h1>Fischwagen</h1>\n<p>Hering</p>\n", "css": "p {\n  color: orange;\n}\n"}
    assert client.post(weg, json={"code": "p { color: red; }"}).json()["css"] == "p { color: red; }"
    merkblatt = client.get("/api/kurs/merkblatt/css-farbe").json()
    assert merkblatt["beispiele"][0]["html"].startswith("<h1>") and merkblatt["beispiele"][0]["ausgabe"] is None
