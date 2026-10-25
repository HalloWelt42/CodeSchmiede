"""Auslieferung der gebauten Oberfläche durch das Backend (Betrieb hinter dem Vorschaltdienst).

- `/assets/...` tragen Prüfsummen im Namen und ändern sich nie (Zwischenspeicher regelt der Vorschaltdienst).
- Dateien in der Wurzel (Symbole, Manifest) kommen, wenn es sie gibt; ein fehlender Dateiname ist 404, damit ein
  alter Zwischenspeicher nie die Startseite statt einer Datei bekommt.
- Alles andere außerhalb von `/api` ist ein Ort der Oberfläche und bekommt die Startseite ohne Zwischenspeicher, damit
  ein Tab nach dem Ausrollen die neue Fassung sieht.
- Pfade, die aus dem Ordner herausführen, gibt es nicht (aufgelöst und geprüft).
"""

import re
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

FASSUNG_META = re.compile(r'<meta\s+name="app-fassung"\s+content="([^"]+)"')


def fassung_der_oberflaeche(ordner: Path | None) -> str | None:
    """Fassung, mit der die Oberfläche gebaut wurde (Meta `app-fassung` der Startseite)."""
    if ordner is None:
        return None
    try:
        treffer = FASSUNG_META.search((ordner / "index.html").read_text(encoding="utf-8"))
    except OSError:
        return None
    return treffer.group(1) if treffer else None


def oberflaeche_einhaengen(app: FastAPI, ordner: Path) -> None:
    wurzel = ordner.resolve()
    startseite = wurzel / "index.html"
    if (wurzel / "assets").is_dir():
        app.mount("/assets", StaticFiles(directory=wurzel / "assets"), name="assets")

    @app.api_route("/{ort:path}", methods=["GET", "HEAD"], include_in_schema=False)
    def ausliefern(ort: str) -> FileResponse:
        if ort.startswith("api/") or ort == "api":
            raise HTTPException(status_code=404, detail="Nicht gefunden")
        if ort:
            datei = (wurzel / ort).resolve()
            if not datei.is_relative_to(wurzel):
                raise HTTPException(status_code=404, detail="Nicht gefunden")
            if datei.is_file():
                return FileResponse(datei)
            if "." in Path(ort).name:
                raise HTTPException(status_code=404, detail="Nicht gefunden")
        return FileResponse(startseite, headers={"Cache-Control": "no-cache"})
