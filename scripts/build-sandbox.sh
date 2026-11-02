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
# (mit der passenden Fassung von Xdebug für den Debugger)
"$ROOT_DIR/backend/.venv/bin/python" -c "from codeschmiede.sandbox.laufzeiten import PHP_FASSUNGEN, xdebug; print(*(f'{f}:{xdebug(f)}' for f in PHP_FASSUNGEN))" \
  | tr ' ' '\n' | while IFS=: read -r fassung xdebug; do
  echo "Baue codeschmiede-sandbox:php-$fassung (Xdebug $xdebug) ..."
  docker build --quiet --build-arg "PHP_FASSUNG=$fassung" --build-arg "XDEBUG=$xdebug" --tag "codeschmiede-sandbox:php-$fassung" \
    --file "$BILDER_DIR/php.Dockerfile" "$BILDER_DIR"
done

echo
docker images --filter "reference=codeschmiede-sandbox" --format '{{.Repository}}:{{.Tag}}  {{.Size}}'
