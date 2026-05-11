SELECT b.id, b.status, ROUND(SUM(p.menge * p.einzelpreis), 2) AS summe FROM bestellungen b JOIN bestellpositionen p ON p.bestellung_id = b.id GROUP BY b.id, b.status ORDER BY b.id;
