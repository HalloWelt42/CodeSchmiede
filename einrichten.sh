#!/usr/bin/env bash
# Einrichten der Codeschmiede. Die Schritte der Neueinrichtung mit ihren Proben stehen in docs/handbuch.md.
#
#   ./einrichten.sh                                       Entwicklung am Mac: Sandbox-Abbilder, Python-Umgebung genau
#                                                         nach uv.lock, Pakete der Oberfläche (das Ausrollen prüft mit
#                                                         dieser Umgebung)
#   ./einrichten.sh --probe --ziel DIR --port-versatz N   Probelauf des Handbuchs: DIR enthält einen Stand der App; daraus
#                                                         entsteht der Betrieb wie auf dem Pi (compose.pi.yml) mit
#                                                         Wegwerfzertifikat, abgeschottet von jeder echten Gegenstelle
#                                                         (deploy/probelauf.compose.yml), Port um N verschoben und nur an
#                                                         127.0.0.1
#   ./einrichten.sh --probe --ziel DIR --abbauen          entfernt alles, was der Probelauf angelegt hat
#
# Der Betrieb auf dem Pi entsteht mit tools/ausrollen.sh (deploy/ausrollen.toml).
set -euo pipefail
HIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KENNUNG="codeschmiede"
PROBE_COMPOSE=(-f compose.pi.yml -f deploy/probelauf.compose.yml)
PROBE_WARTEN_S=600

entwicklung() {
  "$HIER/scripts/setup.sh"
}

# veröffentlichter Port des Vorschaltdienstes laut compose.pi.yml (er steht nur dort)
grundport() {
  SANDBOX_SCHLUESSEL=x docker compose -f "$1/compose.pi.yml" config --format json | python3 -c '
import json, sys
print(json.load(sys.stdin)["services"]["vorne"]["ports"][0]["published"])'
}

probe_aufbauen() {
  local ziel="$1" versatz="$2" port
  port=$(( $(grundport "$ziel") + versatz ))
  cd "$ziel"
  mkdir -p daten zertifikate
  # Wegwerf-Hausstelle in DIR, nie die echte: das Blattzertifikat gilt nur für diesen Rechner
  CAROOT="$ziel/hausstelle" mkcert -cert-file "zertifikate/$KENNUNG.pem" -key-file "zertifikate/$KENNUNG-schluessel.pem" \
    127.0.0.1 localhost "$KENNUNG.local" >/dev/null 2>&1
  cp hausstelle/rootCA.pem zertifikate/rootCA.pem
  ( umask 077; printf 'PROBE_PORT=%s\nSANDBOX_SCHLUESSEL=%s\n' "$port" \
      "$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')" > .env )
  docker compose "${PROBE_COMPOSE[@]}" --profile bilder build --quiet bild-python bild-javascript
  docker compose "${PROBE_COMPOSE[@]}" up -d --build --quiet-pull
  local ende=$(( $(date +%s) + PROBE_WARTEN_S ))
  while [ "$(date +%s)" -lt "$ende" ]; do
    if curl -sf --cacert zertifikate/rootCA.pem "https://127.0.0.1:$port/api/v1/app" >/dev/null; then
      echo "ANTWORTET https://127.0.0.1:$port/api/v1/app"
      return 0
    fi
    sleep 2
  done
  echo "Codeschmiede antwortet nach $PROBE_WARTEN_S s nicht" >&2
  docker compose "${PROBE_COMPOSE[@]}" logs --tail 40 >&2 || true
  return 1
}

probe_abbauen() {
  cd "$1"
  [ -f .env ] || return 0
  docker compose "${PROBE_COMPOSE[@]}" down --volumes --remove-orphans
  docker image rm -f "${COMPOSE_PROJECT_NAME:?}-$KENNUNG" "${COMPOSE_PROJECT_NAME:?}-sandbox" >/dev/null 2>&1 || true
}

probe=0; abbauen=0; ziel=""; versatz=""
while [ $# -gt 0 ]; do
  case "$1" in
    --probe) probe=1 ;;
    --abbauen) abbauen=1 ;;
    --ziel) ziel="${2:?--ziel braucht einen Ordner}"; shift ;;
    --port-versatz) versatz="${2:?--port-versatz braucht eine Zahl}"; shift ;;
    *) echo "unbekannte Angabe: $1" >&2; exit 2 ;;
  esac
  shift
done

if [ "$probe" = 0 ]; then
  entwicklung
elif [ -z "$ziel" ] || [ ! -d "$ziel" ]; then
  echo "--probe braucht --ziel mit einem vorhandenen Ordner" >&2; exit 2
elif [ "$abbauen" = 1 ]; then
  probe_abbauen "$(cd "$ziel" && pwd)"
else
  probe_aufbauen "$(cd "$ziel" && pwd)" "${versatz:?--port-versatz fehlt}"
fi
