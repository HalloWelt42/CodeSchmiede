<script lang="ts">
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { pfadeStore } from '../stores/PfadeStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import type { Pfad } from '../types/Aufgabe';

  onMount(async () => {
    if (pfadeStore.liste.length === 0) await pfadeStore.ladeListe();
    if (aufgabenStore.liste.length === 0) await aufgabenStore.ladeListe();
    if (!progressStore.gesamt) await progressStore.ladeAlles();
  });

  function findeTitel(id: string): string {
    return aufgabenStore.findeKurz(id)?.titel ?? id;
  }

  function oeffne(id: string): void {
    route.setze('aufgabe', id);
  }

  function pfadFortschritt(pfad: Pfad): { geloest: number; gesamt: number; prozent: number } {
    const gesamt = pfad.reihenfolge.length;
    const geloest = pfad.reihenfolge.filter(
      (id) => progressStore.status(id) === 'geloest',
    ).length;
    return { geloest, gesamt, prozent: gesamt === 0 ? 0 : Math.round((geloest / gesamt) * 100) };
  }

  function statusIcon(id: string): string {
    const s = progressStore.status(id);
    if (s === 'geloest') return 'fa-circle-check';
    if (s === 'in_arbeit') return 'fa-pen-to-square';
    return 'fa-circle';
  }
</script>

<div class="liste">
  <header class="kopf">
    <h1>Pfade</h1>
    <p class="lead">Didaktisch geordnete Aufgaben-Reihen.</p>
  </header>

  {#if pfadeStore.laden}
    <p class="info">Lade ...</p>
  {:else if pfadeStore.fehler}
    <p class="info fehler">Fehler: {pfadeStore.fehler}</p>
  {:else}
    {#each pfadeStore.liste as pfad (pfad.id)}
      {@const fb = pfadFortschritt(pfad)}
      <article class="pfad-karte">
        <header class="pfad-kopf">
          <i class="fa-solid fa-route" aria-hidden="true"></i>
          <div class="info-zeile">
            <span class="titel">{pfad.titel}</span>
            <span class="anzahl num">{pfad.reihenfolge.length} Aufgaben</span>
          </div>
        </header>

        <p class="beschreibung">{pfad.beschreibung}</p>

        <ol class="schritte">
          {#each pfad.reihenfolge as id, i (id)}
            {@const status = progressStore.status(id)}
            <li class="schritt status-{status}"
                onclick={() => oeffne(id)} role="button" tabindex="0"
                onkeydown={(e) => { if (e.key === 'Enter') oeffne(id); }}>
              <span class="nummer num">{i + 1}</span>
              <div class="text">
                <span class="aufgabe-id">{id}</span>
                <span class="aufgabe-titel">{findeTitel(id)}</span>
              </div>
              <i class="fa-solid {statusIcon(id)} status-icon-{status}" aria-hidden="true"></i>
            </li>
          {/each}
        </ol>

        <div class="fortschritt">
          <span class="balken"><span class="fuell" style="width: {fb.prozent}%"></span></span>
          <span class="dim num">{fb.geloest} / {fb.gesamt} gelöst</span>
        </div>
      </article>
    {/each}
  {/if}
</div>

<style>
  .liste {
    padding: var(--sp-5) var(--sp-5) var(--sp-4);
    overflow-y: auto;
  }
  .kopf { margin-bottom: var(--sp-4); }
  h1 { margin: 0 0 var(--sp-2); font-size: var(--fs-xl); font-weight: 600; }
  .lead {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .info { color: var(--fg-dim); }
  .info.fehler { color: var(--red); }
  .dim { color: var(--fg-dim); font-size: var(--fs-xs); }

  .pfad-karte {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-4);
    max-width: 760px;
    margin-bottom: var(--sp-3);
  }
  .pfad-kopf {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    margin-bottom: var(--sp-3);
  }
  .pfad-kopf i { color: var(--accent); font-size: var(--fs-xl); }
  .info-zeile {
    display: flex;
    align-items: baseline;
    gap: var(--sp-3);
    flex: 1;
  }
  .titel { font-size: var(--fs-lg); font-weight: 600; }
  .anzahl {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .beschreibung {
    color: var(--fg-dim);
    font-family: var(--quick);
    margin: 0 0 var(--sp-4);
    line-height: 1.65;
  }
  .schritte {
    list-style: none;
    padding: 0;
    margin: 0 0 var(--sp-4);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .schritte li {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: var(--bg-card);
    border: 1px solid var(--border);
    cursor: pointer;
    transition: border-color 0.15s;
  }
  .schritte li:hover { border-color: var(--accent); }
  .schritte li.status-geloest {
    border-left: 3px solid var(--green);
  }
  .schritte li.status-in_arbeit {
    border-left: 3px solid var(--orange);
  }
  .status-icon-geloest { color: var(--green); }
  .status-icon-in_arbeit { color: var(--orange); }
  .status-icon-neu { color: var(--fg-mute); }
  .nummer {
    width: 32px;
    height: 32px;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-elev);
    color: var(--accent);
    border: 1px solid var(--border);
    font-size: var(--fs-md);
  }
  .text {
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 0;
  }
  .aufgabe-id {
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg-mute);
  }
  .aufgabe-titel { font-size: var(--fs-md); font-weight: 500; }
  .fortschritt {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
  }
  .balken {
    flex: 1;
    height: 8px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    overflow: hidden;
  }
  .fuell { display: block; height: 100%; background: var(--accent); }
</style>
