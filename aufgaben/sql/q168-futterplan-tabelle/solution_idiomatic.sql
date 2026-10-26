CREATE TABLE futterplan (
  id INTEGER PRIMARY KEY,
  pinguin_id INTEGER NOT NULL REFERENCES pinguine(id),
  fisch TEXT NOT NULL,
  menge INTEGER NOT NULL DEFAULT 2 CHECK (menge > 0)
);

INSERT INTO futterplan (pinguin_id, fisch)
SELECT id, lieblingsfisch FROM pinguine WHERE lieblingsfisch IS NOT NULL;
