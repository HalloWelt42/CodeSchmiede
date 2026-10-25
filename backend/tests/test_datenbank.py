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


def test_naechtliche_sicherung_behaelt_die_neuesten(tmp_path):
    import sqlite3
    from datetime import datetime

    from codeschmiede.sicherung import bis_zur_stunde, sichern

    db = tmp_path / "quelle.sqlite"
    with sqlite3.connect(db) as conn:
        conn.execute("CREATE TABLE t (x)")
        conn.execute("INSERT INTO t VALUES (42)")
    ordner = tmp_path / "sicherungen"
    (ordner).mkdir()
    (ordner / "codeschmiede-20260101-000000.sqlite").write_text("vom Ausrollen")
    for tag in range(1, 6):
        sichern(db, ordner, behalten=3, jetzt=datetime(2026, 10, tag, 3))
    namen = sorted(p.name for p in ordner.iterdir())
    assert namen == ["codeschmiede-20260101-000000.sqlite", "nachts-20261003.sqlite",
                     "nachts-20261004.sqlite", "nachts-20261005.sqlite"]
    with sqlite3.connect(ordner / "nachts-20261005.sqlite") as conn:
        assert conn.execute("SELECT x FROM t").fetchone()[0] == 42
    assert bis_zur_stunde(3, datetime(2026, 10, 25, 2, 0)) == 3600
    assert bis_zur_stunde(3, datetime(2026, 10, 25, 3, 0)) == 24 * 3600
