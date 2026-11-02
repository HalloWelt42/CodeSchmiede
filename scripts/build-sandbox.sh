#!/usr/bin/env bash
# Baut die Sandbox-Images aller Sprachen aus sandbox-bilder/<sprache>.Dockerfile
# als codeschmiede-sandbox:<sprache>, PHP je Fassung als codeschmiede-sandbox:php-<fassung>. Idempotent; nach jeder Änderung an
# einem Sandbox-Dockerfile erneut ausführen.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BILDER_DIR="$ROOT_DIR/sandbox-bilder"

for datei in "$BILDER_DIR"/*.Dockerfile; do
  sprache="$(basename "$datei" .Dockerfile)"
  [ "$sprache" = php ] && continue        # PHP je Fassung, siehe unten
  echo "Baue codeschmiede-sandbox:$sprache ..."
  docker build --quiet --tag "codeschmiede-sandbox:$sprache" --file "$datei" "$BILDER_DIR"
done

# PHP: je Fassung ein Abbild codeschmiede-sandbox:php-<fassung>; die Fassungen stehen nur in sandbox/laufzeiten.py
for fassung in $("$ROOT_DIR/backend/.venv/bin/python" -c "from codeschmiede.sandbox.laufzeiten import PHP_FASSUNGEN; print(*PHP_FASSUNGEN)"); do
  echo "Baue codeschmiede-sandbox:php-$fassung ..."
  docker build --quiet --build-arg "PHP_FASSUNG=$fassung" --tag "codeschmiede-sandbox:php-$fassung" \
    --file "$BILDER_DIR/php.Dockerfile" "$BILDER_DIR"
done

echo
docker images --filter "reference=codeschmiede-sandbox" --format '{{.Repository}}:{{.Tag}}  {{.Size}}'
