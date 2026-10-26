SELECT name, wassertemperatur,
       CASE WHEN wassertemperatur < 0 THEN 'eisig'
            WHEN wassertemperatur < 5 THEN 'frisch'
            ELSE 'mild'
       END AS gefuehl
FROM kolonien;
