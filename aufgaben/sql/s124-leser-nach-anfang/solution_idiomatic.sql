SELECT SUBSTR(name, 1, 1) AS buchstabe, COUNT(*) AS anzahl FROM leser GROUP BY buchstabe ORDER BY buchstabe;
