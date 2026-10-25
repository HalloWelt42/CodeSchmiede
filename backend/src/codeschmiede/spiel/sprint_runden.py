"""SprintRundenRepository - einziger Ort, der die Tabelle `sprint_runden`
liest und schreibt."""

import json
from datetime import datetime, timedelta

from ..db.connection import Datenbank
from ..models.sprint import GespeicherteRunde, GestellteFrage

AUFBEWAHREN = timedelta(days=1)


class SprintRundenRepository:
    def __init__(self, db: Datenbank):
        self.db = db

    def anlegen(self, runde: GespeicherteRunde) -> None:
        with self.db.connect() as conn:
            conn.execute(
                "DELETE FROM sprint_runden WHERE gestartet < ?",
                ((runde.gestartet - AUFBEWAHREN).isoformat(),),
            )
            conn.execute(
                """
                INSERT INTO sprint_runden
                  (id, aufgabe_id, aufgabe_revision, fragen, antworten, gestartet, frist, abgeschlossen)
                VALUES (?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    runde.id,
                    runde.aufgabe_id,
                    runde.aufgabe_revision,
                    json.dumps([f.model_dump() for f in runde.fragen]),
                    json.dumps(runde.antworten),
                    runde.gestartet.isoformat(),
                    runde.frist.isoformat(),
                ),
            )

    def hole(self, runde_id: str) -> GespeicherteRunde | None:
        with self.db.connect() as conn:
            r = conn.execute("SELECT * FROM sprint_runden WHERE id = ?", (runde_id,)).fetchone()
        if r is None:
            return None
        return GespeicherteRunde(
            id=r["id"],
            aufgabe_id=r["aufgabe_id"],
            aufgabe_revision=r["aufgabe_revision"],
            fragen=[GestellteFrage(**f) for f in json.loads(r["fragen"])],
            antworten=json.loads(r["antworten"]),
            gestartet=datetime.fromisoformat(r["gestartet"]),
            frist=datetime.fromisoformat(r["frist"]),
            abgeschlossen=bool(r["abgeschlossen"]),
        )

    def antworte(self, runde_id: str, frage: int, wahl: int) -> bool:
        """Trägt die Wahl ein, wenn die Frage noch offen ist; False sonst.
        Die Bedingung steht im UPDATE, damit zwei gleichzeitige Antworten
        nicht beide zählen."""
        with self.db.connect() as conn:
            cursor = conn.execute(
                """
                UPDATE sprint_runden
                SET antworten = json_set(antworten, ?, ?)
                WHERE id = ? AND abgeschlossen = 0
                  AND json_extract(antworten, ?) IS NULL
                """,
                (f"$[{frage}]", wahl, runde_id, f"$[{frage}]"),
            )
            return cursor.rowcount == 1

    def abschliessen(self, runde_id: str) -> bool:
        with self.db.connect() as conn:
            cursor = conn.execute(
                "UPDATE sprint_runden SET abgeschlossen = 1 WHERE id = ? AND abgeschlossen = 0",
                (runde_id,),
            )
            return cursor.rowcount == 1
