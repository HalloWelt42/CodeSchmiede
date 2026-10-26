SELECT kolonie,
       SUM(CASE WHEN gewicht_kg > 4 THEN 1 ELSE 0 END) AS schwere,
       COUNT(*) AS alle
FROM pinguine
GROUP BY kolonie
ORDER BY kolonie;
