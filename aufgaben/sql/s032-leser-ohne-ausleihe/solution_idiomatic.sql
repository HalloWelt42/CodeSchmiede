SELECT l.name FROM leser l LEFT JOIN ausleihen a ON a.leser_id = l.id WHERE a.id IS NULL ORDER BY l.name;
