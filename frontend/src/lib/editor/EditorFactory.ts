/*
 * Wrapper um die CodeMirror-Initialisierung. Liefert eine EditorView,
 * die in eine Svelte-Komponente per `bind:this` eingehaengt wird.
 * Sprache wird über den `sprache`-Parameter ausgewaehlt; für noch
 * nicht unterstuetzte Sprachen faellt der Editor auf Plain-Text zurück.
 *
 * Ausstattung wie in einer Entwicklungsumgebung: Farbschema
 * (KlassischDunkel), Vervollständigung einzelner Befehle, Syntaxprüfung
 * beim Tippen (nur in Programmiersprachen), Klammern schließen und
 * markieren, Suchen und Ersetzen, Mehrfachauswahl, deutsche Bedientexte.
 */

import { closeBrackets, closeBracketsKeymap, completionKeymap } from '@codemirror/autocomplete';
import { defaultKeymap, history, historyKeymap, indentWithTab } from '@codemirror/commands';
import { css } from '@codemirror/lang-css';
import { html } from '@codemirror/lang-html';
import { javascript } from '@codemirror/lang-javascript';
import { markdown } from '@codemirror/lang-markdown';
import { python } from '@codemirror/lang-python';
import { sql } from '@codemirror/lang-sql';
import { bracketMatching, foldGutter, foldKeymap, indentOnInput, indentUnit } from '@codemirror/language';
import { lintKeymap } from '@codemirror/lint';
import { highlightSelectionMatches, searchKeymap } from '@codemirror/search';
import { EditorState } from '@codemirror/state';
import {
  crosshairCursor,
  drawSelection,
  dropCursor,
  EditorView,
  highlightActiveLine,
  highlightActiveLineGutter,
  keymap,
  lineNumbers,
  rectangularSelection,
} from '@codemirror/view';

import { klassischDunkel } from './KlassischDunkel';
import { deutscheTexte } from './Phrasen';
import { syntaxpruefung } from './Syntaxpruefung';
import { vervollstaendigung } from './Vervollstaendigung';
import { zeilenMarke } from './ZeilenMarke';

export type Sprache = 'python' | 'javascript' | 'html' | 'css' | 'sql' | 'markdown';

const SPRACHEN_EXTENSIONS = {
  // Python rückt üblicherweise um vier Leerzeichen ein, wie die Startcodes
  python: () => [python(), indentUnit.of('    ')],
  javascript: () => javascript(),
  html: () => html(),
  css: () => css(),
  sql: () => sql(),
  markdown: () => markdown(),
};

/** Sprachen mit Grammatik, deren Schreibweise beim Tippen geprüft wird */
const MIT_SYNTAXPRUEFUNG: ReadonlySet<string> = new Set(['python', 'javascript', 'html', 'css', 'sql']);

function spracheExtension(sprache: string) {
  const factory = SPRACHEN_EXTENSIONS[sprache as Sprache];
  return factory ? factory() : [];
}

export interface EditorOptionen {
  parent: HTMLElement;
  sprache: string;
  initialerCode: string;
  beiAenderung: (code: string) => void;
  /** Befehle der Aufgabe für die Vervollständigung, etwa gehe() */
  befehle?: readonly string[];
}

export function erstelleEditor(opts: EditorOptionen): EditorView {
  const state = EditorState.create({
    doc: opts.initialerCode,
    extensions: [
      lineNumbers(),
      highlightActiveLineGutter(),
      foldGutter(),
      highlightActiveLine(),
      drawSelection(),
      dropCursor(),
      EditorState.allowMultipleSelections.of(true),
      rectangularSelection(),
      crosshairCursor(),
      indentOnInput(),
      bracketMatching(),
      closeBrackets(),
      highlightSelectionMatches(),
      history(),
      keymap.of([
        ...closeBracketsKeymap,
        ...defaultKeymap,
        ...searchKeymap,
        ...historyKeymap,
        ...foldKeymap,
        ...completionKeymap,
        ...lintKeymap,
        indentWithTab,
      ]),
      spracheExtension(opts.sprache),
      vervollstaendigung(opts.befehle),
      MIT_SYNTAXPRUEFUNG.has(opts.sprache) ? syntaxpruefung : [],
      klassischDunkel,
      deutscheTexte,
      zeilenMarke,
      EditorView.lineWrapping,
      EditorView.updateListener.of((upd) => {
        if (upd.docChanged) {
          opts.beiAenderung(upd.state.doc.toString());
        }
      }),
    ],
  });

  return new EditorView({ state, parent: opts.parent });
}
