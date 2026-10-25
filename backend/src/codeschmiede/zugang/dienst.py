"""Zugang: wer die Codeschmiede nutzen darf, und die erste Einrichtung.

Die App hat keine eigenen Konten (Entscheidung 24.10.2026). Angemeldet wird mit dem Konto der Kellerwolke über die
Anmeldung des Appkern: Name und Passwort oder Koppeln eines Geräts mit einem Code aus der Kellerwolke. Nutzen darf die
App das Konto, dem ihr App-Schlüssel gehört, dazu die Konten aus `weitere_konten`.

Solange Adresse und App-Schlüssel fehlen, ist die App uneingerichtet. Dann liegt ein einmaliger Einrichtungscode in
einer Datei am Rechner (Baustein des Appkern); die Einrichtung von einem anderen Gerät braucht ihn, damit niemand im
Heimnetz die App an eine fremde Kellerwolke hängt.

HTTPS im Heimnetz: vertraut wird den üblichen Stellen und dazu der Hausstelle (`ca_datei`, sonst die mkcert-Stelle
dieses Rechners, wenn es eine gibt).
"""

from __future__ import annotations

import logging
import os
import ssl
from pathlib import Path

import certifi
import httpx
from appkern.anmeldung import Anmeldung
from appkern.app.einrichtungscode import Einrichtungscode, Gesperrt
from appkern.kellerwolke import Kellerwolke, KellerwolkeFehler

from ..config import Settings
from ..db.connection import Datenbank
from .speicher import Zugangsdaten, ZugangsSpeicher

logger = logging.getLogger("codeschmiede.zugang")

KENNUNG = "codeschmiede"


class EinrichtungAbgelehnt(Exception):
    def __init__(self, status: int, meldung: str):
        super().__init__(meldung)
        self.status = status
        self.meldung = meldung


def hausstelle() -> Path | None:
    """Wurzelzertifikat der lokalen Zertifikatsstelle (mkcert), von der Kellerwolke und Apps im Heimnetz ihre
    HTTPS-Zertifikate haben: `$CAROOT`, sonst der übliche Ort auf Mac und Linux."""
    orte = [Path(os.environ["CAROOT"]) / "rootCA.pem"] if os.environ.get("CAROOT") else []
    orte += [Path.home() / "Library" / "Application Support" / "mkcert" / "rootCA.pem",
             Path.home() / ".local" / "share" / "mkcert" / "rootCA.pem"]
    return next((o for o in orte if o.is_file()), None)


class Zugang:
    def __init__(self, settings: Settings, db: Datenbank, transport: httpx.AsyncBaseTransport | None = None):
        self.settings = settings
        self.speicher = ZugangsSpeicher(db)
        self.einrichtungscode = Einrichtungscode.aus_umgebung(KENNUNG, settings.daten_pfad)
        self._transport = transport
        self._client = self._neuer_client()
        self.app_name: str | None = None
        self.besitzer: str | None = None
        daten = self.daten
        self.anmeldung = Anmeldung(daten.kellerwolke_adresse, self._erlaubt, client=self._client,
                                   app_name=self._eigener_name)

    # --- Stand -----------------------------------------------------------------------------------------------

    @property
    def daten(self) -> Zugangsdaten:
        """Gespeicherte Zugangsdaten; die Adresse aus der Umgebung gilt nur, solange keine gespeichert ist."""
        daten = self.speicher.lesen()
        if not daten.kellerwolke_adresse and self.settings.kellerwolke_adresse:
            daten.kellerwolke_adresse = self.settings.kellerwolke_adresse
        return daten

    @property
    def einrichtung_noetig(self) -> bool:
        daten = self.speicher.lesen()
        return not (daten.kellerwolke_adresse and daten.kellerwolke_schluessel.get_secret_value())

    def _erlaubt(self) -> set[str]:
        if not self.besitzer:
            return set()
        return {self.besitzer, *self.speicher.lesen().weitere_konten}

    async def _eigener_name(self) -> str | None:
        if self.app_name is None:
            await self.kennenlernen()
        return self.app_name

    # --- Verbindungen ----------------------------------------------------------------------------------------

    def tls_pruefung(self) -> ssl.SSLContext:
        kontext = ssl.create_default_context(cafile=certifi.where())
        zusatz = self.settings.ca_datei or hausstelle()
        if zusatz is not None and Path(zusatz).is_file():
            kontext.load_verify_locations(zusatz)
        return kontext

    def _neuer_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(timeout=httpx.Timeout(15.0), verify=self.tls_pruefung(), transport=self._transport)

    async def kennenlernen(self) -> None:
        """Name der App und Besitzer des App-Schlüssels von der Kellerwolke holen. Ist sie nicht erreichbar, bleibt
        der letzte Stand; ohne ihn lässt die Anmeldung niemanden herein (sie fragt bei der nächsten Anfrage neu)."""
        daten = self.speicher.lesen()
        schluessel = daten.kellerwolke_schluessel.get_secret_value()
        if not (daten.kellerwolke_adresse and schluessel):
            return
        try:
            ich = await Kellerwolke(daten.kellerwolke_adresse, schluessel, client=self._client, geduld_s=0).ich()
        except KellerwolkeFehler as f:
            logger.warning("Kellerwolke unter %s nicht erreichbar oder Schlüssel ungültig: %s",
                           daten.kellerwolke_adresse, f)
            return
        self.app_name, self.besitzer = ich.app, ich.konto

    async def starten(self) -> None:
        """Beim Start: uneingerichtet einen Einrichtungscode bereitlegen, sonst die Kellerwolke kennenlernen."""
        if self.einrichtung_noetig:
            self.einrichtungscode.erzeugen()
            logger.warning("Erste Einrichtung nötig; der Einrichtungscode liegt in %s", self.einrichtungscode.ort)
        else:
            self.einrichtungscode.entfernen()
            await self.kennenlernen()

    async def schliessen(self) -> None:
        await self.anmeldung.schliessen()
        await self._client.aclose()

    # --- Einrichtung -----------------------------------------------------------------------------------------

    async def einrichten(self, adresse: str, schluessel: str, code: str, lokal: bool) -> None:
        """Adresse und App-Schlüssel eintragen, nachdem die Kellerwolke den Schlüssel bestätigt hat. Nur solange
        die App uneingerichtet ist; von einem anderen Gerät nur mit dem Einrichtungscode."""
        if not self.einrichtung_noetig:
            raise EinrichtungAbgelehnt(409, "Die Codeschmiede ist schon eingerichtet")
        if not lokal:
            self._code_pruefen(code)
        adresse = adresse.strip().rstrip("/")
        try:
            ich = await Kellerwolke(adresse, schluessel.strip(), client=self._client, geduld_s=0).ich()
        except KellerwolkeFehler as f:
            raise EinrichtungAbgelehnt(422, f"Die Kellerwolke unter {adresse} bestätigt diesen App-Schlüssel nicht: {f}")
        alt = self.speicher.lesen()
        self.speicher.schreiben(Zugangsdaten(kellerwolke_adresse=adresse, kellerwolke_schluessel=schluessel.strip(),
                                             weitere_konten=alt.weitere_konten))
        self.app_name, self.besitzer = ich.app, ich.konto
        self.anmeldung.verbinden(adresse, self._client)
        self.einrichtungscode.entfernen()
        logger.info("Eingerichtet: Kellerwolke %s, App %s, Besitzer %s", adresse, ich.app, ich.konto)

    def _code_pruefen(self, code: str) -> None:
        if not self.einrichtungscode.aktiv:
            raise EinrichtungAbgelehnt(403, "Kein Einrichtungscode bereit: die App neu starten")
        try:
            richtig = self.einrichtungscode.pruefen(code)
        except Gesperrt as g:
            raise EinrichtungAbgelehnt(429, f"Zu viele falsche Codes, nochmal in {g.sekunden} s")
        if not richtig:
            raise EinrichtungAbgelehnt(403, f"Der Einrichtungscode stimmt nicht; er steht in {self.einrichtungscode.ort}")
