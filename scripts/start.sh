#!/usr/bin/env bash
# Startet Backend + Frontend in einem Schritt fuer die lokale
# Entwicklung. Beide Prozesse laufen parallel; Strg+C beendet beide.
#
# Voraussetzung: ./scripts/setup.sh wurde einmal ausgefuehrt
# (Sandbox-Image gebaut, Backend-venv und Frontend-Pakete installiert).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
BACKEND_PORT=8200
FRONTEND_PORT=5184

# Smoke-Test: ist das Setup ueberhaupt gelaufen?
if [ ! -x "$BACKEND_DIR/.venv/bin/python" ]; then
  echo "Backend-venv fehlt. Bitte zuerst $SCRIPT_DIR/setup.sh ausfuehren."
  exit 1
fi
if [ ! -d "$FRONTEND_DIR/node_modules" ]; then
  echo "Frontend-node_modules fehlt. Bitte zuerst $SCRIPT_DIR/setup.sh ausfuehren."
  exit 1
fi

# Ports pruefen -- nicht blind killen! Eine versehentliche
# Doppel-Ausfuehrung des Skripts wuerde sonst den gerade benutzten
# Server abschiessen. Nur wenn der Nutzer es explizit will:
pruefe_port() {
  local port=$1
  local name=$2
  local pids
  pids=$(lsof -ti:"$port" 2>/dev/null || true)
  if [ -z "$pids" ]; then
    return 0
  fi
  echo "Port $port ($name) ist belegt von PID $pids."
  if [ "${KILL_PORTS:-0}" = "1" ]; then
    echo "  KILL_PORTS=1 gesetzt -- beende PID $pids"
    echo "$pids" | xargs kill -9 2>/dev/null || true
    sleep 1
  else
    echo "  Erst stoppen oder mit KILL_PORTS=1 $0 neu starten."
    exit 1
  fi
}
pruefe_port "$BACKEND_PORT" "Backend"
pruefe_port "$FRONTEND_PORT" "Frontend"

# Tempo-Logs an feste Stellen
LOG_DIR="$ROOT_DIR/data"
mkdir -p "$LOG_DIR"
BACKEND_LOG="$LOG_DIR/backend.log"
FRONTEND_LOG="$LOG_DIR/frontend.log"

echo
echo "Starte Backend (Port $BACKEND_PORT) ..."
cd "$BACKEND_DIR"
.venv/bin/python -m codeschmiede.main > "$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!
echo "  PID $BACKEND_PID, Log: $BACKEND_LOG"

echo
echo "Starte Frontend (Port $FRONTEND_PORT) ..."
cd "$FRONTEND_DIR"
npm run dev -- --port "$FRONTEND_PORT" --strictPort > "$FRONTEND_LOG" 2>&1 &
FRONTEND_PID=$!
echo "  PID $FRONTEND_PID, Log: $FRONTEND_LOG"

# Aufraeumen bei Strg+C oder Skript-Ende
beenden() {
  echo
  echo "Beende Backend (PID $BACKEND_PID) und Frontend (PID $FRONTEND_PID) ..."
  kill "$BACKEND_PID" 2>/dev/null || true
  kill "$FRONTEND_PID" 2>/dev/null || true
  exit 0
}
trap beenden INT TERM

# Health-Check abwarten
echo
echo "Warte auf Backend-Health ..."
for i in {1..15}; do
  if curl -sf "http://localhost:$BACKEND_PORT/api/healthz" > /dev/null; then
    break
  fi
  sleep 1
done
if curl -sf "http://localhost:$BACKEND_PORT/api/healthz" > /dev/null; then
  echo "  Backend antwortet."
else
  echo "  Backend antwortet NICHT -- siehe $BACKEND_LOG"
fi

echo "Warte auf Frontend ..."
for i in {1..15}; do
  if curl -sf "http://localhost:$FRONTEND_PORT/" > /dev/null; then
    break
  fi
  sleep 1
done
if curl -sf "http://localhost:$FRONTEND_PORT/" > /dev/null; then
  echo "  Frontend antwortet."
else
  echo "  Frontend antwortet NICHT -- siehe $FRONTEND_LOG"
fi

echo
echo "=== Codeschmiede laeuft ==="
echo "  Browser:    http://localhost:$FRONTEND_PORT"
echo "  Backend-API: http://localhost:$BACKEND_PORT/api/healthz"
echo "  Backend-Log: tail -f $BACKEND_LOG"
echo "  Frontend-Log: tail -f $FRONTEND_LOG"
echo
echo "Strg+C beendet beide Server."

# Im Vordergrund warten -- dadurch greift der trap bei Strg+C
wait
