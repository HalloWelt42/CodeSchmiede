/*
 * Wrapper um die CodeMirror-Initialisierung. Liefert eine EditorView,
 * die in eine Svelte-Komponente per `bind:this` eingehaengt wird.
 * Sprache wird ueber den `sprache`-Parameter ausgewaehlt; fuer noch
 * nicht unterstuetzte Sprachen faellt der Editor auf Plain-Text zurueck.
 */

import { defaultKeymap, history, historyKeymap, indentWithTab } from '@codemirror/commands';
import { css } from '@codemirror/lang-css';
import { html } from '@codemirror/lang-html';
import { javascript } from '@codemirror/lang-javascript';
import { markdown } from '@codemirror/lang-markdown';
import { python } from '@codemirror/lang-python';
import { sql } from '@codemirror/lang-sql';
import { foldGutter, foldKeymap, indentOnInput } from '@codemirror/language';
import { EditorState } from '@codemirror/state';
import { EditorView, highlightActiveLine, keymap, lineNumbers } from '@codemirror/view';

import { petrolTheme } from './PetrolTheme';

export type Sprache = 'python' | 'javascript' | 'html' | 'css' | 'sql' | 'markdown';

const SPRACHEN_EXTENSIONS = {
  python: () => python(),
  javascript: () => javascript(),
  html: () => html(),
  css: () => css(),
  sql: () => sql(),
  markdown: () => markdown(),
};

function spracheExtension(sprache: string) {
  const factory = SPRACHEN_EXTENSIONS[sprache as Sprache];
  return factory ? factory() : [];
}

export interface EditorOptionen {
  parent: HTMLElement;
  sprache: string;
  initialerCode: string;
  beiAenderung: (code: string) => void;
}

export function erstelleEditor(opts: EditorOptionen): EditorView {
  const state = EditorState.create({
    doc: opts.initialerCode,
    extensions: [
      lineNumbers(),
      foldGutter(),
      highlightActiveLine(),
      indentOnInput(),
      history(),
      keymap.of([...defaultKeymap, ...historyKeymap, ...foldKeymap, indentWithTab]),
      spracheExtension(opts.sprache),
      petrolTheme,
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
