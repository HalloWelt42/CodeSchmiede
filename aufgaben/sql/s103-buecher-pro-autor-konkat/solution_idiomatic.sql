SELECT a.name, GROUP_CONCAT(b.titel, ', ') AS buecher FROM autoren a JOIN buecher b ON b.autor_id = a.id GROUP BY a.id, a.name ORDER BY a.name;
