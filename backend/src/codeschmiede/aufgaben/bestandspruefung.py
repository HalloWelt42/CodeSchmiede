"""Bestandsprüfung -- findet beim Einlesen, was am Aufgabenbestand nicht
stimmt, ohne das Einlesen aufzuhalten.

Befunde:
- Dateien, die sich nicht lesen ließen (Grund aus dem Loader)
- Voraussetzungen und Pfad-Einträge, die auf keine Aufgabe zeigen
- Sprache, Schwierigkeit oder Aufgabentyp, die `_konfig.yml` nicht kennt
- Aufgabentypen ohne Pruefer und was ein Pruefer am Aufbau seiner
  Aufgaben bemängelt (Level-Dateien der Spiele)
- versteckte Tests, die der Aufgabentext samt Erwartung verrät
- Spiele, deren Aufgabentyp oder Pfade es nicht gibt

Die Befunde stehen in der Verwaltung und im Health-Check.
"""

from pydantic import BaseModel

from ..models.aufgabe import Aufgabe
from ..models.konfig import Konfiguration
from ..models.pfad import Pfad
from ..pruefung.registry import PRUEFER_REGISTRY
from .lecksuche import verratene_tests
from .loader import Ladefehler


class Befund(BaseModel):
    ort: str  # Aufgaben-ID, Pfad-ID oder Datei
    meldung: str


def pruefe_bestand(
    aufgaben: list[Aufgabe],
    pfade: list[Pfad],
    ladefehler: list[Ladefehler],
    konfig: Konfiguration,
) -> list[Befund]:
    befunde = [Befund(ort=f.datei, meldung=f.meldung) for f in ladefehler]
    ids = {a.id for a in aufgaben}

    for a in aufgaben:
        for v in a.voraussetzungen:
            if v not in ids:
                befunde.append(Befund(ort=a.id, meldung=f"Voraussetzung '{v}' gibt es nicht"))
        if konfig.sprachen and a.sprache not in konfig.sprache_ids():
            befunde.append(Befund(ort=a.id, meldung=f"Sprache '{a.sprache}' fehlt in _konfig.yml"))
        if konfig.schwierigkeiten and a.schwierigkeit not in konfig.schwierigkeit_ids():
            befunde.append(Befund(ort=a.id, meldung=f"Schwierigkeit '{a.schwierigkeit}' fehlt in _konfig.yml"))
        if konfig.aufgabentypen and a.task_type not in konfig.aufgabentyp_ids():
            befunde.append(Befund(ort=a.id, meldung=f"Aufgabentyp '{a.task_type}' fehlt in _konfig.yml"))
        pruefer = PRUEFER_REGISTRY.get(a.task_type)
        if pruefer is None:
            befunde.append(Befund(ort=a.id, meldung=f"Kein Pruefer für Aufgabentyp '{a.task_type}'"))
        else:
            befunde += [Befund(ort=a.id, meldung=m) for m in pruefer.pruefe_aufbau(a)]
        verraten = verratene_tests(a)
        if verraten:
            nummern = ", ".join(str(i + 1) for i in verraten)
            befunde.append(Befund(ort=a.id, meldung=f"Text verrät versteckte Tests Nr. {nummern}"))

    for p in pfade:
        for aid in p.reihenfolge:
            if aid not in ids:
                befunde.append(Befund(ort=f"Pfad {p.id}", meldung=f"Aufgabe '{aid}' gibt es nicht"))

    pfad_ids = {p.id for p in pfade}
    for s in konfig.spiele:
        if konfig.aufgabentypen and s.aufgabentyp not in konfig.aufgabentyp_ids():
            befunde.append(Befund(ort=f"Spiel {s.id}", meldung=f"Aufgabentyp '{s.aufgabentyp}' fehlt in _konfig.yml"))
        for pid in s.pfade:
            if pid not in pfad_ids:
                befunde.append(Befund(ort=f"Spiel {s.id}", meldung=f"Pfad '{pid}' gibt es nicht"))

    return befunde
