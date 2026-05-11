SELECT l.name, a.ausgeliehen_am, COUNT(*) AS anzahl FROM ausleihen a JOIN leser l ON a.leser_id = l.id GROUP BY l.id, l.name, a.ausgeliehen_am HAVING COUNT(*) >= 2 ORDER BY a.ausgeliehen_am, l.name;
