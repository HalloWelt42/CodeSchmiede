"""Kursinhalte von der Platte lesen: Einführungen, Kurztests, Kurse je Sprache, Begriffskataloge.

Verzeichnislayout (Format in docs/KURS-FORMAT.md):
  kurs/
    <sprache>.yml                                  Kurs: Blöcke, Kapitel, Übungen
    begriffe/<sprache>.yml                         Begriffskatalog
    einfuehrungen/<sprache>/<thema>/einfuehrung.md Kopf (YAML) und Abschnitte (## Titel) mit Blöcken
    einfuehrungen/<sprache>/<thema>/kurztest.yml   eigene Fragen und eine Übung
    einfuehrungen/<sprache>/<thema>/zeichnungen/   eigene Zeichnungen (SVG)
    bilder/<satz>/<schluessel>.webp                Export des Medienpools
    diagramme/<pruefsumme>.svg                     aus den Mermaid-Blöcken gebaut

Ein Abschnitt besteht aus Markdown und Blöcken in Zaunzeilen: ```beispiel, ```frage, ```alltag, ```merke, ```falle,
```zeichnung, ```augenzwinkern (YAML) und ```mermaid (Diagramm). Eine kaputte Datei hält das Einlesen nicht auf: sie fehlt im
Ergebnis und steht mit Grund in `ladefehler`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from pydantic import TypeAdapter, ValidationError

from ..yaml_lesen import lies_yaml
from .modelle import (Abschnitt, Begriffskatalog, Einfuehrung, Frage, FrageTeil, Kopf, Kurs, Kurssprache, Kurztest,
                      Teil)

YAML_BLOECKE = {"beispiel", "frage", "alltag", "merke", "falle", "zeichnung", "augenzwinkern", "kv"}
ZAUN = re.compile(r"^```([a-z]+)\s*$")
_teil = TypeAdapter(Teil)
_frage = TypeAdapter(Frage)


@dataclass(frozen=True)
class Ladefehler:
    datei: str
    meldung: str


@dataclass
class Kursinhalt:
    einfuehrungen: dict[str, Einfuehrung] = field(default_factory=dict)
    kurztests: dict[str, Kurztest] = field(default_factory=dict)
    """Je Einführung ihr Kurztest."""
    kurse: dict[str, Kurs] = field(default_factory=dict)
    begriffe: dict[str, Begriffskatalog] = field(default_factory=dict)
    ladefehler: list[Ladefehler] = field(default_factory=list)


def _meldung(fehler: Exception) -> str:
    if isinstance(fehler, ValidationError):
        return "; ".join(f"{'.'.join(str(x) for x in e['loc'])}: {e['msg']}" for e in fehler.errors())
    return str(fehler)


def zerlege(text: str) -> tuple[dict, str]:
    """YAML-Kopf zwischen `---`-Zeilen und Rumpf."""
    if not text.startswith("---\n"):
        raise ValueError("Kopf fehlt: die Datei beginnt nicht mit ---")
    kopf, trenner, rumpf = text[4:].partition("\n---\n")
    if not trenner:
        raise ValueError("Kopf endet nicht mit ---")
    return lies_yaml(kopf) or {}, rumpf


def _block(art: str, inhalt: str, wo: str) -> Teil:
    if art == "mermaid":
        return _teil.validate_python({"art": "diagramm", "quelle": inhalt.strip()})
    if art not in YAML_BLOECKE:
        raise ValueError(f"{wo}: unbekannter Block ```{art}")
    daten = lies_yaml(inhalt) or {}
    if not isinstance(daten, dict):
        raise ValueError(f"{wo}: Block ```{art} braucht YAML mit Feldern")
    if art == "frage":
        return FrageTeil(frage=_frage.validate_python(daten))
    return _teil.validate_python({"art": art, **daten})


def abschnitte(rumpf: str) -> list[Abschnitt]:
    """Rumpf in Abschnitte (## Titel) mit Text- und Blockteilen zerlegen."""
    ergebnis: list[Abschnitt] = []
    titel: str | None = None
    teile: list = []
    text: list[str] = []
    block: tuple[str, list[str]] | None = None

    def text_abschliessen() -> None:
        markdown = "\n".join(text).strip()
        if markdown:
            if titel is None:
                raise ValueError("Text vor dem ersten Abschnitt (## Titel)")
            teile.append(_teil.validate_python({"art": "text", "markdown": markdown}))
        text.clear()

    def abschnitt_abschliessen() -> None:
        text_abschliessen()
        if titel is not None:
            ergebnis.append(Abschnitt(nummer=len(ergebnis) + 1, titel=titel, teile=list(teile)))
        teile.clear()

    for nummer, zeile in enumerate(rumpf.split("\n"), 1):
        if block is not None:
            if zeile.rstrip() == "```":
                teile.append(_block(block[0], "\n".join(block[1]), f"Zeile {nummer}"))
                block = None
            else:
                block[1].append(zeile)
            continue
        if zeile.startswith("## "):
            abschnitt_abschliessen()
            titel = zeile[3:].strip()
            continue
        treffer = ZAUN.match(zeile)
        if treffer and treffer.group(1) in YAML_BLOECKE | {"mermaid"}:
            text_abschliessen()
            if titel is None:
                raise ValueError(f"Zeile {nummer}: Block vor dem ersten Abschnitt")
            block = (treffer.group(1), [])
            continue
        text.append(zeile)
    if block is not None:
        raise ValueError(f"Block ```{block[0]} wird nicht geschlossen")
    abschnitt_abschliessen()
    if not ergebnis:
        raise ValueError("keine Abschnitte (## Titel)")
    return ergebnis


def lies_einfuehrung(datei: Path, wurzel: Path) -> Einfuehrung:
    kopf, rumpf = zerlege(datei.read_text(encoding="utf-8"))
    e = Einfuehrung(kopf=Kopf.model_validate(kopf), abschnitte=abschnitte(rumpf), pfad=str(datei.parent.relative_to(wurzel)))
    if e.kopf.sprache != datei.parent.parent.name:
        raise ValueError(f"Sprache {e.kopf.sprache!r} passt nicht zum Ordner {datei.parent.parent.name!r}")
    return e


def lade(wurzel: Path) -> Kursinhalt:
    """Alles unter kurs/ lesen; jeder Fehler bleibt bei seiner Datei."""
    inhalt = Kursinhalt()
    if not wurzel.exists():
        return inhalt

    def versuche(datei: Path, lesen) -> object | None:
        try:
            return lesen(datei)
        except (ValueError, ValidationError, yaml.YAMLError, OSError) as fehler:
            inhalt.ladefehler.append(Ladefehler(str(datei.relative_to(wurzel)), _meldung(fehler)))
            return None

    for datei in sorted((wurzel / "einfuehrungen").glob("*/*/einfuehrung.md")):
        e = versuche(datei, lambda d: lies_einfuehrung(d, wurzel))
        if e is None:
            continue
        if e.id in inhalt.einfuehrungen:
            inhalt.ladefehler.append(Ladefehler(str(datei.relative_to(wurzel)), f"Kennung {e.id} gibt es schon"))
            continue
        inhalt.einfuehrungen[e.id] = e
        test = datei.parent / "kurztest.yml"
        if test.exists():
            k = versuche(test, lambda d: Kurztest.model_validate(lies_yaml(d.read_text(encoding="utf-8")) or {}))
            if k is not None:
                inhalt.kurztests[e.id] = k
    sprachen: tuple[Kurssprache, ...] = ("python", "sql", "javascript", "css", "digital")
    for sprache in sprachen:
        datei = wurzel / f"{sprache}.yml"
        if datei.exists():
            kurs = versuche(datei, lambda d: Kurs.model_validate(lies_yaml(d.read_text(encoding="utf-8")) or {}))
            if kurs is not None:
                inhalt.kurse[sprache] = kurs
        datei = wurzel / "begriffe" / f"{sprache}.yml"
        if datei.exists():
            katalog = versuche(datei, lambda d: Begriffskatalog.model_validate(lies_yaml(d.read_text(encoding="utf-8")) or {}))
            if katalog is not None:
                inhalt.begriffe[sprache] = katalog
    return inhalt
