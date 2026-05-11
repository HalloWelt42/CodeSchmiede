SELECT land, COUNT(*) AS anzahl FROM autoren GROUP BY land ORDER BY anzahl DESC, land;
