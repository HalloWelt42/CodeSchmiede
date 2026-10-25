/*
 * Bühne der CSS-Aufgaben: eine Fläche von BUEHNE_B x BUEHNE_H, auf der
 * Ziel und eigenes Ergebnis mit demselben Grundstil stehen. Anzeige
 * (iframe in CssVergleich) und Messung (deckung.ts) bauen ihr Dokument
 * hier, damit beide genau dasselbe zeigen.
 *
 * html und body füllen die Bühne, damit ein Hintergrund überall liegt,
 * auch wo das Motiv nicht hinreicht; die Bühne rollt nicht. Sonst gilt,
 * was ein Browser ab Werk tut (etwa box-sizing: content-box), damit man
 * hier lernt, was auch draußen gilt.
 */

export const BUEHNE_B = 600;
export const BUEHNE_H = 400;

const GRUNDSTIL = `html { height: 100%; overflow: hidden; }
body { margin: 0; min-height: 100%; padding: 12px; font-family: system-ui, sans-serif; background: #1a1d23; color: #e7ecf1; }`;

/** HTML-Dokument der Bühne mit Markup der Aufgabe und einem Stil */
export function buehnenDokument(html: string, css: string): string {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
${GRUNDSTIL}
${css}
</style></head><body>${html}</body></html>`;
}
