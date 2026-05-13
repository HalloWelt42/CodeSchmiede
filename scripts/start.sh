#!/usr/bin/env bash
# Startet Backend + Frontend im Hintergrund. Beide Prozesse werden
# vom Terminal abgehaengt (nohup + disown), die PIDs landen in
# data/codeschmiede.pids -- so kann scripts/stop.sh sie gezielt
# beenden, ohne dass sie an die Session gebunden sind.
#
# Voraussetzung: ./scripts/setup.sh wurde einmal ausgefuehrt.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
BACKEND_PORT=8200
FRONTEND_PORT=5184

LOG_DIR="$ROOT_DIR/data"
mkdir -p "$LOG_DIR"
BACKEND_LOG="$LOG_DIR/backend.log"
FRONTEND_LOG="$LOG_DIR/frontend.log"
PID_FILE="$LOG_DIR/codeschmiede.pids"

# Smoke-Test
if [ ! -x "$BACKEND_DIR/.venv/bin/python" ]; then
  echo "Backend-venv fehlt. Bitte zuerst $SCRIPT_DIR/setup.sh ausfuehren."
  exit 1
fi
if [ ! -d "$FRONTEND_DIR/node_modules" ]; then
  echo "Frontend-node_modules fehlt. Bitte zuerst $SCRIPT_DIR/setup.sh ausfuehren."
  exit 1
fi

# Wenn PID-Datei existiert: pruefen ob die Prozesse noch laufen
if [ -f "$PID_FILE" ]; then
  while IFS=' ' read -r name pid; do
    if [ -n "${pid:-}" ] && kill -0 "$pid" 2>/dev/null; then
      echo "$name laeuft bereits (PID $pid). Mit scripts/stop.sh zuerst beenden."
      exit 1
    fi
  done < "$PID_FILE"
fi

# Pruefen ob ein Server bereits den Port haelt. Nur LISTEN-Sockets
# zaehlen -- ESTABLISHED-Connections (z.B. alte Browser-Sessions zu
# anderen Hosts auf demselben Port) sind irrelevant.
pruefe_server_port() {
  local port=$1
  local pid
  pid=$(lsof -nP -iTCP:"$port" -sTCP:LISTEN -t 2>/dev/null | head -n1 || true)
  if [ -n "$pid" ]; then
    echo "Port $port haengt schon an einem Server-Prozess (PID $pid) -- erst beenden, dann neu starten."
    exit 1
  fi
}
pruefe_server_port "$BACKEND_PORT"
pruefe_server_port "$FRONTEND_PORT"

echo "Starte Backend (Port $BACKEND_PORT) ..."
cd "$BACKEND_DIR"
nohup .venv/bin/python -m codeschmiede.main > "$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!
disown "$BACKEND_PID" 2>/dev/null || true
echo "  PID $BACKEND_PID, Log: $BACKEND_LOG"

echo "Starte Frontend (Port $FRONTEND_PORT) ..."
cd "$FRONTEND_DIR"
nohup npm run dev -- --port "$FRONTEND_PORT" --strictPort > "$FRONTEND_LOG" 2>&1 &
FRONTEND_PID=$!
disown "$FRONTEND_PID" 2>/dev/null || true
echo "  PID $FRONTEND_PID, Log: $FRONTEND_LOG"

# PIDs persistieren
{
  echo "backend $BACKEND_PID"
  echo "frontend $FRONTEND_PID"
} > "$PID_FILE"

# Health-Check abwarten
echo
echo "Warte auf Backend ..."
for i in {1..20}; do
  if curl -sf "http://localhost:$BACKEND_PORT/api/healthz" > /dev/null 2>&1; then
    echo "  Backend antwortet."
    break
  fi
  if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
    echo "  Backend-Prozess (PID $BACKEND_PID) ist gestorben -- siehe $BACKEND_LOG"
    exit 1
  fi
  sleep 1
done

echo "Warte auf Frontend ..."
for i in {1..20}; do
  if curl -sf "http://localhost:$FRONTEND_PORT/" > /dev/null 2>&1; then
    echo "  Frontend antwortet."
    break
  fi
  if ! kill -0 "$FRONTEND_PID" 2>/dev/null; then
    echo "  Frontend-Prozess (PID $FRONTEND_PID) ist gestorben -- siehe $FRONTEND_LOG"
    exit 1
  fi
  sleep 1
done

echo
echo "=== Codeschmiede laeuft ==="
echo "  Browser:     http://localhost:$FRONTEND_PORT"
echo "  Backend-API: http://localhost:$BACKEND_PORT/api/healthz"
echo "  PIDs:        $PID_FILE"
echo "  Beenden:     $SCRIPT_DIR/stop.sh"
echo
echo "Beide Server laufen jetzt im Hintergrund. Du kannst dieses Terminal"
echo "schliessen oder den Mac in den Ruhezustand schicken -- die App"
echo "laeuft weiter, bis du sie aktiv ueber stop.sh beendest."
