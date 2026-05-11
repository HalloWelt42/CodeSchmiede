SELECT DISTINCT a.name FROM autoren a JOIN buecher b ON b.autor_id = a.id WHERE b.jahr >= 2000 ORDER BY a.name;
