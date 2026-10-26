/*
 * Ampelschule: Anlage, Auswertung und Wiedergabe, wie das Backend sie liefert
 * (backend/src/codeschmiede/steuerung/ampel_anlage.py, pruefung/ampel_pruefer.py).
 */
import type { TeilschrittStand } from './Steuerung';

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

export interface AmpelAnsicht {
  anlage: Anlage;
  ablauf: string;
  dauer: number;
  /** Länge und Breite je Art von Teilnehmer */
  arten: Record<Teilnehmerart, { laenge: number; breite: number }>;
  sensoren: string[];
  teilschritte: { titel: string; text: string }[];
  sterne: { fuss: number | null; autos: number | null; zeichen: number };
  /** dessen bestandenes Programm ist der Anfang, wenn es hier noch keins gibt */
  aufbauend_auf: string | null;
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

export interface AblaufStand {
  name: string;
  sichtbar: boolean;
  ok: boolean;
  kennzahlen: Kennzahlen;
  erste_stelle: number | null;
  erster_befund: string | null;
}

export interface AmpelAuswertung {
  teilschritte: TeilschrittStand[];
  ablaeufe: AblaufStand[];
  wiedergaben: Wiedergabe[];
}

export interface AmpelLaeufe {
  auswertung: AmpelAuswertung | null;
  stdout: string;
  stderr: string;
  laufzeit_ms: number;
  timeout: boolean;
}
