/*
 * MarkdownRenderer -- marked + KaTeX + Mermaid + DOMPurify.
 *
 * Reihenfolge:
 *   1. Mermaid-Bloecke (`mermaid`-fence) werden in <div class="mermaid">
 *      ersetzt -- Mermaid rendert sie spaeter direkt im DOM.
 *   2. Display-Math `$$ ... $$` wird über KaTeX zu HTML.
 *   3. Inline-Math `$ ... $` wird über KaTeX zu HTML.
 *   4. marked rendert den Rest (GFM, Tabellen, Codebloecke).
 *   5. DOMPurify saeubert das Ergebnis. SVG-Tags werden zugelassen,
 *      damit Mermaid-Output (der spaeter eingefuegt wird) durchlaeuft.
 */

import DOMPurify from 'dompurify';
import katex from 'katex';
import { marked } from 'marked';
import mermaid from 'mermaid';

let mermaidInitialisiert = false;

function initMermaid(): void {
  if (mermaidInitialisiert) return;
  mermaid.initialize({
    startOnLoad: false,
    theme: 'dark',
    securityLevel: 'loose',
    themeVariables: {
      primaryColor: '#22262d',
      primaryBorderColor: '#2dd4bf',
      primaryTextColor: '#e7ecf1',
      lineColor: '#8a93a0',
      textColor: '#e7ecf1',
      mainBkg: '#22262d',
      nodeBorder: '#2dd4bf',
      clusterBkg: '#2a2f37',
      edgeLabelBackground: '#1a1d23',
    },
  });
  mermaidInitialisiert = true;
}

function escapeHtml(s: string): string {
  return s.replace(/[&<>"']/g, (c) => {
    const map: Record<string, string> = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;',
    };
    return map[c] ?? c;
  });
}

export class MarkdownRenderer {
  constructor() {
    initMermaid();
  }

  rendere(text: string): string {
    let zwischen = text;

    zwischen = zwischen.replace(/```mermaid\n([\s\S]*?)```/g, (_, code: string) => {
      return `\n\n<div class="mermaid">${escapeHtml(code.trim())}</div>\n\n`;
    });

    zwischen = zwischen.replace(/\$\$([\s\S]+?)\$\$/g, (_, latex: string) => {
      try {
        return katex.renderToString(latex.trim(), {
          displayMode: true,
          throwOnError: false,
          output: 'html',
        });
      } catch {
        return `<code class="formel-fehler">${escapeHtml(latex)}</code>`;
      }
    });

    zwischen = zwischen.replace(/(?<!\$)\$([^$\n]+?)\$(?!\$)/g, (_, latex: string) => {
      try {
        return katex.renderToString(latex, {
          displayMode: false,
          throwOnError: false,
          output: 'html',
        });
      } catch {
        return `<code class="formel-fehler">${escapeHtml(latex)}</code>`;
      }
    });

    const roh = marked.parse(zwischen, { gfm: true, breaks: false }) as string;

    return DOMPurify.sanitize(roh, {
      ADD_TAGS: ['mark', 'foreignObject'],
      ADD_ATTR: ['target', 'class', 'style', 'data-idx', 'aria-roledescription'],
    });
  }

  async rendereMermaids(container: HTMLElement): Promise<void> {
    const blocks = container.querySelectorAll<HTMLElement>('.mermaid:not([data-processed="true"])');
    if (blocks.length === 0) return;
    try {
      await mermaid.run({ nodes: Array.from(blocks) });
    } catch (e) {
      console.warn('Mermaid-Render-Fehler:', e);
    }
  }
}

export const markdownRenderer = new MarkdownRenderer();
