<script lang="ts">
  /*
   * Mittelspalte: CodeMirror 6 mit Petrol-Theme. Bidirektional an
   * `code` gebunden, damit der Parent (`AufgabenDetail`) den aktuellen
   * Inhalt kennt und an POST /api/submissions schicken kann.
   */
  import { onDestroy, onMount } from 'svelte';
  import type { EditorView } from '@codemirror/view';
  import { erstelleEditor } from '../editor/EditorFactory';

  let { sprache, code = $bindable() }: { sprache: string; code: string } = $props();

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
</style>
