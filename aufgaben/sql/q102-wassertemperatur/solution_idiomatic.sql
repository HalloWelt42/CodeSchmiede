SELECT p.name, k.wassertemperatur
FROM pinguine p
JOIN kolonien k ON k.name = p.kolonie;
