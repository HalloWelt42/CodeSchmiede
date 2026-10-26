SELECT pf.name AS pfleger, k.lage
FROM pfleger pf
LEFT JOIN kolonien k ON k.name = pf.kolonie;
