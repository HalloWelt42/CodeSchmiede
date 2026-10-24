<script lang="ts">
  /*
   * Gestaffelte Hinweise einer Aufgabe. Das erste Öffnen meldet der
   * Server (kostet Punkte, wenn der Hinweis etwas kostet); danach bleibt
   * er als gesehen markiert.
   */
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { markdownRenderer } from '../markdown/MarkdownRenderer';
  import type { Hint } from '../types/Aufgabe';

  interface Props {
    aufgabeId: string;
    hints: Hint[];
    schwierigkeit_score: number;
  }
  let { aufgabeId, hints, schwierigkeit_score }: Props = $props();

  // aufgeklappt in dieser Ansicht
  let offen = $state<Set<number>>(new Set());
  // schon gemeldet (aus dem Fortschritt)
  let gesehen = $derived(progressStore.proAufgabe[aufgabeId]?.hints_genutzt ?? 0);
  let restPunkte = $derived(
    Math.max(0, schwierigkeit_score - hints.slice(0, gesehen).reduce((s, h) => s + h.kosten, 0)),
  );

  async function umschalten(i: number): Promise<void> {
    const neu = new Set(offen);
    if (neu.has(i)) {
      neu.delete(i);
      offen = neu;
      return;
    }
    neu.add(i);
    offen = neu;
    if (i + 1 > gesehen) {
      try {
        await aufgabenApi.hintGeoeffnet(aufgabeId, i);
        await progressStore.ladeAlles();
      } catch {
        // der Hinweis bleibt trotzdem offen
      }
    }
  }
</script>

<div class="kopf">
  <span class="gruppe">Hinweise</span>
  <span class="num rest">{restPunkte} / {schwierigkeit_score} Punkte</span>
</div>
<ol class="hints">
  {#each hints as hint, i (i)}
    {@const istOffen = offen.has(i)}
    {@const istGesehen = i < gesehen}
    <li>
      <button class="hint-toggle" class:offen={istOffen} class:gesehen={istGesehen && !istOffen} onclick={() => umschalten(i)}>
        <i class="fa-solid {istOffen ? 'fa-lock-open' : istGesehen ? 'fa-eye' : 'fa-lock'}" aria-hidden="true"></i>
        Hinweis {i + 1}
        {#if istGesehen}<span class="status-text">gesehen</span>{/if}
        {#if hint.kosten > 0}
          <span class="kosten">{hint.kosten} Punkte</span>
        {:else}
          <span class="kosten frei">kostenlos</span>
        {/if}
      </button>
      {#if istOffen}
        <div class="hint-text">{@html markdownRenderer.rendere(hint.text)}</div>
      {/if}
    </li>
  {/each}
</ol>

<style>
  .kopf {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: var(--sp-2);
  }
  .kopf .gruppe { margin: 0; }
  .rest {
    font-size: var(--fs-sm);
    color: var(--accent);
  }
  .hints {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
  }
  .hint-toggle {
    width: 100%;
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: 6px var(--sp-3);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--bg-card-2);
    color: var(--fg-dim);
    font-family: var(--sans);
    font-size: var(--fs-sm);
    text-align: left;
  }
  .hint-toggle:hover:not(:disabled) { border-color: var(--accent); color: var(--fg); }
  .hint-toggle.offen { color: var(--accent); border-color: var(--accent); }
  .status-text {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .kosten {
    margin-left: auto;
    font-size: var(--fs-xs);
    color: var(--orange);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .kosten.frei { color: var(--green); }
  .hint-text {
    margin-top: var(--sp-1);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .hint-text :global(p) { margin: 0 0 var(--sp-1); }
  .hint-text :global(p:last-child) { margin: 0; }
</style>
