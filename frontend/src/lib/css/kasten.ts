/*
 * Das Kastenmodell eines Elements auf der Bühne: Inhalt, Innenabstand (padding), Rahmen (border) und Außenabstand
 * (margin), wie der Browser sie berechnet hat. Die Werkbank zeichnet daraus die vier Ringe über die Bühne und zeigt
 * die Zahlen daneben. Die Bühne rollt nicht, die Lage im Fenster ist also die Lage auf der Bühne.
 */

export interface Seiten {
  oben: number;
  rechts: number;
  unten: number;
  links: number;
}

export interface Rechteck {
  x: number;
  y: number;
  b: number;
  h: number;
}

export interface Kasten {
  /** etwa p.preis#heute, so wie ein Selektor es schreiben würde */
  name: string;
  /** Rahmenkante, wie getBoundingClientRect sie liefert */
  rand: Rechteck;
  margin: Seiten;
  border: Seiten;
  padding: Seiten;
  /** Breite und Höhe des Inhalts */
  inhalt: { b: number; h: number };
}

const zahl = (s: string) => Math.round((parseFloat(s) || 0) * 10) / 10;

function seiten(stil: CSSStyleDeclaration, vorne: string, hinten = ''): Seiten {
  const wert = (seite: string) => zahl(stil.getPropertyValue(`${vorne}-${seite}${hinten}`));
  return { oben: wert('top'), rechts: wert('right'), unten: wert('bottom'), links: wert('left') };
}

export function elementName(el: Element): string {
  const klassen = [...el.classList].map((k) => `.${k}`).join('');
  return `${el.tagName.toLowerCase()}${el.id ? `#${el.id}` : ''}${klassen}`;
}

export function kasten(el: Element): Kasten {
  const stil = el.ownerDocument.defaultView?.getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const leer = { oben: 0, rechts: 0, unten: 0, links: 0 };
  const margin = stil ? seiten(stil, 'margin') : leer;
  const border = stil ? seiten(stil, 'border', '-width') : leer;
  const padding = stil ? seiten(stil, 'padding') : leer;
  return {
    name: elementName(el),
    rand: { x: r.left, y: r.top, b: r.width, h: r.height },
    margin, border, padding,
    inhalt: {
      b: zahl(String(r.width - border.links - border.rechts - padding.links - padding.rechts)),
      h: zahl(String(r.height - border.oben - border.unten - padding.oben - padding.unten)),
    },
  };
}

/** Rechteck um r, an jeder Seite um s erweitert (negativ: verkleinert) */
export function erweitert(r: Rechteck, s: Seiten, vorzeichen = 1): Rechteck {
  return {
    x: r.x - vorzeichen * s.links,
    y: r.y - vorzeichen * s.oben,
    b: r.b + vorzeichen * (s.links + s.rechts),
    h: r.h + vorzeichen * (s.oben + s.unten),
  };
}

/** Weg vom body zum Element (Nummern der Kinder), um es nach dem Neuladen der Bühne wiederzufinden */
export function weg(el: Element): number[] {
  const schritte: number[] = [];
  let k: Element | null = el;
  while (k && k.parentElement && k.tagName !== 'BODY') {
    schritte.unshift([...k.parentElement.children].indexOf(k));
    k = k.parentElement;
  }
  return schritte;
}

export function folge(dokument: Document, schritte: number[]): Element | null {
  let k: Element | null = dokument.body;
  for (const i of schritte) k = k?.children[i] ?? null;
  return k === dokument.body ? null : k;
}
