/*
 * Store für Progress-Daten. Lädt die Endpunkte parallel und mit ihnen den
 * daraus abgeleiteten Spielstand; `ladeAlles()` nach jeder Abgabe.
 */

import {
  progressApi,
  type GesamtFortschritt,
  type ProgressEintrag,
  type ProgressStatus,
  type Tagesziel,
} from '../api/ProgressApi';
import { spielStore } from './SpielStore.svelte';

class ProgressStore {
  gesamt = $state<GesamtFortschritt | null>(null);
  heute = $state<Tagesziel | null>(null);
  proAufgabe = $state<Record<string, ProgressEintrag>>({});
  laden = $state(false);
  fehler = $state<string | null>(null);

  async ladeAlles(): Promise<void> {
    this.laden = true;
    this.fehler = null;
    try {
      const [g, h, a] = await Promise.all([
        progressApi.gesamt(),
        progressApi.heute(),
        progressApi.alleAufgaben(),
        spielStore.laden(),
      ]);
      this.gesamt = g;
      this.heute = h;
      this.proAufgabe = a;
    } catch (e) {
      this.fehler = (e as Error).message;
    } finally {
      this.laden = false;
    }
  }

  status(aufgabeId: string): ProgressStatus {
    return this.proAufgabe[aufgabeId]?.status ?? 'neu';
  }
}

export const progressStore = new ProgressStore();
