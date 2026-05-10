<script lang="ts">
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';

  onMount(async () => {
    if (aufgabenStore.liste.length === 0) await aufgabenStore.ladeListe();
    if (!progressStore.gesamt) await progressStore.ladeAlles();
  });

  function oeffne(id: string): void {
    route.setze('aufgabe', id);
  }

  function statusIcon(status: string): string {
    if (status === 'geloest') return 'fa-circle-check';
    if (status === 'in_arbeit') return 'fa-pen-to-square';
    return 'fa-circle';
  }
</script>

<div class="liste">
  <header class="kopf">
    <div>
      <h1>Aufgaben</h1>
      <p class="lead">
        {#if aufgabenStore.ladenListe}
          Lade ...
        {:else if aufgabenStore.fehler}
          Fehler: {aufgabenStore.fehler}
        {:else}
          {aufgabenStore.liste.length} Aufgaben verfügbar.
        {/if}
      </p>
    </div>
  </header>

  <div class="tabelle">
    {#each aufgabenStore.liste as aufgabe (aufgabe.id)}
      {@const status = progressStore.status(aufgabe.id)}
      <article class="zeile status-{status}"
               onclick={() => oeffne(aufgabe.id)} role="button" tabindex="0"
               onkeydown={(e) => { if (e.key === 'Enter') oeffne(aufgabe.id); }}>
        <span class="status-icon" aria-label={status} title={status}>
          <i class="fa-solid {statusIcon(status)}" aria-hidden="true"></i>
        </span>

        <div class="haupt">
          <span class="id">{aufgabe.id}</span>
          <span class="titel">{aufgabe.titel}</span>
        </div>

        <div class="meta">
          <span class="badge schwierigkeit-{aufgabe.schwierigkeit}">{aufgabe.schwierigkeit}</span>
          <span class="badge sprache">{aufgabe.sprache}</span>
          <span class="zeit">
            <i class="fa-regular fa-clock" aria-hidden="true"></i>
            {aufgabe.schaetz_minuten} min
          </span>
          <span class="score num">{aufgabe.schwierigkeit_score}</span>
        </div>

        <div class="tags">
          {#each aufgabe.tags as tag}
            <span class="tag">#{tag}</span>
          {/each}
        </div>

        <button class="oeffnen" aria-label="Aufgabe öffnen" onclick={(e) => { e.stopPropagation(); oeffne(aufgabe.id); }}>
          <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </button>
      </article>
    {/each}
  </div>
</div>

<style>
  .liste {
    padding: var(--sp-5) var(--sp-5) var(--sp-4);
    overflow-y: auto;
  }
  .kopf {
    margin-bottom: var(--sp-4);
  }
  h1 {
    margin: 0 0 var(--sp-2);
    font-size: var(--fs-xl);
    font-weight: 600;
  }
  .lead {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }

  .tabelle {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .zeile {
    display: grid;
    grid-template-columns: 28px 1.6fr 1.4fr 1.2fr 44px;
    gap: var(--sp-3);
    align-items: center;
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-3) var(--sp-4);
    transition: border-color 0.15s, transform 0.15s;
    cursor: pointer;
  }
  .zeile:hover {
    border-color: var(--accent);
    transform: translateY(-1px);
  }
  .zeile.status-geloest {
    border-left: 3px solid var(--green);
  }
  .zeile.status-in_arbeit {
    border-left: 3px solid var(--orange);
  }
  .status-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--fg-mute);
    font-size: var(--fs-md);
  }
  .zeile.status-geloest .status-icon {
    color: var(--green);
  }
  .zeile.status-in_arbeit .status-icon {
    color: var(--orange);
  }
  .haupt {
    display: flex;
    flex-direction: column;
    gap: 2px;
    min-width: 0;
  }
  .id {
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg-mute);
  }
  .titel {
    font-size: var(--fs-md);
    font-weight: 600;
    color: var(--fg);
  }
  .meta {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    flex-wrap: wrap;
  }
  .badge {
    padding: 2px 8px;
    border: 1px solid var(--border);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    border-radius: var(--radius-sm);
    background: var(--bg-card);
  }
  .badge.schwierigkeit-anfaenger { color: var(--green); border-color: var(--green); }
  .badge.schwierigkeit-mittel { color: var(--orange); border-color: var(--orange); }
  .badge.schwierigkeit-fortgeschritten,
  .badge.schwierigkeit-experte { color: var(--red); border-color: var(--red); }
  .badge.sprache { color: var(--accent); border-color: var(--accent); }
  .zeit {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .score { font-size: var(--fs-md); color: var(--fg-dim); }
  .tags { display: flex; gap: var(--sp-1); flex-wrap: wrap; }
  .tag {
    padding: 1px 6px;
    background: var(--bg-elev);
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
    font-family: var(--mono);
  }
  .oeffnen {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 36px;
    height: 36px;
    padding: 0;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .oeffnen:hover { color: var(--accent); border-color: var(--accent); }
</style>
