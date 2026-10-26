SELECT name
FROM pinguine
WHERE id NOT IN (SELECT pinguin_id FROM fuetterungen WHERE fisch = 'Hering');
