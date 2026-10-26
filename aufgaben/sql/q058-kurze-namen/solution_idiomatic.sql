SELECT UPPER(name) AS schild, LENGTH(name) AS laenge
FROM pinguine
WHERE name LIKE '%a%' AND LENGTH(name) <= 4;
