SELECT DISTINCT l.name FROM leser l JOIN ausleihen a ON a.leser_id = l.id WHERE a.zurueck_am IS NULL ORDER BY l.name;
