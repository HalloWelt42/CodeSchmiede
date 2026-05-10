<script lang="ts">
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { farbeZuCss } from '../types/Konfig';
  import type { ProgressStatus } from '../api/ProgressApi';
  import AufgabenFilter from './AufgabenFilter.svelte';
  import EmptyState from './EmptyState.svelte';

  let suche = $state('');
  let sprache = $state('');
  let schwierigkeit = $state('');
  let status = $state<ProgressStatus | ''>('');

  onMount(async () => {
    if (aufgabenStore.liste.length === 0) await aufgabenStore.ladeListe();
    if (!progressStore.gesamt) await progressStore.ladeAlles();
  });

  function oeffne(id: string): void {
    route.setze('aufgabe', id);
  }

  function statusIcon(s: string): string {
    if (s === 'geloest') return 'fa-circle-check';
    if (s === 'in_arbeit') return 'fa-pen-to-square';
    return 'fa-circle';
  }

  function schwierigkeitFarbe(id: string): string {
    return farbeZuCss(konfig.schwierigkeitFarbe(id));
  }

  function schwierigkeitTitel(id: string): string {
    return konfig.schwierigkeitTitel(id);
  }

  function findeTitel(id: string): string {
    return aufgabenStore.findeKurz(id)?.titel ?? id;
  }

  let gefiltert = $derived(
    aufgabenStore.liste.filter((a) => {
      if (sprache && a.sprache !== sprache) return false;
      if (schwierigkeit && a.schwierigkeit !== schwierigkeit) return false;
      if (status && progressStore.status(a.id) !== status) return false;
      if (suche.trim()) {
        const q = suche.trim().toLowerCase();
        const haystack = [
          a.id,
          a.titel,
          ...a.tags,
        ]
          .join(' ')
          .toLowerCase();
        if (!haystack.includes(q)) return false;
      }
      return true;
    }),
  );
</script>

<div class="liste">
  <header class="kopf">
    <h1>Aufgaben</h1>
  </header>

  {#if aufgabenStore.ladenListe}
    <p class="info">Lade Aufgaben ...</p>
  {:else if aufgabenStore.fehler}
    <p class="info fehler">Fehler: {aufgabenStore.fehler}</p>
  {:else if aufgabenStore.liste.length === 0}
    <EmptyState
      icon="fa-folder-open"
      titel="Noch keine Aufgaben"
      hinweis="Lege ein Verzeichnis unter aufgaben/python/NNN-id/ an. Das Backend indiziert sie automatisch."
    />
  {:else}
    <AufgabenFilter
      bind:suche
      bind:sprache
      bind:schwierigkeit
      bind:status
      treffer={gefiltert.length}
      gesamt={aufgabenStore.liste.length}
    />

    {#if gefiltert.length === 0}
      <EmptyState
        icon="fa-magnifying-glass"
        titel="Kein Treffer"
        hinweis="Passe die Filter an oder setze sie zurück."
      />
    {:else}
      <div class="tabelle">
        {#each gefiltert as aufgabe (aufgabe.id)}
          {@const aktSt = progressStore.status(aufgabe.id)}
          {@const farbe = schwierigkeitFarbe(aufgabe.schwierigkeit)}
          <article
            class="zeile status-{aktSt}"
            class:gesperrt={aufgabe.gesperrt}
            onclick={() => oeffne(aufgabe.id)}
            role="button"
            tabindex="0"
            onkeydown={(e) => { if (e.key === 'Enter') oeffne(aufgabe.id); }}
          >
            <span class="status-icon" aria-label={aktSt} title={aufgabe.gesperrt ? 'gesperrt' : aktSt}>
              {#if aufgabe.gesperrt}
                <i class="fa-solid fa-lock" aria-hidden="true"></i>
              {:else}
                <i class="fa-solid {statusIcon(aktSt)}" aria-hidden="true"></i>
              {/if}
            </span>

            <div class="haupt">
              <span class="id">{aufgabe.id}</span>
              <span class="titel">{aufgabe.titel}</span>
              {#if aufgabe.gesperrt}
                <span class="sperre-hint" title="Voraussetzungen offen">
                  <i class="fa-solid fa-link" aria-hidden="true"></i>
                  Erst lösen:
                  {#each aufgabe.voraussetzungen_offen as v, i}
                    <strong>{findeTitel(v)}</strong>{#if i < aufgabe.voraussetzungen_offen.length - 1}, {/if}
                  {/each}
                </span>
              {/if}
            </div>

            <div class="meta">
              <span
                class="badge"
                style:color={farbe}
                style:border-color={farbe}
              >{schwierigkeitTitel(aufgabe.schwierigkeit)}</span>
              <span class="badge sprache">{aufgabe.sprache}</span>
              <span class="zeit">
                <i class="fa-regular fa-clock" aria-hidden="true"></i>
                {aufgabe.schaetz_minuten} min
              </span>
              <span class="score num" title="Erreicht / Maximum">
                <i class="fa-solid fa-coins" aria-hidden="true"></i>
                {progressStore.proAufgabe[aufgabe.id]?.punkte_erreicht ?? 0}/{aufgabe.schwierigkeit_score}
              </span>
            </div>

            <div class="tags">
              {#each aufgabe.tags as tag}
                <span class="tag">#{tag}</span>
              {/each}
            </div>

            <button
              class="oeffnen"
              aria-label="Aufgabe öffnen"
              onclick={(e) => { e.stopPropagation(); oeffne(aufgabe.id); }}
            >
              <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
            </button>
          </article>
        {/each}
      </div>
    {/if}
  {/if}
</div>

<style>
  .liste {
    padding: var(--sp-5) var(--sp-5) var(--sp-4);
    overflow-y: auto;
  }
  .kopf {
    margin-bottom: var(--sp-2);
  }
  h1 {
    margin: 0;
    font-size: var(--fs-xl);
    font-weight: 600;
  }
  .info {
    color: var(--fg-dim);
    font-family: var(--quick);
  }
  .info.fehler {
    color: var(--red);
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
  .zeile.gesperrt {
    opacity: 0.55;
    border-left: 3px dashed var(--fg-mute);
  }
  .zeile.gesperrt:hover {
    opacity: 0.85;
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
  .zeile.gesperrt .status-icon {
    color: var(--fg-mute);
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
  .sperre-hint {
    color: var(--orange);
    font-size: var(--fs-xs);
    font-family: var(--quick);
    margin-top: 2px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    flex-wrap: wrap;
  }
  .sperre-hint strong {
    font-weight: 600;
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
  .badge.sprache { color: var(--accent); border-color: var(--accent); }
  .zeit {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .score {
    font-size: var(--fs-sm);
    color: var(--accent);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
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
