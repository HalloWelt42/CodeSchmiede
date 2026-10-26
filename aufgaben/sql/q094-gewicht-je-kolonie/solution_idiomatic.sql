SELECT kolonie, ROUND(AVG(gewicht_kg), 2) AS schnitt
FROM pinguine
GROUP BY kolonie;
