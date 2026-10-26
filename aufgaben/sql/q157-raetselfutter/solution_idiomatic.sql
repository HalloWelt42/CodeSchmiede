DELETE FROM fuetterungen
WHERE pinguin_id IN (SELECT id FROM pinguine WHERE lieblingsfisch IS NULL);
