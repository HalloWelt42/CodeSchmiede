/* Codes knacken, wie das Backend es liefert (backend/src/codeschmiede/pruefung/codes_pruefer.py, routes/spiel.py). */
import type { AnsichtBasis, Auswertung, Laeufe } from './Steuerung';

export type Verfahren = 'caesar' | 'ersetzung' | 'vigenere' | 'xor' | 'schichten' | 'pin';

export interface GeheimeNachricht {
  name: string;
  /** der Aufruf, wie er im Programm stünde, etwa knacke(geheim) */
  aufruf: string;
  /** das erste Argument: der Geheimtext (beim Verschlüsseln der Klartext) */
  eingabe: string;
}

export interface CodesAnsicht extends AnsichtBasis {
  verfahren: Verfahren;
  funktion: string;
  bereit: string[];
  /** Anteil je Buchstabe im Deutschen in Prozent */
  deutsch: Record<string, number>;
  nachrichten: GeheimeNachricht[];
  mindestens: number;
  sterne: { ms: number; zeichen: number };
}

export interface CodesKennzahlen {
  ms: number;
  /** Anteil der Buchstaben, die stimmen, 0 bis 1 */
  anteil: number;
  zeichen: number;
}

export interface CodesWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: [number][];
  aufruf: string;
  eingabe: string;
  soll: string;
  ergebnis: string | null;
  kennzahlen: CodesKennzahlen;
  fehler: string | null;
}

export type CodesLaeufe = Laeufe<CodesWiedergabe, CodesKennzahlen>;
export type CodesAuswertung = Auswertung<CodesWiedergabe, CodesKennzahlen> & { ms: number };
