/*
 * Store für Aufgaben. Liste wird einmal geladen, Musterloesungen werden
 * lazy geladen und gecached. Details kommen immer frisch, weil sie vom
 * Fortschritt abhängen (gesperrt, Musterlösungen frei).
 */

import { aufgabenApi } from '../api/AufgabenApi';
import { ApiFehler } from '../api/HttpBase';
import type { AufgabeDetail, AufgabeKurz, Musterloesung } from '../types/Aufgabe';

class AufgabenStore {
  liste = $state<AufgabeKurz[]>([]);
  ladenListe = $state(false);
  fehler = $state<string | null>(null);

  musterCache = $state<Record<string, Musterloesung[]>>({});

  async ladeListe(): Promise<void> {
    this.ladenListe = true;
    this.fehler = null;
    try {
      this.liste = await aufgabenApi.liste();
    } catch (e) {
      this.fehler = (e as Error).message;
    } finally {
      this.ladenListe = false;
    }
  }

  /** null nur, wenn es die Aufgabe nicht gibt; andere Fehler gehen an den Aufrufer. */
  async ladeDetail(id: string): Promise<AufgabeDetail | null> {
    try {
      return await aufgabenApi.detail(id);
    } catch (e) {
      if (e instanceof ApiFehler && e.status === 404) return null;
      throw e;
    }
  }

  async ladeMusterloesungen(id: string): Promise<Musterloesung[]> {
    if (this.musterCache[id]) return this.musterCache[id];
    try {
      const ml = await aufgabenApi.musterloesungen(id);
      this.musterCache[id] = ml;
      return ml;
    } catch (e) {
      this.fehler = (e as Error).message;
      return [];
    }
  }

  findeKurz(id: string): AufgabeKurz | undefined {
    return this.liste.find((a) => a.id === id);
  }
}

export const aufgabenStore = new AufgabenStore();
