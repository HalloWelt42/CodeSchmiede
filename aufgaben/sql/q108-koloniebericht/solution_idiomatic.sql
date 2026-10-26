SELECT k.name AS kolonie, k.lage, COUNT(p.id) AS pinguine
FROM kolonien k
LEFT JOIN pinguine p ON p.kolonie = k.name
GROUP BY k.name, k.lage
ORDER BY pinguine DESC, k.name;
