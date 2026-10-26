DELETE FROM fuetterungen
WHERE pinguin_id IN (SELECT id FROM pinguine WHERE name = 'Pepe');

DELETE FROM pinguine
WHERE name = 'Pepe';
