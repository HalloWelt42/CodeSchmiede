/*
 * CodeMirror-Theme im Petrol-Industrial-Look.
 * Verwendet CSS-Variablen aus global.css, sodass das Theme automatisch
 * mit Dark/Light wechselt. Die Token-Farben kommen aus den
 * --code-*-Variablen, die als CSS-Klassen (`cm-cs-*`) angeheftet
 * werden -- so muss CodeMirror selbst kein Theme neu rendern.
 */

import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { EditorView } from '@codemirror/view';
import { tags as t } from '@lezer/highlight';

const editorBasis = EditorView.theme({
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
});

const petrolHighlightStyle = HighlightStyle.define([
  { tag: t.keyword, class: 'cm-cs-keyword' },
  { tag: [t.controlKeyword, t.moduleKeyword], class: 'cm-cs-keyword' },
  { tag: [t.name, t.deleted, t.character, t.macroName], class: 'cm-cs-name' },
  { tag: [t.propertyName], class: 'cm-cs-property' },
  { tag: [t.function(t.variableName), t.labelName], class: 'cm-cs-function' },
  { tag: [t.color, t.constant(t.name), t.standard(t.name)], class: 'cm-cs-number' },
  { tag: [t.definition(t.name), t.separator], class: 'cm-cs-name' },
  { tag: [t.typeName, t.className, t.number, t.changed, t.annotation, t.modifier, t.self, t.namespace], class: 'cm-cs-number' },
  { tag: [t.operator, t.operatorKeyword, t.url, t.escape, t.regexp, t.link, t.special(t.string)], class: 'cm-cs-operator' },
  { tag: [t.meta, t.comment], class: 'cm-cs-comment' },
  { tag: [t.atom, t.bool, t.special(t.variableName)], class: 'cm-cs-number' },
  { tag: [t.processingInstruction, t.string, t.inserted], class: 'cm-cs-string' },
  { tag: t.invalid, class: 'cm-cs-invalid' },
]);

export const petrolTheme = [editorBasis, syntaxHighlighting(petrolHighlightStyle)];
