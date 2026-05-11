SELECT pr.name, SUM(p.menge) AS gesamtmenge FROM bestellpositionen p JOIN produkte pr ON p.produkt_id = pr.id GROUP BY pr.id, pr.name ORDER BY gesamtmenge DESC, pr.name LIMIT 5;
