-- Datensatz "Bibliothek" -- Schule, Buecher, Leser, Ausleihen.
-- Wird pro SQL-Submission frisch in eine In-Memory-SQLite geladen.

CREATE TABLE autoren (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  geburtsjahr INTEGER,
  land TEXT
);

CREATE TABLE buecher (
  id INTEGER PRIMARY KEY,
  titel TEXT NOT NULL,
  autor_id INTEGER NOT NULL REFERENCES autoren(id),
  jahr INTEGER,
  seiten INTEGER,
  kategorie TEXT,
  exemplare INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE leser (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  ort TEXT,
  alter_jahre INTEGER,
  mitglied_seit DATE
);

CREATE TABLE ausleihen (
  id INTEGER PRIMARY KEY,
  leser_id INTEGER NOT NULL REFERENCES leser(id),
  buch_id INTEGER NOT NULL REFERENCES buecher(id),
  ausgeliehen_am DATE NOT NULL,
  zurueck_am DATE
);

INSERT INTO autoren (id, name, geburtsjahr, land) VALUES
  (1, 'Hermann Hesse',   1877, 'Deutschland'),
  (2, 'Stefan Zweig',    1881, 'Österreich'),
  (3, 'Franz Kafka',     1883, 'Tschechien'),
  (4, 'Thomas Mann',     1875, 'Deutschland'),
  (5, 'Astrid Lindgren', 1907, 'Schweden'),
  (6, 'George Orwell',   1903, 'Großbritannien'),
  (7, 'Jane Austen',     1775, 'Großbritannien'),
  (8, 'Haruki Murakami', 1949, 'Japan'),
  (9, 'Cornelia Funke',  1958, 'Deutschland'),
  (10,'Ursula K. Le Guin', 1929,'USA');

INSERT INTO buecher (id, titel, autor_id, jahr, seiten, kategorie, exemplare) VALUES
  (1,  'Siddhartha',                1, 1922, 153, 'Roman',          3),
  (2,  'Der Steppenwolf',           1, 1927, 288, 'Roman',          2),
  (3,  'Schachnovelle',             2, 1942,  96, 'Erzählung',     4),
  (4,  'Die Welt von Gestern',      2, 1942, 528, 'Biographie',     1),
  (5,  'Die Verwandlung',           3, 1915,  74, 'Erzählung',     5),
  (6,  'Der Process',               3, 1925, 312, 'Roman',          2),
  (7,  'Buddenbrooks',              4, 1901, 759, 'Roman',          1),
  (8,  'Der Zauberberg',            4, 1924, 992, 'Roman',          1),
  (9,  'Pippi Langstrumpf',         5, 1945, 168, 'Kinderbuch',     6),
  (10, 'Karlsson vom Dach',         5, 1955, 124, 'Kinderbuch',     4),
  (11, '1984',                      6, 1949, 326, 'Roman',          5),
  (12, 'Farm der Tiere',            6, 1945, 112, 'Roman',          4),
  (13, 'Stolz und Vorurteil',       7, 1813, 432, 'Roman',          2),
  (14, 'Emma',                      7, 1815, 474, 'Roman',          1),
  (15, 'Naokos Laecheln',           8, 1987, 296, 'Roman',          2),
  (16, 'Kafka am Strand',           8, 2002, 624, 'Roman',          3),
  (17, 'Tintenherz',                9, 2003, 576, 'Kinderbuch',     5),
  (18, 'Drachenreiter',             9, 1997, 432, 'Kinderbuch',     4),
  (19, 'Erdsee',                   10, 1968, 224, 'Fantasy',        2),
  (20, 'Die linke Hand der Dunkelheit', 10, 1969, 304, 'Sci-Fi',    2);

INSERT INTO leser (id, name, ort, alter_jahre, mitglied_seit) VALUES
  (1,  'Anna Schmidt',     'Berlin',     34, '2018-03-15'),
  (2,  'Bernd Mueller',    'Hamburg',    42, '2015-07-01'),
  (3,  'Clara Weber',      'München',   28, '2020-01-20'),
  (4,  'David Fischer',    'Berlin',     19, '2022-09-10'),
  (5,  'Eva Schulz',       'Köln',      56, '2010-05-04'),
  (6,  'Felix Bauer',      'Frankfurt',  37, '2017-11-30'),
  (7,  'Greta Hoffmann',   'Hamburg',    25, '2021-06-12'),
  (8,  'Hans Wagner',      'Stuttgart',  61, '2008-02-22'),
  (9,  'Ines Becker',      'Berlin',     45, '2014-04-18'),
  (10, 'Jonas Schaefer',   'München',   30, '2019-08-25'),
  (11, 'Karin Koehler',    'Leipzig',    52, '2012-10-09'),
  (12, 'Lukas Richter',    'Dresden',    22, '2023-01-11'),
  (13, 'Maria Klein',      'Hamburg',    39, '2016-03-03'),
  (14, 'Niklas Wolf',      'Berlin',     27, '2020-12-07'),
  (15, 'Olivia Krueger',   'München',   33, '2018-06-20');

INSERT INTO ausleihen (id, leser_id, buch_id, ausgeliehen_am, zurueck_am) VALUES
  (1,   1,  1, '2025-01-05', '2025-01-19'),
  (2,   1, 11, '2025-02-12', '2025-03-02'),
  (3,   2,  7, '2025-01-10', '2025-02-04'),
  (4,   2,  8, '2025-03-01', NULL),
  (5,   3,  9, '2025-02-20', '2025-03-04'),
  (6,   3, 10, '2025-03-15', '2025-03-22'),
  (7,   3, 17, '2025-04-01', NULL),
  (8,   4, 11, '2025-01-22', '2025-02-15'),
  (9,   5,  3, '2024-12-10', '2024-12-24'),
  (10,  5,  4, '2025-01-15', '2025-02-12'),
  (11,  5, 13, '2025-03-10', '2025-04-05'),
  (12,  6, 16, '2025-02-08', '2025-03-08'),
  (13,  7,  9, '2025-04-12', NULL),
  (14,  7, 18, '2025-04-12', NULL),
  (15,  8,  6, '2024-11-05', '2024-12-01'),
  (16,  8,  2, '2025-02-01', '2025-02-28'),
  (17,  9,  1, '2025-03-22', '2025-04-10'),
  (18,  9, 14, '2025-04-15', NULL),
  (19, 10, 19, '2025-01-30', '2025-02-20'),
  (20, 10, 20, '2025-03-01', '2025-03-25'),
  (21, 11, 11, '2025-02-10', '2025-03-05'),
  (22, 12,  5, '2025-03-20', '2025-04-01'),
  (23, 12, 12, '2025-04-05', NULL),
  (24, 13, 15, '2025-01-18', '2025-02-10'),
  (25, 13, 16, '2025-03-12', '2025-04-08'),
  (26, 14,  6, '2025-04-01', NULL),
  (27, 15,  8, '2025-02-25', NULL);
