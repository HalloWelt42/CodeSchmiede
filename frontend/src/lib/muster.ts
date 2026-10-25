/*
 * Treffer-Regel der Muster-Jagd, wie im Prüfer (backend/.../pruefung/
 * muster_pruefer.py): eine Zeile gilt als getroffen, wenn das Muster darin
 * eine nicht leere Stelle findet. Die Vorschau markiert diese Stellen.
 */

export interface Abschnitt {
  text: string;
  treffer: boolean;
}

export interface ZeilenMarke {
  abschnitte: Abschnitt[];
  getroffen: boolean;
}

export interface Markierung {
  /** null: Muster gültig */
  fehler: string | null;
  zeilen: ZeilenMarke[];
}

function markiere(text: string, re: RegExp): ZeilenMarke {
  const abschnitte: Abschnitt[] = [];
  let letzte = 0;
  let getroffen = false;
  for (const m of text.matchAll(re)) {
    if (m[0] === '') continue;
    getroffen = true;
    if (m.index > letzte) abschnitte.push({ text: text.slice(letzte, m.index), treffer: false });
    abschnitte.push({ text: m[0], treffer: true });
    letzte = m.index + m[0].length;
  }
  if (letzte < text.length) abschnitte.push({ text: text.slice(letzte), treffer: false });
  return { abschnitte, getroffen };
}

export function unmarkiert(zeilen: string[]): Markierung {
  return { fehler: null, zeilen: zeilen.map((t) => ({ abschnitte: [{ text: t, treffer: false }], getroffen: false })) };
}

export function markiereZeilen(muster: string, flags: string, zeilen: string[]): Markierung {
  let re: RegExp;
  try {
    re = new RegExp(muster, `${flags}g`);
  } catch (e) {
    return { ...unmarkiert(zeilen), fehler: (e as Error).message };
  }
  return { fehler: null, zeilen: zeilen.map((t) => markiere(t, re)) };
}
