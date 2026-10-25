/*
 * Typen für Code-Submissions und das Pruef-Ergebnis vom Backend.
 * Versteckte Tests werden nur als Anzahl übertragen.
 */
import type { Belohnung } from '../api/SpielApi';

export interface TestErgebnis {
  index: number;
  bestanden: boolean;
  eingabe: unknown[];
  erwartet: unknown;
  tatsaechlich: unknown;
  fehler: string | null;
}

export interface PruefErgebnis {
  bestanden: boolean;
  sichtbar: TestErgebnis[];
  versteckt_pass: number;
  versteckt_fail: number;
  laufzeit_ms: number;
  stdout: string;
  stderr: string;
  timeout: boolean;
  /** nur bei Aufgabentypen mit Sternen (Spiele, CSS) */
  wertung?: Wertung | null;
}

export interface Kennwerte {
  deckung?: number | null;
  schritte?: number | null;
  zeilen?: number | null;
  treffer?: number | null;
  kuerzer_als_muster?: boolean | null;
}

export interface SternKriterium {
  text: string;
  erreicht: boolean;
}

export interface Wertung {
  sterne: number;
  kriterien: SternKriterium[];
  kennwerte: Kennwerte;
}

export interface ProgressEintragLeicht {
  aufgabe_id: string;
  status: 'neu' | 'in_arbeit' | 'geloest';
  versuche: number;
  hints_genutzt: number;
  punkte_erreicht: number;
  sterne: number | null;
  aufgegeben: boolean;
  geloest_am: string | null;
  ease: number;
  intervall_tage: number;
  faellig_am: string | null;
  letzte_wiederholung: string | null;
}

export interface VergleichEintrag {
  variante: string;
  laufzeit_ms: number;
  codelaenge_zeichen: number;
}

export interface SubmissionAntwort {
  bestanden: boolean;
  pruefung: PruefErgebnis;
  codelaenge_zeichen: number;
  submission_id: number;
  progress: ProgressEintragLeicht;
  vergleich: VergleichEintrag[];
  /** nur bei bestandenen Abgaben */
  belohnung: Belohnung | null;
}

export interface ProbelaufAntwort {
  rueckgabe: unknown;
  stdout: string;
  stderr: string;
  laufzeit_ms: number;
  timeout: boolean;
  fehler: string | null;
}

export interface VerlaufEintrag {
  id: number;
  zeitstempel: string;
  bestanden: boolean;
  laufzeit_ms: number | null;
  codelaenge_zeichen: number | null;
  code: string;
}
