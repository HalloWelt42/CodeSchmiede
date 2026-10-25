#!/usr/bin/env python3
"""Mermaid-Diagramme der Einführungen als SVG bauen: kurs/diagramme/<prüfsumme>.svg.

Der Mermaid-Code steht in der Einführung (eine Wahrheit); dieses Werkzeug zeichnet daraus am Mac ein Vektorbild, das
mit dem Repo ausgerollt wird. Der Browser lädt dafür kein Mermaid. Gezeichnet wird mit Platzhalterfarben, die danach
durch Farbmarken der Oberfläche ersetzt werden (var(--dg-...)); die Oberfläche bettet das SVG ein, so passt es zu
hellem und dunklem Thema. Schon gebaute Diagramme bleiben, überzählige werden entfernt.

Aufruf aus der Projektwurzel:
  backend/.venv/bin/python tools/diagramme.py           fehlende bauen, überzählige entfernen
  backend/.venv/bin/python tools/diagramme.py --alle    alle neu bauen
Einmalig vorher: (cd tools/diagramme && PUPPETEER_SKIP_DOWNLOAD=1 npm ci)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / "backend" / "src"))

from codeschmiede.kurs.einlesen import lade  # noqa: E402
from codeschmiede.kurs.modelle import Diagramm  # noqa: E402

KURS = WURZEL / "kurs"
ZIEL = KURS / "diagramme"
MMDC = WURZEL / "tools" / "diagramme" / "node_modules" / ".bin" / "mmdc"
CHROME = os.environ.get("CODESCHMIEDE_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

# Platzhalterfarbe -> Farbmarke der Oberfläche (definiert in frontend/src/styles/global.css)
FARBEN = {
    "#a10001": "var(--dg-flaeche)",
    "#a10002": "var(--dg-rand)",
    "#a10003": "var(--dg-schrift)",
    "#a10004": "var(--dg-linie)",
    "#a10005": "var(--dg-flaeche-2)",
    "#a10006": "var(--dg-flaeche-3)",
    "#a10007": "var(--dg-grund)",
}
THEMA = {
    "theme": "base",
    "themeVariables": {
        "primaryColor": "#a10001", "primaryBorderColor": "#a10002", "primaryTextColor": "#a10003",
        "lineColor": "#a10004", "secondaryColor": "#a10005", "tertiaryColor": "#a10006",
        "secondaryBorderColor": "#a10002", "tertiaryBorderColor": "#a10002", "secondaryTextColor": "#a10003",
        "tertiaryTextColor": "#a10003", "textColor": "#a10003", "mainBkg": "#a10001", "nodeBorder": "#a10002",
        "edgeLabelBackground": "#a10007", "clusterBkg": "#a10005", "clusterBorder": "#a10002", "titleColor": "#a10003",
        "fontFamily": "Barlow, system-ui, sans-serif", "fontSize": "16px",
    },
    "flowchart": {"htmlLabels": False, "curve": "basis"},
}


def diagramme() -> list[Diagramm]:
    inhalt = lade(KURS)
    for f in inhalt.ladefehler:
        print(f"Ladefehler {f.datei}: {f.meldung}", file=sys.stderr)
    return [t for e in inhalt.einfuehrungen.values() for a in e.abschnitte for t in a.teile if isinstance(t, Diagramm)]


def nachbearbeiten(svg: str, summe: str) -> str:
    """Platzhalterfarben durch Farbmarken ersetzen, eigene Kennung (mehrere Diagramme auf einer Seite teilen sonst
    ihre Stile), feste Breite weg, damit das Bild mit der Spalte mitwächst."""
    for alt, neu in FARBEN.items():
        svg = re.sub(re.escape(alt), neu, svg, flags=re.IGNORECASE)
    svg = svg.replace("my-svg", f"dg-{summe}")
    svg = re.sub(r'\swidth="100%"', "", svg, count=1)
    svg = re.sub(r"max-width:\s*[\d.]+px;?", "max-width:100%;height:auto;", svg, count=1)
    return svg


def bauen(d: Diagramm, ordner: Path) -> str:
    quelle = ordner / "d.mmd"
    ausgabe = ordner / "d.svg"
    quelle.write_text(d.quelle, encoding="utf-8")
    (ordner / "thema.json").write_text(json.dumps(THEMA), encoding="utf-8")
    (ordner / "browser.json").write_text(json.dumps({"executablePath": CHROME, "headless": "shell"}), encoding="utf-8")
    subprocess.run([str(MMDC), "-i", str(quelle), "-o", str(ausgabe), "-c", str(ordner / "thema.json"),
                    "-p", str(ordner / "browser.json"), "-b", "transparent", "-q"], check=True, capture_output=True, text=True)
    return nachbearbeiten(ausgabe.read_text(encoding="utf-8"), d.pruefsumme)


def main() -> None:
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("--alle", action="store_true")
    alle = a.parse_args().alle
    if not MMDC.exists():
        raise SystemExit("mermaid-cli fehlt: (cd tools/diagramme && PUPPETEER_SKIP_DOWNLOAD=1 npm ci)")
    ZIEL.mkdir(parents=True, exist_ok=True)
    liste = {d.pruefsumme: d for d in diagramme()}
    gebaut = 0
    with tempfile.TemporaryDirectory() as tmp:
        for summe, d in liste.items():
            datei = ZIEL / f"{summe}.svg"
            if datei.exists() and not alle:
                continue
            try:
                datei.write_text(bauen(d, Path(tmp)), encoding="utf-8")
            except subprocess.CalledProcessError as fehler:
                raise SystemExit(f"Diagramm {summe} lässt sich nicht zeichnen:\n{d.quelle}\n{fehler.stderr}") from fehler
            gebaut += 1
    weg = [p for p in ZIEL.glob("*.svg") if p.stem not in liste]
    for p in weg:
        p.unlink()
    print(f"{len(liste)} Diagramme, {gebaut} gebaut, {len(weg)} überzählige entfernt")


if __name__ == "__main__":
    main()
