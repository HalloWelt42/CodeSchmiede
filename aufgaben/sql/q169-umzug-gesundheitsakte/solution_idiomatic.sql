INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)
VALUES (9, 'Pelle', 'West', 3.1, 2025, NULL),
       (10, 'Pippa', 'West', 3.6, 2024, 'Hering');
UPDATE pinguine SET gewicht_kg = 3.4 WHERE id = 9;
UPDATE kolonien SET wassertemperatur = -1.0 WHERE name = 'West';
DELETE FROM fuetterungen WHERE pinguin_id = 7;
DELETE FROM pinguine WHERE id = 7;
CREATE TABLE gesundheit (
  id INTEGER PRIMARY KEY,
  pinguin_id INTEGER NOT NULL REFERENCES pinguine(id),
  tag TEXT NOT NULL,
  befund TEXT NOT NULL
);
INSERT INTO gesundheit (pinguin_id, tag, befund)
VALUES (9, '2026-10-24', 'gesund'),
       (10, '2026-10-24', 'leichter Schnupfen');
