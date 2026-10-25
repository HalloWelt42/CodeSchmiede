/*
 * Routing über echte Pfade (History API). Der Server liefert für jeden
 * Ort außerhalb von /api die Startseite aus (backend/.../oberflaeche.py).
 * Pfade:
 *   /                    -> Dashboard
 *   /erfolge             -> alle Erfolge
 *   /aufgaben            -> Liste aller Aufgaben
 *   /pfade               -> Liste aller Pfade
 *   /spiele              -> Spielebereich
 *   /verwaltung          -> Verwaltungsübersicht aller Aufgaben (Admin)
 *   /aufgabe/<id>        -> Detail-Ansicht einer Aufgabe
 *
 * Alte Adressen mit # (#aufgabe/<id>, #pfade ...) werden beim Laden auf
 * den Pfad umgeschrieben, damit Lesezeichen weiter funktionieren.
 */

import { fassung } from './FassungStore.svelte';

export type Route = 'dashboard' | 'erfolge' | 'aufgaben' | 'pfade' | 'spiele' | 'verwaltung' | 'aufgabe';

/** Routen ohne Parameter, deren Pfad ihr Name ist */
const EINFACH: Route[] = ['erfolge', 'aufgaben', 'pfade', 'spiele', 'verwaltung'];

/** Pfad einer Route, etwa für href */
export function pfadVon(ziel: Route, aufgabeId?: string): string {
  if (ziel === 'aufgabe' && aufgabeId) return `/aufgabe/${encodeURIComponent(aufgabeId)}`;
  if (ziel === 'dashboard' || ziel === 'aufgabe') return '/';
  return `/${ziel}`;
}

class RouteStore {
  aktiv = $state<Route>('dashboard');
  aufgabeId = $state<string | null>(null);

  init(): void {
    this.alteAdresseUmschreiben();
    this.lese();
    window.addEventListener('popstate', () => this.ortGewechselt());
  }

  setze(ziel: Route, aufgabeId?: string): void {
    const pfad = pfadVon(ziel, aufgabeId);
    if (pfad !== window.location.pathname) window.history.pushState(null, '', pfad);
    this.ortGewechselt();
  }

  private ortGewechselt(): void {
    this.lese();
    fassung.nachOrtswechsel();
  }

  private alteAdresseUmschreiben(): void {
    const hash = window.location.hash.replace(/^#/, '');
    if (!hash) return;
    const pfad = hash.startsWith('aufgabe/') ? `/${hash}` : (EINFACH as string[]).includes(hash) ? `/${hash}` : '/';
    window.history.replaceState(null, '', pfad);
  }

  private lese(): void {
    const teile = window.location.pathname.split('/').filter(Boolean);
    if (teile[0] === 'aufgabe' && teile[1]) {
      this.aktiv = 'aufgabe';
      this.aufgabeId = decodeURIComponent(teile[1]);
    } else if (teile.length === 1 && (EINFACH as string[]).includes(teile[0])) {
      this.aktiv = teile[0] as Route;
      this.aufgabeId = null;
    } else {
      this.aktiv = 'dashboard';
      this.aufgabeId = null;
    }
  }
}

export const route = new RouteStore();
