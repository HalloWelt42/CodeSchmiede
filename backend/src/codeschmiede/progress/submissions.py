"""SubmissionRepository -- einziger Ort, der die Tabelle `submissions` liest
und schreibt (Speichern, Verlauf, Statistik, Export)."""

from datetime import date

from pydantic import BaseModel

from ..db.connection import Datenbank
from ..models.aufgabe import Aufgabe
from ..pruefung.ergebnis import Kennwerte

# Kalendertag einer Abgabe in der Ortszeit des Servers; date.today() rechnet
# in derselben Zeitzone, so passen Serie, Tagesauftrag und Aktivität zusammen.
TAG = "date(zeitstempel, 'localtime')"


class SubmissionEintrag(BaseModel):
    id: int
    zeitstempel: str
    bestanden: bool
    laufzeit_ms: float | None
    codelaenge_zeichen: int | None
    code: str


class BestandeneAbgabe(BaseModel):
    """Eine bestandene Abgabe, wie die Spielmechanik sie braucht."""

    id: int
    aufgabe_id: str
    tag: date
    # None bei Abgaben von vor der Spielmechanik
    ohne_hilfe: bool | None = None
    sterne: int | None = None
    kennwerte: Kennwerte


class Bestwerte(BaseModel):
    """Bisher beste bestandene Abgabe einer Aufgabe je Maß."""

    zeichen: int | None = None
    laufzeit_ms: float | None = None
    sterne: int | None = None


class SubmissionStatistik(BaseModel):
    gesamt: int = 0
    bestanden: int = 0


class TagesAktivitaet(BaseModel):
    datum: str
    submissions: int
    bestanden: int


def codelaenge(code: str) -> int:
    """Zeichen ohne Leerraum -- Maß für den Vergleich mit Musterlösungen."""
    return sum(1 for c in code if not c.isspace())


class SubmissionRepository:
    def __init__(self, db: Datenbank):
        self.db = db

    def speichere(
        self,
        aufgabe: Aufgabe,
        code: str,
        bestanden: bool,
        laufzeit_ms: float,
        ohne_hilfe: bool,
        sterne: int | None = None,
        kennwerte: Kennwerte | None = None,
    ) -> int:
        with self.db.connect() as conn:
            cursor = conn.execute(
                """
                INSERT INTO submissions (
                    aufgabe_id, aufgabe_revision, code, bestanden,
                    laufzeit_ms, codelaenge_zeichen, ohne_hilfe, sterne, kennwerte
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (aufgabe.id, aufgabe.revision, code, 1 if bestanden else 0,
                 laufzeit_ms, codelaenge(code), 1 if ohne_hilfe else 0, sterne,
                 (kennwerte or Kennwerte()).model_dump_json(exclude_none=True)),
            )
            return cursor.lastrowid or 0

    def bestandene_abgaben(self) -> list[BestandeneAbgabe]:
        with self.db.connect() as conn:
            rows = conn.execute(
                f"""
                SELECT id, aufgabe_id, {TAG} AS tag, ohne_hilfe, sterne, kennwerte
                FROM submissions WHERE bestanden = 1 ORDER BY id
                """
            ).fetchall()
        return [
            BestandeneAbgabe(
                id=r["id"],
                aufgabe_id=r["aufgabe_id"],
                tag=date.fromisoformat(r["tag"]),
                ohne_hilfe=None if r["ohne_hilfe"] is None else bool(r["ohne_hilfe"]),
                sterne=r["sterne"],
                kennwerte=Kennwerte.model_validate_json(r["kennwerte"]) if r["kennwerte"] else Kennwerte(),
            )
            for r in rows
        ]

    def erste_versuche_bestanden(self) -> int:
        """Aufgaben, deren erste Abgabe bestanden hat."""
        with self.db.connect() as conn:
            return conn.execute(
                """
                SELECT COUNT(*) FROM submissions
                WHERE bestanden = 1
                  AND id IN (SELECT MIN(id) FROM submissions GROUP BY aufgabe_id)
                """
            ).fetchone()[0]

    def bestwerte(self, aufgabe_id: str) -> Bestwerte:
        with self.db.connect() as conn:
            r = conn.execute(
                """
                SELECT MIN(codelaenge_zeichen) AS zeichen,
                       MIN(CASE WHEN laufzeit_ms > 0 THEN laufzeit_ms END) AS laufzeit_ms,
                       MAX(sterne) AS sterne
                FROM submissions WHERE aufgabe_id = ? AND bestanden = 1
                """,
                (aufgabe_id,),
            ).fetchone()
        return Bestwerte(zeichen=r["zeichen"], laufzeit_ms=r["laufzeit_ms"], sterne=r["sterne"])

    def verlauf(self, aufgabe_id: str, limit: int = 20) -> list[SubmissionEintrag]:
        with self.db.connect() as conn:
            rows = conn.execute(
                """
                SELECT id, datetime(zeitstempel) AS zeitstempel, bestanden,
                       laufzeit_ms, codelaenge_zeichen, code
                FROM submissions
                WHERE aufgabe_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (aufgabe_id, max(1, min(100, limit))),
            ).fetchall()
        return [
            SubmissionEintrag(
                id=r["id"],
                zeitstempel=r["zeitstempel"],
                bestanden=bool(r["bestanden"]),
                laufzeit_ms=r["laufzeit_ms"],
                codelaenge_zeichen=r["codelaenge_zeichen"],
                code=r["code"],
            )
            for r in rows
        ]

    def letzte(self, aufgabe_id: str) -> SubmissionEintrag | None:
        eintraege = self.verlauf(aufgabe_id, limit=1)
        return eintraege[0] if eintraege else None

    def statistik_je_aufgabe(self) -> dict[str, SubmissionStatistik]:
        with self.db.connect() as conn:
            rows = conn.execute(
                """
                SELECT aufgabe_id, COUNT(*) AS gesamt,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions
                GROUP BY aufgabe_id
                """
            ).fetchall()
        return {
            r["aufgabe_id"]: SubmissionStatistik(gesamt=r["gesamt"], bestanden=r["bestanden"] or 0)
            for r in rows
        }

    def je_tag_im_jahr(self, jahr: int) -> list[TagesAktivitaet]:
        return self._je_tag(f"strftime('%Y', {TAG}) = ?", str(jahr))

    def je_tag_seit(self, tage: int) -> list[TagesAktivitaet]:
        return self._je_tag(f"{TAG} >= date('now', 'localtime', ?)", f"-{tage - 1} days")

    def _je_tag(self, bedingung: str, wert: str) -> list[TagesAktivitaet]:
        with self.db.connect() as conn:
            rows = conn.execute(
                f"""
                SELECT {TAG} AS datum,
                       COUNT(*) AS submissions,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions
                WHERE {bedingung}
                GROUP BY {TAG}
                ORDER BY datum
                """,
                (wert,),
            ).fetchall()
        return [
            TagesAktivitaet(datum=r["datum"], submissions=r["submissions"], bestanden=r["bestanden"] or 0)
            for r in rows
        ]

    def alle_fuer_export(self) -> list[dict]:
        with self.db.connect() as conn:
            return [
                dict(row)
                for row in conn.execute(
                    """
                    SELECT id, aufgabe_id, aufgabe_revision,
                           datetime(zeitstempel) AS zeitstempel,
                           code, bestanden, laufzeit_ms, codelaenge_zeichen,
                           ohne_hilfe, sterne, kennwerte
                    FROM submissions ORDER BY id
                    """
                ).fetchall()
            ]
