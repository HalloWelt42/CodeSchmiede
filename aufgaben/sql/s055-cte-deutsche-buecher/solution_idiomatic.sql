WITH deutsche AS (SELECT id, name FROM autoren WHERE land = 'Deutschland') SELECT b.titel, d.name FROM buecher b JOIN deutsche d ON b.autor_id = d.id ORDER BY d.name, b.titel;
