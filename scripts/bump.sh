#!/usr/bin/env bash
# Versionierung. patch (default) erhoeht +0.0.1, minor +0.1.0, major +1.0.0.
#
# Verwendung:
#   ./scripts/bump.sh             # patch
#   ./scripts/bump.sh patch
#   ./scripts/bump.sh minor
#   ./scripts/bump.sh major

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
VERSION_DATEI="$ROOT_DIR/VERSION"

aktuell=$(tr -d '[:space:]' < "$VERSION_DATEI")
IFS='.' read -r major minor patch <<< "$aktuell"

modus="${1:-patch}"
case "$modus" in
  patch) patch=$((patch + 1)) ;;
  minor) minor=$((minor + 1)); patch=0 ;;
  major) major=$((major + 1)); minor=0; patch=0 ;;
  *) echo "Modus muss patch | minor | major sein, nicht '$modus'"; exit 1 ;;
esac

neu="${major}.${minor}.${patch}"
echo "$neu" > "$VERSION_DATEI"
echo "$aktuell -> $neu"
