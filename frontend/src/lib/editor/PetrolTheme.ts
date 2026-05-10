/*
 * CodeMirror-Theme im Petrol-Industrial-Look.
 * Verwendet CSS-Variablen aus global.css, sodass das Theme automatisch
 * mit Dark/Light wechselt.
 */

import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { EditorView } from '@codemirror/view';
import { tags as t } from '@lezer/highlight';

const editorBasis = EditorView.theme(
  {
    '&': {
      color: 'var(--fg)',
      backgroundColor: 'var(--bg)',
      height: '100%',
    },
    '.cm-scroller': {
      fontFamily: 'var(--mono)',
      fontSize: 'var(--fs-sm)',
      lineHeight: '1.55',
    },
    '.cm-content': {
      caretColor: 'var(--accent)',
      padding: 'var(--sp-3) 0',
    },
    '.cm-cursor, .cm-dropCursor': {
      borderLeftColor: 'var(--accent)',
    },
    '&.cm-focused .cm-selectionBackground, .cm-content ::selection, .cm-selectionBackground': {
      background: 'color-mix(in srgb, var(--accent) 25%, transparent) !important',
    },
    '.cm-gutters': {
      backgroundColor: 'var(--bg-card)',
      color: 'var(--fg-mute)',
      border: 'none',
      borderRight: '1px solid var(--border)',
    },
    '.cm-activeLineGutter': {
      backgroundColor: 'var(--bg-card-2)',
      color: 'var(--accent)',
    },
    '.cm-activeLine': {
      backgroundColor: 'color-mix(in srgb, var(--accent) 5%, transparent)',
    },
    '.cm-foldPlaceholder': {
      backgroundColor: 'var(--bg-card-2)',
      color: 'var(--fg-dim)',
      border: 'none',
      padding: '0 4px',
    },
    '.cm-tooltip': {
      backgroundColor: 'var(--bg-card)',
      border: '1px solid var(--border)',
      color: 'var(--fg)',
    },
  },
  { dark: true },
);

const petrolHighlightStyle = HighlightStyle.define([
  { tag: t.keyword, color: '#5eead4', fontWeight: '600' },
  { tag: [t.controlKeyword, t.moduleKeyword], color: '#5eead4' },
  { tag: [t.name, t.deleted, t.character, t.macroName], color: '#e7ecf1' },
  { tag: [t.propertyName], color: '#a6e3d0' },
  { tag: [t.function(t.variableName), t.labelName], color: '#a6e3d0' },
  { tag: [t.color, t.constant(t.name), t.standard(t.name)], color: '#d29922' },
  { tag: [t.definition(t.name), t.separator], color: '#e7ecf1' },
  { tag: [t.typeName, t.className, t.number, t.changed, t.annotation, t.modifier, t.self, t.namespace], color: '#d29922' },
  { tag: [t.operator, t.operatorKeyword, t.url, t.escape, t.regexp, t.link, t.special(t.string)], color: '#5eead4' },
  { tag: [t.meta, t.comment], color: '#6a737e', fontStyle: 'italic' },
  { tag: t.strong, fontWeight: '700' },
  { tag: t.emphasis, fontStyle: 'italic' },
  { tag: t.link, color: '#2dd4bf', textDecoration: 'underline' },
  { tag: t.heading, fontWeight: '700', color: '#e7ecf1' },
  { tag: [t.atom, t.bool, t.special(t.variableName)], color: '#d29922' },
  { tag: [t.processingInstruction, t.string, t.inserted], color: '#a6e3d0' },
  { tag: t.invalid, color: '#f85149' },
]);

export const petrolTheme = [editorBasis, syntaxHighlighting(petrolHighlightStyle)];
