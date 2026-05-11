SELECT pr.marke, ROUND(SUM(p.menge * p.einzelpreis), 2) AS umsatz FROM bestellpositionen p JOIN produkte pr ON p.produkt_id = pr.id GROUP BY pr.marke ORDER BY umsatz DESC, pr.marke;
