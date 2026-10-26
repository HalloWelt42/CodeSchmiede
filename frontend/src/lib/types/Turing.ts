/* Turingmaschine, wie das Backend sie liefert (backend/src/codeschmiede/pruefung/turing_pruefer.py). */
import type { AnsichtBasis, Auswertung, Laeufe } from './Steuerung';

export interface Band {
  band: string;
  name: string | null;
  soll: string | null;
  soll_zustand: string | null;
}

export interface TuringAnsicht extends AnsichtBasis {
  zeichen: string[];
  start: string;
  ende: string[];
  kopf: 'anfang' | 'ende';
  grenze: number;
  baender: Band[];
  sterne: { zustaende: number; zeilen: number };
}

export interface TuringKennzahlen {
  schritte: number;
  zustaende: number;
  zeilen: number;
}

/** Je Schritt: [Nummer, Band ab Feld von, von, Kopf, Zustand, Zeile der Regel] */
export type TuringBild = [number, string, number, number, string, number | null];

export interface TuringWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: TuringBild[];
  start: string;
  soll: string | null;
  soll_zustand: string | null;
  ergebnis: string;
  kennzahlen: TuringKennzahlen;
  fehler: string | null;
}

export type TuringLaeufe = Laeufe<TuringWiedergabe, TuringKennzahlen>;
export type TuringAuswertung = Auswertung<TuringWiedergabe, TuringKennzahlen>;
