"""AufgabenSchreiber -- speichert Aufgaben + Musterloesungen auf der Platte.

Symmetrisch zum Loader: nimmt ein Dictionary mit Frontmatter-Feldern und
einem Beschreibungs-Markdown und schreibt eine `aufgabe.md`. Ergaenzt
um CRUD fuer Musterloesungen (`solution_*.py`).

Wichtige Design-Punkte:
- Schreibt **immer** zuerst in eine Temp-Datei und ersetzt dann atomar.
  So sieht der Watcher nie eine halb-geschriebene Datei.
- Validiert die Aufgabe ueber den Loader, bevor sie geschrieben wird.
  Wenn die Datei nach dem Schreiben nicht parst, hatten wir ein Problem
  vor dem Schreiben.
- Erlaubt nur ASCII-IDs der Form `nnn-slug`, damit der Pfad ueberall
  sauber funktioniert.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any

import yaml

from .loader import AufgabenLoader, FRONTMATTER_TRENNER, RESERVIERTE_VERZEICHNISSE


ID_MUSTER = re.compile(r"^[0-9]{3}-[a-z][a-z0-9-]*[a-z0-9]$")
VARIANTE_MUSTER = re.compile(r"^[a-z][a-z0-9_]*$")
PFAD_ID_MUSTER = re.compile(r"^[a-z][a-z0-9_]*$")


class AufgabenSchreiberFehler(ValueError):
    """Validierungs- oder IO-Fehler beim Schreiben einer Aufgabe."""


class AufgabenSchreiber:
    def __init__(self, wurzel: Path, loader: AufgabenLoader):
        self.wurzel = wurzel
        self.loader = loader

    # ---- Aufgaben ------------------------------------------------------

    def schreibe_aufgabe(
        self,
        frontmatter: dict[str, Any],
        beschreibung_md: str,
        sprache: str,
        existiert_pruefen: bool = True,
    ) -> Path:
        """Schreibt eine `aufgabe.md`. Gibt den Dateipfad zurueck.

        Wenn `existiert_pruefen=True` und die Aufgabe schon existiert,
        wirft einen Fehler. So unterscheidet sich Create von Update --
        Update setzt das Flag auf False.
        """
        aufgabe_id = frontmatter.get("id", "")
        if not ID_MUSTER.match(aufgabe_id):
            raise AufgabenSchreiberFehler(
                f"Ungueltige Aufgaben-ID '{aufgabe_id}'. Format: 3 Ziffern + Bindestrich + Slug, z.B. 070-mein-wurf"
            )
        if sprache in RESERVIERTE_VERZEICHNISSE:
            raise AufgabenSchreiberFehler(
                f"Sprache '{sprache}' ist reserviert"
            )
        if not re.match(r"^[a-z][a-z0-9]*$", sprache):
            raise AufgabenSchreiberFehler(
                f"Sprach-Verzeichnis '{sprache}' muss Kleinbuchstaben + Ziffern sein"
            )

        ziel_dir = self.wurzel / sprache / aufgabe_id
        ziel_datei = ziel_dir / "aufgabe.md"

        if existiert_pruefen and ziel_datei.exists():
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' existiert bereits unter {ziel_datei}"
            )

        # Frontmatter normalisieren -- Pydantic-Felder kommen oft mit
        # zusaetzlichen Sub-Models, die wir hier zu plain Dicts machen.
        fm_clean = self._normalisiere_frontmatter(frontmatter)

        # Generiere YAML-Block. sort_keys=False erhaelt Reihenfolge,
        # default_flow_style=False = Block-Style, allow_unicode = ae/oe/ue.
        yaml_text = yaml.safe_dump(
            fm_clean,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            width=120,
        )

        markdown_text = (
            f"{FRONTMATTER_TRENNER}\n"
            f"{yaml_text}"
            f"{FRONTMATTER_TRENNER}\n"
            "\n"
            f"{beschreibung_md.strip()}\n"
        )

        # Pre-Validierung: temporaer parsen, Pydantic-Fehler frueh raus
        try:
            from ..models.aufgabe import Frontmatter

            Frontmatter.model_validate(fm_clean)
        except Exception as exc:
            raise AufgabenSchreiberFehler(
                f"Frontmatter ist ungueltig: {exc}"
            ) from exc

        ziel_dir.mkdir(parents=True, exist_ok=True)
        self._atomar_schreiben(ziel_datei, markdown_text)
        return ziel_datei

    def loesche_aufgabe(self, aufgabe_id: str) -> Path:
        """Loescht das ganze Aufgaben-Verzeichnis (inkl. solutions)."""
        verzeichnis = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if verzeichnis is None:
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' nicht gefunden"
            )
        shutil.rmtree(verzeichnis)
        return verzeichnis

    # ---- Musterloesungen ----------------------------------------------

    def schreibe_musterloesung(
        self, aufgabe_id: str, variante: str, code: str
    ) -> Path:
        if not VARIANTE_MUSTER.match(variante):
            raise AufgabenSchreiberFehler(
                f"Variante '{variante}' muss Kleinbuchstaben + Ziffern + Underscore sein"
            )
        verzeichnis = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if verzeichnis is None:
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' nicht gefunden"
            )
        ziel = verzeichnis / f"solution_{variante}.py"
        self._atomar_schreiben(ziel, code if code.endswith("\n") else code + "\n")
        return ziel

    def loesche_musterloesung(self, aufgabe_id: str, variante: str) -> Path:
        verzeichnis = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if verzeichnis is None:
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' nicht gefunden"
            )
        ziel = verzeichnis / f"solution_{variante}.py"
        if not ziel.exists():
            raise AufgabenSchreiberFehler(
                f"Musterloesung '{variante}' nicht gefunden"
            )
        ziel.unlink()
        return ziel

    # ---- Pfade ---------------------------------------------------------

    def schreibe_pfad(
        self,
        pfad_id: str,
        titel: str,
        beschreibung: str,
        reihenfolge: list[str],
        existiert_pruefen: bool = True,
    ) -> Path:
        if not PFAD_ID_MUSTER.match(pfad_id):
            raise AufgabenSchreiberFehler(
                f"Ungueltige Pfad-ID '{pfad_id}'. Format: kleinbuchstaben + ziffern + underscore"
            )
        ziel_dir = self.wurzel / "pfade"
        ziel_dir.mkdir(parents=True, exist_ok=True)
        ziel = ziel_dir / f"{pfad_id}.yml"
        if existiert_pruefen and ziel.exists():
            raise AufgabenSchreiberFehler(
                f"Pfad '{pfad_id}' existiert bereits"
            )
        daten = {
            "id": pfad_id,
            "titel": titel,
            "beschreibung": beschreibung,
            "reihenfolge": reihenfolge,
        }
        text = yaml.safe_dump(
            daten,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
        )
        self._atomar_schreiben(ziel, text)
        return ziel

    def loesche_pfad(self, pfad_id: str) -> Path:
        ziel = self.wurzel / "pfade" / f"{pfad_id}.yml"
        if not ziel.exists():
            raise AufgabenSchreiberFehler(f"Pfad '{pfad_id}' nicht gefunden")
        ziel.unlink()
        return ziel

    # ---- Helfer --------------------------------------------------------

    def _finde_aufgaben_verzeichnis(self, aufgabe_id: str) -> Path | None:
        for sprache_dir in self.wurzel.iterdir():
            if not sprache_dir.is_dir() or sprache_dir.name in RESERVIERTE_VERZEICHNISSE:
                continue
            kandidat = sprache_dir / aufgabe_id
            if (kandidat / "aufgabe.md").exists():
                return kandidat
        return None

    @staticmethod
    def _atomar_schreiben(ziel: Path, inhalt: str) -> None:
        """Schreibt erst in temporaere Datei, ersetzt dann atomar."""
        tmp = ziel.with_suffix(ziel.suffix + ".tmp")
        tmp.write_text(inhalt, encoding="utf-8")
        tmp.replace(ziel)

    @staticmethod
    def _normalisiere_frontmatter(fm: dict[str, Any]) -> dict[str, Any]:
        """Saeubert das Frontmatter fuer YAML-Output.

        - Entfernt None-Werte bei optionalen Feldern (sonst landen sie als
          `feld: null` im YAML, was unschoen aussieht und semantisch
          gleich ist wie weglassen).
        - Stellt sicher, dass `quelle` ein Dict ist (nicht Pydantic-Modell).
        """
        bereinigt: dict[str, Any] = {}
        for schluessel, wert in fm.items():
            if wert is None:
                # bewahre None nur fuer Schluessel, wo es semantisch ist
                if schluessel in {"funktion", "autor", "erstellt_am"}:
                    bereinigt[schluessel] = None
                continue
            if isinstance(wert, dict):
                bereinigt[schluessel] = {
                    k: v for k, v in wert.items() if v is not None
                } or None
                if bereinigt[schluessel] is None:
                    del bereinigt[schluessel]
            else:
                bereinigt[schluessel] = wert
        return bereinigt
