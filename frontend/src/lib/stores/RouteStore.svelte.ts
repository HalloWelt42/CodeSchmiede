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
 *   /kurs                -> Kursübersicht
 *   /kurs/<id>           -> Einführung eines Kapitels
 *   /kurs/<id>/kurztest  -> Kurztest zum Überspringen
 *   /kurs/<id>/merkblatt -> Merkblatt des Kapitels
 *
 * Alte Adressen mit # (#aufgabe/<id>, #pfade ...) werden beim Laden auf
 * den Pfad umgeschrieben, damit Lesezeichen weiter funktionieren.
 */

import { fassung } from './FassungStore.svelte';

export type Route = 'dashboard' | 'erfolge' | 'kurs' | 'einfuehrung' | 'kurztest' | 'merkblatt' | 'aufgaben' | 'pfade' | 'spiele' | 'verwaltung' | 'aufgabe';

/** Routen mit einer Kennung im Pfad */
const KURS_UNTERSEITEN: Partial<Record<Route, string>> = { einfuehrung: '', kurztest: '/kurztest', merkblatt: '/merkblatt' };

/** Routen ohne Parameter, deren Pfad ihr Name ist */
const EINFACH: Route[] = ['erfolge', 'kurs', 'aufgaben', 'pfade', 'spiele', 'verwaltung'];

/** Pfad einer Route, etwa für href */
export function pfadVon(ziel: Route, kennung?: string): string {
  if (ziel === 'aufgabe' && kennung) return `/aufgabe/${encodeURIComponent(kennung)}`;
  const unter = KURS_UNTERSEITEN[ziel];
  if (unter !== undefined) return kennung ? `/kurs/${encodeURIComponent(kennung)}${unter}` : '/kurs';
  if (ziel === 'dashboard' || ziel === 'aufgabe') return '/';
  return `/${ziel}`;
}

class RouteStore {
  aktiv = $state<Route>('dashboard');
  aufgabeId = $state<string | null>(null);
  /** Kennung der Einführung bei Einführung, Kurztest und Merkblatt */
  kursId = $state<string | null>(null);

  init(): void {
    this.alteAdresseUmschreiben();
    this.lese();
    window.addEventListener('popstate', () => this.ortGewechselt());
  }

  setze(ziel: Route, kennung?: string): void {
    const pfad = pfadVon(ziel, kennung);
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
    this.kursId = null;
    if (teile[0] === 'aufgabe' && teile[1]) {
      this.aktiv = 'aufgabe';
      this.aufgabeId = decodeURIComponent(teile[1]);
    } else if (teile[0] === 'kurs' && teile[1]) {
      this.aktiv = teile[2] === 'kurztest' ? 'kurztest' : teile[2] === 'merkblatt' ? 'merkblatt' : 'einfuehrung';
      this.kursId = decodeURIComponent(teile[1]);
      this.aufgabeId = null;
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
