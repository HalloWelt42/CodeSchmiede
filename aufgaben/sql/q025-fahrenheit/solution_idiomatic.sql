SELECT name, ROUND(wassertemperatur * 9 / 5 + 32, 1) AS fahrenheit
FROM kolonien;
