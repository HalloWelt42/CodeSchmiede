/*
 * FassungStore -- neue Fassung auf dem Server: nie ein hartes Neuladen
 * verlangen. Die Startseite kommt ohne Zwischenspeicher (nginx), Skripte
 * und Gestaltung tragen Prüfsummen im Namen. Meldet /api/healthz eine
 * andere Fassung als die eingebaute, lädt die Seite von selbst neu: in
 * den ersten Sekunden nach dem Start sofort, später beim nächsten
 * Seitenwechsel oder wenn das Fenster wieder nach vorn kommt. Nie,
 * solange eine Ansicht eine Sperre hält (laufende Prüfung, ungeprüfter
 * Code, offener Editor). Dazwischen steht ein Band mit Knopf. Je
 * Serverfassung nur ein selbsttätiger Versuch (Merker in der Sitzung),
 * damit ein hängender Zwischenspeicher keine Schleife auslöst.
 */

import { tick, untrack } from 'svelte';
import { systemApi } from '../api/SystemApi';

export const OBERFLAECHE_FASSUNG = __APP_VERSION__;
const MERKER = 'codeschmiede.neu_geladen';
const START_FENSTER_MS = 10_000;
const PRUEFEN_MS = 60_000;

export type Anlass = 'start' | 'takt' | 'ortswechsel' | 'sichtbar';

class FassungStore {
  /** Fassung, die der Server zuletzt gemeldet hat (null: noch keine Antwort). */
  server = $state<string | null>(null);
  private sperren = $state(0);

  /** Neue Fassung auf dem Server, oder null, wenn die Oberfläche aktuell ist. */
  get neu(): string | null {
    return this.server !== null && this.server !== OBERFLAECHE_FASSUNG ? this.server : null;
  }

  /** Nichts offen, was ein Neuladen abbrechen würde. */
  ruhig(): boolean {
    return this.sperren === 0;
  }

  /**
   * Eine Ansicht hält eine Sperre, solange bei ihr etwas verloren ginge.
   * Gibt die Freigabe zurück; passt als Rückgabe eines $effect.
   */
  halten(): () => void {
    // untrack: der Zähler darf nicht zur Abhängigkeit des aufrufenden
    // $effect werden, sonst stoßen sich die Ansichten gegenseitig an.
    untrack(() => (this.sperren += 1));
    let frei = false;
    return () => {
      if (frei) return;
      frei = true;
      untrack(() => (this.sperren -= 1));
    };
  }

  vielleichtNeuLaden(anlass: Anlass): void {
    const neu = this.neu;
    if (!neu || anlass === 'takt' || !this.ruhig()) return;
    if (anlass === 'start' && performance.now() > START_FENSTER_MS) return;
    if (this.erlaubt(neu)) location.reload();
  }

  /** Erst nach dem Umbau der Ansicht prüfen: dann hat die alte ihre Sperren gelöst. */
  nachOrtswechsel(): void {
    void tick().then(() => this.vielleichtNeuLaden('ortswechsel'));
  }

  async pruefen(anlass: Anlass): Promise<void> {
    try {
      this.server = (await systemApi.gesundheit()).version;
    } catch {
      return; // ohne Verbindung bleibt es beim alten Stand
    }
    this.vielleichtNeuLaden(anlass);
  }

  verfolgen(): () => void {
    void this.pruefen('start');
    const takt = setInterval(() => void this.pruefen('takt'), PRUEFEN_MS);
    const sichtbar = (): void => {
      if (document.visibilityState === 'visible') void this.pruefen('sichtbar');
    };
    document.addEventListener('visibilitychange', sichtbar);
    return () => {
      clearInterval(takt);
      document.removeEventListener('visibilitychange', sichtbar);
    };
  }

  private erlaubt(neu: string): boolean {
    try {
      if (sessionStorage.getItem(MERKER) === neu) return false;
      sessionStorage.setItem(MERKER, neu);
    } catch {
      // ohne Sitzungsspeicher kein Merker: dann lieber einmal laden als nie
    }
    return true;
  }
}

export const fassung = new FassungStore();
