SELECT pinguin_id, COUNT(*) AS mahlzeiten
FROM fuetterungen
GROUP BY pinguin_id
HAVING COUNT(*) > 1;
