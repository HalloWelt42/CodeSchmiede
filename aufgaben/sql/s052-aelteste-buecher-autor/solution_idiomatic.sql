SELECT a.name, b.titel, b.jahr FROM buecher b JOIN autoren a ON b.autor_id = a.id WHERE b.jahr = (SELECT MIN(jahr) FROM buecher WHERE autor_id = b.autor_id) ORDER BY a.name;
