SELECT name, ROUND(preis * lager, 2) AS lagerwert FROM produkte ORDER BY lagerwert DESC LIMIT 10;
