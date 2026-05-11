SELECT a.name, SUM(b.seiten) AS gesamt FROM buecher b JOIN autoren a ON b.autor_id = a.id GROUP BY a.id, a.name ORDER BY gesamt DESC, a.name;
