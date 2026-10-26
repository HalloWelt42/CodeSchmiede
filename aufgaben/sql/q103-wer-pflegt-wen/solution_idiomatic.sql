SELECT p.name AS pinguin, pf.name AS pfleger
FROM pinguine p
JOIN pfleger pf ON pf.kolonie = p.kolonie;
