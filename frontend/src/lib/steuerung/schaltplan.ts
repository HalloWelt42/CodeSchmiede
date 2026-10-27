/*
 * Schaltplan als Zeilen: Bausteine (name = ART(Eingänge) @ x,y), Ausgänge (Ausgang = Signal) und alles andere als
 * Text. Der Text ist die eine Wahrheit; der Plan in der Oberfläche liest ihn mit `zerlege` und schreibt ihn mit
 * `zusammen` zurück. Was gilt und was herauskommt, rechnet das Backend (backend/src/codeschmiede/steuerung/schaltung.py).
 */

export const OFFEN = '?';
export const EINGAENGE_JE_ART: Record<string, number> = { UND: 2, ODER: 2, XOR: 2, NAND: 2, NOR: 2, NICHT: 1, FF: 1 };
/** Flipflop: merkt sich beim Takt seinen Eingang D (Schaltungen mit Takt) */
export const SPEICHER = 'FF';
/** Ausgänge, die zusammen eine 7-Segment-Anzeige sind: a oben, dann im Uhrzeigersinn, g in der Mitte */
export const SEGMENTE = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];

export function istSiebenSegment(ausgaenge: string[]): boolean {
  return ausgaenge.join('') === SEGMENTE.join('');
}

export interface Baustein {
  art: 'baustein';
  name: string;
  typ: string;
  eingaenge: string[];
  x: number | null;
  y: number | null;
}

export interface Ausgang {
  art: 'ausgang';
  name: string;
  quelle: string;
}

export interface Text {
  art: 'text';
  text: string;
}

export type Zeile = Baustein | Ausgang | Text;

const BAUSTEIN = /^(\w+)\s*=\s*([A-Z]+)\s*\(([^)]*)\)\s*(?:@\s*(-?\d+)\s*,\s*(-?\d+))?$/;
const AUSGANG = /^(\w+)\s*=\s*(\S+)$/;

export function zerlege(text: string, ausgaenge: string[]): Zeile[] {
  return text.split('\n').map((roh): Zeile => {
    const zeile = roh.split('#')[0].trim();
    const b = BAUSTEIN.exec(zeile);
    if (b) {
      const [, name, typ, ein, x, y] = b;
      return {
        art: 'baustein',
        name,
        typ,
        eingaenge: ein.trim() ? ein.split(',').map((e) => e.trim()) : [],
        x: x ? Number(x) : null,
        y: y ? Number(y) : null,
      };
    }
    const a = AUSGANG.exec(zeile);
    if (a && ausgaenge.includes(a[1])) return { art: 'ausgang', name: a[1], quelle: a[2] };
    return { art: 'text', text: roh };
  });
}

export function zusammen(zeilen: Zeile[]): string {
  return zeilen
    .map((z) => {
      if (z.art === 'text') return z.text;
      if (z.art === 'ausgang') return `${z.name} = ${z.quelle}`;
      const lage = z.x != null && z.y != null ? ` @ ${z.x},${z.y}` : '';
      return `${z.name} = ${z.typ}(${z.eingaenge.join(', ')})${lage}`;
    })
    .join('\n');
}

/** Freier Name für einen neuen Baustein dieser Art: und1, oder2, ... */
export function neuerName(zeilen: Zeile[], typ: string, belegt: string[]): string {
  const namen = new Set([...belegt, ...zeilen.flatMap((z) => (z.art === 'text' ? [] : [z.name]))]);
  const stamm = typ.toLowerCase();
  for (let i = 1; ; i++) if (!namen.has(`${stamm}${i}`)) return `${stamm}${i}`;
}
