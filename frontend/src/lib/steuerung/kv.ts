/*
 * KV-Werkstatt in der Oberfläche: die Formel als Zeilen lesen und schreiben, das Raster in Gray-Reihenfolge und
 * Blöcke zwischen Feldern und Termen umrechnen. Die Formel ist die eine Wahrheit (je Ausgang `e = !B !D + C !D`);
 * was stimmt, rechnet das Backend (backend/src/codeschmiede/steuerung/kv.py).
 */

/** je Eingang 1, 0 oder null (egal) */
export type Stellen = (0 | 1 | null)[];

export interface FormelZeile {
  art: 'formel';
  name: string;
  terme: Stellen[];
}
export interface TextZeile {
  art: 'text';
  text: string;
}
export type Zeile = FormelZeile | TextZeile;

const ZEILE = /^(\w+)\s*=\s*(.*)$/;

/** Liest die Zeilen; was sich nicht lesen lässt, bleibt Text (der Server meldet den Fehler). */
export function zerlege(text: string, eingaenge: string[], ausgaenge: string[]): Zeile[] {
  return text.split('\n').map((roh): Zeile => {
    const zeile = roh.split('#')[0].trim();
    const m = ZEILE.exec(zeile);
    if (!m || !ausgaenge.includes(m[1])) return { art: 'text', text: roh };
    const terme: Stellen[] = [];
    for (const term of m[2].split('+').map((t) => t.trim())) {
      if (!term || term === '0') continue;
      const stellen: Stellen = eingaenge.map(() => null);
      if (term !== '1') {
        for (const lit of term.replace(/[*·]/g, ' ').split(/\s+/)) {
          const i = eingaenge.indexOf(lit.replace(/^!/, ''));
          if (i < 0) return { art: 'text', text: roh };
          stellen[i] = lit.startsWith('!') ? 0 : 1;
        }
      }
      terme.push(stellen);
    }
    return { art: 'formel', name: m[1], terme };
  });
}

export function termText(stellen: Stellen, eingaenge: string[]): string {
  const teile = stellen.flatMap((s, i) => (s == null ? [] : [`${s ? '' : '!'}${eingaenge[i]}`]));
  return teile.length ? teile.join(' ') : '1';
}

export function zusammen(zeilen: Zeile[], eingaenge: string[]): string {
  return zeilen
    .map((z) => (z.art === 'text' ? z.text : `${z.name} = ${z.terme.map((t) => termText(t, eingaenge)).join(' + ')}`))
    .join('\n');
}

/** Setzt die Terme eines Ausgangs; fehlt seine Zeile, kommt sie ans Ende (ohne Leerzeilen davor). */
export function mitTermen(zeilen: Zeile[], name: string, terme: Stellen[]): Zeile[] {
  if (zeilen.some((z) => z.art === 'formel' && z.name === name)) {
    return zeilen.map((z) => (z.art === 'formel' && z.name === name ? { ...z, terme } : z));
  }
  let ende = zeilen.length;
  while (ende > 0 && zeilen[ende - 1].art === 'text' && !(zeilen[ende - 1] as TextZeile).text.trim()) ende -= 1;
  return [...zeilen.slice(0, ende), { art: 'formel', name, terme }];
}

// ---------- Raster ----------

const GRAY: Record<number, number[]> = { 1: [0, 1], 2: [0, 1, 3, 2] };

export interface Raster {
  /** Eingänge an den Zeilen und an den Spalten */
  zeilenEin: string[];
  spaltenEin: string[];
  zeilen: number;
  spalten: number;
  /** Belegung im Feld (Zeile, Spalte), binär gezählt mit dem ersten Eingang vorn */
  belegung: (z: number, s: number) => number;
  /** Zeile und Spalte einer Belegung */
  feld: (belegung: number) => [number, number];
  /** Beschriftung einer Zeile oder Spalte, etwa "01" */
  zeilenText: (z: number) => string;
  spaltenText: (s: number) => string;
}

export function raster(eingaenge: string[]): Raster {
  const n = eingaenge.length;
  const zb = n >> 1;
  const sb = n - zb;
  const gz = GRAY[zb];
  const gs = GRAY[sb];
  const bits = (wert: number, breite: number) => wert.toString(2).padStart(breite, '0');
  return {
    zeilenEin: eingaenge.slice(0, zb),
    spaltenEin: eingaenge.slice(zb),
    zeilen: gz.length,
    spalten: gs.length,
    belegung: (z, s) => (gz[z] << sb) | gs[s],
    feld: (b) => [gz.indexOf(b >> sb), gs.indexOf(b & ((1 << sb) - 1))],
    zeilenText: (z) => bits(gz[z], zb),
    spaltenText: (s) => bits(gs[s], sb),
  };
}

export function enthaelt(stellen: Stellen, belegung: number): boolean {
  const n = stellen.length;
  return stellen.every((s, i) => s == null || ((belegung >> (n - 1 - i)) & 1) === s);
}

export function felder(stellen: Stellen): number[] {
  return Array.from({ length: 2 ** stellen.length }, (_, b) => b).filter((b) => enthaelt(stellen, b));
}

/** Der Block aus einem Bereich von Feldern: was in allen gleich bleibt, steht im Term. */
export function blockAus(belegungen: number[], n: number): Stellen {
  return Array.from({ length: n }, (_, i) => {
    const werte = new Set(belegungen.map((b) => (b >> (n - 1 - i)) & 1));
    return werte.size === 1 ? ([...werte][0] as 0 | 1) : null;
  });
}

/** Indizes von a bis b (b darf vor oder hinter dem Raster liegen), um den Rand herum; null, wenn die Länge keine
 * Zweierpotenz ist oder größer als das Raster. */
export function spanne(a: number, b: number, laenge: number): number[] | null {
  const schritte = Math.abs(b - a) + 1;
  if (schritte > laenge || (schritte & (schritte - 1)) !== 0) return null;
  const richtung = b >= a ? 1 : -1;
  return Array.from({ length: schritte }, (_, k) => (((a + k * richtung) % laenge) + laenge) % laenge);
}

/** Rechtecke [Spalte, Zeile, Breite, Höhe], in die ein Block über die Ränder zerfällt. */
export function rechtecke(stellen: Stellen, r: Raster): [number, number, number, number][] {
  const lagen = felder(stellen).map((b) => r.feld(b));
  const laeufe = (werte: number[]) => {
    const l: number[][] = [];
    [...new Set(werte)].sort((x, y) => x - y).forEach((w) => (l.length && w === l.at(-1)!.at(-1)! + 1 ? l.at(-1)!.push(w) : l.push([w])));
    return l;
  };
  const spalten = laeufe(lagen.map(([, s]) => s));
  const zeilen = laeufe(lagen.map(([z]) => z));
  return spalten.flatMap((sp) => zeilen.map((ze): [number, number, number, number] => [sp[0], ze[0], sp.length, ze.length]));
}
