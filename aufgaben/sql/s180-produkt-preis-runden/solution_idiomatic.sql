SELECT name, preis, ROUND(preis * 10) / 10.0 AS rund_zehn FROM produkte ORDER BY name;
