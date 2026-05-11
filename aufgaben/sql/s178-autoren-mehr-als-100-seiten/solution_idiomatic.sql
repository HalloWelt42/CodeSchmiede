SELECT a.name, ROUND(AVG(b.seiten), 1) AS schnitt FROM autoren a JOIN buecher b ON b.autor_id = a.id GROUP BY a.id, a.name HAVING AVG(b.seiten) > 200 ORDER BY schnitt DESC, a.name;
