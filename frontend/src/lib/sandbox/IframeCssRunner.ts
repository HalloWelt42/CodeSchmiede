/*
 * IframeCssRunner -- bewertet CSS-Klon-Aufgaben.
 *
 * Eine CSS-Klon-Aufgabe liefert ein Ziel-Markup (HTML), eine Sammlung
 * von Asserts (Selector + CSS-Property + erwarteter Wert) und das CSS
 * des Nutzers. Wir rendern das Markup in einem sandboxed Iframe (mit
 * dem Nutzer-CSS injiziert) und vergleichen die berechneten Stile
 * gegen die Asserts.
 *
 * Das Ziel-CSS aus dem Frontmatter kommt nicht in den Vergleich --
 * es ist nur dafuer da, dem Nutzer eine visuelle Vorlage zu zeigen.
 * Die Bewertung haengt allein an den Asserts. Daher kann der Nutzer
 * jeden CSS-Weg waehlen, solange das Ergebnis die Asserts erfuellt.
 */

export interface CssAssert {
  selector: string;
  property: string;
  expected: string;
  /** Optionale numerische Toleranz (z.B. 1px). 0 = exakter String-Vergleich. */
  toleranz?: number;
}

export interface CssAssertErgebnis {
  index: number;
  selector: string;
  property: string;
  expected: string;
  tatsaechlich: string;
  bestanden: boolean;
  fehler: string | null;
}

export interface CssLaufErgebnis {
  bestanden: boolean;
  sichtbar: CssAssertErgebnis[];
  versteckt_pass: number;
  versteckt_fail: number;
  laufzeit_ms: number;
  stdout: string;
  stderr: string;
  timeout: boolean;
}

class IframeCssRunner {
  /**
   * Rendert das Ziel-HTML mit dem Nutzer-CSS in einem sandboxed Iframe
   * und prueft alle Asserts. Iframe wird nach Auswertung wieder entfernt.
   */
  async run(
    ziel_html: string,
    nutzer_css: string,
    asserts: CssAssert[],
    timeout_ms: number = 3000,
  ): Promise<CssLaufErgebnis> {
    const start = performance.now();
    const iframe = document.createElement('iframe');
    // Sandbox absichern: kein top-level-Navigation, keine Same-Origin-
    // Privilegien (Iframe-DOM bleibt aber ueber contentDocument lesbar,
    // weil wir es selbst befuellen). 'allow-same-origin' WIRD gesetzt,
    // damit getComputedStyle ueberhaupt funktioniert.
    iframe.setAttribute('sandbox', 'allow-same-origin');
    // Sichtbares aber off-screen platzieren -- ein wirklich hidden Iframe
    // (display: none) wuerde keine Layout-Berechnung ausfuehren und
    // getComputedStyle koennte schimaerische Werte liefern. Daher: an die
    // linke Seite raus, aber ins Layout.
    iframe.style.cssText = 'position:fixed;left:-9999px;top:0;width:600px;height:400px;border:0;visibility:hidden;';
    document.body.appendChild(iframe);
    try {
      const lauf = this.lauf_intern(iframe, ziel_html, nutzer_css, asserts);
      const timer = new Promise<CssLaufErgebnis>((resolve) =>
        setTimeout(() => resolve({
          bestanden: false,
          sichtbar: asserts.map((a, i) => ({
            index: i, selector: a.selector, property: a.property,
            expected: a.expected, tatsaechlich: '(Timeout)',
            bestanden: false, fehler: 'Auswertung dauerte zu lange',
          })),
          versteckt_pass: 0, versteckt_fail: 0,
          laufzeit_ms: performance.now() - start,
          stdout: '', stderr: 'Timeout', timeout: true,
        }), timeout_ms),
      );
      return await Promise.race([lauf, timer]);
    } finally {
      iframe.remove();
    }
  }

  private async lauf_intern(
    iframe: HTMLIFrameElement,
    ziel_html: string,
    nutzer_css: string,
    asserts: CssAssert[],
  ): Promise<CssLaufErgebnis> {
    const start = performance.now();
    const doc = iframe.contentDocument!;
    doc.open();
    doc.write(`<!doctype html>
<html><head><meta charset="utf-8"><style>
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; color: rgb(231, 236, 241); }
${nutzer_css}
</style></head><body>${ziel_html}</body></html>`);
    doc.close();
    // Layout-Berechnung anstossen + abwarten. getComputedStyle erzwingt
    // selbst schon ein Layout, aber wir geben dem Browser eine Mikro-
    // Pause -- das hat sich als zuverlaessiger erwiesen als
    // requestAnimationFrame im versteckten Iframe.
    await new Promise<void>((r) => setTimeout(r, 0));
    // Layout-Erzwingung per offsetHeight-Read auf body, damit Browser
    // garantiert gerendert hat.
    void doc.body.offsetHeight;

    const ergebnisse: CssAssertErgebnis[] = [];
    for (let i = 0; i < asserts.length; i++) {
      ergebnisse.push(this.pruefe_assert(doc, asserts[i], i));
    }
    const bestanden = ergebnisse.every((e) => e.bestanden);
    return {
      bestanden,
      sichtbar: ergebnisse,
      versteckt_pass: 0,
      versteckt_fail: 0,
      laufzeit_ms: performance.now() - start,
      stdout: '',
      stderr: '',
      timeout: false,
    };
  }

  private pruefe_assert(
    doc: Document,
    a: CssAssert,
    index: number,
  ): CssAssertErgebnis {
    const el = doc.querySelector(a.selector);
    if (!el) {
      return {
        index,
        selector: a.selector,
        property: a.property,
        expected: a.expected,
        tatsaechlich: '(Element nicht gefunden)',
        bestanden: false,
        fehler: `Selector "${a.selector}" liefert kein Element`,
      };
    }
    const stil = doc.defaultView!.getComputedStyle(el);
    const ist = stil.getPropertyValue(a.property).trim();
    const erwartet = a.expected.trim();
    let bestanden = ist === erwartet;
    if (!bestanden && a.toleranz && a.toleranz > 0) {
      bestanden = this.numerisch_im_rahmen(ist, erwartet, a.toleranz);
    }
    return {
      index,
      selector: a.selector,
      property: a.property,
      expected: erwartet,
      tatsaechlich: ist,
      bestanden,
      fehler: bestanden ? null : null,
    };
  }

  private numerisch_im_rahmen(ist: string, soll: string, tol: number): boolean {
    const ist_n = this.zahl(ist);
    const soll_n = this.zahl(soll);
    if (ist_n === null || soll_n === null) return false;
    return Math.abs(ist_n - soll_n) <= tol;
  }

  private zahl(s: string): number | null {
    const m = s.match(/-?\d+(?:\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  }
}

export const iframeCssRunner = new IframeCssRunner();
