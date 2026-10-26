SELECT name,
       CASE WHEN geburtsjahr >= 2021 THEN 'jung' ELSE 'erfahren' END AS stufe
FROM pinguine;
