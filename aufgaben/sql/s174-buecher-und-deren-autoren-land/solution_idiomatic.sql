SELECT b.titel, a.land FROM buecher b JOIN autoren a ON b.autor_id = a.id WHERE a.land != 'Deutschland' ORDER BY a.land, b.titel;
