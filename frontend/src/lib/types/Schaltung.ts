/* Digitale Schaltungen, wie das Backend sie liefert (backend/src/codeschmiede/pruefung/schaltung_pruefer.py). */
import type { AnsichtBasis, Auswertung, Laeufe } from './Steuerung';

export interface Vorgabe {
  name: string;
  art: string;
  x: number;
  y: number;
}

export interface SchaltungAnsicht extends AnsichtBasis {
  eingaenge: string[];
  ausgaenge: string[];
  bausteine: string[];
  vorgabe: Vorgabe[];
  /** je Ausgang die Spalte der Wahrheitstabelle aus 0, 1 und x */
  soll: Record<string, string>;
  sterne: { bausteine: number; tiefe: number };
}

export interface SchaltungKennzahlen {
  bausteine: number;
  tiefe: number;
  richtig: number;
  zeilen: number;
}

/** Je Zeile der Wahrheitstabelle: [Nummer, Werte aller Signale und Ausgänge] */
export type TabellenZeile = [number, Record<string, number>];

export interface SchaltungWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: TabellenZeile[];
  kennzahlen: SchaltungKennzahlen;
  fehler: string | null;
}

export type SchaltungLaeufe = Laeufe<SchaltungWiedergabe, SchaltungKennzahlen>;
