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
- Erlaubt nur ASCII-IDs (`AUFGABEN_ID_MUSTER`), auch beim Löschen, damit
  kein Pfad aus dem Aufgabenordner hinausführt.
- Wechselt die Sprache einer bestehenden Aufgabe, zieht der ganze Ordner
  (samt Musterlösungen) in die neue Sprache um.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any

import yaml

from ..models.aufgabe import AUFGABEN_ID_MUSTER
from .loader import (
    FRONTMATTER_TRENNER,
    MUSTERLOESUNG_ENDUNGEN,
    RESERVIERTE_VERZEICHNISSE,
    AufgabenLoader,
)


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
        self._pruefe_id(aufgabe_id)
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

        bisher = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if existiert_pruefen and bisher is not None:
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' existiert bereits unter {bisher}"
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

        if bisher is not None and bisher != ziel_dir:
            # Sprachwechsel: Ordner samt Musterlösungen umziehen
            ziel_dir.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(bisher), str(ziel_dir))
        ziel_dir.mkdir(parents=True, exist_ok=True)
        self._atomar_schreiben(ziel_datei, markdown_text)
        return ziel_datei

    def loesche_aufgabe(self, aufgabe_id: str) -> Path:
        """Loescht das ganze Aufgaben-Verzeichnis (inkl. solutions)."""
        self._pruefe_id(aufgabe_id)
        verzeichnis = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if verzeichnis is None:
            raise AufgabenSchreiberFehler(
                f"Aufgabe '{aufgabe_id}' nicht gefunden"
            )
        shutil.rmtree(verzeichnis)
        return verzeichnis

    # ---- Musterloesungen ----------------------------------------------

    def schreibe_musterloesung(
        self, aufgabe_id: str, variante: str, code: str, endung: str
    ) -> Path:
        """Schreibt `solution_<variante>.<endung>`; die Endung kommt aus der
        Sprache der Aufgabe (`_konfig.yml`)."""
        self._pruefe_variante(variante)
        if endung not in MUSTERLOESUNG_ENDUNGEN:
            raise AufgabenSchreiberFehler(f"Endung '{endung}' ist für Musterlösungen nicht vorgesehen")
        verzeichnis = self._finde_verzeichnis_oder_fehler(aufgabe_id)
        for alt in self._musterloesung_dateien(verzeichnis, variante):
            if alt.suffix != f".{endung}":
                alt.unlink()
        ziel = verzeichnis / f"solution_{variante}.{endung}"
        self._atomar_schreiben(ziel, code if code.endswith("\n") else code + "\n")
        return ziel

    def loesche_musterloesung(self, aufgabe_id: str, variante: str) -> None:
        self._pruefe_variante(variante)
        verzeichnis = self._finde_verzeichnis_oder_fehler(aufgabe_id)
        dateien = self._musterloesung_dateien(verzeichnis, variante)
        if not dateien:
            raise AufgabenSchreiberFehler(f"Musterloesung '{variante}' nicht gefunden")
        for datei in dateien:
            datei.unlink()

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
        if not PFAD_ID_MUSTER.match(pfad_id):
            raise AufgabenSchreiberFehler(f"Ungueltige Pfad-ID '{pfad_id}'")
        ziel = self.wurzel / "pfade" / f"{pfad_id}.yml"
        if not ziel.exists():
            raise AufgabenSchreiberFehler(f"Pfad '{pfad_id}' nicht gefunden")
        ziel.unlink()
        return ziel

    # ---- Helfer --------------------------------------------------------

    @staticmethod
    def _pruefe_id(aufgabe_id: str) -> None:
        if not AUFGABEN_ID_MUSTER.match(aufgabe_id):
            raise AufgabenSchreiberFehler(
                f"Ungueltige Aufgaben-ID '{aufgabe_id}'. Format z.B. 070-mein-wurf oder c001-button-pill"
            )

    @staticmethod
    def _pruefe_variante(variante: str) -> None:
        if not VARIANTE_MUSTER.match(variante):
            raise AufgabenSchreiberFehler(
                f"Variante '{variante}' muss Kleinbuchstaben + Ziffern + Underscore sein"
            )

    def _finde_verzeichnis_oder_fehler(self, aufgabe_id: str) -> Path:
        self._pruefe_id(aufgabe_id)
        verzeichnis = self._finde_aufgaben_verzeichnis(aufgabe_id)
        if verzeichnis is None:
            raise AufgabenSchreiberFehler(f"Aufgabe '{aufgabe_id}' nicht gefunden")
        return verzeichnis

    @staticmethod
    def _musterloesung_dateien(verzeichnis: Path, variante: str) -> list[Path]:
        return [
            verzeichnis / f"solution_{variante}.{endung}"
            for endung in MUSTERLOESUNG_ENDUNGEN
            if (verzeichnis / f"solution_{variante}.{endung}").exists()
        ]

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
