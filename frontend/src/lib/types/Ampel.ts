/*
 * Ampelschule: Anlage, Auswertung und Wiedergabe, wie das Backend sie liefert
 * (backend/src/codeschmiede/steuerung/ampel_anlage.py, pruefung/ampel_pruefer.py).
 */
import type { AnsichtBasis, Auswertung, Laeufe } from './Steuerung';

export type Punkt = [number, number];
export type Bewegung = 'gerade' | 'rechts' | 'links';
export type Gruppenart = 'auto' | 'fuss';
export type Signal = 'rot' | 'rotgelb' | 'gruen' | 'gelb' | 'gelb_blinkt' | 'aus';

export interface Gruppe {
  name: string;
  art: Gruppenart;
  text: string;
  vorfahrt: boolean;
}

export interface Weg {
  id: string;
  art: 'fahrbahn' | 'ueberweg';
  gruppe: string;
  zufahrt: string;
  spur: string;
  punkte: Punkt[];
  halt: number | null;
  schleife: [number, number] | null;
}

export interface Zeichnung {
  flaechen: { klasse: 'gehweg' | 'strasse' | 'zebra' | 'schleife'; punkte: Punkt[] }[];
  striche: { klasse: 'mittellinie' | 'spurlinie' | 'haltlinie'; punkte: Punkt[] }[];
  signale: { gruppe: string; art: Gruppenart; x: number; y: number; drehung: number }[];
  taster: { gruppe: string; x: number; y: number }[];
  pfeile: { x: number; y: number; drehung: number; richtungen: Bewegung[] }[];
}

export interface Anlage {
  breite: number;
  hoehe: number;
  gruppen: Gruppe[];
  wege: Weg[];
  zeichnung: Zeichnung;
}

export interface AmpelAnsicht extends AnsichtBasis {
  anlage: Anlage;
  ablauf: string;
  /** Länge und Breite je Art von Teilnehmer */
  arten: Record<Teilnehmerart, { laenge: number; breite: number }>;
  sterne: { fuss: number | null; autos: number | null; zeichen: number };
}

export interface Kennzahlen {
  unfaelle: number;
  verstoesse: number;
  fuss_max: number;
  autos_mittel: number;
}

export type Teilnehmerart = 'auto' | 'lkw' | 'einsatz' | 'fuss';

export interface Unfall {
  t: number;
  art: 'fuss' | 'blech';
  ids: [number, number];
  gruppen: [string, string];
  x: number;
  y: number;
}

export interface Wiedergabe {
  name: string;
  sichtbar: boolean;
  dauer: number;
  signale: Record<string, Signal>[];
  teilnehmer: { id: number; art: Teilnehmerart; weg: string }[];
  /** je Takt: [Zeit, [[id, Strecke], ...]] */
  bilder: [number, [number, number][]][];
  unfaelle: Unfall[];
  nacht: [number, number][];
  /** je Sekunde die Gruppen, bei denen jemand auf Grün wartete */
  bedarf: string[][];
  kennzahlen: Kennzahlen;
  fehler: string | null;
}

export type AmpelAuswertung = Auswertung<Wiedergabe, Kennzahlen>;
export type AmpelLaeufe = Laeufe<Wiedergabe, Kennzahlen>;
