/*
 * Ableitungen für Pfade, geteilt von Rechner- und Telefonansicht:
 * Sprache (aus den Aufgaben des Pfads), Fortschritt und Stand.
 */
import { aufgabenStore } from './stores/AufgabenStore.svelte';
import { progressStore } from './stores/ProgressStore.svelte';
import type { Pfad } from './types/Aufgabe';

export type PfadStand = 'offen' | 'begonnen' | 'fertig';

/** Häufigste Sprache der Aufgaben im Pfad; leer, solange die Liste fehlt */
export function pfadSprache(p: Pfad): string {
  const zaehler = new Map<string, number>();
  for (const id of p.reihenfolge) {
    const s = aufgabenStore.findeKurz(id)?.sprache;
    if (s) zaehler.set(s, (zaehler.get(s) ?? 0) + 1);
  }
  return [...zaehler].sort((a, b) => b[1] - a[1])[0]?.[0] ?? '';
}

export function pfadGeloest(p: Pfad): number {
  return p.reihenfolge.filter((id) => progressStore.status(id) === 'geloest').length;
}

export function pfadStand(p: Pfad): PfadStand {
  const g = pfadGeloest(p);
  if (g === 0 && !p.reihenfolge.some((id) => progressStore.status(id) === 'in_arbeit')) return 'offen';
  return g === p.reihenfolge.length ? 'fertig' : 'begonnen';
}

export function pfadProzent(p: Pfad): number {
  return p.reihenfolge.length ? (pfadGeloest(p) / p.reihenfolge.length) * 100 : 0;
}

/** Pfade nach Sprache gruppiert, Gruppen in der Reihenfolge der Konfiguration */
export function nachSprache(pfade: Pfad[], reihenfolge: string[]): [string, Pfad[]][] {
  const gruppen = new Map<string, Pfad[]>();
  for (const p of pfade) {
    const s = pfadSprache(p);
    gruppen.set(s, [...(gruppen.get(s) ?? []), p]);
  }
  const rang = (s: string): number => {
    const i = reihenfolge.indexOf(s);
    return i < 0 ? reihenfolge.length : i;
  };
  return [...gruppen].sort((a, b) => rang(a[0]) - rang(b[0]));
}
