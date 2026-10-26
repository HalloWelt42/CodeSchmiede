/*
 * Spielt einen aufgezeichneten Ablauf ab: Bild für Bild im Takt der Aufzeichnung, mal Tempo. Gemeinsam für die
 * Steuerungsspiele; was ein Bild zeigt, weiß die Szene.
 */

export const TEMPI = [1, 2, 4, 8] as const;

export class Abspieler {
  /** Nummer des gezeigten Bilds, -1 vor dem ersten */
  bild = $state(-1);
  laeuft = $state(false);
  tempo = $state<number>(2);
  anzahl = $state(0);
  private uhr: ReturnType<typeof setInterval> | undefined;

  /** takt: Sekunden je Bild der Aufzeichnung; beiBild: läuft für jedes Bild beim Abspielen (Ton) */
  constructor(
    private takt: number,
    private beiBild: (nr: number) => void = () => {},
  ) {}

  get fertig(): boolean {
    return this.bild >= this.anzahl - 1;
  }

  laden(anzahl: number, ab = -1): void {
    this.anhalten();
    this.anzahl = anzahl;
    this.bild = Math.min(ab, anzahl - 1);
  }

  abspielen(): void {
    if (this.anzahl === 0) return;
    this.anhalten();
    if (this.fertig) this.bild = -1;
    this.laeuft = true;
    this.uhr = setInterval(() => {
      this.bild += 1;
      this.beiBild(this.bild);
      if (this.fertig) this.anhalten();
    }, (this.takt * 1000) / this.tempo);
  }

  anhalten(): void {
    clearInterval(this.uhr);
    this.uhr = undefined;
    this.laeuft = false;
  }

  springe(bild: number): void {
    this.anhalten();
    this.bild = Math.max(-1, Math.min(this.anzahl - 1, bild));
  }

  setzeTempo(tempo: number): void {
    this.tempo = tempo;
    if (this.laeuft) this.abspielen();
  }
}
