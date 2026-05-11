SELECT DISTINCT a.name FROM autoren a WHERE NOT EXISTS (  SELECT 1 FROM buecher b JOIN ausleihen au ON au.buch_id = b.id   WHERE b.autor_id = a.id) ORDER BY a.name;
