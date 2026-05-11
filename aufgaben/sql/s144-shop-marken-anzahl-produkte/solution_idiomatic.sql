SELECT marke, COUNT(*) AS anzahl FROM produkte GROUP BY marke HAVING COUNT(*) >= 3 ORDER BY anzahl DESC, marke;
