/*
 * Store fuer Aufgaben. Liste wird einmal geladen, Detail-Daten und
 * Musterloesungen werden lazy geladen und gecached.
 */

import { aufgabenApi } from '../api/AufgabenApi';
import type { AufgabeDetail, AufgabeKurz, Musterloesung } from '../types/Aufgabe';

class AufgabenStore {
  liste = $state<AufgabeKurz[]>([]);
  ladenListe = $state(false);
  fehler = $state<string | null>(null);

  detailCache = $state<Record<string, AufgabeDetail>>({});
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

  async ladeDetail(id: string): Promise<AufgabeDetail | null> {
    if (this.detailCache[id]) return this.detailCache[id];
    try {
      const detail = await aufgabenApi.detail(id);
      this.detailCache[id] = detail;
      return detail;
    } catch (e) {
      this.fehler = (e as Error).message;
      return null;
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
