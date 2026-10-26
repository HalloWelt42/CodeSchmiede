/*
 * Code ohne Editor hervorheben (Beispiele im Lesetext, Fragen, Merkblatt): je Zeile ein HTML-Stück mit Klassen
 * tok-keyword, tok-string ... aus @lezer/highlight; die Farben stehen in styles/kurs.css (Schema des Editors).
 */
import { css } from '@codemirror/lang-css';
import { html } from '@codemirror/lang-html';
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { sql } from '@codemirror/lang-sql';
import type { Parser } from '@lezer/common';
import { classHighlighter, highlightCode } from '@lezer/highlight';

const PARSER: Record<string, () => Parser> = {
  python: () => python().language.parser,
  javascript: () => javascript().language.parser,
  css: () => css().language.parser,
  html: () => html().language.parser,
  sql: () => sql().language.parser,
};

function schuetzen(s: string): string {
  return s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c] ?? c);
}

/** Zeilen als HTML; ohne bekannte Sprache nur geschützter Text. Im CSS-Kurs ist Code, der mit < beginnt, Markup
 * (wie in der Begriffserkennung des Servers). */
export function zeilen(code: string, sprache: string): string[] {
  const text = code.replace(/\n$/, '');
  const parser = PARSER[sprache === 'css' && text.trimStart().startsWith('<') ? 'html' : sprache]?.();
  if (!parser) return text.split('\n').map(schuetzen);
  const ergebnis: string[] = [''];
  highlightCode(
    text,
    parser.parse(text),
    classHighlighter,
    (stueck, klassen) => {
      const teil = schuetzen(stueck);
      ergebnis[ergebnis.length - 1] += klassen ? `<span class="${klassen}">${teil}</span>` : teil;
    },
    () => ergebnis.push(''),
  );
  return ergebnis;
}
