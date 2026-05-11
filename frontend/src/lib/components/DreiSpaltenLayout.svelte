<script lang="ts">
  /*
   * Wiederverwendbares 3-Spalten-Layout fuer Aufgaben-Detail-Views.
   *
   * Verwaltet die Resizer (Pointer-Drag) und bindet sie an den globalen
   * LayoutStore -- damit sich alle Aufgaben-Typen die Spaltenbreite
   * teilen und Anpassungen persistiert sind.
   *
   * Nutzung:
   *   <DreiSpaltenLayout>
   *     {#snippet links()}...{/snippet}
   *     {#snippet mitte()}...{/snippet}
   *     {#snippet rechts()}...{/snippet}
   *   </DreiSpaltenLayout>
   */
  import type { Snippet } from 'svelte';
  import { layout } from '../stores/LayoutStore.svelte';

  interface Props {
    links: Snippet;
    mitte: Snippet;
    rechts: Snippet;
  }
  let { links, mitte, rechts }: Props = $props();

  const HANDLE_PX = 6;
  let container: HTMLDivElement | undefined = $state();

  let spaltenStil = $derived(
    `grid-template-columns: ${layout.detailSpalten[0]}fr ${HANDLE_PX}px ${layout.detailSpalten[1]}fr ${HANDLE_PX}px ${layout.detailSpalten[2]}fr;`,
  );

  function startDrag(event: PointerEvent, position: 0 | 1): void {
    if (!container) return;
    event.preventDefault();
    const breite = container.clientWidth - HANDLE_PX * 2;
    if (breite <= 0) return;
    const startX = event.clientX;
    const startAnteile: [number, number, number] = [
      layout.detailSpalten[0],
      layout.detailSpalten[1],
      layout.detailSpalten[2],
    ];
    const target = event.currentTarget as HTMLElement;
    target.setPointerCapture(event.pointerId);

    function bewegen(e: PointerEvent): void {
      const deltaPx = e.clientX - startX;
      const deltaAnteil = deltaPx / breite;
      const neu: [number, number, number] = [...startAnteile] as [number, number, number];
      if (position === 0) {
        neu[0] = startAnteile[0] + deltaAnteil;
        neu[1] = startAnteile[1] - deltaAnteil;
      } else {
        neu[1] = startAnteile[1] + deltaAnteil;
        neu[2] = startAnteile[2] - deltaAnteil;
      }
      layout.setzeSpalten(neu);
    }
    function beenden(): void {
      target.releasePointerCapture(event.pointerId);
      window.removeEventListener('pointermove', bewegen);
      window.removeEventListener('pointerup', beenden);
      window.removeEventListener('pointercancel', beenden);
    }
    window.addEventListener('pointermove', bewegen);
    window.addEventListener('pointerup', beenden);
    window.addEventListener('pointercancel', beenden);
  }
</script>

<div class="spalten" bind:this={container} style={spaltenStil}>
  <section class="spalte links">{@render links()}</section>

  <div
    class="resizer"
    role="separator"
    aria-orientation="vertical"
    aria-label="Linke Spalte verschieben"
    onpointerdown={(e) => startDrag(e, 0)}
    ondblclick={() => layout.resetSpalten()}
    title="Ziehen zum Anpassen, Doppelklick setzt zurück"
  ></div>

  <section class="spalte mitte">{@render mitte()}</section>

  <div
    class="resizer"
    role="separator"
    aria-orientation="vertical"
    aria-label="Rechte Spalte verschieben"
    onpointerdown={(e) => startDrag(e, 1)}
    ondblclick={() => layout.resetSpalten()}
    title="Ziehen zum Anpassen, Doppelklick setzt zurück"
  ></div>

  <section class="spalte rechts">{@render rechts()}</section>
</div>

<style>
  .spalten {
    display: grid;
    flex: 1 1 auto;
    min-height: 0;
    overflow: hidden;
    height: 100%;
  }
  .spalte {
    display: flex;
    flex-direction: column;
    min-width: 0;
    min-height: 0;
    background: var(--bg-card);
    overflow: hidden;
    border-right: 1px solid var(--border);
  }
  .spalte.rechts { border-right: none; }
  .spalte.mitte { background: var(--bg); }

  .resizer {
    background: var(--border);
    cursor: col-resize;
    position: relative;
    transition: background 0.15s;
  }
  .resizer::before {
    content: '';
    position: absolute;
    inset: 0 -3px;
  }
  .resizer:hover {
    background: var(--accent);
  }
</style>
