/*
 * Spielstand für Kopf, Startseite und Erfolge. ProgressStore lädt ihn
 * mit, sobald sich der Fortschritt ändert (nach jeder Abgabe).
 */
import { spielApi, type ErfolgsListe, type Spielstand, type StufenStand } from '../api/SpielApi';

/** Anteil der aktuellen Stufe in Prozent, für Ring und Balken. */
export function stufenAnteil(s: StufenStand): number {
  const spanne = s.bis - s.ab;
  return spanne > 0 ? Math.min(100, ((s.punkte - s.ab) / spanne) * 100) : 100;
}

class SpielStore {
  stand = $state<Spielstand | null>(null);
  erfolge = $state<ErfolgsListe | null>(null);
  fehler = $state<string | null>(null);

  async laden(): Promise<void> {
    try {
      const [stand, erfolge] = await Promise.all([spielApi.stand(), spielApi.erfolge()]);
      this.stand = stand;
      this.erfolge = erfolge;
      this.fehler = null;
    } catch (e) {
      this.fehler = (e as Error).message;
    }
  }
}

export const spielStore = new SpielStore();
