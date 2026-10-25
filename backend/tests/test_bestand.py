"""Der echte Aufgabenbestand: lädt ohne Fehler, und jede Musterlösung
besteht ihre eigenen Tests, bei Spielen mit allen drei Sternen. Dauert einige Minuten, darum nur mit
CODESCHMIEDE_BESTAND=1 (vor jedem Ausrollen und nach Änderungen am Bestand).
Liest aufgaben/ nur; Datenbank im Temp-Ordner.
"""

import os
import threading
from concurrent.futures import ThreadPoolExecutor

import pytest

from codeschmiede.config import PROJEKT_WURZEL, Settings
from codeschmiede.models.progress import Progress
from codeschmiede.pruefung.orchestrator import pruefe, pruefer_fuer
from codeschmiede.spiel.dienst import mit_verlauf
from codeschmiede.state import AppState

from .conftest import braucht_sandbox

pytestmark = [
    braucht_sandbox,
    pytest.mark.skipif(os.environ.get("CODESCHMIEDE_BESTAND") != "1", reason="CODESCHMIEDE_BESTAND=1 setzen"),
]


@pytest.fixture(scope="module")
def state(tmp_path_factory, docker_runner):
    tmp = tmp_path_factory.mktemp("bestand")
    settings = Settings(
        aufgaben_pfad=PROJEKT_WURZEL / "aufgaben",
        daten_pfad=tmp,
        db_datei=tmp / "bestand.db",
        aufgaben_schreibbar=False,
        aufgaben_beobachten=False,
    )
    return AppState(settings, runner=docker_runner)


def test_keine_befunde(state):
    assert [f"{b.ort}: {b.meldung}" for b in state.befunde] == []


def test_musterloesungen_bestehen(state):
    auftraege = [
        (a, ml)
        for a in state.aufgaben.alle_aufgaben()
        if pruefer_fuer(a).abgabe == "server"
        for ml in state.loader.lade_musterloesungen(a.id)
    ]

    fertig = 0
    zaehler = threading.Lock()

    def lauf(auftrag):
        nonlocal fertig
        try:
            return pruefe_eine(auftrag)
        finally:
            with zaehler:
                fertig += 1
                # sichtbar mit pytest -s: Fortschritt für lange Läufe
                print(f"fortschritt {fertig}/{len(auftraege)}", flush=True)

    def pruefe_eine(auftrag):
        a, ml = auftrag
        erg = pruefe(a, ml["code"], state.runner)
        if not erg.bestanden and erg.timeout:
            # Zeitüberschreitung unter paralleler Last (langsamer Containerstart): einmal wiederholen
            erg = pruefe(a, ml["code"], state.runner)
        if erg.wertung:
            # Sterne aus dem Verlauf so, als gelänge die Musterlösung im ersten Versuch ohne Hinweis
            erg = erg.model_copy(update={"wertung": mit_verlauf(erg.wertung, Progress(aufgabe_id=a.id, status="neu"))})
        if erg.bestanden and (erg.wertung is None or erg.wertung.sterne == 3):
            return None
        if erg.bestanden:
            return f"{a.id}/{ml['variante']}: Musterlösung erreicht nur {erg.wertung.sterne} Sterne"
        sichtbar = [t for t in erg.sichtbar if not t.bestanden]
        detail = (sichtbar[0].fehler or f"ist {sichtbar[0].tatsaechlich!r}, soll {sichtbar[0].erwartet!r}") if sichtbar else ""
        return f"{a.id}/{ml['variante']}: versteckt {erg.versteckt_fail} falsch {detail} {erg.stderr[-200:]}".strip()

    with ThreadPoolExecutor(max_workers=4) as pool:
        fehler = [f for f in pool.map(lauf, auftraege) if f]
    assert fehler == [], f"{len(fehler)} von {len(auftraege)}:\n" + "\n".join(fehler)


def test_sprint_schnipsel_stimmen(state):
    """Jeder Schnipsel gibt in der Sandbox genau die richtige Option aus;
    "Fehler" heißt, der Code bricht ab."""
    from codeschmiede.pruefung.sprint_pruefer import FEHLER, level_von
    from codeschmiede.sandbox.result import RunLimits

    auftraege = [
        (a, i, s)
        for a in state.aufgaben.alle_aufgaben()
        if a.task_type == "ausgabe_sprint"
        for i, s in enumerate(level_von(a).schnipsel)
    ]

    def lauf(auftrag):
        a, i, s = auftrag
        for _ in range(2):
            erg = state.runner.run_code(s.code, a.sprache, RunLimits(timeout_sekunden=15))
            if not erg.timeout:
                break
        ist = FEHLER if erg.exit_code != 0 else erg.stdout.strip()
        soll = s.optionen[s.richtig]
        return None if ist == soll else f"{a.id} #{i}: soll {soll!r}, ist {ist!r}"

    with ThreadPoolExecutor(max_workers=4) as pool:
        fehler = [f for f in pool.map(lauf, auftraege) if f]
    assert auftraege and fehler == [], "\n".join(fehler)


def test_beispiele_laufen_und_vorhersagen_stimmen(state):
    """Jedes Beispiel der Einführungen (Python und SQL) läuft ohne Fehler; bei einer Vorhersage als Auswahl ist die
    richtige Option genau die Ausgabe des echten Laufs, oder bei `vergleich: zeilen` ihre Zeilenzahl."""
    import re

    from codeschmiede.kurs.dienst import MIT_ABLAUF, normalisiert, zeilenzahl
    from codeschmiede.kurs.modelle import Beispiel

    falsch = []
    for e in state.kurs.inhalt.einfuehrungen.values():
        if e.kopf.sprache not in MIT_ABLAUF:
            continue
        for a in e.abschnitte:
            for t in a.teile:
                if not isinstance(t, Beispiel):
                    continue
                lauf = state.kurs.lauf(e, t)
                if lauf.fehler:
                    falsch.append(f"{e.id}/{t.id}: {lauf.fehler}")
                    continue
                v = t.vorhersage
                if v is None or v.art != "auswahl":
                    continue
                richtig = next(o.text for o in v.optionen if o.richtig)
                if v.vergleich == "zeilen":
                    zahl = re.search(r"\d+", richtig)
                    if zahl is None or int(zahl.group()) != zeilenzahl(lauf.ausgabe):
                        falsch.append(f"{e.id}/{t.id}: richtige Option {richtig!r}, Lauf hat {zeilenzahl(lauf.ausgabe)} Zeilen")
                elif normalisiert(richtig) != normalisiert(lauf.ausgabe):
                    falsch.append(f"{e.id}/{t.id}: richtige Option {richtig!r}, Lauf gibt {lauf.ausgabe!r}")
    assert falsch == []
