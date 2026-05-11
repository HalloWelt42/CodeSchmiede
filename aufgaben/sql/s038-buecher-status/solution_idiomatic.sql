SELECT titel, CASE   WHEN exemplare = 1 THEN 'einzeln'   WHEN exemplare BETWEEN 2 AND 4 THEN 'wenige'   ELSE 'viele' END AS status FROM buecher ORDER BY id;
