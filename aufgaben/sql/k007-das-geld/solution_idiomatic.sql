SELECT p.name, u.betrag, u.datum
FROM ueberweisungen u
JOIN personen p ON p.id = u.von_id
WHERE u.an_id = (SELECT id FROM personen WHERE name = 'Mira Kessler')
  AND u.datum BETWEEN '2026-03-15' AND '2026-03-21'
  AND u.betrag > 500;
