SELECT l.name, b.titel FROM ausleihen a JOIN leser l ON a.leser_id = l.id JOIN buecher b ON a.buch_id = b.id WHERE a.zurueck_am IS NULL ORDER BY l.name, b.titel;
