# Architektur-Notizen

Kurzer Lagebericht über die wichtigsten Bausteine, mit Fokus auf
Erweiterungspunkte. Wer hier etwas Neues hinzufügen will, findet die
relevanten Dateien direkt benannt.

## Hochlevel-Sicht

```
Browser
   |
   v
Frontend (Vite-Dev :5184  oder  Nginx :8201 in Compose)
   |  fetch /api/*  (Vite-Proxy oder Nginx-Proxy)
   v
Backend (FastAPI :8200, uvicorn)
   +-- Aufgaben-Loader  (liest aufgaben/*/*.md)
   +-- AufgabenWatcher  (watchfiles, triggert Reindex)
   +-- AufgabenRepository (SQLite-Index, UPSERT)
   +-- ProgressRepository (SM-2, Streak, Aggregate)
   +-- Pruefer-Registry  (task_type -> Pruefer-Funktion)
   +-- Runner  (DockerRunner -> spawnt python:3.11-slim Container)
   +-- SQLite (data/codeschmiede.db)

Sandbox-Container (codeschmiede-sandbox:python)
   - --network=none
   - --read-only mit tmpfs auf /tmp
   - Memory 128m, CPU 0.5, pids-limit 64
```

## Backend-Pakete (`backend/src/codeschmiede/`)

| Modul             | Verantwortung |
|-------------------|----------------|
| `main.py`         | uvicorn-Entry, lädt Settings |
| `api.py`          | FastAPI-App, Lifespan (startet Watcher), Router-Mount, CORS, healthz |
| `config.py`       | Pydantic-Settings (Pfade, Sandbox-Image, Port) |
| `state.py`        | AppState bündelt Datenbank, Repositories, Runner |
| `db/connection.py`        | SQLite-Connection-Manager + Migrations-Loader |
| `db/migrations/*.sql`     | Nummerierte Schema-Migrationen |
| `models/*.py`             | Pydantic-Modelle (Aufgabe, Pfad, Submission, Progress) |
| `aufgaben/loader.py`      | Markdown + YAML -> Pydantic |
| `aufgaben/repository.py`  | UPSERT-Index in SQLite, FK-bewusst |
| `aufgaben/watcher.py`     | watchfiles -> Repository.neu_aufbauen |
| `sandbox/runner.py`       | Runner-Protocol |
| `sandbox/docker_runner.py`| DockerRunner (subprocess `docker run --rm`) |
| `sandbox/result.py`       | RunResult, RunLimits |
| `pruefung/registry.py`    | PRUEFER_REGISTRY + `@registriere`-Decorator |
| `pruefung/yaml_pruefer.py`| Pruefer für `task_type=code_schreiben` |
| `pruefung/orchestrator.py`| Wählt Pruefer nach `task_type` |
| `progress/sm2.py`         | SM-2 Algorithmus |
| `progress/streak.py`      | Tagesserie |
| `progress/repository.py`  | ProgressRepository (SQLite) |
| `routes/*.py`             | FastAPI-Router pro Domäne |

## Erweiterungs-Patterns

### Neuer Aufgabentyp (z.B. `output_quiz`)

1. Pruefer-Modul anlegen, z.B. `pruefung/output_quiz_pruefer.py`:
   ```python
   from .registry import registriere
   from .ergebnis import PruefErgebnis
   from ..models.aufgabe import Aufgabe
   from ..sandbox.runner import Runner

   @registriere("output_quiz")
   def pruefe(aufgabe: Aufgabe, antwort: str, runner: Runner) -> PruefErgebnis:
       ...
   ```
2. In `pruefung/orchestrator.py` einen Import ergänzen, damit die
   Registry zur Startzeit befüllt ist:
   ```python
   from . import output_quiz_pruefer  # noqa: F401
   ```
3. Aufgaben mit `task_type: output_quiz` im Frontmatter funktionieren
   automatisch.

### Neue Sprache / neuer Runner (z.B. JavaScript via Web-Worker)

1. Neuen Runner anlegen, z.B. `sandbox/webworker_runner.py` (Backend
   speichert in dem Fall nur das Ergebnis -- der eigentliche Code-Run
   passiert im Browser).
2. Aufgaben mit `runner_type: webworker_js` markieren.
3. Frontend braucht eine Worker-Implementierung in
   `frontend/src/lib/runner/` und im Submit-Flow einen Switch nach
   `runner_type`.

### Neue Sprache (Backend-Side, z.B. Ruby)

1. Sandbox-Dockerfile pro Sprache (`aufgaben/sandbox/Dockerfile.ruby`).
2. `DockerRunner` parametrisierbar machen (Image-Name aus `runner_type`
   ableiten) oder einen `RubyDockerRunner` ergänzen.
3. CodeMirror-Sprach-Plugin in `EditorFactory.ts` hinzufügen.

## Frontend-Schichten (`frontend/src/`)

| Verzeichnis              | Inhalt |
|--------------------------|--------|
| `App.svelte`             | Root-Layout, Routing-Switch |
| `lib/components/`        | Eine Komponente pro Datei |
| `lib/api/`               | HTTP-Wrapper + eine Klasse pro Domäne |
| `lib/stores/`            | Svelte 5 Runes (`*.svelte.ts`) |
| `lib/markdown/`          | MarkdownRenderer (marked + KaTeX + Mermaid + DOMPurify) |
| `lib/editor/`            | CodeMirror-Setup + Petrol-Theme |
| `lib/routing/`           | -- (aktuell direkt in `RouteStore.svelte.ts`) |
| `lib/types/`             | TS-Interfaces, gespiegelt zu Pydantic |
| `styles/`                | CSS-Variablen + Font-Imports |

## Datenbank

SQLite, Datei `data/codeschmiede.db` (gitignored).

| Tabelle              | Inhalt |
|----------------------|--------|
| `aufgaben`           | Index aller geladenen Aufgaben (UPSERT bei Reindex) |
| `aufgaben_versionen` | Frontmatter+Beschreibung je `(aufgabe_id, revision)`, **unveränderlich** |
| `pfade`              | Lernpfade |
| `submissions`        | Jede Code-Einreichung mit Metriken, FK zu `aufgaben_versionen` |
| `progress`           | Pro Aufgabe: Status, Versuche, SM-2-Felder, fällig_am |
| `kv_state`           | Singleton-Werte (Streak) |
| `schema_version`     | Letzte angewandte Migration |

Migrations laufen in `db/connection.py:Datenbank.migriere()` beim
Backend-Start. Neue Migration hinzufügen: `db/migrations/00N_xxx.sql`,
Backend neu starten.

## Sandbox-Sicherheit

Aufgaben-Code läuft im Container `codeschmiede-sandbox:python`
(siehe `aufgaben/sandbox/Dockerfile`). Limits werden in
`sandbox/docker_runner.py:DockerRunner._befehl_bauen` gesetzt:

- `--network=none` -- keine ausgehenden Verbindungen
- `--read-only` + tmpfs auf `/tmp` -- Schreibzugriff nur auf 16 MB
  vergänglichen Speicher
- `--memory=128m`, `--cpus=0.5`
- `--pids-limit=64`, `--ulimit nofile=64`
- Code-Verzeichnis als read-only Bind-Mount unter `/sandbox/code`
- Default-Timeout 5 s (per Aufgabe konfigurierbar)
- Non-root User `sandbox` im Container

Verifiziert in den Spike-Tests: Network-Zugriff schlägt fehl, Schreiben
außerhalb von `/tmp` schlägt fehl, /tmp ist beschreibbar, Endlosschleife
wird per Timeout abgebrochen.

## Anti-Hardcoding

Sichtbare Tests stehen im Frontmatter unter `tests_sichtbar` und werden
dem Nutzer angezeigt. Versteckte Tests stehen unter `tests_versteckt`,
werden serverseitig ausgeführt und nur als Pass/Fail-Anzahl ans
Frontend gemeldet (nie die Eingaben oder erwarteten Werte). Der
YAML-Pruefer kombiniert beide für den Container-Lauf.

## Versionierung

Single Source of Truth: `VERSION` im Repo-Wurzel. Backend liest sie in
`__init__.py` mit Fallback auf `/app/VERSION` (Docker) und `/VERSION`.
Frontend liest sie in `vite.config.ts` aus `../VERSION` (Dev) oder
`./VERSION` (Docker-Build-Context). `scripts/bump.sh` aktualisiert sie.
