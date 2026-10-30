"""Migrationen laufen atomar."""

import sqlite3

import pytest

from codeschmiede.db import connection
from codeschmiede.db.connection import Datenbank


def test_fehlgeschlagene_migration_bleibt_folgenlos(tmp_path, monkeypatch):
    ordner = tmp_path / "migrationen"
    ordner.mkdir()
    (ordner / "001_a.sql").write_text("CREATE TABLE a (x INTEGER);")
    (ordner / "002_b.sql").write_text("CREATE TABLE b (x INTEGER);\nTHIS IS NOT SQL;")
    monkeypatch.setattr(connection, "MIGRATIONS_DIR", ordner)
    db = Datenbank(tmp_path / "t.db")
    with pytest.raises(sqlite3.Error):
        db.migriere()
    with db.connect() as conn:
        tabellen = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        version = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()[0]
    assert "a" in tabellen and "b" not in tabellen and version == 1


def test_sicherung_nach_der_regel_des_appkern(tmp_path, monkeypatch):
    """Die Regel des Appkern mit den Werten der Settings (auch aus CODESCHMIEDE_SICHERUNG_*): neu nur ohne jüngere
    Sicherung, höchstens `sicherung_behalten` Stände codeschmiede-*.sqlite, alte nachts-*.sqlite bleiben liegen."""
    import asyncio
    import os
    import time

    from codeschmiede.api import sicherung_bauen
    from codeschmiede.config import Settings

    db = tmp_path / "daten" / "codeschmiede.sqlite"
    db.parent.mkdir()
    with sqlite3.connect(db) as conn:
        conn.execute("CREATE TABLE t (x)")
        conn.execute("INSERT INTO t VALUES (42)")
    ordner = tmp_path / "sicherungen"
    ordner.mkdir()
    vor_tagen = time.time() - 30 * 24 * 3600
    for nr, name in enumerate(["codeschmiede-20261001-000000.sqlite", "codeschmiede-20261002-000000.sqlite",
                               "nachts-20261003.sqlite"]):
        (ordner / name).write_text("alt")
        os.utime(ordner / name, (vor_tagen + nr, vor_tagen + nr))
    monkeypatch.setenv("CODESCHMIEDE_SICHERUNG_BEHALTEN", "2")
    settings = Settings(db_datei=db, daten_pfad=db.parent, sicherungen_pfad=ordner)
    assert (settings.sicherung_abstand_tage, settings.sicherung_vor_ausrollen_ab_stunden) == (7, 24)
    assert sicherung_bauen(Settings(db_datei=db, daten_pfad=db.parent)) is None

    sicherung = sicherung_bauen(settings)
    ergebnis = asyncio.run(sicherung.pruefen())
    assert ergebnis.angelegt and ergebnis.entfernt == ["codeschmiede-20261001-000000.sqlite"]
    namen = sorted(p.name for p in ordner.iterdir())
    assert namen == sorted([ergebnis.angelegt, "codeschmiede-20261002-000000.sqlite", "nachts-20261003.sqlite"])
    with sqlite3.connect(ordner / ergebnis.angelegt) as conn:
        assert conn.execute("SELECT x FROM t").fetchone()[0] == 42
    # gleich danach ist keine fällig
    assert asyncio.run(sicherung.pruefen()).angelegt is None
