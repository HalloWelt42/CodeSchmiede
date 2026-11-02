"""Sandbox für andere Apps (Nachschlag WIKI-48, "Ausprobieren"): eine App auf der Erlaubnisliste schickt Code und
Sprache und bekommt die Aufzeichnung zurück (Ausgabe, Fehler, Schritte mit Speicher; dieselbe wie der Debugger der
Codeschmiede; PHP in der gewählten Fassung über Xdebug). Nur ausführen geht über "ausfuehren"; welche Sprachen und
Fassungen es gibt, sagt "sprachen", welche Funktionen eine PHP-Fassung kennt, "funktionen/php" (für den Editor,
WIKI-52). Der Sandbox-Dienst bleibt im eigenen Netz; offen ist nur dieser Weg, mit dem App-Schlüssel der Kellerwolke.
Je App höchstens ein Lauf zugleich, Code begrenzt, Grenzen wie im Debugger."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Literal

from appkern.anmeldung import Konto
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ..aufzeichnung.debuglauf import DEBUGGER, MIN_SEKUNDEN
from ..aufzeichnung.lauf import Aufzeichnung, aufzeichnen
from ..sandbox.ausfuehrung import Ausfuehrung, ausfuehren, php_funktionen
from ..sandbox.laufzeiten import EINE_FASSUNG, MIT_AUFZEICHNUNG, PHP_FASSUNGEN
from ..sandbox.result import RunLimits
from ..sandbox.runner import SandboxFehler
from ..state import AppState

#: so lang darf der Code einer App sein (ein Beispiel aus einem Handbuch, keine Programme)
HOECHSTENS_ZEICHEN = 20_000


class SandboxAnfrage(BaseModel):
    code: str = Field(min_length=1, max_length=HOECHSTENS_ZEICHEN)
    sprache: Literal["python", "javascript", "php"]
    fassung: str = Field("", max_length=10, description="PHP-Fassung, etwa 8.3; leer: die neueste")
    eingabe: list[str] = Field(default_factory=list, max_length=50, description="Zeilen für input(), prompt() oder STDIN")


class AusfuehrenAnfrage(BaseModel):
    code: str = Field(min_length=1, max_length=HOECHSTENS_ZEICHEN)
    sprache: Literal["python", "javascript", "php"]
    fassung: str = Field("", max_length=10, description="PHP-Fassung, etwa 8.3; leer: die neueste")


class Sprachangebot(BaseModel):
    sprache: str
    fassungen: list[str] = Field(default_factory=list, description="wählbare Fassungen, neueste zuerst; leer: eine")
    aufzeichnen: bool = Field(description="ob der Debugger den Lauf aufzeichnen kann (sonst nur ausführen)")


def angebot() -> list[Sprachangebot]:
    return [Sprachangebot(sprache=s, fassungen=list(PHP_FASSUNGEN) if s == "php" else [], aufzeichnen=s in MIT_AUFZEICHNUNG)
            for s in (*EINE_FASSUNG, "php")]


def fassung_von(sprache: str, wunsch: str) -> str:
    """Die Fassung eines Laufs: bei PHP die gewünschte (leer: die neueste), sonst keine."""
    fassung = wunsch.strip()
    if sprache == "php":
        fassung = fassung or PHP_FASSUNGEN[0]
        if fassung not in PHP_FASSUNGEN:
            raise HTTPException(status_code=422, detail=f"PHP {fassung} gibt es in der Sandbox nicht ({', '.join(PHP_FASSUNGEN)})")
    elif fassung:
        raise HTTPException(status_code=422, detail=f"Für {sprache} gibt es keine Wahl der Fassung")
    return fassung


def baue_sandbox_apps_router(state: AppState, pruefen: Callable[..., Awaitable[Konto]],
                             erlaubt: Callable[[], list[str]]) -> APIRouter:
    """`pruefen`: die Anmeldung (App-Schlüssel der Kellerwolke); `erlaubt`: die Erlaubnisliste der Apps."""
    r = APIRouter(prefix="/api/v1/sandbox", tags=["sandbox"])
    laufend: set[str] = set()
    funktionen: dict[str, list[str]] = {}          # je PHP-Fassung, einmal gefragt (die Abbilder ändern sich nur beim Ausrollen)
    funktionen_sperre = asyncio.Lock()

    def app_von(konto: Konto) -> str:
        # die Kellerwolke nennt die App mit ihrem Namen ("Nachschlag"), die Liste führt Kennungen: ohne Groß/klein
        app = (konto.app or "").strip().lower()
        if not app or app not in {e.strip().lower() for e in erlaubt()}:
            raise HTTPException(status_code=403, detail="Diese App darf die Sandbox nicht nutzen (Einstellung Sandbox für Apps)")
        return app

    async def einzeln(konto: Konto, lauf: Callable[[], object]):
        """Je App höchstens ein Lauf zugleich; der Lauf selbst geht in einen eigenen Faden."""
        app = app_von(konto)
        if app in laufend:
            raise HTTPException(status_code=429, detail="Es läuft schon ein Lauf dieser App")
        laufend.add(app)
        try:
            return await asyncio.to_thread(lauf)
        finally:
            laufend.discard(app)

    @r.get("/sprachen", response_model=list[Sprachangebot])
    async def sprachen(konto: Konto = Depends(pruefen)) -> list[Sprachangebot]:
        """Was die Sandbox kann: Sprachen, bei PHP die Fassungen, und ob der Debugger aufzeichnet."""
        app_von(konto)
        return angebot()

    @r.post("/aufzeichnen", response_model=Aufzeichnung)
    async def aufzeichnen_fuer_app(anfrage: SandboxAnfrage, konto: Konto = Depends(pruefen)) -> Aufzeichnung:
        fassung = fassung_von(anfrage.sprache, anfrage.fassung)
        return await einzeln(konto, lambda: aufzeichnen(state.runner, anfrage.code, RunLimits(timeout_sekunden=MIN_SEKUNDEN),
                                                        anfrage.eingabe, anfrage.sprache, DEBUGGER, fassung))

    @r.post("/ausfuehren", response_model=Ausfuehrung)
    async def ausfuehren_fuer_app(anfrage: AusfuehrenAnfrage, konto: Konto = Depends(pruefen)) -> Ausfuehrung:
        """Nur ausführen (ohne Aufzeichnung): Ausgabe, Hinweise, Fehler mit Zeile. PHP in der gewählten Fassung."""
        fassung = fassung_von(anfrage.sprache, anfrage.fassung)
        try:
            return await einzeln(konto, lambda: ausfuehren(state.runner, anfrage.code, anfrage.sprache, fassung,
                                                          RunLimits(timeout_sekunden=MIN_SEKUNDEN)))
        except SandboxFehler as f:
            raise HTTPException(status_code=503, detail=str(f)) from f

    @r.get("/funktionen/php", response_model=dict[str, list[str]])
    async def funktionen_php(konto: Konto = Depends(pruefen)) -> dict[str, list[str]]:
        """Je PHP-Fassung die eingebauten Funktionen (klein geschrieben); eine Fassung, die nicht antwortet, fehlt."""
        app_von(konto)
        async with funktionen_sperre:
            for fassung in PHP_FASSUNGEN:
                if fassung in funktionen:
                    continue
                try:
                    funktionen[fassung] = await asyncio.to_thread(php_funktionen, state.runner, fassung,
                                                                  RunLimits(timeout_sekunden=MIN_SEKUNDEN))
                except (SandboxFehler, ValueError):
                    continue                        # beim nächsten Mal wieder gefragt
        return {f: funktionen[f] for f in PHP_FASSUNGEN if f in funktionen}

    return r
