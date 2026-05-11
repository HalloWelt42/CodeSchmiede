SELECT pr.marke, SUM(p.menge) AS gesamtmenge FROM bestellpositionen p JOIN produkte pr ON p.produkt_id = pr.id GROUP BY pr.marke ORDER BY gesamtmenge DESC, pr.marke;
