"""AufgabenRepository -- haelt Aufgaben + Pfade in-memory und in SQLite-Index.

Beim Start (oder Hot-Reload) wird `neu_aufbauen()` aufgerufen: lese alle
Aufgaben + Pfade von der Platte, leere die Index-Tabellen, schreibe neu.
Submissions referenzieren `aufgaben_versionen(aufgabe_id, revision)`,
sodass alte Submissions auch nach Aufgaben-Aenderungen reproduzierbar
bleiben.
"""

import json

from ..db.connection import Datenbank
from ..models.aufgabe import Aufgabe
from ..models.pfad import Pfad
from .loader import AufgabenLoader


class AufgabenRepository:
    def __init__(self, db: Datenbank, loader: AufgabenLoader):
        self.db = db
        self.loader = loader
        self._aufgaben: dict[str, Aufgabe] = {}
        self._pfade: dict[str, Pfad] = {}

    def neu_aufbauen(self) -> None:
        aufgaben = self.loader.lade_alle_aufgaben()
        pfade = self.loader.lade_alle_pfade()

        self._aufgaben = {a.id: a for a in aufgaben}
        self._pfade = {p.id: p for p in pfade}

        with self.db.connect() as conn:
            conn.execute("DELETE FROM aufgaben")
            conn.execute("DELETE FROM pfade")

            for a in aufgaben:
                conn.execute(
                    """
                    INSERT INTO aufgaben (
                        id, titel, sprache, schwierigkeit, schwierigkeit_score,
                        schaetz_minuten, tags, pfade, voraussetzungen,
                        task_type, runner_type, aktuelle_revision,
                        dateipfad, hash
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        a.id, a.titel, a.sprache, a.schwierigkeit, a.schwierigkeit_score,
                        a.schaetz_minuten, json.dumps(a.tags), json.dumps(a.pfade),
                        json.dumps(a.voraussetzungen), a.task_type, a.runner_type,
                        a.revision, str(a.dateipfad), a.hash,
                    ),
                )

                fm_dict = a.model_dump(
                    mode="json",
                    exclude={"beschreibung_md", "dateipfad", "hash"},
                )
                conn.execute(
                    """
                    INSERT OR REPLACE INTO aufgaben_versionen (
                        aufgabe_id, revision, hash, frontmatter_json,
                        beschreibung_md, gueltig_ab
                    ) VALUES (?, ?, ?, ?, ?, datetime('now'))
                    """,
                    (a.id, a.revision, a.hash, json.dumps(fm_dict), a.beschreibung_md),
                )

            for p in pfade:
                conn.execute(
                    """
                    INSERT INTO pfade (id, titel, beschreibung, reihenfolge)
                    VALUES (?, ?, ?, ?)
                    """,
                    (p.id, p.titel, p.beschreibung, json.dumps(p.reihenfolge)),
                )

    def alle_aufgaben(self) -> list[Aufgabe]:
        return list(self._aufgaben.values())

    def aufgabe(self, id: str) -> Aufgabe | None:
        return self._aufgaben.get(id)

    def alle_pfade(self) -> list[Pfad]:
        return list(self._pfade.values())

    def pfad(self, id: str) -> Pfad | None:
        return self._pfade.get(id)
