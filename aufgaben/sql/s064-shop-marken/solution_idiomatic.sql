SELECT marke, COUNT(*) AS anzahl FROM produkte GROUP BY marke ORDER BY anzahl DESC, marke;
