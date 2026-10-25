SELECT a.zeit
FROM aussagen a
JOIN personen p ON p.id = a.person_id
WHERE p.name = 'Erika Brenner'
  AND a.beobachtung LIKE '%Lieferwagen%';
