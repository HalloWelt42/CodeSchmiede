/*
 * Eine Sitzung des Debuggers in der Aufgabenansicht: der aufgezeichnete Lauf, der Code, aus dem er stammt, und die
 * Eingabe des Probelaufs. Ändert sich der Code danach, ist die Aufzeichnung veraltet; "neu" zeichnet mit derselben
 * Eingabe noch einmal auf. Die Haltepunkte gehören dem Editor und überdauern die Sitzung.
 */
import { submissionsApi } from '../api/SubmissionsApi';
import type { Debuglauf } from '../types/Aufzeichnung';

export class DebugSitzung {
  lauf = $state<Debuglauf | null>(null);
  /** Code, aus dem der Lauf stammt */
  code = $state('');
  /** Aufruf wie im Probelauf, etwa nur_gerade([1, 2]); bei Programmen null */
  aufruf = $state<string | null>(null);
  laeuft = $state(false);
  fehler = $state<string | null>(null);
  haltepunkte = $state<number[]>([]);
  /** zählt die Läufe; ein neuer beginnt am ersten Haltepunkt */
  nummer = $state(0);
  private aufgabeId = '';
  private eingabe: unknown[] = [];

  get aktiv(): boolean {
    return this.lauf !== null || this.laeuft || this.fehler !== null;
  }

  veraltet(code: string): boolean {
    return this.lauf !== null && code !== this.code;
  }

  async starten(aufgabeId: string, code: string, eingabe: unknown[], aufruf: string | null): Promise<void> {
    this.aufgabeId = aufgabeId;
    this.eingabe = eingabe;
    this.aufruf = aufruf;
    await this.neu(code);
  }

  async neu(code: string): Promise<void> {
    this.laeuft = true;
    this.fehler = null;
    try {
      this.lauf = await submissionsApi.debuggen(this.aufgabeId, code, this.eingabe);
      this.code = code;
      this.nummer += 1;
    } catch (e) {
      this.lauf = null;
      this.fehler = e instanceof Error ? e.message : String(e);
    } finally {
      this.laeuft = false;
    }
  }

  beenden(): void {
    this.lauf = null;
    this.fehler = null;
  }
}
