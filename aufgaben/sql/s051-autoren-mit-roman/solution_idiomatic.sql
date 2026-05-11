SELECT name FROM autoren WHERE id IN (SELECT autor_id FROM buecher WHERE kategorie = 'Roman') ORDER BY name;
