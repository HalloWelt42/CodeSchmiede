SELECT z.raum_nr, z.zeit
FROM zutritte z
WHERE z.person_id = (SELECT id FROM personen WHERE name = 'Holger Brandt')
  AND z.zeit > '2026-03-14 21:47'
ORDER BY z.zeit
LIMIT 1;
