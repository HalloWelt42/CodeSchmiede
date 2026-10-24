"""DienstRunner -- der Runner des Backends: reicht Läufe an den
Sandbox-Dienst weiter (HTTP mit gemeinsamem Schlüssel)."""

import httpx

from .dienst import SCHLUESSEL_HEADER
from .result import RunLimits, RunResult
from .runner import SandboxFehler

# Zuschlag auf die Laufzeitgrenze: Containerstart plus Warten auf einen
# Platz; liegt über Start- und Wartezeit des Dienstes, damit dessen
# eigene Antwort (Ergebnis oder 503) zuerst ankommt.
ZUSCHLAG_SEKUNDEN = 60


class DienstRunner:
    def __init__(self, url: str, schluessel: str, client: httpx.Client | None = None):
        self.url = url.rstrip("/")
        self.schluessel = schluessel
        self.client = client or httpx.Client()

    def run_code(
        self, code: str, sprache: str, limits: RunLimits | None = None
    ) -> RunResult:
        limits = limits or RunLimits()
        try:
            antwort = self.client.post(
                f"{self.url}/laeufe",
                json={"code": code, "sprache": sprache, "limits": limits.model_dump()},
                headers={SCHLUESSEL_HEADER: self.schluessel},
                timeout=limits.timeout_sekunden + ZUSCHLAG_SEKUNDEN,
            )
        except httpx.HTTPError as fehler:
            raise SandboxFehler(f"Sandbox-Dienst nicht erreichbar ({self.url})") from fehler
        if antwort.status_code != 200:
            try:
                detail = antwort.json().get("detail", antwort.text)
            except ValueError:
                detail = antwort.text
            raise SandboxFehler(f"Sandbox-Dienst lehnt ab ({antwort.status_code}): {detail}")
        return RunResult.model_validate(antwort.json())
