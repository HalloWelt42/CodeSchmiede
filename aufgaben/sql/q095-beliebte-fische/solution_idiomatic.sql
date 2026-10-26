SELECT fisch, SUM(menge) AS fische
FROM fuetterungen
GROUP BY fisch
HAVING SUM(menge) > 10;
