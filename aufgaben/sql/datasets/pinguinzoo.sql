-- Datensatz "Pinguinzoo": Datensatz des SQL-Kurses. Klein genug, dass jede Zwischentabelle auf den Bildschirm passt.

CREATE TABLE kolonien (
  name TEXT PRIMARY KEY,
  lage TEXT NOT NULL,
  wassertemperatur REAL NOT NULL     -- Grad Celsius
);

CREATE TABLE pinguine (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  kolonie TEXT NOT NULL REFERENCES kolonien(name),
  gewicht_kg REAL NOT NULL,
  geburtsjahr INTEGER NOT NULL,
  lieblingsfisch TEXT                -- NULL: noch nicht herausgefunden
);

CREATE TABLE pfleger (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  kolonie TEXT REFERENCES kolonien(name)   -- NULL: springt überall ein
);

CREATE TABLE fuetterungen (
  id INTEGER PRIMARY KEY,
  pinguin_id INTEGER NOT NULL REFERENCES pinguine(id),
  tag TEXT NOT NULL,                 -- JJJJ-MM-TT
  fisch TEXT NOT NULL,
  menge INTEGER NOT NULL             -- Stück
);

INSERT INTO kolonien (name, lage, wassertemperatur) VALUES
  ('Nord', 'Packeis', -1.5),
  ('Süd', 'Felsenküste', 4.0),
  ('Ost', 'Sandstrand', 9.5),
  ('West', 'Eishöhle', -0.5);

INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch) VALUES
  (1, 'Pit', 'Nord', 4.2, 2019, 'Hering'),
  (2, 'Pia', 'Süd', 3.8, 2020, 'Lachs'),
  (3, 'Paul', 'Nord', 5.1, 2017, 'Hering'),
  (4, 'Pina', 'Nord', 3.5, 2022, NULL),
  (5, 'Pepe', 'Süd', 4.9, 2018, 'Makrele'),
  (6, 'Polly', 'Nord', 4.6, 2019, 'Lachs'),
  (7, 'Pablo', 'Ost', 4.0, 2021, 'Hering'),
  (8, 'Pünktchen', 'Ost', 2.9, 2023, NULL);

INSERT INTO pfleger (id, name, kolonie) VALUES
  (1, 'Greta', 'Nord'),
  (2, 'Hannes', 'Süd'),
  (3, 'Ida', 'Ost'),
  (4, 'Jonas', NULL);

INSERT INTO fuetterungen (id, pinguin_id, tag, fisch, menge) VALUES
  (1, 1, '2026-10-20', 'Hering', 6),
  (2, 2, '2026-10-20', 'Lachs', 4),
  (3, 3, '2026-10-20', 'Hering', 8),
  (4, 5, '2026-10-20', 'Makrele', 5),
  (5, 1, '2026-10-21', 'Hering', 5),
  (6, 4, '2026-10-21', 'Sardine', 3),
  (7, 6, '2026-10-21', 'Lachs', 6),
  (8, 7, '2026-10-21', 'Hering', 4),
  (9, 3, '2026-10-22', 'Makrele', 7),
  (10, 8, '2026-10-22', 'Sardine', 2),
  (11, 2, '2026-10-22', 'Lachs', 5),
  (12, 1, '2026-10-22', 'Sardine', 3);
