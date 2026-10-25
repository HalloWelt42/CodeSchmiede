-- Spielmechanik (docs/SPIELE.md).
--
-- Jede Abgabe hält fest, was sie über das Bestehen hinaus erreicht hat;
-- Serie, Tagesauftrag, Bestwerte und Erfolge leiten sich daraus ab.
-- `ohne_hilfe`: kein Hinweis geöffnet und nicht aufgegeben (NULL bei
-- Abgaben von vor dieser Migration). `sterne`: 0 bis 3, NULL bei
-- Aufgabentypen ohne Sterne. `kennwerte`: JSON der Kennwerte des Prüfers
-- (Deckung, Schritte, Treffer ...).

ALTER TABLE submissions ADD COLUMN ohne_hilfe INTEGER;
ALTER TABLE submissions ADD COLUMN sterne INTEGER;
ALTER TABLE submissions ADD COLUMN kennwerte TEXT;

-- beste Sterne je Aufgabe, gehören wie die Punkte zum besten Versuch
ALTER TABLE progress ADD COLUMN sterne INTEGER;

-- Gutschrift eines ganz erledigten Tagesauftrags. Gespeichert statt
-- abgeleitet, damit spätere Änderungen an den Zielen alte Tage nicht
-- umbewerten: verdiente Punkte bleiben verdient.
CREATE TABLE tagesauftraege (
  datum DATE PRIMARY KEY,
  punkte INTEGER NOT NULL,
  erledigt_am DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- die Serie wird aus den bestandenen Abgaben abgeleitet
DELETE FROM kv_state WHERE key LIKE 'streak.%';
