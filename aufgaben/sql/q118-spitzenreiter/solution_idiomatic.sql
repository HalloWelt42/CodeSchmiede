SELECT name, gewicht_kg
FROM pinguine
WHERE gewicht_kg > (SELECT AVG(gewicht_kg) FROM pinguine)
  AND id IN (SELECT pinguin_id FROM fuetterungen WHERE fisch = 'Hering');
