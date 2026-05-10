"""Datenbank-Verbindung fuer SQLite und nummerierte Migrations-Loader.

Migrations liegen als `001_*.sql`, `002_*.sql` etc. neben dieser Datei.
Beim ersten Aufruf von `migriere()` wird eine `schema_version`-Tabelle
angelegt, die die hoechste angewandte Migrationsnummer trackt. Spaetere
Aufrufe wenden nur die fehlenden Migrationen an.
"""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class Datenbank:
    """Schmaler Wrapper um sqlite3.connect mit Foreign-Keys + Row-Factory."""

    def __init__(self, datei: Path):
        self.datei = datei
        self.datei.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.datei)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def migriere(self) -> None:
        """Wendet alle neuen Migrationen in `migrations/*.sql` in Reihenfolge an."""
        migrationen = sorted(MIGRATIONS_DIR.glob("*.sql"))

        with self.connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS schema_version (version INTEGER NOT NULL)"
            )
            row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
            aktuell = (row[0] if row else None) or 0

            for migration in migrationen:
                nummer = int(migration.name.split("_", 1)[0])
                if nummer <= aktuell:
                    continue
                sql = migration.read_text(encoding="utf-8")
                conn.executescript(sql)
                conn.execute(
                    "INSERT INTO schema_version (version) VALUES (?)", (nummer,)
                )
