WITH zaehler AS (  SELECT leser_id, COUNT(*) AS anz FROM ausleihen GROUP BY leser_id) SELECT ROUND(AVG(anz), 2) AS schnitt FROM zaehler;
