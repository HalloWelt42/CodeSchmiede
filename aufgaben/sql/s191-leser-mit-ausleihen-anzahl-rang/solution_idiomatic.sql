SELECT l.name, COUNT(a.id) AS anz, RANK() OVER (ORDER BY COUNT(a.id) DESC) AS rang FROM leser l LEFT JOIN ausleihen a ON a.leser_id = l.id GROUP BY l.id, l.name ORDER BY rang, l.name;
