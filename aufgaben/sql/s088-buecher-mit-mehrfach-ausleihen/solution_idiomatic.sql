SELECT b.titel, COUNT(*) AS anzahl FROM ausleihen a JOIN buecher b ON a.buch_id = b.id GROUP BY b.id, b.titel HAVING COUNT(*) > 2 ORDER BY anzahl DESC, b.titel;
