/*
 * Typen für Code-Submissions und das Pruef-Ergebnis vom Backend.
 * Versteckte Tests werden nur als Anzahl übertragen.
 */

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
}

export interface ProgressEintragLeicht {
  aufgabe_id: string;
  status: 'neu' | 'in_arbeit' | 'geloest';
  versuche: number;
  hints_genutzt: number;
  punkte_erreicht: number;
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
  laufzeit_ms: number;
  codelaenge_zeichen: number;
  code: string;
}
