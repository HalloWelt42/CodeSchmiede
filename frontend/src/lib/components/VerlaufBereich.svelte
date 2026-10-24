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
  }
  let { aufgabeId, stand, onUebernehmen }: Props = $props();

  let offen = $state(false);
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
      year: 'numeric',
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
  <button class="umschalter" onclick={() => (offen = !offen)}>
    <i class="fa-solid {offen ? 'fa-chevron-down' : 'fa-chevron-right'}" aria-hidden="true"></i>
    Verlauf{eintraege ? ` (${eintraege.length})` : ''}
  </button>
  {#if offen}
    {#if fehler}
      <div class="info">{fehler}</div>
    {:else if !eintraege}
      <div class="info">Lade Verlauf ...</div>
    {:else if eintraege.length === 0}
      <div class="info leer">Noch keine Abgaben vorhanden.</div>
    {:else}
      <ul class="liste">
        {#each eintraege as v (v.id)}
          <li class:bestanden={v.bestanden}>
            <button
              type="button"
              class="eintrag"
              onclick={() => uebernehmen(v)}
              title="Diesen Code in den Editor übernehmen"
            >
              <span class="status">
                <i class="fa-solid {v.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
              </span>
              <span class="zeit">{formatiereDatum(v.zeitstempel)}</span>
              <span class="metrik num">{v.laufzeit_ms === null ? '' : `${v.laufzeit_ms.toFixed(0)} ms`}</span>
              <span class="metrik num">{v.codelaenge_zeichen ?? 0} Z.</span>
            </button>
          </li>
        {/each}
      </ul>
    {/if}
  {/if}
</div>

<style>
  .verlauf {
    border-top: 1px dashed var(--border);
    padding: var(--sp-3);
  }
  .umschalter {
    background: transparent;
    border: none;
    color: var(--accent);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    cursor: pointer;
    padding: 0;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .umschalter:hover:not(:disabled) {
    background: transparent;
  }
  .info {
    margin-top: var(--sp-2);
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .info.leer {
    color: var(--fg-mute);
  }
  .liste {
    list-style: none;
    padding: 0;
    margin: var(--sp-3) 0 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .eintrag {
    width: 100%;
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 6px var(--sp-2);
    cursor: pointer;
    display: grid;
    grid-template-columns: 24px minmax(0, 1fr) 70px 70px;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-xs);
    text-align: left;
  }
  .eintrag:hover {
    border-color: var(--accent);
  }
  .status {
    color: var(--red);
    text-align: center;
  }
  .liste li.bestanden .status { color: var(--green); }
  .zeit {
    font-family: var(--mono);
    color: var(--fg-dim);
  }
  .metrik {
    color: var(--fg);
    text-align: right;
  }
</style>
