<script lang="ts">
  /*
   * Spalten jeder Aufgabenansicht: Aufgabe | Editor | Ergebnis.
   *
   * Am Rechner drei Spalten nebeneinander. Raster "frei" hat verschiebbare
   * Trenner (Breiten im LayoutStore, für alle Aufgabentypen gleich),
   * Raster "css" feste, mitwachsende Seitenspalten für den Bildvergleich.
   * Am Telefon werden dieselben Inhalte zu drei Schritten mit Segment oben
   * und Knopf unten; nach dem Prüfen springt die Ansicht zum Ergebnis.
   *
   * Der Prüfen-Knopf gehört dem Layout, damit er überall an derselben
   * Stelle steht: im Kopf der Editorspalte, am Telefon unten.
   *
   * Nutzung:
   *   <DreiSpaltenLayout mitteTitel="Editor, Python" pruefen={{ aktion, laeuft, moeglich }}>
   *     {#snippet links()}...{/snippet}
   *     {#snippet mitte()}...{/snippet}
   *     {#snippet rechts()}...{/snippet}
   *   </DreiSpaltenLayout>
   */
  import type { Snippet } from 'svelte';
  import { layout } from '../stores/LayoutStore.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';

  interface Pruefen {
    aktion: () => void;
    laeuft: boolean;
    moeglich: boolean;
  }

  interface Props {
    links: Snippet;
    mitte: Snippet;
    rechts: Snippet;
    raster?: 'frei' | 'css';
    mitteTitel: string;
    /** rechts im Kopf der Editorspalte, vor dem Prüfen-Knopf */
    mitteZusatz?: Snippet;
    /** ohne Titel hat die rechte Spalte keinen eigenen Kopf */
    rechtsTitel?: string;
    pruefen?: Pruefen;
    /** Beschriftung der drei Schritte am Telefon */
    schritte?: [string, string, string];
    /** Knopf am Telefon zum mittleren Schritt, ab Werk "Zum <Schritt>" */
    zumEditor?: string;
  }
  let {
    links,
    mitte,
    rechts,
    raster = 'frei',
    mitteTitel,
    mitteZusatz,
    rechtsTitel,
    pruefen,
    schritte = ['Aufgabe', 'Code', 'Ergebnis'],
    zumEditor,
  }: Props = $props();

  const SCHRITT_ICONS = ['fa-file-lines', 'fa-code', 'fa-flask'];
  const TRENNER_PX = 5;

  let container: HTMLDivElement | undefined = $state();
  let schritt = $state(0);

  let spaltenStil = $derived(
    raster === 'frei'
      ? `grid-template-columns: minmax(0, ${layout.detailSpalten[0]}fr) ${TRENNER_PX}px minmax(0, ${layout.detailSpalten[1]}fr) ${TRENNER_PX}px minmax(0, ${layout.detailSpalten[2]}fr);`
      : '',
  );

  function pruefenStarten(): void {
    pruefen?.aktion();
    if (geraet.telefon) schritt = 2;
  }

  function startDrag(event: PointerEvent, position: 0 | 1): void {
    if (!container) return;
    event.preventDefault();
    const breite = container.clientWidth - TRENNER_PX * 2;
    if (breite <= 0) return;
    const startX = event.clientX;
    const start: [number, number, number] = [...layout.detailSpalten];
    const ziel = event.currentTarget as HTMLElement;
    ziel.setPointerCapture(event.pointerId);

    function bewegen(e: PointerEvent): void {
      const delta = (e.clientX - startX) / breite;
      const neu: [number, number, number] = [...start];
      neu[position] = start[position] + delta;
      neu[position + 1] = start[position + 1] - delta;
      layout.setzeSpalten(neu);
    }
    function beenden(): void {
      ziel.releasePointerCapture(event.pointerId);
      window.removeEventListener('pointermove', bewegen);
      window.removeEventListener('pointerup', beenden);
      window.removeEventListener('pointercancel', beenden);
    }
    window.addEventListener('pointermove', bewegen);
    window.addEventListener('pointerup', beenden);
    window.addEventListener('pointercancel', beenden);
  }
</script>

{#snippet pruefenKnopf(gross: boolean)}
  {#if pruefen}
    <button class="knopf voll" class:gross disabled={pruefen.laeuft || !pruefen.moeglich} onclick={pruefenStarten}>
      <i class="fa-solid {pruefen.laeuft ? 'fa-spinner fa-spin' : 'fa-play'}" aria-hidden="true"></i>
      {pruefen.laeuft ? 'Läuft ...' : 'Prüfen'}
    </button>
  {/if}
{/snippet}

{#snippet mitteKopf()}
  <div class="spalten-kopf">
    <span class="kopf-titel">{mitteTitel}</span>
    {#if mitteZusatz}<span class="zusatz">{@render mitteZusatz()}</span>{/if}
    {#if !geraet.telefon}{@render pruefenKnopf(false)}{/if}
  </div>
{/snippet}

{#if geraet.telefon}
  <div class="telefon-schritte">
    <div class="segment-rahmen">
      <div class="segment" role="tablist">
        {#each schritte as titel, i (i)}
          <button class:aktiv={schritt === i} role="tab" aria-selected={schritt === i} onclick={() => (schritt = i)}>
            <i class="fa-solid {SCHRITT_ICONS[i]}" aria-hidden="true"></i>{titel}
          </button>
        {/each}
      </div>
    </div>
    <section class="pane" class:aktiv={schritt === 0}>
      <div class="pane-inhalt">{@render links()}</div>
      <div class="t-unten">
        <button class="knopf voll" onclick={() => (schritt = 1)}>
          <i class="fa-solid fa-code" aria-hidden="true"></i>{zumEditor ?? `Zum ${schritte[1]}`}
        </button>
      </div>
    </section>
    <section class="pane mitte" class:aktiv={schritt === 1}>
      {@render mitteKopf()}
      <div class="pane-inhalt">{@render mitte()}</div>
      {#if pruefen}<div class="t-unten">{@render pruefenKnopf(true)}</div>{/if}
    </section>
    <section class="pane" class:aktiv={schritt === 2}>
      <div class="pane-inhalt">{@render rechts()}</div>
    </section>
  </div>
{:else}
  <div class="spalten raster-{raster}" bind:this={container} style={spaltenStil}>
    <section class="spalte">{@render links()}</section>
    {#if raster === 'frei'}
      <div
        class="trenner"
        role="separator"
        aria-orientation="vertical"
        aria-label="Linke Spalte verschieben"
        onpointerdown={(e) => startDrag(e, 0)}
        ondblclick={() => layout.resetSpalten()}
        title="Ziehen zum Anpassen, Doppelklick setzt zurück"
      ></div>
    {/if}
    <section class="spalte mitte">
      {@render mitteKopf()}
      {@render mitte()}
    </section>
    {#if raster === 'frei'}
      <div
        class="trenner"
        role="separator"
        aria-orientation="vertical"
        aria-label="Rechte Spalte verschieben"
        onpointerdown={(e) => startDrag(e, 1)}
        ondblclick={() => layout.resetSpalten()}
        title="Ziehen zum Anpassen, Doppelklick setzt zurück"
      ></div>
    {/if}
    <section class="spalte">
      {#if rechtsTitel}<div class="spalten-kopf"><span>{rechtsTitel}</span></div>{/if}
      {@render rechts()}
    </section>
  </div>
{/if}

<style>
  .spalten {
    flex: 1;
    min-height: 0;
    display: grid;
    overflow: hidden;
  }
  /* Aufgabe und Vergleich wachsen mit der Breite bis zur Obergrenze, der Editor bekommt den Rest */
  .spalten.raster-css {
    grid-template-columns: clamp(270px, 22vw, 290px) minmax(0, 1fr) clamp(340px, 30vw, 400px);
  }
  .spalten.raster-css > .spalte + .spalte {
    border-left: 1px solid var(--border);
  }
  .spalte {
    min-width: 0;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .spalte.mitte { background: var(--bg); }
  .trenner {
    background: var(--border);
    cursor: col-resize;
    position: relative;
    transition: background 0.15s;
  }
  .trenner::before {
    content: '';
    position: absolute;
    inset: 0 -3px;
  }
  .trenner:hover { background: var(--accent); }
  .mitte .spalten-kopf { background: var(--bg-card); }
  .kopf-titel {
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .zusatz {
    margin-left: auto;
    text-transform: none;
    letter-spacing: 0;
    color: var(--fg);
  }
  .zusatz + .knopf { margin-left: var(--sp-2); }

  /* Telefon: drei Schritte */
  .telefon-schritte {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
  }
  .segment-rahmen {
    flex: none;
    padding: var(--sp-2) var(--sp-3);
    border-bottom: 1px solid var(--border);
  }
  .pane {
    display: none;
    flex: 1;
    min-height: 0;
    flex-direction: column;
  }
  .pane.aktiv { display: flex; }
  .pane.mitte { background: var(--bg); }
  .pane-inhalt {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
  }
  .t-unten {
    background: var(--bg-card);
  }
  .knopf.gross {
    flex: 1;
    justify-content: center;
    height: 48px;
    font-size: var(--fs-sm);
  }
</style>
