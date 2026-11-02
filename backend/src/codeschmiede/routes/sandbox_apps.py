"""Sandbox für andere Apps (Nachschlag WIKI-48, "Ausprobieren"): eine App auf der Erlaubnisliste schickt Code und
Sprache und bekommt die Aufzeichnung zurück (Ausgabe, Fehler, Schritte mit Speicher; dieselbe wie der Debugger der
Codeschmiede). Der Sandbox-Dienst bleibt im eigenen Netz; offen ist nur dieser Weg, mit dem App-Schlüssel der
Kellerwolke. Je App höchstens ein Lauf zugleich, Code begrenzt, Grenzen wie im Debugger."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Literal

from appkern.anmeldung import Konto
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ..aufzeichnung.debuglauf import DEBUGGER, MIN_SEKUNDEN
from ..aufzeichnung.lauf import Aufzeichnung, aufzeichnen
from ..sandbox.result import RunLimits
from ..state import AppState

#: so lang darf der Code einer App sein (ein Beispiel aus einem Handbuch, keine Programme)
HOECHSTENS_ZEICHEN = 20_000


class SandboxAnfrage(BaseModel):
    code: str = Field(min_length=1, max_length=HOECHSTENS_ZEICHEN)
    sprache: Literal["python", "javascript"]
    eingabe: list[str] = Field(default_factory=list, max_length=50, description="Zeilen für input() oder prompt()")


def baue_sandbox_apps_router(state: AppState, pruefen: Callable[..., Awaitable[Konto]],
                             erlaubt: Callable[[], list[str]]) -> APIRouter:
    """`pruefen`: die Anmeldung (App-Schlüssel der Kellerwolke); `erlaubt`: die Erlaubnisliste der Apps."""
    r = APIRouter(prefix="/api/v1/sandbox", tags=["sandbox"])
    laufend: set[str] = set()

    @r.post("/aufzeichnen", response_model=Aufzeichnung)
    async def aufzeichnen_fuer_app(anfrage: SandboxAnfrage, konto: Konto = Depends(pruefen)) -> Aufzeichnung:
        if not konto.app or konto.app not in erlaubt():
            raise HTTPException(status_code=403, detail="Diese App darf die Sandbox nicht nutzen (Einstellung Sandbox für Apps)")
        if konto.app in laufend:
            raise HTTPException(status_code=429, detail="Es läuft schon ein Lauf dieser App")
        laufend.add(konto.app)
        try:
            return await asyncio.to_thread(aufzeichnen, state.runner, anfrage.code, RunLimits(timeout_sekunden=MIN_SEKUNDEN),
                                           anfrage.eingabe, anfrage.sprache, DEBUGGER)
        finally:
            laufend.discard(konto.app)

    return r
