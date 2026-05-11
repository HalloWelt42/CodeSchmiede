SELECT bestellung_id, COUNT(*) AS positionen FROM bestellpositionen GROUP BY bestellung_id HAVING COUNT(*) > 2 ORDER BY positionen DESC, bestellung_id;
