CREATE TABLE paten (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  pinguin_id INTEGER NOT NULL REFERENCES pinguine(id)
);

INSERT INTO paten (name, pinguin_id)
VALUES ('Familie Kim', 4), ('Klasse 5b', 4);
