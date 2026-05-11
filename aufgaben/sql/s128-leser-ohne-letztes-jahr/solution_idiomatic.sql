SELECT l.name FROM leser l WHERE l.id NOT IN (  SELECT leser_id FROM ausleihen   WHERE strftime('%Y', ausgeliehen_am) = '2025') ORDER BY l.name;
