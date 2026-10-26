SELECT COUNT(*) AS mahlzeiten, SUM(menge) AS fische
FROM fuetterungen
WHERE pinguin_id = 1;
