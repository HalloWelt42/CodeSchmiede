SELECT ((jahr - 1) / 100) + 1 AS jahrhundert, COUNT(*) AS anzahl FROM buecher GROUP BY jahrhundert ORDER BY jahrhundert;
