SELECT pr.name, COALESCE(SUM(p.menge), 0) AS verkauft FROM produkte pr LEFT JOIN bestellpositionen p ON p.produkt_id = pr.id GROUP BY pr.id, pr.name ORDER BY verkauft DESC, pr.name;
