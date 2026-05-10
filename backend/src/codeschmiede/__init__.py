"""Codeschmiede -- Backend-Paket.

Version wird aus der `VERSION`-Datei gelesen. Kandidaten in Reihenfolge:
1. relativ zum Modul (Dev-Modus, `pip install -e .`)
2. Container-typische Pfade (Docker)
3. Fallback "0.0.0", wenn nichts gefunden wurde.
"""

from pathlib import Path


def _finde_version() -> str:
    kandidaten = [
        Path(__file__).resolve().parents[3] / "VERSION",
        Path("/app/VERSION"),
        Path("/VERSION"),
    ]
    for k in kandidaten:
        if k.exists():
            return k.read_text(encoding="utf-8").strip()
    return "0.0.0"


__version__ = _finde_version()
