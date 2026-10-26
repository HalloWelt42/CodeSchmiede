SELECT name, gewicht_kg
FROM pinguine
WHERE (kolonie = 'Nord' OR kolonie = 'Ost') AND gewicht_kg < 4;
