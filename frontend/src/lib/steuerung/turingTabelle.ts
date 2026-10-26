/*
 * Übergangstabelle der Turingmaschine als Zeilen: Regeln (Zustand liest -> schreibt geht danach) und alles andere
 * (Kommentare, Leerzeilen, Unfertiges) als Text. Der Text ist die eine Wahrheit; die Tabelle in der Oberfläche liest
 * ihn mit `zerlege` und schreibt ihn mit `zusammen` zurück. Was eine gültige Regel ist, entscheidet das Backend
 * (backend/src/codeschmiede/steuerung/turing.py); hier wird nur fürs Bearbeiten zerlegt.
 */

export type Richtung = 'L' | 'R' | 'N';

export interface Regel {
  art: 'regel';
  zustand: string;
  liest: string;
  schreibt: string;
  geht: Richtung;
  danach: string;
  /** Kommentar hinter der Regel, ohne # */
  kommentar: string;
}

export interface Text {
  art: 'text';
  text: string;
}

export type Zeile = Regel | Text;

const REGEL = /^(\S+)\s+(\S)\s*->\s*(\S)\s+([LRN])\s+(\S+)$/;

export function zerlege(text: string): Zeile[] {
  return text.split('\n').map((roh): Zeile => {
    const [vorne, ...rest] = roh.split('#');
    const treffer = REGEL.exec(vorne.trim());
    if (!treffer) return { art: 'text', text: roh };
    const [, zustand, liest, schreibt, geht, danach] = treffer;
    return { art: 'regel', zustand, liest, schreibt, geht: geht as Richtung, danach, kommentar: rest.join('#').trim() };
  });
}

export function zusammen(zeilen: Zeile[]): string {
  return zeilen
    .map((z) =>
      z.art === 'text'
        ? z.text
        : `${z.zustand} ${z.liest} -> ${z.schreibt} ${z.geht} ${z.danach}${z.kommentar ? `  # ${z.kommentar}` : ''}`,
    )
    .join('\n');
}

export function regeln(zeilen: Zeile[]): { regel: Regel; zeile: number }[] {
  return zeilen.flatMap((z, i) => (z.art === 'regel' ? [{ regel: z, zeile: i + 1 }] : []));
}
