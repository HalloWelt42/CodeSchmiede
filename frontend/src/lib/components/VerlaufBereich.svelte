<script lang="ts">
  /*
   * Verlauf der eigenen Abgaben zu einer Aufgabe -- gemeinsam für alle
   * Aufgabentypen mit Editor. Ein Klick auf einen Eintrag holt dessen
   * Code zurück in den Editor.
   *
   * `stand` zählt die Elternansicht nach jeder Abgabe hoch; ist der
   * Verlauf schon geladen, lädt er dann neu.
   */
  import { aufgabenApi } from '../api/AufgabenApi';
  import type { VerlaufEintrag } from '../types/Submission';

  interface Props {
    aufgabeId: string;
    stand: number;
    onUebernehmen: (code: string) => void;
    /** gleich aufgeklappt, etwa in einem eigenen Reiter */
    anfangsOffen?: boolean;
  }
  let { aufgabeId, stand, onUebernehmen, anfangsOffen = false }: Props = $props();

  // svelte-ignore state_referenced_locally
  let offen = $state(anfangsOffen);
  let eintraege = $state<VerlaufEintrag[] | null>(null);
  let fehler = $state<string | null>(null);

  async function lade(): Promise<void> {
    try {
      eintraege = await aufgabenApi.submissionsVerlauf(aufgabeId, 20);
      fehler = null;
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  $effect(() => {
    stand;
    if (offen) lade();
  });

  function formatiereDatum(iso: string): string {
    return new Date(iso).toLocaleString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
    });
  }

  function uebernehmen(eintrag: VerlaufEintrag): void {
    onUebernehmen(eintrag.code);
    offen = false;
  }
</script>

<div class="verlauf">
  <button class="gruppe umschalter" onclick={() => (offen = !offen)} aria-expanded={offen}>
    <i class="fa-solid {offen ? 'fa-chevron-down' : 'fa-chevron-right'}" aria-hidden="true"></i>
    Verlauf{eintraege ? ` (${eintraege.length})` : ''}
  </button>
  {#if offen}
    {#if fehler}
      <p class="info">{fehler}</p>
    {:else if !eintraege}
      <p class="info">Lade Verlauf ...</p>
    {:else if eintraege.length === 0}
      <p class="info">Noch keine Abgaben.</p>
    {:else}
      {#each eintraege as v (v.id)}
        <button class="test-zeile eintrag" onclick={() => uebernehmen(v)} title="Diesen Code in den Editor übernehmen">
          <i class="fa-solid {v.bestanden ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>
          <span class="zeit">{formatiereDatum(v.zeitstempel)}</span>
          <span class="num rechts">{v.laufzeit_ms === null ? '' : `${v.laufzeit_ms.toFixed(0)} ms`}</span>
          <span class="dim zeichen">{v.codelaenge_zeichen ?? 0} Z.</span>
        </button>
      {/each}
    {/if}
  {/if}
</div>

<style>
  .verlauf { margin-top: var(--sp-4); }
  .umschalter {
    border: 0;
    padding: 0;
    background: transparent;
    cursor: pointer;
  }
  .umschalter:hover:not(:disabled) { background: transparent; color: var(--accent); }
  .info {
    margin: var(--sp-2) 0 0;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }
  .eintrag {
    width: 100%;
    border: 0;
    border-bottom: 1px solid var(--border);
    border-radius: 0;
    background: transparent;
    color: var(--fg);
    text-align: left;
    cursor: pointer;
  }
  .eintrag:hover:not(:disabled) { background: var(--bg-card-2); border-color: var(--border); }
  .zeit { color: var(--fg-dim); }
  .rechts { margin-left: auto; font-weight: 500; }
  .zeichen { width: 52px; text-align: right; }
</style>
