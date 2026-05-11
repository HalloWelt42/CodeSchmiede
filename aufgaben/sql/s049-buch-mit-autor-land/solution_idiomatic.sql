SELECT b.titel, a.name, a.land FROM buecher b JOIN autoren a ON b.autor_id = a.id ORDER BY a.land, a.name, b.titel;
