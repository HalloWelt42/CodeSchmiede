SELECT name, ort FROM leser WHERE ort IN (SELECT ort FROM leser GROUP BY ort ORDER BY COUNT(*) DESC LIMIT 3) ORDER BY ort, name;
