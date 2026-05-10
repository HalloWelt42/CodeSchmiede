/*
 * Store fuer Progress-Daten. Laedt initial alle vier Endpunkte parallel,
 * stellt einen `neuLaden()`-Trigger zur Verfuegung (z.B. nach Submission).
 */

import {
  progressApi,
  type GesamtFortschritt,
  type ProgressEintrag,
  type ProgressStatus,
  type Streak,
  type Tagesziel,
} from '../api/ProgressApi';

class ProgressStore {
  gesamt = $state<GesamtFortschritt | null>(null);
  heute = $state<Tagesziel | null>(null);
  streak = $state<Streak | null>(null);
  proAufgabe = $state<Record<string, ProgressEintrag>>({});
  laden = $state(false);
  fehler = $state<string | null>(null);

  async ladeAlles(): Promise<void> {
    this.laden = true;
    this.fehler = null;
    try {
      const [g, h, s, a] = await Promise.all([
        progressApi.gesamt(),
        progressApi.heute(),
        progressApi.streak(),
        progressApi.alleAufgaben(),
      ]);
      this.gesamt = g;
      this.heute = h;
      this.streak = s;
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
