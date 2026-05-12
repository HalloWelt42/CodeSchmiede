<script lang="ts">
  /*
   * Filter-Leiste für die Aufgabenliste.
   * Schwierigkeiten und Sprachen kommen aus dem KonfigStore -- nichts
   * mehr im Code hardcodiert.
   */
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import { pfadeStore } from '../stores/PfadeStore.svelte';
  import type { ProgressStatus } from '../api/ProgressApi';

  interface Props {
    suche: string;
    sprache: string;
    schwierigkeit: string;
    status: ProgressStatus | '';
    pfad: string;
    treffer: number;
    gesamt: number;
  }

  let {
    suche = $bindable(),
    sprache = $bindable(),
    schwierigkeit = $bindable(),
    status = $bindable(),
    pfad = $bindable(),
    treffer,
    gesamt,
  }: Props = $props();

  function zuruecksetzen(): void {
    suche = '';
    sprache = '';
    schwierigkeit = '';
    status = '';
    pfad = '';
  }

  let aktiv = $derived(
    suche.length > 0 || sprache !== '' || schwierigkeit !== '' || status !== '' || pfad !== '',
  );

  let pfade_sortiert = $derived([...pfadeStore.liste].sort((a, b) => a.titel.localeCompare(b.titel)));
</script>

<div class="filter">
  <div class="suche">
    <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
    <input
      type="text"
      placeholder="Suchen (Titel, ID, Tag)"
      bind:value={suche}
    />
  </div>

  <select bind:value={sprache} aria-label="Sprache">
    <option value="">Alle Sprachen</option>
    {#each konfig.daten.sprachen as s (s.id)}
      <option value={s.id}>{s.titel}</option>
    {/each}
  </select>

  <select bind:value={schwierigkeit} aria-label="Schwierigkeit">
    <option value="">Alle Stufen</option>
    {#each konfig.daten.schwierigkeiten as st (st.id)}
      <option value={st.id}>{st.titel}</option>
    {/each}
  </select>

  <select bind:value={status} aria-label="Status">
    <option value="">Alle Status</option>
    <option value="neu">Neu</option>
    <option value="in_arbeit">In Arbeit</option>
    <option value="geloest">Gelöst</option>
  </select>

  <select bind:value={pfad} aria-label="Pfad">
    <option value="">Alle Pfade</option>
    <option value="__ohne__">Ohne Pfad</option>
    {#each pfade_sortiert as p (p.id)}
      <option value={p.id}>{p.titel}</option>
    {/each}
  </select>

  <span class="treffer" class:gefiltert={aktiv}>
    {#if aktiv}
      <i class="fa-solid fa-filter" aria-hidden="true"></i>
      <span class="num">{treffer}</span>
      von <span class="num">{gesamt}</span> Aufgaben sichtbar
    {:else}
      <span class="num">{gesamt}</span> Aufgaben
    {/if}
  </span>

  {#if aktiv}
    <button class="reset" onclick={zuruecksetzen}>
      <i class="fa-solid fa-xmark" aria-hidden="true"></i>
      Filter zurücksetzen
    </button>
  {/if}
</div>

<style>
  .filter {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: var(--sp-2) 0 var(--sp-3);
    flex-wrap: wrap;
  }
  .suche {
    position: relative;
    flex: 1;
    min-width: 220px;
  }
  .suche i {
    position: absolute;
    left: var(--sp-3);
    top: 50%;
    transform: translateY(-50%);
    color: var(--fg-mute);
    font-size: var(--fs-sm);
    pointer-events: none;
  }
  .suche input {
    width: 100%;
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--fg);
    font-family: var(--sans);
    font-size: var(--fs-sm);
    padding: 8px var(--sp-3) 8px var(--sp-5);
    border-radius: var(--radius-sm);
    height: 36px;
  }
  .suche input:focus {
    outline: none;
    border-color: var(--accent);
  }
  select {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--fg);
    font-family: var(--sans);
    font-size: var(--fs-sm);
    padding: 0 var(--sp-3);
    height: 36px;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  select:focus {
    outline: none;
    border-color: var(--accent);
  }
  .treffer {
    color: var(--fg-dim);
    font-size: var(--fs-sm);
    margin-left: auto;
    padding: 0 var(--sp-2);
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .treffer.gefiltert {
    color: var(--accent);
  }
  .treffer .num {
    color: var(--fg);
    font-weight: 600;
  }
  .treffer.gefiltert .num {
    color: var(--accent);
  }
  .reset {
    background: transparent;
    border: 1px solid var(--accent);
    color: var(--accent);
    height: 36px;
    padding: 0 12px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: var(--fs-sm);
    font-weight: 500;
  }
  .reset:hover {
    color: var(--red);
    border-color: var(--red);
  }
</style>
