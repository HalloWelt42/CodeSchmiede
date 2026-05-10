-- Initial-Schema fuer Codeschmiede.
-- Aufgaben + Pfade als Index ueber den Aufgaben-Verzeichnisbaum.
-- Versionierung pro Aufgabe (revision) damit alte Submissions
-- reproduzierbar bleiben, wenn die Aufgabe spaeter geaendert wird.

CREATE TABLE aufgaben (
  id TEXT PRIMARY KEY,
  titel TEXT NOT NULL,
  sprache TEXT NOT NULL,
  schwierigkeit TEXT,
  schwierigkeit_score INTEGER,
  schaetz_minuten INTEGER,
  tags TEXT,                    -- JSON-Array
  pfade TEXT,                   -- JSON-Array
  voraussetzungen TEXT,         -- JSON-Array
  task_type TEXT NOT NULL,
  runner_type TEXT NOT NULL,
  aktuelle_revision INTEGER NOT NULL,
  dateipfad TEXT NOT NULL,
  hash TEXT NOT NULL            -- SHA1 fuer Watcher-Diff
);
CREATE INDEX idx_aufgaben_sprache ON aufgaben(sprache);
CREATE INDEX idx_aufgaben_schwierigkeit ON aufgaben(schwierigkeit_score);

CREATE TABLE aufgaben_versionen (
  aufgabe_id TEXT NOT NULL,
  revision INTEGER NOT NULL,
  hash TEXT NOT NULL,
  frontmatter_json TEXT NOT NULL,
  beschreibung_md TEXT NOT NULL,
  gueltig_ab DATETIME NOT NULL,
  PRIMARY KEY (aufgabe_id, revision)
);

CREATE TABLE pfade (
  id TEXT PRIMARY KEY,
  titel TEXT NOT NULL,
  beschreibung TEXT,
  reihenfolge TEXT              -- JSON-Array von aufgaben_ids
);

CREATE TABLE submissions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  aufgabe_id TEXT NOT NULL,
  aufgabe_revision INTEGER NOT NULL,
  zeitstempel DATETIME DEFAULT CURRENT_TIMESTAMP,
  code TEXT NOT NULL,
  bestanden INTEGER NOT NULL,
  laufzeit_ms REAL,
  codelaenge_zeichen INTEGER,
  FOREIGN KEY (aufgabe_id, aufgabe_revision)
    REFERENCES aufgaben_versionen(aufgabe_id, revision)
);
CREATE INDEX idx_submissions_aufgabe ON submissions(aufgabe_id, zeitstempel DESC);

CREATE TABLE progress (
  aufgabe_id TEXT PRIMARY KEY,
  status TEXT NOT NULL,         -- neu / in_arbeit / geloest
  versuche INTEGER DEFAULT 0,
  hints_genutzt INTEGER DEFAULT 0,
  geloest_am DATETIME,
  ease REAL DEFAULT 2.5,
  intervall_tage INTEGER DEFAULT 0,
  faellig_am DATE,
  letzte_wiederholung DATETIME,
  FOREIGN KEY (aufgabe_id) REFERENCES aufgaben(id)
);
CREATE INDEX idx_progress_faellig ON progress(faellig_am);

CREATE TABLE kv_state (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
