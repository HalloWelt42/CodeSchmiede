/* KV-Werkstatt, wie das Backend sie liefert (backend/src/codeschmiede/pruefung/kv_pruefer.py, routes/spiel.py). */
import type { AnsichtBasis, Laeufe } from './Steuerung';

export interface KvAnsicht extends AnsichtBasis {
  eingaenge: string[];
  ausgaenge: string[];
  /** je Ausgang je Belegung 0, 1 oder x, binär gezählt mit dem ersten Eingang vorn */
  werte: Record<string, string>;
  /** wie eine Belegung heißt (etwa die Ziffer); leer: ihre Bits */
  namen: string[];
  /** Blöcke und Buchstaben der kleinsten Lösung */
  sterne: { bloecke: number; buchstaben: number };
}

export interface KvKennzahlen {
  bloecke: number;
  buchstaben: number;
  richtig: number;
  zeilen: number;
  bausteine: number;
  tiefe: number;
}

/** Je Belegung: [Nummer, Wert je Ausgang] */
export type KvBild = [number, Record<string, number>];

export interface KvWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: KvBild[];
  /** die Formel als Schaltplan im Text der Schaltungen */
  plan: string;
  kennzahlen: KvKennzahlen;
  fehler: string | null;
}

export type KvLaeufe = Laeufe<KvWiedergabe, KvKennzahlen>;
