/*
 * Hauptbereiche der App -- einzige Liste für Seitenleiste (Rechner) und
 * Reiterleiste (Telefon). `telefon: false` hält einen Bereich am Rechner.
 */
import type { Route } from './stores/RouteStore.svelte';

export interface Bereich {
  id: Route;
  titel: string;
  icon: string;
  telefon: boolean;
}

export const BEREICHE: Bereich[] = [
  { id: 'dashboard', titel: 'Dashboard', icon: 'fa-house', telefon: true },
  { id: 'aufgaben', titel: 'Aufgaben', icon: 'fa-list-check', telefon: true },
  { id: 'pfade', titel: 'Pfade', icon: 'fa-route', telefon: true },
  { id: 'verwaltung', titel: 'Verwaltung', icon: 'fa-table-cells-large', telefon: false },
];

/** Eine geöffnete Aufgabe gehört zum Bereich Aufgaben. */
export function istAktiv(bereich: Bereich, aktiv: Route): boolean {
  return bereich.id === aktiv || (bereich.id === 'aufgaben' && aktiv === 'aufgabe');
}
