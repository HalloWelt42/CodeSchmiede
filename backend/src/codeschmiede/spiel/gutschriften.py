"""GutschriftRepository -- einziger Ort, der die Tabelle `tagesauftraege`
liest und schreibt."""

from datetime import date

from ..db.connection import Datenbank


class GutschriftRepository:
    def __init__(self, db: Datenbank):
        self.db = db

    def alle(self) -> dict[date, int]:
        with self.db.connect() as conn:
            rows = conn.execute("SELECT datum, punkte FROM tagesauftraege").fetchall()
        return {date.fromisoformat(r["datum"]): r["punkte"] for r in rows}

    def schreibe(self, datum: date, punkte: int) -> bool:
        """Schreibt die Gutschrift eines Tages einmal; False, wenn es sie
        schon gab (zwei gleichzeitige Abgaben schreiben nicht doppelt)."""
        with self.db.connect() as conn:
            cursor = conn.execute(
                "INSERT OR IGNORE INTO tagesauftraege (datum, punkte) VALUES (?, ?)",
                (datum.isoformat(), punkte),
            )
            return cursor.rowcount == 1

    def fuer_export(self) -> list[dict]:
        with self.db.connect() as conn:
            return [
                dict(r)
                for r in conn.execute(
                    "SELECT datum, punkte, datetime(erledigt_am) AS erledigt_am FROM tagesauftraege ORDER BY datum"
                ).fetchall()
            ]
