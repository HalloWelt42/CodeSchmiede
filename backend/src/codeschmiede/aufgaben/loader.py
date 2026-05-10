"""AufgabenLoader -- liest Aufgaben + Pfade aus dem aufgaben/-Verzeichnis.

Verzeichnislayout:
  aufgaben/
    pfade/<id>.yml
    sandbox/Dockerfile          (vom Loader ignoriert)
    <sprache>/<aufgabe-id>/aufgabe.md   (+ optional solution_*.py)

Eine Aufgabe-Datei beginnt mit YAML-Frontmatter zwischen `---`-Linien,
gefolgt von Markdown-Beschreibung. Loader produziert Pydantic-Modelle.
"""

import hashlib
from pathlib import Path

import yaml

from ..models.aufgabe import Aufgabe, Frontmatter
from ..models.pfad import Pfad


FRONTMATTER_TRENNER = "---"
RESERVIERTE_VERZEICHNISSE = {"pfade", "sandbox"}


class AufgabenLoader:
    """Liest Aufgaben und Pfade von der Platte. Keine Persistenz, kein Caching."""

    def __init__(self, wurzel: Path):
        self.wurzel = wurzel

    def lade_alle_aufgaben(self) -> list[Aufgabe]:
        if not self.wurzel.exists():
            return []
        aufgaben: list[Aufgabe] = []
        for sprache_dir in sorted(self.wurzel.iterdir()):
            if not sprache_dir.is_dir() or sprache_dir.name in RESERVIERTE_VERZEICHNISSE:
                continue
            for aufgabe_dir in sorted(sprache_dir.iterdir()):
                aufgabe_md = aufgabe_dir / "aufgabe.md"
                if aufgabe_md.exists():
                    aufgaben.append(self.lade_aufgabe(aufgabe_md))
        return aufgaben

    def lade_aufgabe(self, datei: Path) -> Aufgabe:
        text = datei.read_text(encoding="utf-8")
        frontmatter_text, beschreibung = self._spalte(text)

        frontmatter_dict = yaml.safe_load(frontmatter_text) or {}
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
            with datei.open(encoding="utf-8") as f:
                daten = yaml.safe_load(f) or {}
            pfade.append(Pfad.model_validate(daten))
        return pfade

    def lade_musterloesungen(self, aufgabe_id: str) -> list[dict[str, str]]:
        """Liest alle `solution_*.{py,js,ts,html,css,sql}`-Dateien neben
        der `aufgabe.md`.

        Rückgabe: Liste von `{variante, code}`. Reihenfolge ist stabil
        und didaktisch sortiert: naive vor idiomatic vor optimal, der
        Rest alphabetisch.
        """
        endungen = ("*.py", "*.js", "*.ts", "*.html", "*.css", "*.sql")
        for sprache_dir in self.wurzel.iterdir():
            if not sprache_dir.is_dir() or sprache_dir.name in RESERVIERTE_VERZEICHNISSE:
                continue
            kandidat = sprache_dir / aufgabe_id
            if (kandidat / "aufgabe.md").exists():
                ergebnis: list[dict[str, str]] = []
                gesehen: set[str] = set()
                for muster in endungen:
                    for datei in kandidat.glob(f"solution_{muster}"):
                        variante = datei.stem.removeprefix("solution_")
                        if variante in gesehen:
                            continue
                        gesehen.add(variante)
                        ergebnis.append(
                            {"variante": variante, "code": datei.read_text(encoding="utf-8")}
                        )

                ordnung = ["naive", "idiomatic", "optimal"]

                def sortier_key(item: dict[str, str]) -> tuple[int, str]:
                    if item["variante"] in ordnung:
                        return (ordnung.index(item["variante"]), item["variante"])
                    return (len(ordnung), item["variante"])

                ergebnis.sort(key=sortier_key)
                return ergebnis
        return []

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
