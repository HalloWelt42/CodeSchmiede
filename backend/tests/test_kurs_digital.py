"""Aufbaukurs Digitaltechnik: der Teil `kv` (Würfel und KV-Raster in der Werkbank), Übungen aus der KV-Werkstatt unter
"maschine" und der echte Kurs."""

import textwrap
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from codeschmiede.api import app_bauen
from codeschmiede.config import PROJEKT_WURZEL, Settings
from codeschmiede.kurs.einlesen import lade
from codeschmiede.kurs.modelle import KvTeil
from codeschmiede.state import AppState

from .conftest import schreibe_aufgabe

EINFUEHRUNG = '''\
---
id: digital-probe
sprache: digital
titel: Vereinfachen
kurz: Kürzer schalten.
fuehrt_ein: [block]
lernziele: [Blöcke einkreisen]
karte: Ich kreise ein
---

## Würfel

Text.

```kv
id: wuerfel
eingaenge: [A, B, C]
werte: "01010111"
start: wuerfel
regler: true
formeln:
  - titel: Große Blöcke
    formel: "C + A B"
```
'''


def baue_digital_kurs(kurs: Path, aufgaben: Path) -> None:
    (kurs / "begriffe").mkdir(parents=True)
    (kurs / "begriffe" / "digital.yml").write_text("sprache: digital\nbegriffe:\n  - {id: block, titel: Blöcke}\n", encoding="utf-8")
    ordner = kurs / "einfuehrungen" / "digital" / "probe"
    ordner.mkdir(parents=True)
    (ordner / "einfuehrung.md").write_text(EINFUEHRUNG, encoding="utf-8")
    (kurs / "digital.yml").write_text(textwrap.dedent("""\
        sprache: digital
        titel: Digitaltechnik
        bloecke:
          - titel: Schaltungen
            kapitel:
              - {einfuehrung: digital-probe, uebungen: [b901-oder]}
        """), encoding="utf-8")
    ordner = schreibe_aufgabe(aufgaben, "maschine", "b901-oder", "kv", """\
        kv:
          eingaenge: [A, B]
          ausgaenge: [L]
          werte: {L: "0111"}
        starter_code: "L = "
        """)
    (ordner / "solution_idiomatic.txt").write_text("L = A + B\n")


@pytest.mark.parametrize(("aenderung", "erwartet"), [
    ({"formeln": [{"titel": "falsch", "formel": "C"}]}, "stimmt nicht bei Belegung 6"),
    ({"formeln": [{"titel": "kaputt", "formel": "C + Q"}]}, "Q ist kein Eingang"),
    ({"werte": "0101"}, "8 Zeichen"),
    ({"eingaenge": ["A", "B"], "werte": "0111", "formeln": [{"titel": "f", "formel": "A + B"}]}, "nur bei drei Eingängen"),
])
def test_kv_teil_prueft_seine_formeln(aenderung, erwartet):
    daten = {"id": "w", "eingaenge": ["A", "B", "C"], "werte": "01010111", "start": "wuerfel",
             "formeln": [{"titel": "gut", "formel": "C + A B"}], **aenderung}
    with pytest.raises(ValidationError, match=erwartet):
        KvTeil.model_validate(daten)


def test_egal_felder_duerfen_beliebig_sein():
    KvTeil.model_validate({"id": "e", "eingaenge": list("ABCD"), "werte": "1010001010xxxxxx",
                           "formeln": [{"titel": "mit Joker", "formel": "!B !D + C !D"}]})


def test_kurs_mit_uebungen_unter_maschine(settings: Settings):
    baue_digital_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    # die Konfiguration der Probe kennt "maschine" nicht; hier zählt nur, was die Kursprüfung meldet
    kurs = [b for b in AppState(settings).befunde if b.ort.startswith("kurs/")]
    assert kurs == []


def test_einfuehrung_liefert_kv_mit_bausteinen(settings: Settings):
    baue_digital_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    client = TestClient(app_bauen(settings))
    teil = client.get("/api/kurs/einfuehrung/digital-probe").json()["abschnitte"][0]["teile"][1]
    assert teil["art"] == "kv" and teil["start"] == "wuerfel" and teil["regler"] is True
    assert teil["formeln"] == [{"titel": "Große Blöcke", "formel": "C + A B", "bausteine": 2,
                                "plan": "und1 = UND(A, B)\noder1 = ODER(C, und1)\nf = oder1\n"}]


def test_echter_kurs_liest_sich():
    inhalt = lade(PROJEKT_WURZEL / "kurs")
    e = inhalt.einfuehrungen["digital-vereinfachen"]
    assert len(e.abschnitte) == 7 and "digital" in inhalt.kurse
    kv = [t for a in e.abschnitte for t in a.teile if isinstance(t, KvTeil)]
    assert {t.id for t in kv} >= {"minterme", "aufklappen", "segment-e", "zum-plan"}
