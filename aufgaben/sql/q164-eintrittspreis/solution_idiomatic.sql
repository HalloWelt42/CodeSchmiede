CREATE TABLE eintritt (
  id INTEGER PRIMARY KEY,
  besucher TEXT NOT NULL,
  preis REAL NOT NULL DEFAULT 12.5
);

INSERT INTO eintritt (besucher) VALUES ('Mia');
