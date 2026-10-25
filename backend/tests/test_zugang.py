"""Anmeldung mit dem Kellerwolke-Konto, erste Einrichtung und Auslieferung der Oberfläche.

Die Kellerwolke ist eine Schein-Gegenstelle (httpx.MockTransport) mit genau den Wegen, die der Appkern nutzt.
"""

import json
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings

ADRESSE = "https://kellerwolke.test"
SCHLUESSEL = "kw_app_codeschmiede_probe"
KONTEN = {"marcel": "geheim", "fremd": "auch"}


def schein_kellerwolke() -> httpx.MockTransport:
    sitzungen: dict[str, str] = {}

    def antwort(anfrage: httpx.Request) -> httpx.Response:
        pfad = anfrage.url.path
        if pfad == "/api/v1/ablage/ich":
            if anfrage.headers.get("authorization") != f"Bearer {SCHLUESSEL}":
                return httpx.Response(401, json={"detail": "Schlüssel ungültig"})
            return httpx.Response(200, json={"app": "Codeschmiede", "konto": "marcel", "rechte": []})
        if pfad == "/api/v1/auth/login":
            daten = json.loads(anfrage.content)
            if KONTEN.get(daten["kennung"]) != daten["passwort"] or daten.get("fuer_app") != "Codeschmiede":
                return httpx.Response(401, json={"detail": "falsch"})
            token = f"sitzung-{daten['kennung']}"
            sitzungen[token] = daten["kennung"]
            return httpx.Response(200, json={"token": token, "benutzer": {"id": 1, "name": daten["kennung"]}})
        if pfad == "/api/v1/auth/status":
            name = sitzungen.get(anfrage.headers.get("x-kellerwolke-sitzung", ""))
            if name is None:
                return httpx.Response(200, json={"angemeldet": False})
            return httpx.Response(200, json={"angemeldet": True, "benutzer": {"id": 1, "name": name},
                                             "app": "Codeschmiede"})
        if pfad == "/api/v1/auth/logout":
            sitzungen.pop(anfrage.headers.get("x-kellerwolke-sitzung", ""), None)
            return httpx.Response(204)
        return httpx.Response(404)

    return httpx.MockTransport(antwort)


@pytest.fixture
def zugangs_settings(settings: Settings) -> Settings:
    return settings.model_copy(update={"anmeldung_pflicht": True})


@pytest.fixture
def client(zugangs_settings: Settings):
    with TestClient(app_bauen(zugangs_settings, kellerwolke_transport=schein_kellerwolke())) as c:
        yield c


def einrichten(client: TestClient, settings: Settings) -> None:
    code = (settings.daten_pfad / "einrichtungscode").read_text().strip()
    antwort = client.post("/api/v1/einrichtung", json={
        "kellerwolke_adresse": ADRESSE, "kellerwolke_schluessel": SCHLUESSEL, "einrichtungscode": code})
    assert antwort.status_code == 200, antwort.text


def anmelden(client: TestClient, name: str = "marcel") -> dict[str, str]:
    antwort = client.post("/api/v1/anmeldung", json={"kennung": name, "passwort": KONTEN[name]})
    assert antwort.status_code == 200, antwort.text
    return {"X-Kellerwolke-Sitzung": antwort.json()["token"]}


def test_uneingerichtet_nennt_nur_den_ort_des_codes(client, zugangs_settings):
    info = client.get("/api/v1/app").json()
    assert info["einrichtung_noetig"] is True
    assert info["einrichtungscode"] == str(zugangs_settings.daten_pfad / "einrichtungscode")
    code = (zugangs_settings.daten_pfad / "einrichtungscode").read_text().strip()
    assert code not in json.dumps(info)
    assert client.get("/api/aufgaben").status_code == 401


def test_einrichtung_braucht_den_code(client, zugangs_settings):
    eingabe = {"kellerwolke_adresse": ADRESSE, "kellerwolke_schluessel": SCHLUESSEL}
    assert client.post("/api/v1/einrichtung", json=eingabe).status_code == 403
    assert client.post("/api/v1/einrichtung", json={**eingabe, "einrichtungscode": "AAAA-BBBB"}).status_code == 403
    einrichten(client, zugangs_settings)
    info = client.get("/api/v1/app").json()
    assert info["einrichtung_noetig"] is False and info["besitzer"] == "marcel" and info["app_name"] == "Codeschmiede"
    assert info["einrichtungscode"] is None
    assert not (zugangs_settings.daten_pfad / "einrichtungscode").exists()
    # nur einmal
    assert client.post("/api/v1/einrichtung", json={**eingabe, "einrichtungscode": "x"}).status_code == 409


def test_falscher_app_schluessel_wird_nicht_gespeichert(client, zugangs_settings):
    code = (zugangs_settings.daten_pfad / "einrichtungscode").read_text().strip()
    antwort = client.post("/api/v1/einrichtung", json={
        "kellerwolke_adresse": ADRESSE, "kellerwolke_schluessel": "kw_app_falsch_xyz", "einrichtungscode": code})
    assert antwort.status_code == 422
    assert client.get("/api/v1/app").json()["einrichtung_noetig"] is True


def test_besitzer_darf_rein(client, zugangs_settings):
    einrichten(client, zugangs_settings)
    kopf = anmelden(client)
    assert client.get("/api/aufgaben", headers=kopf).status_code == 200
    ohne = client.get("/api/aufgaben")
    assert ohne.status_code == 401
    assert ohne.headers["www-authenticate"] == "Kellerwolke-Sitzung"
    client.post("/api/v1/anmeldung/abmelden", headers=kopf)
    assert client.get("/api/aufgaben", headers=kopf).status_code == 401


def test_fremdes_konto_wird_abgewiesen(client, zugangs_settings):
    einrichten(client, zugangs_settings)
    antwort = client.post("/api/v1/anmeldung", json={"kennung": "fremd", "passwort": KONTEN["fremd"]})
    assert antwort.status_code == 403


def test_falsches_passwort(client, zugangs_settings):
    einrichten(client, zugangs_settings)
    antwort = client.post("/api/v1/anmeldung", json={"kennung": "marcel", "passwort": "nein"})
    assert antwort.status_code == 401


def test_oberflaeche_wird_ausgeliefert(zugangs_settings, tmp_path: Path):
    dist = tmp_path / "dist"
    (dist / "assets").mkdir(parents=True)
    (dist / "index.html").write_text('<html><head><meta name="app-fassung" content="9.9.9"></head></html>')
    (dist / "assets" / "app-abc123.js").write_text("console.log(1)")
    (dist / "favicon.ico").write_bytes(b"\0")
    settings = zugangs_settings.model_copy(update={"oberflaeche_pfad": dist})
    with TestClient(app_bauen(settings, kellerwolke_transport=schein_kellerwolke())) as c:
        assert c.get("/api/v1/app").json()["oberflaeche"] == "9.9.9"
        start = c.get("/")
        assert start.status_code == 200 and "app-fassung" in start.text
        assert start.headers["cache-control"] == "no-cache"
        assert "app-fassung" in c.get("/aufgabe/123").text
        assert c.get("/assets/app-abc123.js").status_code == 200
        assert c.get("/favicon.ico").status_code == 200
        assert c.get("/fehlt.png").status_code == 404
        assert c.get("/..%2F..%2Fetc/passwd").status_code == 404
        assert c.get("/api/gibt-es-nicht").status_code == 404
