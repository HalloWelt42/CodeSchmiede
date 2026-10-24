#!/usr/bin/env bash
# Baut die Sandbox-Images aller Sprachen aus sandbox-bilder/<sprache>.Dockerfile
# als codeschmiede-sandbox:<sprache>. Idempotent; nach jeder Änderung an
# einem Sandbox-Dockerfile erneut ausführen.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BILDER_DIR="$ROOT_DIR/sandbox-bilder"

for datei in "$BILDER_DIR"/*.Dockerfile; do
  sprache="$(basename "$datei" .Dockerfile)"
  echo "Baue codeschmiede-sandbox:$sprache ..."
  docker build --quiet --tag "codeschmiede-sandbox:$sprache" --file "$datei" "$BILDER_DIR"
done

echo
docker images --filter "reference=codeschmiede-sandbox" --format '{{.Repository}}:{{.Tag}}  {{.Size}}'
