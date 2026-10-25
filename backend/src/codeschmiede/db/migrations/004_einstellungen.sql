-- Einstellungen der App, die zur Laufzeit gesetzt werden (Zugang zur
-- Kellerwolke aus der Einrichtung). Ein Wert je Schlüssel, als JSON-Text.

CREATE TABLE IF NOT EXISTS einstellungen (
    schluessel TEXT PRIMARY KEY,
    wert TEXT NOT NULL
);
