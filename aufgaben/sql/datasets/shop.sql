-- Datensatz "Online-Shop" -- Lebensmittel-Lieferdienst.

CREATE TABLE kategorien (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE produkte (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  kategorie_id INTEGER NOT NULL REFERENCES kategorien(id),
  preis REAL NOT NULL,        -- Euro
  lager INTEGER NOT NULL,     -- Stueck
  marke TEXT
);

CREATE TABLE kunden (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  ort TEXT,
  plz TEXT,
  alter_jahre INTEGER
);

CREATE TABLE bestellungen (
  id INTEGER PRIMARY KEY,
  kunde_id INTEGER NOT NULL REFERENCES kunden(id),
  bestellt_am DATE NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('offen','versandt','geliefert','storniert'))
);

CREATE TABLE bestellpositionen (
  bestellung_id INTEGER NOT NULL REFERENCES bestellungen(id),
  produkt_id INTEGER NOT NULL REFERENCES produkte(id),
  menge INTEGER NOT NULL,
  einzelpreis REAL NOT NULL,
  PRIMARY KEY (bestellung_id, produkt_id)
);

INSERT INTO kategorien (id, name) VALUES
  (1, 'Obst'),
  (2, 'Gemüse'),
  (3, 'Milchprodukte'),
  (4, 'Backwaren'),
  (5, 'Getränke'),
  (6, 'Süßwaren');

INSERT INTO produkte (id, name, kategorie_id, preis, lager, marke) VALUES
  (1,  'Apfel Boskoop',        1, 0.45,  200, 'Bio-Hof Schulz'),
  (2,  'Banane',                1, 0.30,  500, 'Tropico'),
  (3,  'Erdbeeren 500g',        1, 3.99,   80, 'Bio-Hof Schulz'),
  (4,  'Orange Navel',          1, 0.55,  150, 'Citrus Plus'),
  (5,  'Tomate Strauch',        2, 0.65,  220, 'GartenFrisch'),
  (6,  'Gurke',                 2, 1.20,  140, 'GartenFrisch'),
  (7,  'Karotte 1kg',           2, 1.49,  300, 'Bio-Hof Schulz'),
  (8,  'Brokkoli',              2, 1.99,   90, 'GartenFrisch'),
  (9,  'Vollmilch 1L',          3, 1.29,  400, 'Alpenglück'),
  (10, 'Joghurt Natur 500g',    3, 0.89,  260, 'Alpenglück'),
  (11, 'Butter 250g',           3, 2.49,  180, 'Alpenglück'),
  (12, 'Gouda Scheiben 200g',   3, 3.29,  120, 'KäseHof'),
  (13, 'Brot Roggen 500g',      4, 2.79,   50, 'Bauernbäckerei'),
  (14, 'Brötchen 5er-Pack',     4, 1.49,   80, 'Bauernbäckerei'),
  (15, 'Croissant',             4, 0.99,   60, 'Pariser Art'),
  (16, 'Mineralwasser 6x1L',    5, 4.99,  150, 'AquaPur'),
  (17, 'Apfelsaft 1L',          5, 1.89,  200, 'FruchtFest'),
  (18, 'Cola 1L',               5, 1.29,  300, 'BlubberCo'),
  (19, 'Schokolade 100g',       6, 1.99,  220, 'KakaoLuxus'),
  (20, 'Kekse 200g',            6, 2.49,  150, 'KekseRoll');

INSERT INTO kunden (id, name, ort, plz, alter_jahre) VALUES
  (1,  'Alex Becker',     'Berlin',     '10115', 31),
  (2,  'Beate Frank',     'Hamburg',    '20095', 44),
  (3,  'Carla Diaz',      'München',   '80331', 28),
  (4,  'Daniel Engel',    'Berlin',     '10247', 19),
  (5,  'Elena Vogel',     'Köln',      '50667', 56),
  (6,  'Frank Berger',    'Frankfurt',  '60311', 37),
  (7,  'Gisela Hahn',     'Hamburg',    '22041', 65),
  (8,  'Hugo Meier',      'Stuttgart',  '70173', 22),
  (9,  'Iris Schaefer',   'Berlin',     '10405', 49),
  (10, 'Jan Petersen',    'München',   '80801', 33),
  (11, 'Karin Berger',    'Leipzig',    '04109', 41),
  (12, 'Leon Wolf',       'Dresden',    '01067', 26);

INSERT INTO bestellungen (id, kunde_id, bestellt_am, status) VALUES
  (1,   1, '2025-04-01', 'geliefert'),
  (2,   1, '2025-04-15', 'versandt'),
  (3,   2, '2025-03-10', 'geliefert'),
  (4,   2, '2025-04-20', 'offen'),
  (5,   3, '2025-04-05', 'geliefert'),
  (6,   3, '2025-04-22', 'storniert'),
  (7,   4, '2025-04-12', 'geliefert'),
  (8,   5, '2025-03-25', 'geliefert'),
  (9,   5, '2025-04-18', 'geliefert'),
  (10,  6, '2025-04-08', 'versandt'),
  (11,  7, '2025-04-02', 'geliefert'),
  (12,  8, '2025-04-21', 'offen'),
  (13,  9, '2025-03-30', 'geliefert'),
  (14, 10, '2025-04-10', 'geliefert'),
  (15, 11, '2025-04-14', 'versandt'),
  (16, 12, '2025-04-19', 'offen');

INSERT INTO bestellpositionen (bestellung_id, produkt_id, menge, einzelpreis) VALUES
  (1, 1, 6, 0.45),
  (1, 9, 2, 1.29),
  (1, 13,1, 2.79),
  (2, 3, 1, 3.99),
  (2, 17,2, 1.89),
  (3, 5, 4, 0.65),
  (3, 6, 2, 1.20),
  (3, 7, 1, 1.49),
  (3, 12,1, 3.29),
  (4, 18,3, 1.29),
  (5, 2, 5, 0.30),
  (5, 19,2, 1.99),
  (5, 20,1, 2.49),
  (6, 4, 4, 0.55),
  (7, 14,2, 1.49),
  (7, 15,4, 0.99),
  (8, 11,2, 2.49),
  (8, 13,1, 2.79),
  (8, 16,1, 4.99),
  (9, 1, 4, 0.45),
  (9, 9, 1, 1.29),
  (9, 10,2, 0.89),
  (10,5, 6, 0.65),
  (10,8, 2, 1.99),
  (11,12,3, 3.29),
  (11,13,1, 2.79),
  (12,18,2, 1.29),
  (12,19,2, 1.99),
  (13,3, 2, 3.99),
  (13,7, 1, 1.49),
  (14,2, 6, 0.30),
  (14,17,1, 1.89),
  (15,16,2, 4.99),
  (15,11,1, 2.49),
  (16,8, 1, 1.99),
  (16,9, 1, 1.29);
