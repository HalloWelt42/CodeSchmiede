SELECT kolonie, MAX(gewicht_kg) AS schwerster
FROM pinguine
WHERE geburtsjahr < 2022
GROUP BY kolonie;
