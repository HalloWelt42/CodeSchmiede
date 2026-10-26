/*
 * CSS in Regeln und Angaben zerlegen, damit die Werkbank einzelne Angaben abschalten kann: jede Angabe kennt ihre
 * Stelle im Text, abgeschaltet wird sie, indem ihr Text beim Zusammensetzen fehlt. So bleibt alles andere (Kommentare,
 * Reihenfolge, @media um Regeln herum) genau wie geschrieben.
 *
 * Gelesen wird nur, was der Kurs braucht: Regeln mit Selektor und Block, at-Regeln mit Block (darin wieder Regeln,
 * bei @keyframes die Schritte) und Kommentare; Zeichenketten und Klammern werden übersprungen, damit ein ; oder }
 * darin nichts beendet.
 */

export interface Angabe {
  /** laufende Nummer über das ganze CSS */
  nr: number;
  eigenschaft: string;
  wert: string;
  /** Stelle im Text, einschließlich des abschließenden ; */
  von: number;
  bis: number;
}

export interface Regel {
  /** Selektor oder at-Regel mit Bedingung, wie geschrieben (Leerraum zusammengezogen) */
  kopf: string;
  angaben: Angabe[];
  /** Regeln in @media und Schritte in @keyframes */
  innen: Regel[];
}

/** Ende eines Kommentars, einer Zeichenkette oder Klammer ab Stelle i, sonst i + 1 */
function ueberspringen(css: string, i: number): number {
  const c = css[i];
  if (c === '/' && css[i + 1] === '*') {
    const ende = css.indexOf('*/', i + 2);
    return ende < 0 ? css.length : ende + 2;
  }
  if (c === '"' || c === "'") {
    let j = i + 1;
    while (j < css.length && css[j] !== c && css[j] !== '\n') j += css[j] === '\\' ? 2 : 1;
    return j + 1;
  }
  if (c === '(') {
    let j = i + 1;
    while (j < css.length && css[j] !== ')') j = ueberspringen(css, j);
    return j + 1;
  }
  return i + 1;
}

const ohneKommentare = (s: string) => s.replace(/\/\*[\s\S]*?(\*\/|$)/g, ' ').replace(/\s+/g, ' ').trim();

/** Angaben und Regeln im Block zwischen von und bis */
function block(css: string, von: number, bis: number, zaehler: { nr: number }): { angaben: Angabe[]; innen: Regel[] } {
  const angaben: Angabe[] = [];
  const innen: Regel[] = [];
  let anfang = von;
  let i = von;
  while (i < bis) {
    const c = css[i];
    if (c === '{') {
      // geschachtelte Regel (in @media) oder Schritt (in @keyframes)
      const ende = blockEnde(css, i, bis);
      const unter = block(css, i + 1, ende, zaehler);
      innen.push({ kopf: ohneKommentare(css.slice(anfang, i)), ...unter });
      i = ende + 1;
      anfang = i;
    } else if (c === ';') {
      angabeLesen(css, anfang, i + 1, zaehler, angaben);
      i += 1;
      anfang = i;
    } else {
      i = ueberspringen(css, i);
    }
  }
  if (ohneKommentare(css.slice(anfang, bis))) angabeLesen(css, anfang, bis, zaehler, angaben);
  return { angaben, innen };
}

function angabeLesen(css: string, von: number, bis: number, zaehler: { nr: number }, angaben: Angabe[]): void {
  const text = ohneKommentare(css.slice(von, bis)).replace(/;$/, '');
  const doppelpunkt = text.indexOf(':');
  if (doppelpunkt < 1) return;
  // Leerraum und Kommentare vor der Angabe bleiben stehen
  let start = von;
  while (start < bis && (/\s/.test(css[start]) || css.startsWith('/*', start))) start = /\s/.test(css[start]) ? start + 1 : ueberspringen(css, start);
  let ende = bis;
  while (ende > start && /\s/.test(css[ende - 1])) ende -= 1;
  angaben.push({ nr: zaehler.nr++, eigenschaft: text.slice(0, doppelpunkt).trim(), wert: text.slice(doppelpunkt + 1).trim(), von: start, bis: ende });
}

/** Stelle der schließenden Klammer zum { an Stelle i */
function blockEnde(css: string, i: number, bis: number): number {
  let tiefe = 0;
  let j = i;
  while (j < bis) {
    if (css[j] === '{') tiefe += 1;
    else if (css[j] === '}') {
      tiefe -= 1;
      if (tiefe === 0) return j;
    }
    j = css[j] === '{' || css[j] === '}' ? j + 1 : ueberspringen(css, j);
  }
  return bis;
}

/** Regeln eines Stücks CSS */
export function zerlege(css: string): Regel[] {
  const zaehler = { nr: 0 };
  const regeln: Regel[] = [];
  let anfang = 0;
  let i = 0;
  while (i < css.length) {
    if (css[i] === '{') {
      const ende = blockEnde(css, i, css.length);
      regeln.push({ kopf: ohneKommentare(css.slice(anfang, i)), ...block(css, i + 1, ende, zaehler) });
      i = ende + 1;
      anfang = i;
    } else {
      i = ueberspringen(css, i);
    }
  }
  return regeln;
}

/** Das CSS ohne die abgeschalteten Angaben */
export function ohne(css: string, regeln: Regel[], aus: ReadonlySet<number>): string {
  const stellen: Angabe[] = [];
  const sammeln = (rs: Regel[]) => rs.forEach((r) => { stellen.push(...r.angaben.filter((a) => aus.has(a.nr))); sammeln(r.innen); });
  sammeln(regeln);
  stellen.sort((a, b) => b.von - a.von);
  let ergebnis = css;
  for (const a of stellen) ergebnis = ergebnis.slice(0, a.von) + ergebnis.slice(a.bis);
  return ergebnis;
}
