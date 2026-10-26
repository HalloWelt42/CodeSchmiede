SELECT tag, pinguin_id, menge
FROM fuetterungen
WHERE menge > (SELECT AVG(menge) FROM fuetterungen);
