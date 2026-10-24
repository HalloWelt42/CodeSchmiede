"""API ohne Sandbox: Herkunft, Lösungsschutz, Schreibrecht, Verwaltung, Bestand."""

from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen

from .conftest import schreibe_aufgabe


def test_fremde_herkunft_abgewiesen(client):
    ziel = "/api/progress/reset-alles"
    assert client.post(ziel, headers={"Sec-Fetch-Site": "cross-site"}).status_code == 403
    assert client.post(ziel, headers={"Origin": "http://boese.example"}).status_code == 403
    assert client.post(ziel, headers={"Sec-Fetch-Site": "same-origin"}).status_code == 200
    assert client.post(ziel).status_code == 200
    # Lesen bleibt erlaubt
    assert client.get("/api/healthz", headers={"Sec-Fetch-Site": "cross-site"}).status_code == 200


def test_keine_cors_freigabe(client):
    antwort = client.get("/api/healthz", headers={"Origin": "http://boese.example"})
    assert "access-control-allow-origin" not in antwort.headers


def test_musterloesungen_erst_nach_aufgeben(client):
    assert client.get("/api/aufgaben/001-verdoppeln/musterloesungen").status_code == 403
    detail = client.get("/api/aufgaben/001-verdoppeln").json()
    assert detail["musterloesungen_anzahl"] == 1 and not detail["musterloesungen_frei"]
    progress = client.post("/api/aufgaben/001-verdoppeln/aufgeben").json()
    assert progress["aufgegeben"]
    antwort = client.get("/api/aufgaben/001-verdoppeln/musterloesungen")
    assert antwort.status_code == 200 and antwort.json()[0]["variante"] == "idiomatic"


def test_aufgeben_kostet_die_punkte(client):
    client.post("/api/aufgaben/001-verdoppeln/aufgeben")
    state = client.app.state.codeschmiede
    aufgabe = state.aufgaben.aufgabe("001-verdoppeln")
    p = state.progress.aktualisiere_nach_submission(aufgabe, True)
    assert p.status == "geloest" and p.punkte_erreicht == 0


def test_versteckte_tests_nie_im_detail(client):
    detail = client.get("/api/aufgaben/001-verdoppeln").json()
    assert detail["anzahl_versteckte_tests"] == 2
    assert "42" not in str(detail)
    sql = client.get("/api/aufgaben/s006-werte").json()
    assert sql["anzahl_versteckte_tests"] == 2


def test_nur_lesend(settings, docker_runner):
    settings.aufgaben_schreibbar = False
    client = TestClient(app_bauen(settings, runner=docker_runner))
    assert client.delete("/api/admin/aufgaben/002-paar").status_code == 409
    assert client.get("/api/admin/aufgaben").status_code == 200


def test_css_und_sql_ids_speicherbar(client):
    eintrag = client.get("/api/admin/aufgaben/c005-knopf").json()
    fm = {k: eintrag[k] for k in ("schema_version", "id", "revision", "titel", "sprache", "task_type", "schwierigkeit", "schwierigkeit_score", "schaetz_minuten")}
    fm["titel"] = "Knopf neu"
    antwort = client.put("/api/admin/aufgaben/c005-knopf", json={"frontmatter": fm, "beschreibung_md": "neu"})
    assert antwort.status_code == 200 and antwort.json()["titel"] == "Knopf neu"


def test_sprachwechsel_zieht_um(client, bestand):
    eintrag = client.get("/api/admin/aufgaben/002-paar").json()
    fm = {k: eintrag[k] for k in ("schema_version", "id", "revision", "titel", "task_type", "schwierigkeit", "schwierigkeit_score", "schaetz_minuten", "funktion")}
    fm["sprache"] = "javascript"
    assert client.put("/api/admin/aufgaben/002-paar", json={"frontmatter": fm}).status_code == 200
    assert not (bestand / "python" / "002-paar").exists()
    assert (bestand / "javascript" / "002-paar" / "aufgabe.md").exists()


def test_musterloesung_mit_endung_der_sprache(client, bestand):
    antwort = client.put("/api/admin/aufgaben/003-js-summe/musterloesungen/naive", json={"code": "const summe = () => 0"})
    assert antwort.status_code == 200
    assert (bestand / "javascript" / "003-js-summe" / "solution_naive.js").exists()


def test_loeschen_prueft_ids(client):
    assert client.delete("/api/admin/aufgaben/..").status_code == 404
    assert client.delete("/api/admin/aufgaben/001-verdoppeln/musterloesungen/..x").status_code == 404


def test_kaputte_datei_haelt_einlesen_nicht_auf(settings, bestand, docker_runner):
    (bestand / "python" / "009-kaputt").mkdir()
    (bestand / "python" / "009-kaputt" / "aufgabe.md").write_text("---\nid: [\n---\n")
    schreibe_aufgabe(bestand, "python", "010-falscher-ordner", "code_schreiben", "funktion: f\n").joinpath("aufgabe.md")
    (bestand / "python" / "010-falscher-ordner" / "aufgabe.md").write_text(
        (bestand / "python" / "010-falscher-ordner" / "aufgabe.md").read_text().replace("id: 010-falscher-ordner", "id: 011-anders")
    )
    schreibe_aufgabe(bestand, "python", "012-mit-luecke", "code_schreiben", "funktion: f\nvoraussetzungen: [999-gibts-nicht]\n")
    client = TestClient(app_bauen(settings, runner=docker_runner))
    gesund = client.get("/api/healthz").json()
    assert gesund["aufgaben_anzahl"] == 7
    befunde = client.get("/api/admin/befunde").json()
    orte = {b["ort"] for b in befunde}
    assert "python/009-kaputt/aufgabe.md" in orte
    assert "python/010-falscher-ordner/aufgabe.md" in orte
    assert any("999-gibts-nicht" in b["meldung"] for b in befunde)


def test_ungueltige_id_und_funktion_abgelehnt(client):
    fm = {"id": "../x", "titel": "x", "sprache": "python", "schwierigkeit": "anfaenger", "schwierigkeit_score": 1, "schaetz_minuten": 1}
    assert client.post("/api/admin/aufgaben", json={"frontmatter": fm}).status_code == 400
    fm = {**fm, "id": "013-neu", "funktion": "f(); import os"}
    assert client.post("/api/admin/aufgaben", json={"frontmatter": fm}).status_code == 400


def test_pfade_kommen_aus_der_pfad_datei(client):
    assert client.get("/api/aufgaben/001-verdoppeln").json()["pfade"] == ["start"]
    assert client.get("/api/aufgaben/003-js-summe").json()["pfade"] == []
    ids = [a["id"] for a in client.get("/api/aufgaben?pfad=start").json()]
    assert sorted(ids) == ["001-verdoppeln", "002-paar"]


def test_pfade_im_aufgabenkopf_abgelehnt(client):
    fm = {"id": "014-neu", "titel": "x", "sprache": "python", "schwierigkeit": "anfaenger",
          "schwierigkeit_score": 1, "schaetz_minuten": 1, "pfade": ["start"]}
    antwort = client.post("/api/admin/aufgaben", json={"frontmatter": fm})
    assert antwort.status_code == 400 and "aufgaben/pfade" in antwort.json()["detail"]
