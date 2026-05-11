SELECT pr.name, ROUND(AVG(p.menge), 2) AS schnitt_menge FROM bestellpositionen p JOIN produkte pr ON p.produkt_id = pr.id GROUP BY pr.id, pr.name ORDER BY schnitt_menge DESC, pr.name;
