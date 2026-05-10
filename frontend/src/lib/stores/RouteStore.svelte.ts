/*
 * Hash-basiertes Routing. Rein deklarativ: Komponenten lesen `route.aktiv`,
 * Navigation ueber `route.setze(...)`. Initialisierung beim Mount.
 */

export type Route = 'dashboard' | 'aufgaben' | 'pfade';

const ERLAUBT: Route[] = ['dashboard', 'aufgaben', 'pfade'];

class RouteStore {
  aktiv = $state<Route>('dashboard');

  init(): void {
    this.lese();
    window.addEventListener('hashchange', () => this.lese());
  }

  setze(ziel: Route): void {
    window.location.hash = `#${ziel}`;
  }

  private lese(): void {
    const hash = window.location.hash.replace(/^#/, '') as Route;
    this.aktiv = ERLAUBT.includes(hash) ? hash : 'dashboard';
  }
}

export const route = new RouteStore();
