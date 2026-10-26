SELECT p.name, k.lage
FROM pinguine p
JOIN kolonien k ON k.name = p.kolonie;
