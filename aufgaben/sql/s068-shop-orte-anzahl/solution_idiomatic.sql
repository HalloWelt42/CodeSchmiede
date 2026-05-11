SELECT ort, COUNT(*) AS anzahl FROM kunden GROUP BY ort ORDER BY anzahl DESC, ort;
