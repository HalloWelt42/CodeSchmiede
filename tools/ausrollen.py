"""Ausrollen der Codeschmiede auf den Pi (vom Mac aus, über tools/ausrollen.sh).

Die Schritte, die für alle Apps gleich sind, kommen aus dem Appkern (appkern.werkzeuge.ausrollen): Pi prüfen,
Zertifikat der Hausstelle, Stand holen, bauen, laufende Arbeit abwarten, Datenbank sichern (nach der Regel des Appkern,
im Abbild der App mit ihren Werten CODESCHMIEDE_SICHERUNG_*), starten, nach dem Prüfen Docker aufräumen. Eigen sind hier,
weil die Codeschmiede nicht auf dem Gerüst des Appkern steht:

- Stand und Tests: nur gepushte Stände; Backend-Tests und Typprüfung der Oberfläche grün (die Prüfung des ganzen
  Aufgabenbestands gehört vor den Commit, siehe docs/handbuch.md)
- Schlüssel des Sandbox-Dienstes: einmal auf dem Pi erzeugt in `<wurzel>/.env` (Modus 0600), nie im Repo
- Sandbox-Abbilder: die Dienste mit Profil "bilder" werden mitgebaut
- Prüfen: Server, gebaute Oberfläche und VERSION nennen dieselbe Fassung, HTTP/2, Symbole und Manifest, Symbole des
  Startbildschirms deckend

Aufruf: tools/ausrollen.py --ergaenzung DATEI [--sofort]
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path

from appkern.werkzeuge import ausrollen as a

WURZEL = Path(__file__).resolve().parents[1]


def stand_und_tests(z: a.Ziel) -> None:
    a._schritt("Stand und Tests")
    if a._lauf(["git", "status", "--porcelain"], ort=WURZEL):
        raise a.Abbruch("Erst committen.")
    a._lauf(["git", "fetch", "-q", "origin"], ort=WURZEL)
    if a._lauf(["git", "rev-parse", "HEAD"], ort=WURZEL) != a._lauf(["git", "rev-parse", f"origin/{z.zweig}"], ort=WURZEL):
        raise a.Abbruch(f"Erst pushen ({z.zweig} ist nicht auf origin).")
    tests = subprocess.run([".venv/bin/python", "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                           cwd=WURZEL / "backend", capture_output=True, text=True)
    print("Backend:", (tests.stdout.strip().splitlines() or [""])[-1])
    if tests.returncode != 0:
        raise a.Abbruch("Backend-Tests nicht grün")
    typen = subprocess.run(["npx", "svelte-check", "--tsconfig", "./tsconfig.json", "--threshold", "error"],
                           cwd=WURZEL / "frontend", capture_output=True, text=True)
    print("Oberfläche:", (typen.stdout.strip().splitlines() or [""])[-1])
    if typen.returncode != 0:
        raise a.Abbruch("Typprüfung der Oberfläche nicht grün")
    a.rahmen_nachweis(WURZEL)      # Rahmen am Telefon für diesen Stand geprüft (HELF-13)


def sandbox_schluessel(z: a.Ziel) -> None:
    """Der gemeinsame Schlüssel von Backend und Sandbox-Dienst entsteht einmal auf dem Pi und bleibt dort."""
    a._schritt("Schlüssel des Sandbox-Dienstes")
    print(a._ssh(z, f"""set -e
  cd {shlex.quote(z.wurzel)}
  touch .env && chmod 600 .env
  if grep -q '^SANDBOX_SCHLUESSEL=' .env; then echo 'vorhanden'; else
    printf 'SANDBOX_SCHLUESSEL=%s\\n' "$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')" >> .env
    echo 'neu angelegt'
  fi"""))


def bilder(z: a.Ziel) -> None:
    a._schritt("Sandbox-Abbilder bauen")
    a._ssh(z, f"cd {shlex.quote(z.wurzel)} && docker compose -f {shlex.quote(z.compose)} --profile bilder build --quiet "
              "bild-python bild-javascript")
    print(a._ssh(z, "docker images --filter reference=codeschmiede-sandbox --format '{{.Repository}}:{{.Tag}} {{.Size}}'"))


def pruefen(z: a.Ziel) -> None:
    a._schritt("Prüfen")
    w = shlex.quote(z.wurzel)
    a._ssh(z, f"cd {w} && for i in $(seq 1 60); do curl -sf --cacert zertifikate/rootCA.pem "
              f"{shlex.quote(z.adresse)}/api/v1/app >/dev/null && exit 0; sleep 2; done; echo 'Die App antwortet nicht'; exit 1")
    info = json.loads(a._ssh(z, f"curl -sf --cacert {w}/zertifikate/rootCA.pem {shlex.quote(z.adresse)}/api/v1/app"))
    fassung = (WURZEL / "VERSION").read_text(encoding="utf-8").strip()
    print(f"Server {info['fassung']}, Oberfläche {info.get('oberflaeche')}, VERSION {fassung}, Appkern {info['appkern']}")
    if not info["fassung"] == fassung == info.get("oberflaeche"):
        raise a.Abbruch("Fassungen passen nicht zusammen")
    if a._curl(z, "-o", "/dev/null", "-w", "%{http_version}", "--http2", f"{z.adresse}/") != "2":
        raise a.Abbruch(f"Die Seite kommt nicht über HTTP/2: docker compose -f {z.compose} logs vorne")
    for pfad, typ in a.SYMBOLE.items():
        antwort = a._curl(z, "-o", "/dev/null", "-w", "%{http_code} %{content_type}", f"{z.adresse}/{pfad}")
        if not antwort.startswith(f"200 {typ}"):
            raise a.Abbruch(f"Symbol {pfad}: {antwort} (erwartet 200 {typ})")
    # Lehre 3 der Apps: iOS nimmt das Symbol aus dem Manifest und zeigt keins, wenn es durchsichtige Stellen hat
    hausstelle = Path(a._lauf(["mkcert", "-CAROOT"])) / "rootCA.pem"
    for pfad in a.DECKEND:
        daten = subprocess.run(["curl", "-s", "--cacert", str(hausstelle), f"{z.adresse}/{pfad}"], capture_output=True).stdout
        if not a._deckend(daten):
            raise a.Abbruch(f"Symbol {pfad} hat durchsichtige Stellen (iOS zeigt dann keins): python3 scripts/symbole.py")
    if info["einrichtung_noetig"]:
        print(f"Erste Einrichtung nötig: Einrichtungscode in {info['einrichtungscode']}")
    print("HTTP/2 über den Vorschaltdienst, Symbole deckend, Manifest in Ordnung")


def ausrollen(ergaenzung: Path, sofort: bool) -> int:
    try:
        z = a.laden(WURZEL, ergaenzung=ergaenzung)
    except (OSError, ValueError) as f:
        print(f"\nAbbruch: Ziel nicht lesbar: {f}", file=sys.stderr)
        return 1
    try:
        stand_und_tests(z)
        a.pi_pruefen(z)
        a.zertifikat(z)
        a.stand_holen(z)
        sandbox_schluessel(z)
        a.bauen(z)
        bilder(z)
        a.ruhe_abwarten(z, sofort)
        a.sichern(z)
        a.starten(z)
        pruefen(z)
        a.aufraeumen(z)
    except a.Abbruch as f:
        print(f"\nAbbruch: {f}", file=sys.stderr)
        return 1
    print(f"\nAusgerollt: {z.adresse}")
    return 0


if __name__ == "__main__":
    teile = argparse.ArgumentParser(description="Codeschmiede auf den Pi ausrollen")
    teile.add_argument("--ergaenzung", type=Path, required=True, help="Ziel aus der privaten Wahrheit (handbuch ziel)")
    teile.add_argument("--sofort", action="store_true", help="nicht auf laufende Prüfungen warten")
    argumente = teile.parse_args()
    sys.exit(ausrollen(argumente.ergaenzung, argumente.sofort))
