/*
 * Typen fuer Code-Submissions und das Pruef-Ergebnis vom Backend.
 * Versteckte Tests werden nur als Anzahl uebertragen.
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

export interface SubmissionAntwort {
  bestanden: boolean;
  pruefung: PruefErgebnis;
  codelaenge_zeichen: number;
  submission_id: number;
}
