/* Schaltungen mit Takt, wie das Backend sie liefert (backend/src/codeschmiede/pruefung/takt_pruefer.py). */
import type { Vorgabe } from './Schaltung';
import type { AnsichtBasis, Laeufe } from './Steuerung';

export interface TaktAblauf {
  name: string;
  takte: number;
  /** je Eingang eine Folge aus 0 und 1, ein Zeichen je Takt; fehlt einer, ist er 0 */
  eingaben: Record<string, string>;
  /** je Ausgang eine Folge aus 0, 1 und x (egal) */
  soll: Record<string, string>;
}

export interface TaktAnsicht extends AnsichtBasis {
  eingaenge: string[];
  ausgaenge: string[];
  bausteine: string[];
  vorgabe: Vorgabe[];
  /** Ausgänge, die zusammen eine Zahl zeigen, höchste Stelle vorn */
  zahl: string[];
  /** die sichtbaren Abläufe */
  ablaeufe: TaktAblauf[];
  sterne: { bausteine: number; tiefe: number };
}

export interface TaktKennzahlen {
  bausteine: number;
  flipflops: number;
  tiefe: number;
  richtig: number;
  takte: number;
}

/** Je Takt: [Nummer, Werte aller Signale, Flipflops und Ausgänge] */
export type TaktBild = [number, Record<string, number>];

export interface TaktWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: TaktBild[];
  eingaben: Record<string, string>;
  soll: Record<string, string>;
  kennzahlen: TaktKennzahlen;
  fehler: string | null;
}

export type TaktLaeufe = Laeufe<TaktWiedergabe, TaktKennzahlen>;
