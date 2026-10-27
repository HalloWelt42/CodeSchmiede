#!/usr/bin/env python3
"""Bildaufträge des Kurses mit dem Medienpool abgleichen.

Die Codeschmiede kennt je Zeichnung nur Schlüssel, Art, Sprache, Motiv (deutsch) und Seitenverhältnis. Prompts,
Stil, Erzeugung, Auswahl und Freistellen gehören dem Medienpool (~/Entwicklung/medienpool, Projekt codeschmiede);
der Export legt die gewählten Bilder als WebP nach kurs/bilder/kurs/<schluessel>.webp (vorerst nur Karten).

Quellen der Aufträge: kurs/stilprobe.yml und die Bildaufträge der Einführungen (kurs/einfuehrungen/**).

Aufruf aus der Projektwurzel:
  backend/.venv/bin/python tools/bildschluessel.py               Liste prüfen und zeigen
  backend/.venv/bin/python tools/bildschluessel.py --einrichten  Projekt im Medienpool anlegen (nur wenn es fehlt)
  backend/.venv/bin/python tools/bildschluessel.py --abgleich    Liste an den Medienpool senden
Umgebung: CODESCHMIEDE_MEDIENPOOL (Vorgabe http://127.0.0.1:8470), CODESCHMIEDE_MEDIENPOOL_PROJEKT (codeschmiede).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import yaml

WURZEL = Path(__file__).resolve().parent.parent
KURS = WURZEL / "kurs"
MEDIENPOOL = os.environ.get("CODESCHMIEDE_MEDIENPOOL", "http://127.0.0.1:8470").rstrip("/")
PROJEKT = os.environ.get("CODESCHMIEDE_MEDIENPOOL_PROJEKT", "codeschmiede")
SCHLUESSEL = re.compile(r"^[a-z0-9_]{1,60}$")
ARTEN = {"sinnbild": "Sinnbild", "alltag": "Alltagsbeispiel", "sammelkarte": "Sammelkarte", "bereich": "Bildkarte Bereich"}
SPRACHEN = ("python", "sql", "javascript", "css", "digital")

# Erste Fassung von Stil und Farbfamilien beim Anlegen; danach gehören sie dem Medienpool und werden dort gepflegt.
STIL = {
    "kopf": "Friendly flat illustration for a beginner programming course, clean bold dark slate outlines, soft cel "
            "shading, rounded shapes, gentle humor, one clear central idea, simple readable composition, cute "
            "characters (penguins are welcome), object centered with generous margin.",
    "fuss": "Plain flat pure white background, no scenery behind the subject, only a soft contact shadow. No text, no "
            "letters, no numbers, no digits, no words, no labels, no signs with writing, no logos, no watermark, no "
            "user interface, no program code.",
    "negativ": "text, letters, numbers, digits, words, captions, labels, writing, watermark, logo, photo, "
               "photorealistic, 3d render, blurry, busy background, gradient background, frame, border",
    "kopf_de": "Freundliche flache Illustration für einen Programmierkurs für Einsteiger, klare kräftige dunkle "
               "Konturen, weiche Schattierung, runde Formen, sanfter Humor, eine klare Idee, einfach lesbar, "
               "niedliche Figuren (gern Pinguine), Motiv mittig mit viel Rand.",
    "fuss_de": "Schlichter rein weißer Hintergrund, nichts hinter dem Motiv, nur ein weicher Bodenschatten. Keine "
               "Schrift, keine Buchstaben, keine Zahlen, keine Wörter, keine Beschriftung, keine Logos, kein "
               "Wasserzeichen, keine Oberfläche, kein Programmcode.",
}
FARBFAMILIEN = {
    "python": ("Python", "#f2b84b", "#4f8fd6", "warm sunflower yellow (#f2b84b), calm blue (#4f8fd6) and cream (#fde7b0) with small dark slate accents",
               "warmes Sonnenblumengelb (#f2b84b), ruhiges Blau (#4f8fd6) und Creme (#fde7b0) mit kleinen dunklen Akzenten",
               "cozy, friendly and playful", "gemütlich, freundlich und verspielt"),
    "sql": ("SQL", "#8b7cf6", "#38bdf8", "soft violet (#8b7cf6), sky blue (#38bdf8) and pale lavender (#ddd6fe) with small dark slate accents",
            "sanftes Violett (#8b7cf6), Himmelblau (#38bdf8) und blasses Lavendel (#ddd6fe) mit kleinen dunklen Akzenten",
            "tidy, curious, a little detective-like", "ordentlich, neugierig, ein wenig detektivisch"),
    "javascript": ("JavaScript", "#e9d44c", "#f08a5d", "lemon yellow (#e9d44c), warm coral (#f08a5d) and pale butter (#fbf3b8) with small dark slate accents",
                   "Zitronengelb (#e9d44c), warmes Koralle (#f08a5d) und blasses Butter (#fbf3b8) mit kleinen dunklen Akzenten",
                   "lively, quick and cheerful", "lebhaft, flink und fröhlich"),
    "css": ("CSS", "#ec6aa8", "#4fd1a5", "raspberry pink (#ec6aa8), mint green (#4fd1a5) and blush (#fbcfe8) with small dark slate accents",
            "Himbeerrosa (#ec6aa8), Mintgrün (#4fd1a5) und Zartrosa (#fbcfe8) mit kleinen dunklen Akzenten",
            "artful, neat and decorative", "kunstvoll, sauber und dekorativ"),
    "digital": ("Digitaltechnik", "#fb923c", "#34d399", "copper orange (#fb923c), circuit board green (#34d399) and pale apricot (#fed7aa) with small dark slate accents",
                "Kupferorange (#fb923c), Platinengrün (#34d399) und blasses Apricot (#fed7aa) mit kleinen dunklen Akzenten",
                "tinkering, precise and a little electric", "tüftelnd, genau und ein wenig elektrisch"),
}


@dataclass(frozen=True)
class Auftrag:
    schluessel: str
    art: str
    sprache: str
    motiv: str
    groesse: str
    abschnitt: str

    def kurz(self) -> dict[str, str]:
        """Was der Medienpool beim Abgleich erfährt (SchluesselKurz)."""
        return {"schluessel": self.schluessel, "name": f"{ARTEN[self.art]}: {self.motiv[:60]}", "art": "bild",
                "abschnitt": self.abschnitt, "groesse": self.groesse, "beschreibung_de": self.motiv}


def _auftrag(roh: dict, abschnitt: str, quelle: Path) -> Auftrag:
    a = Auftrag(schluessel=str(roh["schluessel"]), art=str(roh["art"]), sprache=str(roh["sprache"]), motiv=str(roh["motiv"]).strip(),
                groesse=str(roh.get("groesse", "4 x 3")), abschnitt=abschnitt)
    fehler = []
    if not SCHLUESSEL.match(a.schluessel):
        fehler.append(f"Schlüssel {a.schluessel!r} nur aus a-z, 0-9 und _")
    if a.art not in ARTEN:
        fehler.append(f"Art {a.art!r} unbekannt ({', '.join(ARTEN)})")
    if a.sprache not in SPRACHEN:
        fehler.append(f"Sprache {a.sprache!r} unbekannt ({', '.join(SPRACHEN)})")
    if not re.match(r"^\d+ x \d+$", a.groesse):
        fehler.append(f"Größe {a.groesse!r} als 'B x H'")
    if fehler:
        raise SystemExit(f"{quelle.relative_to(WURZEL)}: " + "; ".join(fehler))
    return a


def auftraege() -> list[Auftrag]:
    """Alle Bildaufträge: Stilprobe, danach die Einführungen (Kopf `bilder:`) in Pfadreihenfolge."""
    liste: list[Auftrag] = []
    probe = KURS / "stilprobe.yml"
    if probe.exists():
        liste += [_auftrag(r, "Stilprobe", probe) for r in yaml.safe_load(probe.read_text(encoding="utf-8"))["auftraege"]]
    for datei in sorted((KURS / "einfuehrungen").glob("*/*/einfuehrung.md")):
        kopf = _kopf(datei)
        abschnitt = f"{kopf.get('sprache', datei.parent.parent.name)}: {kopf.get('titel', datei.parent.name)}"
        liste += [_auftrag(r, abschnitt, datei) for r in kopf.get("bilder", [])]
    doppelt = sorted({a.schluessel for a in liste if sum(b.schluessel == a.schluessel for b in liste) > 1})
    if doppelt:
        raise SystemExit("Doppelte Bildschlüssel: " + ", ".join(doppelt))
    return liste


def _kopf(datei: Path) -> dict:
    text = datei.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text.split("\n---\n", 1)[0][4:]) or {}


def _anfrage(methode: str, pfad: str, daten: object | None = None) -> object:
    koerper = None if daten is None else json.dumps(daten).encode()
    anfrage = urllib.request.Request(MEDIENPOOL + pfad, data=koerper, method=methode, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(anfrage, timeout=30) as antwort:
            inhalt = antwort.read()
            return json.loads(inhalt) if inhalt else None
    except urllib.error.HTTPError as fehler:
        raise SystemExit(f"Medienpool {methode} {pfad}: {fehler.code} {fehler.read().decode(errors='replace')}") from fehler
    except urllib.error.URLError as fehler:
        raise SystemExit(f"Medienpool nicht erreichbar ({MEDIENPOOL}): {fehler.reason}") from fehler


def einrichten() -> None:
    if any(p["schluessel"] == PROJEKT for p in _anfrage("GET", "/api/projekte")):
        print(f"Projekt {PROJEKT} gibt es schon; Stil und Farbfamilien pflegt der Medienpool.")
        return
    gruppen = {kennung: {"name": name, "kennfarbe": a, "zweitfarbe": b, "palette": palette, "palette_de": palette_de,
                         "charakter": charakter, "charakter_de": charakter_de}
               for kennung, (name, a, b, palette, palette_de, charakter, charakter_de) in FARBFAMILIEN.items()}
    _anfrage("POST", "/api/projekte", {"schluessel": PROJEKT, "name": "Codeschmiede", "export_ziel": str(KURS / "bilder"),
                                       "stil": STIL, "gruppen": gruppen})
    # Zeichnungen in voller Größe, alle freigestellt (die Kurse setzen sie auf eigene Flächen)
    _anfrage("PATCH", f"/api/projekte/{PROJEKT}", {"erzeugung": {"kante": 768},
                                                   "export": {"kante": 768, "flaechen_kante": 1024, "frei_gruppen": list(FARBFAMILIEN),
                                                              "kugel_vorsilben": [], "kreis_vorsilben": [], "ganz_vorsilben": []}})
    print(f"Projekt {PROJEKT} angelegt, Export nach {KURS / 'bilder'}")


def abgleichen(liste: list[Auftrag]) -> None:
    ergebnis = _anfrage("POST", f"/api/projekte/{PROJEKT}/schluessel/abgleich", {"schluessel_liste": [a.kurz() for a in liste]})
    projekt = _anfrage("GET", f"/api/projekte/{PROJEKT}")["projekt"]
    ohne_gruppe = {e["schluessel"] for e in projekt["schluessel_liste"] if not e.get("gruppe")}
    # Die Farbfamilie folgt der Sprache, aber nur beim ersten Mal: danach gehört die Gruppe dem Medienpool
    for a in liste:
        if a.schluessel in ohne_gruppe:
            _anfrage("PATCH", f"/api/projekte/{PROJEKT}/schluessel/{a.schluessel}", {"gruppe": a.sprache})
    print(f"neu {len(ergebnis['neu'])}, geändert {len(ergebnis['geaendert'])}, überzählig {len(ergebnis['ueberzaehlig'])}")


def main() -> None:
    argumente = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    argumente.add_argument("--einrichten", action="store_true")
    argumente.add_argument("--abgleich", action="store_true")
    a = argumente.parse_args()
    liste = auftraege()
    if a.einrichten:
        einrichten()
    if a.abgleich:
        abgleichen(liste)
    if not (a.einrichten or a.abgleich):
        for e in liste:
            print(f"{e.schluessel:40} {ARTEN[e.art]:18} {e.sprache:11} {e.groesse:7} {e.motiv}")
        print(f"{len(liste)} Bildaufträge")


if __name__ == "__main__":
    sys.exit(main())
