SELECT name,
       CASE WHEN lieblingsfisch IS NULL THEN 'Rätsel' ELSE lieblingsfisch END AS fisch
FROM pinguine;
