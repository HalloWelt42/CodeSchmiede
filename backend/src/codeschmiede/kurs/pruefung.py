"""Prüfung des Kursbestands beim Einlesen: Verweise, Bilder, Diagramme und "nichts vorausgesetzt".

Für jedes Kapitel gilt als bekannt, was dieses und alle früheren Kapitel einführen (`fuehrt_ein`). Benutzt Code in
Beispielen, Fragen, Kurztest, Übungen oder Kapitelprojekt einen Begriff, der an dieser Stelle noch nicht eingeführt
ist, ist das ein Befund. Was die Prüfung nur mit der Sandbox kann (Vorhersagen gegen den echten Lauf), steht in
tests/test_bestand.py.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from ..aufgaben.bestandspruefung import Befund
from ..models.aufgabe import Aufgabe
from .begriffe import erkenne
from .einlesen import Kursinhalt
from .modelle import (Alltag, Auswahlfrage, Beispiel, Bild, Diagramm, Einfuehrung, Fehlerstellenfrage, FrageTeil,
                      Lueckenfrage, Ordnungsfrage)


def frage_code(f: Auswahlfrage | Lueckenfrage | Ordnungsfrage | Fehlerstellenfrage) -> str | None:
    """Der Code einer Frage, wie er gemeint ist (Lücken mit der ersten richtigen Antwort gefüllt)."""
    if isinstance(f, Lueckenfrage):
        code = f.code
        for antworten in f.antworten:
            code = code.replace("___", antworten[0], 1)
        return code
    if isinstance(f, Ordnungsfrage):
        return "\n".join(f.zeilen)
    return f.code


def codestuecke(e: Einfuehrung) -> list[tuple[str, str]]:
    """(Ort, Code) aller Beispiele und Fragen einer Einführung."""
    stuecke: list[tuple[str, str]] = []
    for a in e.abschnitte:
        for t in a.teile:
            if isinstance(t, Beispiel):
                stuecke.append((f"Abschnitt {a.nummer}, Beispiel {t.id}", t.code))
            elif isinstance(t, FrageTeil) and (code := frage_code(t.frage)):
                stuecke.append((f"Abschnitt {a.nummer}, Frage {t.frage.id}", code))
    return stuecke


def pruefe_kurs(inhalt: Kursinhalt, aufgaben: dict[str, Aufgabe], musterloesungen: Callable[[str], list[dict[str, str]]],
                wurzel: Path) -> list[Befund]:
    befunde = [Befund(ort=f"kurs/{f.datei}", meldung=f.meldung) for f in inhalt.ladefehler]

    def befund(ort: str, meldung: str) -> None:
        befunde.append(Befund(ort=ort, meldung=meldung))

    # Bilder und Diagramme je Einführung
    for e in inhalt.einfuehrungen.values():
        ort = f"kurs/{e.pfad}"
        erklaert = {b.schluessel for b in e.kopf.bilder}
        for a in e.abschnitte:
            for t in a.teile:
                schluessel = t.schluessel if isinstance(t, Bild) else t.bild if isinstance(t, Alltag) else None
                if schluessel and schluessel not in erklaert:
                    befund(ort, f"Abschnitt {a.nummer}: Bild {schluessel} steht nicht unter bilder im Kopf")
                if isinstance(t, Diagramm) and not (wurzel / "diagramme" / f"{t.pruefsumme}.svg").exists():
                    befund(ort, f"Abschnitt {a.nummer}: Diagramm noch nicht gebaut (tools/diagramme.py)")

    # Kurse: Verweise und Vorgriffe
    verwendet: set[str] = set()
    for sprache, kurs in inhalt.kurse.items():
        katalog = inhalt.begriffe.get(sprache)
        if katalog is None:
            befund(f"kurs/{sprache}.yml", f"Begriffskatalog kurs/begriffe/{sprache}.yml fehlt")
        bekannte_begriffe = {b.id for b in katalog.begriffe} if katalog else set()
        eingefuehrt: set[str] = set()
        for nr, kapitel in enumerate(kurs.kapitel(), 1):
            ort = f"kurs/{sprache}.yml, Kapitel {nr}"
            e = inhalt.einfuehrungen.get(kapitel.einfuehrung)
            if e is None:
                befund(ort, f"Einführung {kapitel.einfuehrung} gibt es nicht")
                continue
            if e.kopf.sprache != sprache:
                befund(ort, f"Einführung {e.id} gehört zu {e.kopf.sprache}")
            verwendet.add(e.id)
            for begriff in e.kopf.fuehrt_ein:
                if begriff not in bekannte_begriffe:
                    befund(f"kurs/{e.pfad}", f"Begriff {begriff} steht nicht im Begriffskatalog")
                elif begriff in eingefuehrt:
                    befund(f"kurs/{e.pfad}", f"Begriff {begriff} wurde schon früher eingeführt")
            eingefuehrt |= set(e.kopf.fuehrt_ein)

            stuecke = [(f"kurs/{e.pfad}: {wo}", code) for wo, code in codestuecke(e)]
            test = inhalt.kurztests.get(e.id)
            aufgaben_ids = [*kapitel.uebungen, *kapitel.projekt, *([test.uebung] if test else [])]
            if test:
                stuecke += [(f"kurs/{e.pfad}/kurztest.yml: Frage {f.id}", c) for f in test.fragen if (c := frage_code(f))]
            for aid in aufgaben_ids:
                a = aufgaben.get(aid)
                if a is None:
                    befund(ort, f"Aufgabe {aid} gibt es nicht")
                    continue
                if a.sprache != sprache:
                    befund(ort, f"Aufgabe {aid} ist {a.sprache}, nicht {sprache}")
                stuecke += [(f"Aufgabe {aid}, Musterlösung {m['variante']}", m["code"]) for m in musterloesungen(aid)]
                if a.starter_code:
                    stuecke.append((f"Aufgabe {aid}, Startcode", a.starter_code))
            if katalog is None:
                continue
            for wo, code in stuecke:
                benutzt = erkenne(katalog, code)
                if benutzt is None:
                    continue
                vorgriff = sorted(benutzt - eingefuehrt)
                if vorgriff:
                    befund(wo, f"Kapitel {nr} setzt voraus, was noch nicht eingeführt ist: {', '.join(vorgriff)}")

    for e in inhalt.einfuehrungen.values():
        if e.id not in verwendet:
            befund(f"kurs/{e.pfad}", "Einführung steht in keinem Kurs")
    return befunde
