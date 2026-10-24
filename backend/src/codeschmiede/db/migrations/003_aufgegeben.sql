-- Aufgeben: wer die Musterlösungen vor dem Bestehen ansieht, gibt die
-- Aufgabe auf. Danach bringt ein Bestehen keine Punkte mehr.

ALTER TABLE progress ADD COLUMN aufgegeben INTEGER NOT NULL DEFAULT 0;
