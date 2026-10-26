SELECT tag, pinguin_id, menge,
       CASE WHEN menge >= 7 THEN 'riesig'
            WHEN menge >= 4 THEN 'ordentlich'
            ELSE 'klein'
       END AS portion
FROM fuetterungen;
