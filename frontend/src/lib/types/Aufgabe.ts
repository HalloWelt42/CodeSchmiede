/*
 * TypeScript-Typen, gespiegelt zu den Pydantic-Modellen im Backend.
 * Aufgabe in zwei Sichten: Kurz (Liste) und Detail (Beschreibung +
 * sichtbare Tests + Hints, ohne tests_versteckt).
 */

export type Schwierigkeit = 'anfaenger' | 'mittel' | 'fortgeschritten' | 'experte';

export interface AufgabeKurz {
  id: string;
  titel: string;
  sprache: string;
  schwierigkeit: Schwierigkeit;
  schwierigkeit_score: number;
  schaetz_minuten: number;
  tags: string[];
  pfade: string[];
  revision: number;
}

export interface Quelle {
  url: string | null;
  notiz: string | null;
}

export interface Hint {
  kosten: number;
  text: string;
}

export interface TestFall {
  input: unknown[];
  expected: unknown;
}

export interface AufgabeDetail {
  schema_version: number;
  id: string;
  revision: number;
  titel: string;
  sprache: string;
  task_type: string;
  runner_type: string;
  schwierigkeit: Schwierigkeit;
  schwierigkeit_score: number;
  schaetz_minuten: number;
  tags: string[];
  pfade: string[];
  voraussetzungen: string[];
  quelle: Quelle;
  lizenz: string;
  autor: string | null;
  erstellt_am: string | null;
  zeitlimit_sekunden: number;
  funktion: string | null;
  hints: Hint[];
  tests_sichtbar: TestFall[];
  starter_code: string;
  beschreibung_md: string;
  anzahl_versteckte_tests: number;
}

export interface Musterloesung {
  variante: string;
  code: string;
}

export interface Pfad {
  id: string;
  titel: string;
  beschreibung: string;
  reihenfolge: string[];
}
