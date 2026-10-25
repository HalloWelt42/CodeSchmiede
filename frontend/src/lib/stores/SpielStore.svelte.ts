/*
 * Spielstand für Kopf, Startseite und Erfolge. ProgressStore lädt ihn
 * mit, sobald sich der Fortschritt ändert (nach jeder Abgabe).
 */
import {
  spielApi,
  type ErfolgsListe,
  type LevelStand,
  type SpielUebersicht,
  type Spielstand,
  type StufenStand,
} from '../api/SpielApi';

/** Anteil der aktuellen Stufe in Prozent, für Ring und Balken. */
export function stufenAnteil(s: StufenStand): number {
  const spanne = s.bis - s.ab;
  return spanne > 0 ? Math.min(100, ((s.punkte - s.ab) / spanne) * 100) : 100;
}

class SpielStore {
  stand = $state<Spielstand | null>(null);
  erfolge = $state<ErfolgsListe | null>(null);
  spiele = $state<SpielUebersicht[]>([]);
  fehler = $state<string | null>(null);

  async laden(): Promise<void> {
    try {
      const [stand, erfolge, spiele] = await Promise.all([spielApi.stand(), spielApi.erfolge(), spielApi.spiele()]);
      this.stand = stand;
      this.erfolge = erfolge;
      this.spiele = spiele;
      this.fehler = null;
    } catch (e) {
      this.fehler = (e as Error).message;
    }
  }

  /** Spiel und Level einer Aufgabe, wenn sie ein Level ist */
  levelVon(aufgabeId: string): { spiel: SpielUebersicht; level: LevelStand } | null {
    for (const spiel of this.spiele) {
      const level = spiel.levels.find((l) => l.id === aufgabeId);
      if (level) return { spiel, level };
    }
    return null;
  }
}

export const spielStore = new SpielStore();
