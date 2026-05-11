SELECT a.name, COUNT(*) AS anzahl FROM buecher b JOIN autoren a ON b.autor_id = a.id GROUP BY a.id, a.name HAVING COUNT(*) > 1 ORDER BY anzahl DESC, a.name;
