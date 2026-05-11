SELECT DISTINCT l.name FROM ausleihen a JOIN leser l ON a.leser_id = l.id JOIN buecher b ON a.buch_id = b.id WHERE b.kategorie = 'Roman' ORDER BY l.name;
