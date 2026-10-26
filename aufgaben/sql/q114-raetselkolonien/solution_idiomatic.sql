SELECT name, lage
FROM kolonien
WHERE name IN (SELECT kolonie FROM pinguine WHERE lieblingsfisch IS NULL);
