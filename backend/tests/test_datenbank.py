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
