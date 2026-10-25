"""Zugangsdaten der Kellerwolke in der Datenbank der App (Tabelle `einstellungen`).

Die Datenbank hat Vorrang vor der Vorgabe aus der Umgebung: die Einrichtung schreibt Adresse und App-Schlüssel
hierher, die Umgebung (`CODESCHMIEDE_KELLERWOLKE_ADRESSE`) füllt nur das Formular vor.
"""

import json

from pydantic import BaseModel, SecretStr

from ..db.connection import Datenbank


class Zugangsdaten(BaseModel):
    kellerwolke_adresse: str = ""
    kellerwolke_schluessel: SecretStr = SecretStr("")
    # Konten, die die App außer dem Besitzer des App-Schlüssels nutzen dürfen
    weitere_konten: list[str] = []


class ZugangsSpeicher:
    def __init__(self, db: Datenbank):
        self.db = db

    def lesen(self) -> Zugangsdaten:
        with self.db.connect() as conn:
            zeilen = conn.execute("SELECT schluessel, wert FROM einstellungen").fetchall()
        werte = {z["schluessel"]: json.loads(z["wert"]) for z in zeilen}
        return Zugangsdaten(**{k: v for k, v in werte.items() if k in Zugangsdaten.model_fields})

    def schreiben(self, daten: Zugangsdaten) -> None:
        werte = {
            "kellerwolke_adresse": daten.kellerwolke_adresse,
            "kellerwolke_schluessel": daten.kellerwolke_schluessel.get_secret_value(),
            "weitere_konten": daten.weitere_konten,
        }
        with self.db.connect() as conn:
            conn.executemany(
                "INSERT INTO einstellungen (schluessel, wert) VALUES (?, ?) "
                "ON CONFLICT (schluessel) DO UPDATE SET wert = excluded.wert",
                [(k, json.dumps(v, ensure_ascii=False)) for k, v in werte.items()],
            )
