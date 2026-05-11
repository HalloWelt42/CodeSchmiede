SELECT b.titel, a.name FROM buecher b JOIN autoren a ON b.autor_id = a.id ORDER BY a.name, b.titel;
