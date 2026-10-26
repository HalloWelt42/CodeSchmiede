SELECT name, COALESCE(lieblingsfisch, 'unbekannt') AS fisch
FROM pinguine
WHERE lieblingsfisch <> 'Hering' OR lieblingsfisch IS NULL;
