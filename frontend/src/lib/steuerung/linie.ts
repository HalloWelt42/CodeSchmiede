/*
 * Linienzug eines Wegs: Punkt bei einer Strecke, davor und dahinter geht es geradeaus weiter. Dieselbe Rechnung wie
 * Linie.punkt in backend/src/codeschmiede/steuerung/ampel_welt.py; die Strecken kommen von dort.
 */
import type { Punkt } from '../types/Ampel';

export class Linie {
  private bis: number[] = [0];
  readonly laenge: number;

  constructor(private punkte: Punkt[]) {
    for (let i = 1; i < punkte.length; i++) {
      const [x1, y1] = punkte[i - 1];
      const [x2, y2] = punkte[i];
      this.bis.push(this.bis[i - 1] + Math.hypot(x2 - x1, y2 - y1));
    }
    this.laenge = this.bis[this.bis.length - 1];
  }

  punkt(s: number): Punkt {
    const p = this.punkte;
    let k = 0;
    if (s >= this.laenge) k = p.length - 2;
    else if (s > 0) while (this.bis[k + 1] < s) k++;
    const [x1, y1] = p[k];
    const [x2, y2] = p[k + 1];
    const stueck = this.bis[k + 1] - this.bis[k] || 1;
    const f = (s - this.bis[k]) / stueck;
    return [x1 + (x2 - x1) * f, y1 + (y2 - y1) * f];
  }
}
