/*
 * Schrift vergrößern: alle Schriftstufen (--fs-*, global.css) wachsen mit --schrift-zoom, das Layout bleibt und fließt
 * mit (kein CSS zoom, das schob die Seite aus dem Bild und verschob die Klicks im Editor). Je Gerät gemerkt.
 */

const SCHLUESSEL = 'codeschmiede.zoom';
const STUFEN = [0.9, 1, 1.1, 1.25, 1.4, 1.6] as const;
const NORMAL = STUFEN.indexOf(1);

class ZoomStore {
  stufe = $state<number>(NORMAL);

  get faktor(): number {
    return STUFEN[this.stufe];
  }

  get prozent(): number {
    return Math.round(this.faktor * 100);
  }

  get kleinste(): boolean {
    return this.stufe === 0;
  }

  get groesste(): boolean {
    return this.stufe === STUFEN.length - 1;
  }

  init(): void {
    const gespeichert = Number(localStorage.getItem(SCHLUESSEL));
    const i = STUFEN.indexOf(gespeichert as (typeof STUFEN)[number]);
    if (i >= 0) this.stufe = i;
    this.anwenden();
  }

  groesser(): void {
    this.setze(Math.min(this.stufe + 1, STUFEN.length - 1));
  }

  kleiner(): void {
    this.setze(Math.max(this.stufe - 1, 0));
  }

  zuruecksetzen(): void {
    this.setze(NORMAL);
  }

  private setze(stufe: number): void {
    this.stufe = stufe;
    localStorage.setItem(SCHLUESSEL, String(this.faktor));
    this.anwenden();
  }

  private anwenden(): void {
    document.documentElement.style.setProperty('--schrift-zoom', String(this.faktor));
  }
}

export const zoom = new ZoomStore();
