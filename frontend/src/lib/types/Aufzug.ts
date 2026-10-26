/*
 * Aufzugsteuerung: Haus, Auswertung und Wiedergabe, wie das Backend sie liefert
 * (backend/src/codeschmiede/steuerung/aufzug_welt.py, pruefung/aufzug_pruefer.py).
 */
import type { AnsichtBasis, Auswertung, Laeufe } from './Steuerung';

export interface Haus {
  etagen: number;
  namen: string[];
  aufzuege: string[];
  plaetze: number;
  last: number;
}

export interface AufzugAnsicht extends AnsichtBasis {
  haus: Haus;
  ablauf: string;
  sterne: { warten: number; zeichen: number };
}

export interface AufzugKennzahlen {
  verstoesse: number;
  bedient: number;
  fahrgaeste: number;
  warten_mittel: number;
  warten_max: number;
}

export interface Ereignis {
  t: number;
  art: 'auf' | 'zu' | 'offen' | 'verstoss';
  aufzug: string;
  etage: number;
  text?: string;
  grund?: string;
}

/** Kabine: [Lage in Etagen, Tür 0 bis 1, Fahrgäste] */
export type KabinenBild = [number, number, number];
/** Wartender: [id, Etage, Richtung] */
export type WartenderBild = [number, number, number];
/** Läufer durch die Tür: [id, Kabine, +1 rein oder -1 raus, Anteil des Wegs] */
export type LaeuferBild = [number, number, number, number];

export interface AufzugWiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: [number, KabinenBild[], WartenderBild[], LaeuferBild[]][];
  fahrgaeste: { id: number; von: number; nach: number; ankunft: number }[];
  ereignisse: Ereignis[];
  feuer: number | null;
  kennzahlen: AufzugKennzahlen;
  fehler: string | null;
}

export type AufzugLaeufe = Laeufe<AufzugWiedergabe, AufzugKennzahlen>;
