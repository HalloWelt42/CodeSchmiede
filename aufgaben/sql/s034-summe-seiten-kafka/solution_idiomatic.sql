SELECT SUM(b.seiten) AS gesamt_seiten FROM buecher b JOIN autoren a ON b.autor_id = a.id WHERE a.name = 'Franz Kafka';
