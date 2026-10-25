/*
 * Deckung einer CSS-Aufgabe: Ziel und eigenes Ergebnis werden auf der
 * Bühne gerastert und Bildpunkt für Bildpunkt verglichen.
 *
 * Gerastert wird als Bild über SVG-foreignObject: ein solches Bild führt
 * keine Skripte aus und lädt nichts nach. Beide Seiten laufen durch
 * denselben Weg im selben Browser, Schrift und Kantenglättung stimmen
 * also überein.
 *
 * Grund ist die häufigste Farbe am Rand des Zielbilds. Motiv sind alle
 * Punkte, die bei Ziel oder eigenem Bild nicht Grund sind; die Deckung
 * ist der Anteil davon, der übereinstimmt. Ein leeres Bild deckt so
 * nichts, auch wenn das Ziel nur ein kleiner Kreis auf großer Bühne ist.
 *
 * Das Abweichungsbild zeigt gleiche Punkte gedämpft, fehlende blau (das
 * eigene Bild zeigt Grund, wo das Ziel etwas zeigt) und zu viel oder
 * falsche Farbe rot.
 */
import { BUEHNE_B, BUEHNE_H, buehnenDokument } from './buehne';

/**
 * größte Abweichung je Farbkanal, die noch als gleich gilt. Klein, weil
 * beide Bilder im selben Browser entstehen; zarte Töne wie ein Grau mit
 * 60 % Deckkraft auf dem Grund liegen nur 8 bis 23 Stufen daneben.
 */
const TOLERANZ = 6;
const GEDAEMPFT = 0.35;
const FEHLT = [96, 165, 250];
const ZU_VIEL = [248, 81, 73];
// Steuerzeichen sind in XML verboten und würden das Bild brechen
const STEUERZEICHEN = /[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g;

export interface Vergleich {
  /** Anteil der Motivpunkte, die übereinstimmen, 0 bis 1 */
  deckung: number;
  abweichung: ImageData;
}

/** Rendert Markup und Stil auf der Bühne zu Bildpunkten */
export async function rastere(html: string, css: string): Promise<ImageData> {
  const dokument = new DOMParser().parseFromString(buehnenDokument(html, css.replace(STEUERZEICHEN, '')), 'text/html');
  const xhtml = new XMLSerializer().serializeToString(dokument.documentElement);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${BUEHNE_B}" height="${BUEHNE_H}">`
    + `<foreignObject width="100%" height="100%">${xhtml}</foreignObject></svg>`;
  const bild = new Image();
  bild.src = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
  await bild.decode();
  const leinwand = document.createElement('canvas');
  leinwand.width = BUEHNE_B;
  leinwand.height = BUEHNE_H;
  const g = leinwand.getContext('2d', { willReadFrequently: true });
  if (!g) throw new Error('Keine Zeichenfläche verfügbar');
  g.drawImage(bild, 0, 0);
  return g.getImageData(0, 0, BUEHNE_B, BUEHNE_H);
}

function aehnlich(a: Uint8ClampedArray, i: number, b: ArrayLike<number>, j: number): boolean {
  return Math.abs(a[i] - b[j]) <= TOLERANZ
    && Math.abs(a[i + 1] - b[j + 1]) <= TOLERANZ
    && Math.abs(a[i + 2] - b[j + 2]) <= TOLERANZ
    && Math.abs(a[i + 3] - b[j + 3]) <= TOLERANZ;
}

/** häufigste Farbe der Randpunkte (RGBA) */
function randfarbe(bild: ImageData): number[] {
  const { width: b, height: h, data } = bild;
  const zaehler = new Map<number, number>();
  const zaehle = (x: number, y: number) => {
    const i = (y * b + x) * 4;
    const schluessel = ((data[i] << 24) | (data[i + 1] << 16) | (data[i + 2] << 8) | data[i + 3]) >>> 0;
    zaehler.set(schluessel, (zaehler.get(schluessel) ?? 0) + 1);
  };
  for (let x = 0; x < b; x++) {
    zaehle(x, 0);
    zaehle(x, h - 1);
  }
  for (let y = 1; y < h - 1; y++) {
    zaehle(0, y);
    zaehle(b - 1, y);
  }
  let beste = 0;
  let anzahl = -1;
  for (const [schluessel, n] of zaehler) {
    if (n > anzahl) [beste, anzahl] = [schluessel, n];
  }
  return [beste >>> 24, (beste >>> 16) & 255, (beste >>> 8) & 255, beste & 255];
}

/** Vergleicht das eigene Bild mit dem Ziel */
export function vergleiche(ziel: ImageData, eigen: ImageData): Vergleich {
  const a = ziel.data;
  const b = eigen.data;
  const grund = randfarbe(ziel);
  const abweichung = new ImageData(ziel.width, ziel.height);
  const d = abweichung.data;
  let motiv = 0;
  let gleich = 0;
  for (let i = 0; i < a.length; i += 4) {
    const eigenGrund = aehnlich(b, i, grund, 0);
    const imMotiv = !eigenGrund || !aehnlich(a, i, grund, 0);
    const passt = aehnlich(a, i, b, i);
    if (imMotiv) motiv += 1;
    if (imMotiv && passt) gleich += 1;
    if (passt) {
      d[i] = a[i] * GEDAEMPFT;
      d[i + 1] = a[i + 1] * GEDAEMPFT;
      d[i + 2] = a[i + 2] * GEDAEMPFT;
    } else {
      const farbe = eigenGrund ? FEHLT : ZU_VIEL;
      d[i] = farbe[0];
      d[i + 1] = farbe[1];
      d[i + 2] = farbe[2];
    }
    d[i + 3] = 255;
  }
  return { deckung: motiv ? gleich / motiv : 1, abweichung };
}
