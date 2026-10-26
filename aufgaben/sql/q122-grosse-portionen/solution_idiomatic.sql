SELECT tag, menge,
       CASE WHEN menge >= 6 THEN 'groß' ELSE 'normal' END AS portion
FROM fuetterungen;
