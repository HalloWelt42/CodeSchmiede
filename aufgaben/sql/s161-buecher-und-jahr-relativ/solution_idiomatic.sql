SELECT titel, jahr, CASE   WHEN jahr < 1900 THEN '19. Jh'   WHEN jahr < 2000 THEN '20. Jh'   ELSE '21. Jh' END AS epoche FROM buecher ORDER BY jahr, titel;
