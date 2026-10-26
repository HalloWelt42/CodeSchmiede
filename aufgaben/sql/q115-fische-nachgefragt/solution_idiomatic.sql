SELECT p.name,
       (SELECT SUM(f.menge) FROM fuetterungen f WHERE f.pinguin_id = p.id) AS fische
FROM pinguine p;
