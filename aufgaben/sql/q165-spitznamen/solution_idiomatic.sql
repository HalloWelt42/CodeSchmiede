ALTER TABLE pinguine ADD COLUMN spitzname TEXT;

UPDATE pinguine SET spitzname = 'Pünkti' WHERE name = 'Pünktchen';
