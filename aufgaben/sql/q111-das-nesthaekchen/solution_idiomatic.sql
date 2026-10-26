SELECT name, geburtsjahr
FROM pinguine
WHERE geburtsjahr = (SELECT MAX(geburtsjahr) FROM pinguine);
