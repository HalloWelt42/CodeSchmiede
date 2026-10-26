SELECT tag, SUM(menge) AS fische
FROM fuetterungen
GROUP BY tag;
