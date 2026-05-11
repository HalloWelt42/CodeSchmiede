SELECT DISTINCT l.name FROM leser l JOIN ausleihen a ON a.leser_id = l.id WHERE strftime('%Y', a.ausgeliehen_am) = '2025' ORDER BY l.name;
