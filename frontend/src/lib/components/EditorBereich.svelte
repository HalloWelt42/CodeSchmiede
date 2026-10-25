<script lang="ts">
  /*
   * Mittelspalte: CodeMirror 6 mit Petrol-Theme. Bidirektional an
   * `code` gebunden, damit der Parent (`AufgabenDetail`) den aktuellen
   * Inhalt kennt und an POST /api/submissions schicken kann.
   */
  import { onDestroy, onMount } from 'svelte';
  import type { EditorView } from '@codemirror/view';
  import { erstelleEditor } from '../editor/EditorFactory';
  import { setzeZeilenMarke } from '../editor/ZeilenMarke';

  interface Props {
    sprache: string;
    code: string;
    /** hervorgehobene Zeile (ab 1), etwa beim Abspielen eines Laufs */
    markierteZeile?: number | null;
  }
  let { sprache, code = $bindable(), markierteZeile = null }: Props = $props();

  let host: HTMLDivElement | undefined = $state();
  let view: EditorView | null = null;

  onMount(() => {
    if (!host) return;
    view = erstelleEditor({
      parent: host,
      sprache,
      initialerCode: code,
      beiAenderung: (neuerCode) => {
        code = neuerCode;
      },
    });
  });

  // Synchronisiere CodeMirror, wenn der Parent code von aussen aendert
  // (z.B. Reset auf starter_code, oder Detail-Wechsel). Schleifen-Schutz:
  // nur dispatchen, wenn der Doc-Inhalt wirklich abweicht -- sonst zaehlt
  // jedes beiAenderung-Update nochmal hier rein und triggert sich selbst.
  $effect(() => {
    if (view && code !== view.state.doc.toString()) {
      view.dispatch({
        changes: { from: 0, to: view.state.doc.length, insert: code },
      });
    }
  });

  $effect(() => {
    if (view) setzeZeilenMarke(view, markierteZeile);
  });

  onDestroy(() => {
    view?.destroy();
  });
</script>

<div class="editor" bind:this={host}></div>

<style>
  .editor {
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: var(--bg);
  }
  .editor :global(.cm-editor) {
    height: 100%;
  }
  .editor :global(.cm-editor.cm-focused) {
    outline: none;
  }
  .editor :global(.cm-zeilen-marke) {
    background: color-mix(in srgb, var(--accent) 16%, transparent);
  }
</style>
