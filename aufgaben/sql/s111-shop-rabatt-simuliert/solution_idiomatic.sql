SELECT name, preis, ROUND(preis * 0.9, 2) AS rabattpreis FROM produkte WHERE preis >= 2 ORDER BY preis DESC, name;
