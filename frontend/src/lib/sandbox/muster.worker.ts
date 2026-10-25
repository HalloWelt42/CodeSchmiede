/*
 * Markiert Zeilen mit einem Muster abseits des Hauptfadens: ein zu
 * gieriges Muster blockiert nur diesen Arbeiter, den die Vorschau dann
 * beendet.
 */
import { markiereZeilen } from '../muster';

interface Auftrag {
  nr: number;
  muster: string;
  flags: string;
  zeilen: string[];
}

self.onmessage = (e: MessageEvent<Auftrag>) => {
  const { nr, muster, flags, zeilen } = e.data;
  self.postMessage({ nr, markierung: markiereZeilen(muster, flags, zeilen) });
};
