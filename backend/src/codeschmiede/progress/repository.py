"""ProgressRepository -- liest und schreibt Progress, Streak und
Aggregate aus der SQLite-DB.
"""

import sqlite3
from datetime import date, datetime, timedelta

from ..db.connection import Datenbank
from ..models.aufgabe import Aufgabe
from ..models.progress import GesamtFortschritt, Progress, Streak
from .sm2 import berechne_naechsten_schritt
from .streak import aktualisiere_streak


KV_AKTUELL = "streak.aktuell"
KV_LAENGSTER = "streak.laengster"
KV_LETZTER_TAG = "streak.letzter_tag"


class ProgressRepository:
    def __init__(self, db: Datenbank):
        self.db = db

    # --- Progress lesen ---------------------------------------------------

    def hole_progress(self, aufgabe_id: str) -> Progress | None:
        with self.db.connect() as conn:
            row = conn.execute(
                "SELECT * FROM progress WHERE aufgabe_id = ?", (aufgabe_id,)
            ).fetchone()
        return self._row_zu_progress(row) if row else None

    def hole_alle_progress(self) -> list[Progress]:
        with self.db.connect() as conn:
            rows = conn.execute("SELECT * FROM progress").fetchall()
        return [self._row_zu_progress(r) for r in rows]

    def faellige_aufgaben(self, am: date | None = None) -> list[str]:
        am = am or date.today()
        with self.db.connect() as conn:
            rows = conn.execute(
                """
                SELECT aufgabe_id FROM progress
                WHERE faellig_am IS NOT NULL
                  AND faellig_am <= ?
                  AND status = 'geloest'
                ORDER BY faellig_am ASC
                """,
                (am.isoformat(),),
            ).fetchall()
        return [r["aufgabe_id"] for r in rows]

    def letzte_aktive_aufgabe(self) -> str | None:
        with self.db.connect() as conn:
            row = conn.execute(
                """
                SELECT aufgabe_id FROM progress
                WHERE status = 'in_arbeit'
                ORDER BY letzte_wiederholung DESC NULLS LAST
                LIMIT 1
                """
            ).fetchone()
            if row:
                return row["aufgabe_id"]
            row = conn.execute(
                """
                SELECT aufgabe_id FROM progress
                WHERE status = 'geloest'
                ORDER BY letzte_wiederholung DESC NULLS LAST
                LIMIT 1
                """
            ).fetchone()
        return row["aufgabe_id"] if row else None

    def gesamt_fortschritt(self, aufgaben: list[Aufgabe]) -> GesamtFortschritt:
        with self.db.connect() as conn:
            rows = conn.execute(
                "SELECT status, COUNT(*) AS n FROM progress GROUP BY status"
            ).fetchall()
            sub_total = conn.execute("SELECT COUNT(*) FROM submissions").fetchone()[0]
            sub_bestanden = conn.execute(
                "SELECT COUNT(*) FROM submissions WHERE bestanden = 1"
            ).fetchone()[0]
            punkte_row = conn.execute(
                "SELECT COALESCE(SUM(punkte_erreicht), 0) FROM progress"
            ).fetchone()

        counts = {r["status"]: r["n"] for r in rows}
        geloest = counts.get("geloest", 0)
        in_arbeit = counts.get("in_arbeit", 0)
        return GesamtFortschritt(
            aufgaben_gesamt=len(aufgaben),
            aufgaben_geloest=geloest,
            aufgaben_in_arbeit=in_arbeit,
            aufgaben_neu=max(0, len(aufgaben) - geloest - in_arbeit),
            submissions_gesamt=sub_total,
            bestandene_submissions=sub_bestanden,
            punkte_gesamt=int(punkte_row[0] or 0),
            punkte_maximal=sum(a.schwierigkeit_score for a in aufgaben),
        )

    # --- Update bei Submission --------------------------------------------

    def aktualisiere_nach_submission(
        self, aufgabe: Aufgabe, bestanden: bool, heute: date | None = None
    ) -> Progress:
        heute = heute or date.today()
        jetzt = datetime.now()

        bisher = self.hole_progress(aufgabe.id) or Progress(
            aufgabe_id=aufgabe.id, status="neu"
        )
        neue_versuche = bisher.versuche + 1

        if not bestanden:
            # "geloest" bleibt "geloest" -- ein Re-Versuch nach Erfolg
            # darf den Status nicht zurueckwerfen. Punkte und SM-2-Werte
            # bleiben ohnehin unangetastet (best-of im else-Zweig).
            neuer_status = bisher.status if bisher.status == "geloest" else "in_arbeit"
            neu = bisher.model_copy(
                update={
                    "status": neuer_status,
                    "versuche": neue_versuche,
                    "letzte_wiederholung": jetzt,
                }
            )
        else:
            qualitaet = 4 if bisher.versuche == 0 else 3
            sm2 = berechne_naechsten_schritt(
                bisher.ease, bisher.intervall_tage, qualitaet
            )
            faellig = heute + timedelta(days=sm2.intervall_tage)
            erreichte_punkte = self._berechne_punkte(aufgabe, bisher.hints_genutzt)
            best_of = max(bisher.punkte_erreicht, erreichte_punkte)
            neu = bisher.model_copy(
                update={
                    "status": "geloest",
                    "versuche": neue_versuche,
                    "punkte_erreicht": best_of,
                    "geloest_am": bisher.geloest_am or jetzt,
                    "ease": sm2.ease,
                    "intervall_tage": sm2.intervall_tage,
                    "faellig_am": faellig,
                    "letzte_wiederholung": jetzt,
                }
            )
            self._aktualisiere_streak(heute)

        self._schreibe(neu)
        return neu

    # --- Hint-Tracking ----------------------------------------------------

    def markiere_hint_gesehen(self, aufgabe_id: str, hint_index: int) -> Progress:
        """Erhoeht hints_genutzt mindestens auf hint_index+1 (idempotent
        bei mehrfachem Klick auf den gleichen Hint).
        """
        bisher = self.hole_progress(aufgabe_id) or Progress(
            aufgabe_id=aufgabe_id, status="neu"
        )
        neuer_status = bisher.status if bisher.status != "neu" else "in_arbeit"
        neu = bisher.model_copy(
            update={
                "hints_genutzt": max(bisher.hints_genutzt, hint_index + 1),
                "status": neuer_status,
                "letzte_wiederholung": datetime.now(),
            }
        )
        self._schreibe(neu)
        return neu

    # --- Reset ------------------------------------------------------------

    def reset_aufgabe(self, aufgabe_id: str) -> None:
        """Setzt Progress für eine Aufgabe zurück. Submissions bleiben
        als Historie erhalten. Streak bleibt unangetastet.
        """
        with self.db.connect() as conn:
            conn.execute("DELETE FROM progress WHERE aufgabe_id = ?", (aufgabe_id,))

    def reset_alles(self) -> None:
        """Globaler Reset: Submissions + Progress + Streak komplett weg.
        Aufgaben-Dateien bleiben unangetastet.
        """
        with self.db.connect() as conn:
            conn.execute("DELETE FROM submissions")
            conn.execute("DELETE FROM progress")
            conn.execute("DELETE FROM kv_state WHERE key LIKE 'streak.%'")

    # --- Streak -----------------------------------------------------------

    def hole_streak(self) -> Streak:
        with self.db.connect() as conn:
            rows = conn.execute(
                "SELECT key, value FROM kv_state WHERE key LIKE 'streak.%'"
            ).fetchall()
        kv = {r["key"]: r["value"] for r in rows}
        letzter_tag_str = kv.get(KV_LETZTER_TAG)
        return Streak(
            aktuell=int(kv.get(KV_AKTUELL, "0")),
            laengster=int(kv.get(KV_LAENGSTER, "0")),
            letzter_tag=date.fromisoformat(letzter_tag_str) if letzter_tag_str else None,
        )

    def _aktualisiere_streak(self, heute: date) -> None:
        bisher = self.hole_streak()
        neuer = aktualisiere_streak(bisher, heute)
        with self.db.connect() as conn:
            for k, v in [
                (KV_AKTUELL, str(neuer.aktuell)),
                (KV_LAENGSTER, str(neuer.laengster)),
                (KV_LETZTER_TAG, neuer.letzter_tag.isoformat() if neuer.letzter_tag else ""),
            ]:
                conn.execute(
                    """
                    INSERT INTO kv_state (key, value) VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value = excluded.value
                    """,
                    (k, v),
                )

    # --- Schreib-Helfer ---------------------------------------------------

    def _schreibe(self, p: Progress) -> None:
        with self.db.connect() as conn:
            conn.execute(
                """
                INSERT INTO progress (
                    aufgabe_id, status, versuche, hints_genutzt, punkte_erreicht,
                    geloest_am, ease, intervall_tage, faellig_am, letzte_wiederholung
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(aufgabe_id) DO UPDATE SET
                    status=excluded.status,
                    versuche=excluded.versuche,
                    hints_genutzt=excluded.hints_genutzt,
                    punkte_erreicht=excluded.punkte_erreicht,
                    geloest_am=excluded.geloest_am,
                    ease=excluded.ease,
                    intervall_tage=excluded.intervall_tage,
                    faellig_am=excluded.faellig_am,
                    letzte_wiederholung=excluded.letzte_wiederholung
                """,
                (
                    p.aufgabe_id,
                    p.status,
                    p.versuche,
                    p.hints_genutzt,
                    p.punkte_erreicht,
                    p.geloest_am.isoformat() if p.geloest_am else None,
                    p.ease,
                    p.intervall_tage,
                    p.faellig_am.isoformat() if p.faellig_am else None,
                    p.letzte_wiederholung.isoformat() if p.letzte_wiederholung else None,
                ),
            )

    @staticmethod
    def _berechne_punkte(aufgabe: Aufgabe, hints_genutzt: int) -> int:
        """Erreichte Punkte = Score - Summe Hint-Kosten der bereits
        geoeffneten Hints."""
        kosten = sum(h.kosten for h in aufgabe.hints[:hints_genutzt])
        return max(0, aufgabe.schwierigkeit_score - kosten)

    @staticmethod
    def _row_zu_progress(row: sqlite3.Row) -> Progress:
        # `punkte_erreicht` kann fehlen, wenn die DB noch nicht migriert
        # ist (Test-Setup). Sicher abfragen.
        try:
            punkte = row["punkte_erreicht"] or 0
        except (KeyError, IndexError):
            punkte = 0
        return Progress(
            aufgabe_id=row["aufgabe_id"],
            status=row["status"],
            versuche=row["versuche"],
            hints_genutzt=row["hints_genutzt"],
            punkte_erreicht=punkte,
            geloest_am=datetime.fromisoformat(row["geloest_am"]) if row["geloest_am"] else None,
            ease=row["ease"],
            intervall_tage=row["intervall_tage"],
            faellig_am=date.fromisoformat(row["faellig_am"]) if row["faellig_am"] else None,
            letzte_wiederholung=datetime.fromisoformat(row["letzte_wiederholung"])
            if row["letzte_wiederholung"]
            else None,
        )
