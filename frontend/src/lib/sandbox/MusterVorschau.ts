/*
 * Live-Vorschau der Muster-Jagd. Markiert im Worker; braucht er länger
 * als die Grenze, wird er beendet und beim nächsten Auftrag neu gestartet.
 */
import type { Markierung } from '../muster';

export const ZU_GIERIG = 'zu_gierig';

export class MusterVorschau {
  private arbeiter: Worker | null = null;
  private nr = 0;

  constructor(private grenzeMs = 400) {}

  markiere(muster: string, flags: string, zeilen: string[]): Promise<Markierung | typeof ZU_GIERIG> {
    const arbeiter = (this.arbeiter ??= new Worker(new URL('./muster.worker.ts', import.meta.url), { type: 'module' }));
    const nr = ++this.nr;
    return new Promise((fertig) => {
      const uhr = setTimeout(() => {
        arbeiter.removeEventListener('message', antwort);
        arbeiter.terminate();
        if (this.arbeiter === arbeiter) this.arbeiter = null;
        fertig(ZU_GIERIG);
      }, this.grenzeMs);
      const antwort = (e: MessageEvent<{ nr: number; markierung: Markierung }>) => {
        if (e.data.nr !== nr) return;
        clearTimeout(uhr);
        arbeiter.removeEventListener('message', antwort);
        fertig(e.data.markierung);
      };
      arbeiter.addEventListener('message', antwort);
      arbeiter.postMessage({ nr, muster, flags, zeilen });
    });
  }

  beenden(): void {
    this.arbeiter?.terminate();
    this.arbeiter = null;
  }
}
