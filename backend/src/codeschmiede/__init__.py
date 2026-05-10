"""Codeschmiede -- Backend-Paket.

Version wird aus der `VERSION`-Datei im Repo-Wurzel gelesen, damit
Backend, Frontend und CLI immer den gleichen Stand zeigen.
"""

from pathlib import Path


_VERSION_DATEI = Path(__file__).resolve().parents[3] / "VERSION"
__version__ = (
    _VERSION_DATEI.read_text(encoding="utf-8").strip()
    if _VERSION_DATEI.exists()
    else "0.0.0"
)
