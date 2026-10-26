SELECT p.name AS pinguin, SUM(f.menge) AS fische
FROM pinguine p
JOIN fuetterungen f ON f.pinguin_id = p.id
GROUP BY p.name
ORDER BY fische DESC, pinguin;
