SELECT l.name, MIN(a.ausgeliehen_am) AS erste, MAX(a.ausgeliehen_am) AS letzte FROM leser l JOIN ausleihen a ON a.leser_id = l.id GROUP BY l.id, l.name ORDER BY l.name;
