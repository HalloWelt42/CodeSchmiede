/* Gemeinsames der Steuerungsspiele (backend/src/codeschmiede/steuerung/teilschritte.py). */

export interface TeilschrittStand {
  titel: string;
  text: string;
  erfuellt: boolean;
  /** false, wenn der Schritt versteckte Abläufe braucht, die ein Probelauf nicht hat */
  geprueft: boolean;
  befunde: string[];
}

/** Was jedes Steuerungsspiel vor dem ersten Lauf vom Level zeigt. */
export interface AnsichtBasis {
  dauer: number;
  sensoren: string[];
  teilschritte: { titel: string; text: string }[];
  /** dessen bestandenes Programm ist der Anfang, wenn es hier noch keins gibt */
  aufbauend_auf: string | null;
}

/** Ein Ablauf zum Abspielen: je Takt ein Bild, das mit seiner Zeit beginnt. */
export interface WiedergabeBasis {
  name: string;
  sichtbar: boolean;
  dauer: number;
  bilder: [number, ...unknown[]][];
  fehler: string | null;
}

export interface AblaufStand<K> {
  name: string;
  sichtbar: boolean;
  ok: boolean;
  kennzahlen: K;
  erste_stelle: number | null;
  erster_befund: string | null;
}

export interface Auswertung<W, K> {
  teilschritte: TeilschrittStand[];
  ablaeufe: AblaufStand<K>[];
  wiedergaben: W[];
}

export interface Laeufe<W, K> {
  auswertung: Auswertung<W, K> | null;
  stdout: string;
  stderr: string;
  laufzeit_ms: number;
  timeout: boolean;
}

/** Lesen und Schreiben des Programms für einen eigenen Editor */
export interface CodeZugriff {
  code: string;
}
