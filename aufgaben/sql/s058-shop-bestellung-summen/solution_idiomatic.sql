SELECT bestellung_id, ROUND(SUM(menge * einzelpreis), 2) AS gesamt FROM bestellpositionen GROUP BY bestellung_id ORDER BY bestellung_id;
