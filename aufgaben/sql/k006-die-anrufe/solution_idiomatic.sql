SELECT p.name, COUNT(*) AS anrufe
FROM anrufe a
JOIN personen p ON p.telefon = a.an
WHERE a.von = (SELECT telefon FROM personen WHERE name = 'Lars Pohl')
  AND a.zeit LIKE '2026-03-14%'
GROUP BY p.name
ORDER BY anrufe DESC
LIMIT 1;
