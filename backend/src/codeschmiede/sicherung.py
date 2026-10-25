"""Nächtliche Sicherung der Datenbank (Lernfortschritt, Abgaben, Einstellungen).

Einmal am Tag zur eingestellten Stunde eine Kopie über die Sicherungsschnittstelle von SQLite (konsistent auch bei
laufendem Betrieb) nach `<ordner>/nachts-JJJJMMTT.sqlite`; die neuesten `behalten` bleiben. Die Kopien vor jedem
Ausrollen (`codeschmiede-*.sqlite`, vom Ausrollen) liegen im selben Ordner und werden hier nicht angefasst. Von dort
holt das Werkzeug Sicherungen sie auf den Mac.
"""

import asyncio
import logging
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger("codeschmiede.sicherung")


def sichern(db_datei: Path, ordner: Path, behalten: int, jetzt: datetime | None = None) -> Path:
    ordner.mkdir(parents=True, exist_ok=True)
    ziel = ordner / f"nachts-{(jetzt or datetime.now()):%Y%m%d}.sqlite"
    quelle = sqlite3.connect(db_datei)
    kopie = sqlite3.connect(ziel)
    try:
        quelle.backup(kopie)
    finally:
        kopie.close()
        quelle.close()
    for alt in sorted(ordner.glob("nachts-*.sqlite"), reverse=True)[behalten:]:
        alt.unlink()
    return ziel


def bis_zur_stunde(stunde: int, jetzt: datetime) -> float:
    naechste = jetzt.replace(hour=stunde, minute=0, second=0, microsecond=0)
    if naechste <= jetzt:
        naechste += timedelta(days=1)
    return (naechste - jetzt).total_seconds()


async def nachts_sichern(db_datei: Path, ordner: Path, stunde: int, behalten: int) -> None:
    while True:
        await asyncio.sleep(bis_zur_stunde(stunde, datetime.now()))
        try:
            ziel = await asyncio.to_thread(sichern, db_datei, ordner, behalten)
            logger.info("Datenbank gesichert: %s", ziel)
        except (OSError, sqlite3.Error):
            logger.exception("Nächtliche Sicherung gescheitert")
