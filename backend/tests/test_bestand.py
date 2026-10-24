"""Der echte Aufgabenbestand: lädt ohne Fehler, und jede Musterlösung
besteht ihre eigenen Tests. Dauert einige Minuten, darum nur mit
CODESCHMIEDE_BESTAND=1 (vor jedem Ausrollen und nach Änderungen am Bestand).
Liest aufgaben/ nur; Datenbank im Temp-Ordner.
"""

import os
from concurrent.futures import ThreadPoolExecutor

import pytest

from codeschmiede.config import PROJEKT_WURZEL, Settings
from codeschmiede.pruefung.orchestrator import pruefe, pruefer_fuer
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
    )
    return AppState(settings, runner=docker_runner)


def test_keine_befunde(state):
    assert [f"{b.ort}: {b.meldung}" for b in state.befunde] == []


def test_musterloesungen_bestehen(state):
    auftraege = [
        (a, ml)
        for a in state.aufgaben.alle_aufgaben()
        if not pruefer_fuer(a).im_browser
        for ml in state.loader.lade_musterloesungen(a.id)
    ]

    def lauf(auftrag):
        a, ml = auftrag
        erg = pruefe(a, ml["code"], state.runner)
        if erg.bestanden:
            return None
        sichtbar = [t for t in erg.sichtbar if not t.bestanden]
        detail = (sichtbar[0].fehler or f"ist {sichtbar[0].tatsaechlich!r}, soll {sichtbar[0].erwartet!r}") if sichtbar else ""
        return f"{a.id}/{ml['variante']}: versteckt {erg.versteckt_fail} falsch {detail} {erg.stderr[-200:]}".strip()

    with ThreadPoolExecutor(max_workers=6) as pool:
        fehler = [f for f in pool.map(lauf, auftraege) if f]
    assert fehler == [], f"{len(fehler)} von {len(auftraege)}:\n" + "\n".join(fehler)
