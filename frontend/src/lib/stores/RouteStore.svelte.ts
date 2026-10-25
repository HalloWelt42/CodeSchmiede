/*
 * Hash-basiertes Routing.
 * Routen:
 *   #dashboard           -> Dashboard
 *   #erfolge             -> alle Erfolge
 *   #aufgaben            -> Liste aller Aufgaben
 *   #pfade               -> Liste aller Pfade
 *   #spiele              -> Spielebereich
 *   #verwaltung          -> Verwaltungsübersicht aller Aufgaben (Admin)
 *   #aufgabe/<id>        -> Detail-Ansicht einer Aufgabe
 */

import { fassung } from './FassungStore.svelte';

export type Route = 'dashboard' | 'erfolge' | 'aufgaben' | 'pfade' | 'spiele' | 'verwaltung' | 'aufgabe';

/** Routen ohne Parameter, deren Name gleich dem Hash ist */
const EINFACH: Route[] = ['erfolge', 'aufgaben', 'pfade', 'spiele', 'verwaltung'];

class RouteStore {
  aktiv = $state<Route>('dashboard');
  aufgabeId = $state<string | null>(null);

  init(): void {
    this.lese();
    window.addEventListener('hashchange', () => {
      this.lese();
      fassung.nachOrtswechsel();
    });
  }

  setze(ziel: Route, aufgabeId?: string): void {
    if (ziel === 'aufgabe' && aufgabeId) {
      window.location.hash = `#aufgabe/${aufgabeId}`;
    } else {
      window.location.hash = `#${ziel}`;
    }
  }

  private lese(): void {
    const hash = window.location.hash.replace(/^#/, '');
    if (hash.startsWith('aufgabe/')) {
      this.aktiv = 'aufgabe';
      this.aufgabeId = hash.slice('aufgabe/'.length);
    } else if ((EINFACH as string[]).includes(hash)) {
      this.aktiv = hash as Route;
      this.aufgabeId = null;
    } else {
      this.aktiv = 'dashboard';
      this.aufgabeId = null;
    }
  }
}

export const route = new RouteStore();
