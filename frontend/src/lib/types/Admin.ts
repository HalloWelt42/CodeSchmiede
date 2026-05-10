/*
 * Typen für die Verwaltungs-Übersicht.
 * Vollständige Sicht einer Aufgabe inklusive versteckter Tests, Hints,
 * Statistik aus submissions/progress -- nur für die Admin-Ansicht.
 */

import type { Hint, Quelle, Schwierigkeit, TestFall } from './Aufgabe';

export interface AufgabenStatistik {
  submissions_gesamt: number;
  bestandene_submissions: number;
  versuche: number;
  hints_genutzt: number;
  punkte_erreicht: number;
  status: 'neu' | 'in_arbeit' | 'geloest';
}

export interface VerwaltungsEintrag {
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
  tests_versteckt: TestFall[];
  starter_code: string;
  beschreibung_md: string;
  musterloesungen_anzahl: number;
  dateipfad: string;
  hash: string;
  statistik: AufgabenStatistik;
}
