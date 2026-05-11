SELECT l.name, COUNT(*) AS anzahl FROM ausleihen a JOIN leser l ON a.leser_id = l.id GROUP BY l.id, l.name ORDER BY anzahl DESC, l.name;
