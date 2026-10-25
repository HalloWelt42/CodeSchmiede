/*
 * Anzeigehilfen der Spielmechanik, geteilt von Rechner und Telefon.
 */
import type { ErfolgStand, Rang, SerienStand } from './api/SpielApi';

const ZAHL = new Intl.NumberFormat('de-DE');
const PROZENT = new Intl.NumberFormat('de-DE', { minimumFractionDigits: 1, maximumFractionDigits: 1 });

/** Ganze Zahl mit Tausenderpunkt */
export function zahl(n: number): string {
  return ZAHL.format(n);
}

/** Anteil von 0 bis 1 als Prozentzahl mit einer Stelle, etwa "96,4" */
export function prozentZahl(anteil: number): string {
  return PROZENT.format(anteil * 100);
}

export const RANG_NAME: Record<Rang, string> = { bronze: 'Bronze', silber: 'Silber', gold: 'Gold' };

/** Klasse der Medaille: Rang oder ungefüllt */
export function medaille(rang: Rang | null): string {
  return rang ?? 'keine';
}

export function tage(n: number): string {
  return n === 1 ? '1 Tag' : `${n} Tage`;
}

const ZAHLWORT = ['kein', 'ein', 'zwei', 'drei', 'vier', 'fünf'];

/** "2 Schutzschilde, der dritte in 2 Tagen" */
export function schildText(s: SerienStand): string {
  const zahlwort = (n: number) => ZAHLWORT[n] ?? String(n);
  const was = s.schilde === 1 ? 'ein Schutzschild' : `${zahlwort(s.schilde)} Schutzschilde`;
  if (s.naechster_schild_in === null) return `${was}, alle da`;
  const naechster = s.schilde === 0 ? 'der erste' : 'der nächste';
  const wann = s.naechster_schild_in === 1 ? 'morgen' : `in ${tage(s.naechster_schild_in)}`;
  return `${was.charAt(0).toUpperCase()}${was.slice(1)}, ${naechster} ${wann}`;
}

export function serieUnter(s: SerienStand): string {
  const heute = s.heute_geuebt ? 'Heute schon geübt.' : 'Heute noch nicht geübt.';
  if (s.aktuell === 0) return 'Löse heute eine Aufgabe, um die Serie zu starten.';
  if (s.laengste > s.aktuell) return `Bestmarke ${tage(s.laengste)}. ${heute}`;
  return `Persönliche Bestmarke. ${heute}`;
}

const RANG_FOLGE: (Rang | null)[] = [null, 'bronze', 'silber', 'gold'];

/** Erreichte nach Rang zuerst, dann offene nach Nähe zum Ziel */
export function erfolgeNachStand(liste: ErfolgStand[]): ErfolgStand[] {
  const gewicht = (e: ErfolgStand) =>
    e.erreicht ? 10 + RANG_FOLGE.indexOf(e.rang) : Math.min(1, e.wert / Math.max(1, e.ziel));
  return [...liste].sort((a, b) => gewicht(b) - gewicht(a));
}
