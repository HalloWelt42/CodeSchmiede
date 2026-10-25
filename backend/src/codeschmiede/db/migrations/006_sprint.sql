-- Runden des Ausgabe-Sprints (spiel/sprint.py). Eine Runde hält fest,
-- welche Schnipsel in welcher Antwortreihenfolge gefragt wurden und was
-- gewählt wurde; abgeschlossene Runden werden als Abgabe verbucht.
-- Unvollendete Runden räumt der nächste Rundenstart nach einem Tag ab.

CREATE TABLE sprint_runden (
  id TEXT PRIMARY KEY,
  aufgabe_id TEXT NOT NULL,
  aufgabe_revision INTEGER NOT NULL,
  fragen TEXT NOT NULL,        -- JSON: [{schnipsel, reihenfolge}]
  antworten TEXT NOT NULL,     -- JSON: gewählte Stelle je Frage, null = offen
  gestartet DATETIME NOT NULL,
  frist DATETIME NOT NULL,
  abgeschlossen INTEGER NOT NULL DEFAULT 0
);
