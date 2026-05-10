/*
 * Hash-basiertes Routing.
 * Routen:
 *   #dashboard           -> Dashboard
 *   #aufgaben            -> Liste aller Aufgaben
 *   #pfade               -> Liste aller Pfade
 *   #verwaltung          -> Verwaltungsübersicht aller Aufgaben (Admin)
 *   #aufgabe/<id>        -> Detail-Ansicht einer Aufgabe
 */

export type Route = 'dashboard' | 'aufgaben' | 'pfade' | 'verwaltung' | 'aufgabe';

class RouteStore {
  aktiv = $state<Route>('dashboard');
  aufgabeId = $state<string | null>(null);

  init(): void {
    this.lese();
    window.addEventListener('hashchange', () => this.lese());
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
    } else if (hash === 'aufgaben') {
      this.aktiv = 'aufgaben';
      this.aufgabeId = null;
    } else if (hash === 'pfade') {
      this.aktiv = 'pfade';
      this.aufgabeId = null;
    } else if (hash === 'verwaltung') {
      this.aktiv = 'verwaltung';
      this.aufgabeId = null;
    } else {
      this.aktiv = 'dashboard';
      this.aufgabeId = null;
    }
  }
}

export const route = new RouteStore();
