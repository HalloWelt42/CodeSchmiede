SELECT fisch, COUNT(*) AS mal, SUM(menge) AS fische
FROM fuetterungen
WHERE tag >= '2026-10-21'
GROUP BY fisch
HAVING COUNT(*) >= 2
ORDER BY fische DESC;
