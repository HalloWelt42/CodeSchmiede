"""KursfortschrittRepository - einziger Ort, der die Tabelle `kurs_ereignisse` liest und schreibt."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Literal

from ..db.connection import Datenbank

Ereignisart = Literal["frage", "vorhersage", "abschnitt", "kurztest_frage", "kurztest"]


@dataclass(frozen=True)
class Ereignis:
    art: Ereignisart
    einfuehrung: str
    element: str
    richtig: bool
    zeit: datetime

    @property
    def tag(self) -> date:
        return self.zeit.date()


class KursfortschrittRepository:
    def __init__(self, db: Datenbank):
        self.db = db

    def eintragen(self, art: Ereignisart, einfuehrung: str, element: str, richtig: bool) -> None:
        with self.db.connect() as conn:
            conn.execute(
                "INSERT INTO kurs_ereignisse (art, einfuehrung, element, richtig, zeit) VALUES (?, ?, ?, ?, ?)",
                (art, einfuehrung, element, 1 if richtig else 0, datetime.now().isoformat(timespec="seconds")),
            )

    def alle(self) -> list[Ereignis]:
        with self.db.connect() as conn:
            rows = conn.execute("SELECT art, einfuehrung, element, richtig, zeit FROM kurs_ereignisse ORDER BY id").fetchall()
        return [Ereignis(art=r["art"], einfuehrung=r["einfuehrung"], element=r["element"], richtig=bool(r["richtig"]),
                         zeit=datetime.fromisoformat(r["zeit"])) for r in rows]


@dataclass(frozen=True)
class Stand:
    """Was aus den Ereignissen folgt, je Einführung abgefragt."""

    ereignisse: list[Ereignis]

    def richtig(self, art: Ereignisart, einfuehrung: str, element: str) -> bool:
        return any(e.art == art and e.einfuehrung == einfuehrung and e.element == element and e.richtig for e in self.ereignisse)

    def beantwortet(self, art: Ereignisart, einfuehrung: str, element: str) -> bool:
        return any(e.art == art and e.einfuehrung == einfuehrung and e.element == element for e in self.ereignisse)

    def abschnitte_fertig(self, einfuehrung: str) -> set[int]:
        return {int(e.element) for e in self.ereignisse if e.art == "abschnitt" and e.einfuehrung == einfuehrung}

    def kurztest_bestanden(self, einfuehrung: str) -> bool:
        return any(e.art == "kurztest" and e.einfuehrung == einfuehrung and e.richtig for e in self.ereignisse)
