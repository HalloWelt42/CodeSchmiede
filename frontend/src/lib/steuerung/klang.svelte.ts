/*
 * Klänge der Steuerungsspiele (aus dem Medienpool, CC0; Quellen in docs/KLAENGE.md). Ton ist aus, bis
 * man ihn einschaltet; die Wahl merkt sich der Browser.
 */

export type Klangname = 'taster' | 'ticken' | 'matsch' | 'blechschaden' | 'blech_klein' | 'motor' | 'gong' | 'tuer_auf' | 'tuer_zu';

const SCHLUESSEL = 'codeschmiede.steuerung.ton';
const LAUTSTAERKE = 0.45;

class Klang {
  an = $state(false);
  private dateien = new Map<Klangname, HTMLAudioElement>();

  constructor() {
    try {
      this.an = localStorage.getItem(SCHLUESSEL) === '1';
    } catch {
      // ohne Speicher bleibt der Ton aus
    }
  }

  umschalten(): void {
    this.an = !this.an;
    try {
      localStorage.setItem(SCHLUESSEL, this.an ? '1' : '0');
    } catch {
      // nur für diese Sitzung
    }
  }

  spiele(name: Klangname): void {
    if (!this.an) return;
    let audio = this.dateien.get(name);
    if (!audio) {
      audio = new Audio(`/klaenge/${name}.m4a`);
      audio.volume = LAUTSTAERKE;
      this.dateien.set(name, audio);
    }
    audio.currentTime = 0;
    audio.play().catch(() => {});
  }
}

export const klang = new Klang();
