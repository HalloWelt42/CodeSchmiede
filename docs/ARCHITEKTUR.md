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
   |  fetch /api/*  (Vite-Proxy oder Nginx-Proxy, gleiche Herkunft)
   v
Backend (FastAPI :8200)                       kein Docker-Zugang
   +-- AufgabenLoader + Bestandsprüfung (liest aufgaben/, meldet Befunde)
   +-- AufgabenWatcher  (watchfiles, liest bei Änderung neu ein)
   +-- AufgabenRepository, ProgressRepository, SubmissionRepository (SQLite)
   +-- Pruefer-Registry (task_type -> Pruefer)
   +-- DienstRunner  ----HTTP + Schlüssel---->  Sandbox-Dienst (:8203)
                                                   +-- DockerRunner
                                                   +-- Docker-Socket
                                                         |
                                                         v
                                   Container codeschmiede-sandbox:<sprache>
                                   (Code über stdin, kein Netz, nur lesend,
                                    nobody, keine Capabilities)
```

## Backend-Pakete (`backend/src/codeschmiede/`)

| Modul             | Verantwortung |
|-------------------|----------------|
| `main.py`         | uvicorn-Entry, lädt Settings |
| `api.py`          | FastAPI-App, Lifespan (Watcher), Router, Herkunftsprüfung, CORS nur für erlaubte Herkünfte, healthz |
| `config.py`       | Pydantic-Settings (Pfade, Sandbox-URL und Schlüssel, Schreibrecht, Dateibeobachter, erlaubte Herkünfte) |
| `state.py`        | AppState bündelt Datenbank, Repositories, Runner; `neu_einlesen()` |
| `db/connection.py`        | SQLite-Verbindung + Migrationen (jede in einer Transaktion) |
| `db/migrations/*.sql`     | Nummerierte Schema-Migrationen |
| `models/*.py`             | Pydantic-Modelle (Aufgabe mit ID- und Funktionsprüfung, Pfad, Progress, Konfig) |
| `aufgaben/loader.py`      | Markdown + YAML -> Pydantic; kaputte Dateien landen in `ladefehler` |
| `aufgaben/bestandspruefung.py` | Befunde: Ladefehler, tote Verweise, unbekannte Sprache/Stufe/Typ |
| `aufgaben/repository.py`  | Index in SQLite, Versionen je Revision |
| `aufgaben/schreiber.py`   | Aufgaben, Musterlösungen und Pfade schreiben (nur wenn `aufgaben_schreibbar`) |
| `aufgaben/watcher.py`     | watchfiles -> `AppState.neu_einlesen()` |
| `sandbox/runner.py`       | Runner-Protocol, `SandboxFehler` |
| `sandbox/docker_runner.py`| Gehärteter Containerlauf (nur im Sandbox-Dienst) |
| `sandbox/dienst.py`       | Sandbox-Dienst (FastAPI, Schlüssel, begrenzte Parallelität) |
| `sandbox/dienst_runner.py`| Runner des Backends: HTTP zum Dienst |
| `sandbox/schluessel.py`   | Gemeinsamer Schlüssel (Umgebung oder Datei) |
| `pruefung/registry.py`    | Pruefer je Typ mit `verbirgt`, `im_browser`, `zaehle_versteckt` |
| `pruefung/orchestrator.py`| Wählt den Pruefer, liefert öffentliches `extra` und Anzahl versteckter Tests |
| `pruefung/testlauf.py`    | Ruft die Funktion in der Sandbox auf (Python, JavaScript), nur Eingaben gehen hinein |
| `pruefung/kodierung.py`   | Typgetreue Rückgaben (Tupel, Mengen, undefined ...) und Vergleich im Backend |
| `pruefung/*_pruefer.py`   | code_schreiben, bug_finden, lueckentext, output_quiz, sql_abfrage, css_klon |
| `progress/*.py`           | SM-2, Serie, Progress, Submissions |
| `routes/*.py`             | FastAPI-Router pro Domäne |

## Erweiterungs-Patterns

### Neuer Aufgabentyp

1. Pruefer-Modul anlegen, z.B. `pruefung/muster_jagd_pruefer.py`:
   ```python
   from .registry import registriere

   @registriere("muster_jagd", verbirgt=("loesung",))
   def pruefe(aufgabe, antwort, runner):
       ...
   ```
   `verbirgt` nennt Felder des `extra`-Blocks, die nie an den Browser
   gehen. `im_browser=True` nur, wenn ausschließlich ein Browser prüfen
   kann (wie CSS-Nachbauten).
2. In `pruefung/orchestrator.py` den Import ergänzen.
3. Typ in `aufgaben/_konfig.yml` eintragen; die Bestandsprüfung meldet
   Aufgaben mit unbekanntem Typ.

### Neue Sprache in der Sandbox

1. `sandbox-bilder/<sprache>.Dockerfile` anlegen und mit
   `scripts/build-sandbox.sh` bauen.
2. In `sandbox/docker_runner.py:SPRACHBEFEHLE` eintragen, wie die Sprache
   ihr Programm von stdin liest; das Image steht in den Einstellungen
   des Dienstes (`bilder`).
3. In `pruefung/testlauf.py:LAEUFE` einen Testlauf für die Sprache
   ergänzen (Rückgaben mit Typmarken, siehe `kodierung.py`).
4. Sprache in `_konfig.yml` (mit `endung` und `runner_type`) und das
   CodeMirror-Sprach-Plugin in `EditorFactory.ts`.

## Frontend-Schichten (`frontend/src/`)

| Verzeichnis              | Inhalt |
|--------------------------|--------|
| `App.svelte`             | Root-Layout, Routing-Switch |
| `lib/components/`        | Eine Komponente pro Datei; Musterlösungen (`MusterloesungenBereich`) und Verlauf (`VerlaufBereich`) gemeinsam für alle Aufgabentypen |
| `lib/api/`               | HTTP-Wrapper + eine Klasse pro Domäne; Fehlertext kommt aus `detail` des Servers |
| `lib/stores/`            | Svelte 5 Runes (`*.svelte.ts`) |
| `lib/markdown/`          | MarkdownRenderer (marked + KaTeX + Mermaid strikt + DOMPurify) |
| `lib/editor/`            | CodeMirror-Setup + Petrol-Theme |
| `lib/sandbox/`           | `IframeCssRunner` für CSS-Nachbauten (einziger Lauf im Browser) |
| `lib/types/`             | TS-Interfaces, gespiegelt zu Pydantic |
| `styles/`                | CSS-Variablen + Font-Imports |

## Datenbank

SQLite, Datei `data/codeschmiede.db` (gitignored).

| Tabelle              | Inhalt |
|----------------------|--------|
| `aufgaben`           | Index aller geladenen Aufgaben (UPSERT bei Reindex) |
| `aufgaben_versionen` | Frontmatter+Beschreibung je `(aufgabe_id, revision)`, **unveränderlich** |
| `pfade`              | Lernpfade |
| `submissions`        | Jede Einreichung mit Metriken, FK zu `aufgaben_versionen` |
| `progress`           | Pro Aufgabe: Status, Versuche, Punkte, aufgegeben, SM-2-Felder |
| `kv_state`           | Einzelwerte (Serie) |
| `schema_version`     | Angewandte Migrationen |

Migrationen laufen beim Start in `db/connection.py:Datenbank.migriere()`,
jede samt Versionszeile in einer Transaktion. Neue Migration:
`db/migrations/00N_xxx.sql`, Backend neu starten.

## Sicherheit

**Sandbox.** Nur der Sandbox-Dienst sieht den Docker-Socket. Er nimmt
Läufe nur mit dem gemeinsamen Schlüssel an, kennt nur die eingetragenen
Images und hält höchstens `max_parallel` Läufe gleichzeitig. Je Lauf
(`sandbox/docker_runner.py:_befehl_bauen`):

- `--network=none`, `--read-only`, tmpfs `/tmp` (16 MB, nosuid, nodev)
- `--cap-drop=ALL`, `--security-opt=no-new-privileges`, Nutzer `65534:65534`
- `--memory` gleich `--memory-swap`, `--cpus`, `--pids-limit=64`, `nofile=64`
- Code über stdin, kein Mount
- Laufzeit über `timeout` im Container; hängt der Container länger als
  Laufzeit plus Startreserve, beendet der Dienst ihn über seinen Namen
- Ausgabe höchstens `max_ausgabe_bytes`, darüber Abbruch

SQL-Aufgaben laufen ebenfalls in der Sandbox (SQLite im Speicher),
`ATTACH` und `DETACH` sind verboten.

**Browser.** CORS nur für `erlaubte_herkuenfte` (Vorgabe: keine).
Ändernde Anfragen aus fremder Herkunft (`Sec-Fetch-Site`, sonst `Origin`
gegen Host) weist die API ab. Mermaid rendert mit `securityLevel: strict`,
Markdown geht durch DOMPurify.

**Aufgabendateien.** IDs sind ASCII nach `AUFGABEN_ID_MUSTER`, auch beim
Löschen geprüft; Funktionsnamen müssen gültige Bezeichner sein. Mit
`aufgaben_schreibbar=false` (Compose, Pi) schreibt die API nichts.

## Lösungsschutz

- Versteckte Tests: In die Sandbox gehen nur Eingaben. Die Rückgaben
  kommen typgetreu kodiert zurück und werden im Backend verglichen. Ein
  manipuliertes `__eq__`, eine gefälschte Ergebniszeile oder das Lesen
  des eigenen Prozesses bringt nichts, die Erwartungen sind nie dort.
  Ans Frontend gehen nur Anzahlen.
- Musterlösungen gibt es erst nach dem Bestehen oder nach dem Aufgeben
  (`POST /api/aufgaben/{id}/aufgeben`); danach bringt ein Bestehen keine
  Punkte mehr.
- Quiz: `richtig_index` geht nie an den Browser.
- SQL: Die Zieltabelle ist der sichtbare Test. Gegen eingetippte Werte
  laufen Abfrage und Musterlösung zusätzlich auf zwei ausgedünnten
  Fassungen des Datensatzes (versteckte Tests).
- CSS-Nachbauten prüft der Browser (`im_browser`); Ziel und Stile sind
  dort von Natur aus sichtbar.

## Tests

`backend/tests/` mit eigenem Aufgabenbestand im Temp-Ordner und eigener
Datenbank; `data/` wird nie berührt. Sandbox-Tests laufen gegen die
echten Images. `CODESCHMIEDE_BESTAND=1` prüft zusätzlich den ganzen
echten Bestand (keine Befunde, jede Musterlösung besteht).

## Versionierung

Single Source of Truth: `VERSION` im Repo-Wurzel. Backend liest sie in
`__init__.py` mit Fallback auf `/app/VERSION` (Docker) und `/VERSION`.
Frontend liest sie in `vite.config.ts` aus `../VERSION` (Dev) oder
`./VERSION` (Docker-Build-Context). `scripts/bump.sh` aktualisiert sie.
