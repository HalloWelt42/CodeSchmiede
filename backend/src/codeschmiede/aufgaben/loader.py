"""AufgabenLoader -- liest Aufgaben + Pfade aus dem aufgaben/-Verzeichnis.

Verzeichnislayout:
  aufgaben/
    _konfig.yml
    pfade/<id>.yml
    <sprache>/<aufgabe-id>/aufgabe.md   (+ optional solution_*.<endung>)
    sql/datasets/<name>.sql             (Datensätze der SQL-Aufgaben)

Eine Aufgabe-Datei beginnt mit YAML-Frontmatter zwischen `---`-Linien,
gefolgt von Markdown-Beschreibung. Loader produziert Pydantic-Modelle.

Eine kaputte Datei hält das Einlesen nicht auf: sie fehlt im Ergebnis
und steht mit Grund in `ladefehler`.
"""

import hashlib
from dataclasses import dataclass
from pathlib import Path

import yaml

from ..models.aufgabe import Aufgabe, Frontmatter
from ..models.pfad import Pfad
from ..yaml_lesen import lies_yaml


FRONTMATTER_TRENNER = "---"
RESERVIERTE_VERZEICHNISSE = {"pfade"}
MUSTERLOESUNG_ENDUNGEN = ("py", "js", "ts", "html", "css", "sql", "txt")
# Didaktische Reihenfolge der Musterlösungen laut Aufgabenformat
# (docs/AUFGABEN-FORMAT.md); andere Varianten folgen alphabetisch.
MUSTERLOESUNG_REIHENFOLGE = ("naive", "idiomatic", "optimal")


@dataclass(frozen=True)
class Ladefehler:
    datei: str
    meldung: str


class AufgabenLoader:
    """Liest Aufgaben und Pfade von der Platte. Keine Persistenz, kein Caching von Inhalten; gemerkt wird nur, in
    welchem Ordner eine Aufgabe beim letzten Einlesen lag (jedes Dateisystem-Nachsehen kostet über eingebundene
    Ordner viel Zeit)."""

    def __init__(self, wurzel: Path):
        self.wurzel = wurzel
        self.ladefehler: list[Ladefehler] = []
        self._ordner: dict[str, Path] = {}

    def aufgaben_dateien(self) -> list[Path]:
        if not self.wurzel.exists():
            return []
        dateien: list[Path] = []
        for sprache_dir in sorted(self.wurzel.iterdir()):
            if not sprache_dir.is_dir() or sprache_dir.name in RESERVIERTE_VERZEICHNISSE:
                continue
            for aufgabe_dir in sorted(sprache_dir.iterdir()):
                aufgabe_md = aufgabe_dir / "aufgabe.md"
                if aufgabe_md.exists():
                    dateien.append(aufgabe_md)
        return dateien

    def lade_alle_aufgaben(self) -> list[Aufgabe]:
        aufgaben: list[Aufgabe] = []
        fehler: list[Ladefehler] = []
        for datei in self.aufgaben_dateien():
            try:
                aufgabe = self.lade_aufgabe(datei)
            except (ValueError, yaml.YAMLError, OSError) as e:
                fehler.append(Ladefehler(self._relativ(datei), str(e)))
                continue
            if aufgabe.id != datei.parent.name:
                fehler.append(Ladefehler(
                    self._relativ(datei),
                    f"ID '{aufgabe.id}' passt nicht zum Ordner '{datei.parent.name}'",
                ))
                continue
            aufgaben.append(aufgabe)
        self.ladefehler = fehler
        self._ordner = {a.id: a.dateipfad.parent for a in aufgaben}
        return aufgaben

    def lade_aufgabe(self, datei: Path) -> Aufgabe:
        text = datei.read_text(encoding="utf-8")
        frontmatter_text, beschreibung = self._spalte(text)

        frontmatter_dict = lies_yaml(frontmatter_text) or {}
        frontmatter = Frontmatter.model_validate(frontmatter_dict)

        return Aufgabe(
            **frontmatter.model_dump(),
            beschreibung_md=beschreibung.strip(),
            dateipfad=datei,
            hash=hashlib.sha1(text.encode("utf-8")).hexdigest(),
        )

    def lade_alle_pfade(self) -> list[Pfad]:
        pfade_dir = self.wurzel / "pfade"
        if not pfade_dir.exists():
            return []
        pfade: list[Pfad] = []
        for datei in sorted(pfade_dir.glob("*.yml")):
            try:
                with datei.open(encoding="utf-8") as f:
                    daten = lies_yaml(f.read()) or {}
                pfade.append(Pfad.model_validate(daten))
            except (ValueError, yaml.YAMLError, OSError) as e:
                self.ladefehler.append(Ladefehler(self._relativ(datei), str(e)))
        return pfade

    def lade_musterloesungen(self, aufgabe_id: str) -> list[dict[str, str]]:
        bekannt = self._ordner.get(aufgabe_id)
        if bekannt is not None:
            try:
                return self.musterloesungen_neben(bekannt)
            except OSError:
                pass  # seit dem Einlesen verschoben oder gelöscht: neu suchen
        for sprache_dir in self.wurzel.iterdir():
            if not sprache_dir.is_dir() or sprache_dir.name in RESERVIERTE_VERZEICHNISSE:
                continue
            kandidat = sprache_dir / aufgabe_id
            if (kandidat / "aufgabe.md").exists():
                return self.musterloesungen_neben(kandidat)
        return []

    @staticmethod
    def musterloesungen_neben(verzeichnis: Path) -> list[dict[str, str]]:
        """Alle `solution_<variante>.<endung>` eines Aufgabenordners als
        `{variante, code}`, didaktisch sortiert."""
        ergebnis: dict[str, str] = {}
        # einmal nachsehen, dann je Endung in ihrer Reihenfolge
        namen = sorted(d.name for d in verzeichnis.iterdir() if d.name.startswith("solution_"))
        for endung in MUSTERLOESUNG_ENDUNGEN:
            for name in namen:
                if name.endswith(f".{endung}"):
                    variante = name.removesuffix(f".{endung}").removeprefix("solution_")
                    ergebnis.setdefault(variante, (verzeichnis / name).read_text(encoding="utf-8"))

        def sortier_key(variante: str) -> tuple[int, str]:
            if variante in MUSTERLOESUNG_REIHENFOLGE:
                return (MUSTERLOESUNG_REIHENFOLGE.index(variante), variante)
            return (len(MUSTERLOESUNG_REIHENFOLGE), variante)

        return [
            {"variante": v, "code": ergebnis[v]} for v in sorted(ergebnis, key=sortier_key)
        ]

    def _relativ(self, datei: Path) -> str:
        try:
            return str(datei.relative_to(self.wurzel))
        except ValueError:
            return str(datei)

    @staticmethod
    def _spalte(text: str) -> tuple[str, str]:
        """Trennt YAML-Frontmatter (zwischen `---`-Linien) vom Markdown-Rest."""
        lines = text.splitlines(keepends=True)
        if not lines or lines[0].strip() != FRONTMATTER_TRENNER:
            raise ValueError("Aufgabe muss mit '---' (Frontmatter) beginnen")
        for i in range(1, len(lines)):
            if lines[i].strip() == FRONTMATTER_TRENNER:
                return "".join(lines[1:i]), "".join(lines[i + 1 :])
        raise ValueError("Schließendes '---' im Frontmatter fehlt")
