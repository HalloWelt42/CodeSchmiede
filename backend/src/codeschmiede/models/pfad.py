"""Datenmodell für didaktische Pfade -- geordnete Aufgaben-Reihen."""

from pydantic import BaseModel


class Pfad(BaseModel):
    """Ein Pfad gruppiert Aufgaben-IDs in eine sinnvolle Reihenfolge."""

    id: str
    titel: str
    beschreibung: str = ""
    reihenfolge: list[str]
