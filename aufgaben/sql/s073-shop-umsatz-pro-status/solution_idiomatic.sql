SELECT b.status, ROUND(SUM(p.menge * p.einzelpreis), 2) AS umsatz FROM bestellpositionen p JOIN bestellungen b ON p.bestellung_id = b.id GROUP BY b.status ORDER BY umsatz DESC, b.status;
