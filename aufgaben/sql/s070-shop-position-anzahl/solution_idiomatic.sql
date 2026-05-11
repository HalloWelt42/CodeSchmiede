SELECT bestellung_id, COUNT(*) AS positionen FROM bestellpositionen GROUP BY bestellung_id ORDER BY positionen DESC, bestellung_id;
