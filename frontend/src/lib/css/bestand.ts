/*
 * Messung des CSS-Bestands im Browser, mit derselben Messung wie beim Lösen (deckung.ts): jede Musterlösung muss das
 * Ziel voll decken, der Startcode darf nicht bestehen. Die Schwellen kommen vom Server (Prüfer der CSS-Nachbauten).
 */
import type { Befund, CssBestand } from '../api/AdminApi';
import { rastere, vergleiche } from './deckung';

const prozent = (x: number) => `${(x * 100).toFixed(1).replace('.', ',')} %`;

/** Befunde des ganzen Bestands; beiFortschritt meldet, wie viele Aufgaben schon gemessen sind */
export async function messeBestand(bestand: CssBestand, beiFortschritt: (fertig: number) => void): Promise<Befund[]> {
  const befunde: Befund[] = [];
  for (const [i, a] of bestand.aufgaben.entries()) {
    const ort = `aufgaben/css/${a.id}`;
    try {
      const ziel = await rastere(a.ziel_html, a.ziel_css);
      const deckung = async (css: string) => vergleiche(ziel, await rastere(a.ziel_html, css)).deckung;
      if (!a.musterloesungen.length) befunde.push({ ort, meldung: 'keine Musterlösung' });
      for (const m of a.musterloesungen) {
        const d = await deckung(m.code);
        if (d < bestand.voll) befunde.push({ ort, meldung: `Musterlösung ${m.variante} deckt nur ${prozent(d)}` });
      }
      const start = await deckung(a.starter_code);
      if (start >= bestand.bestehen) befunde.push({ ort, meldung: `Startcode besteht schon (${prozent(start)})` });
    } catch (e) {
      befunde.push({ ort, meldung: `nicht messbar: ${e instanceof Error ? e.message : String(e)}` });
    }
    beiFortschritt(i + 1);
  }
  return befunde;
}
