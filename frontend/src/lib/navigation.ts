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
  { id: 'kurs', titel: 'Kurs', icon: 'fa-graduation-cap', telefon: true },
  { id: 'aufgaben', titel: 'Aufgaben', icon: 'fa-list-check', telefon: true },
  { id: 'pfade', titel: 'Pfade', icon: 'fa-route', telefon: true },
  { id: 'spiele', titel: 'Spiele', icon: 'fa-gamepad', telefon: true },
  { id: 'verwaltung', titel: 'Verwaltung', icon: 'fa-table-cells-large', telefon: false },
];

/** Unterseiten und ihr Bereich: eine geöffnete Aufgabe gehört zu Aufgaben, die Erfolge zum Dashboard, Einführung,
 * Kurztest und Merkblatt zum Kurs. */
const GEHOERT_ZU: Partial<Record<Route, Route>> = {
  aufgabe: 'aufgaben', erfolge: 'dashboard', einfuehrung: 'kurs', kurztest: 'kurs', merkblatt: 'kurs',
};

export function istAktiv(bereich: Bereich, aktiv: Route): boolean {
  return bereich.id === aktiv || GEHOERT_ZU[aktiv] === bereich.id;
}
