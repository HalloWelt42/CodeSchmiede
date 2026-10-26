UPDATE fuetterungen
SET fisch = 'Hering', menge = menge + 1
WHERE fisch = 'Sardine';

UPDATE pinguine
SET lieblingsfisch = 'Hering'
WHERE lieblingsfisch IS NULL;
