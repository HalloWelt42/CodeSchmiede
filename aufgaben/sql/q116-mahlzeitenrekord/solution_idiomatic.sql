SELECT MAX(mahlzeiten) AS rekord
FROM (SELECT pinguin_id, COUNT(*) AS mahlzeiten
      FROM fuetterungen
      GROUP BY pinguin_id);
