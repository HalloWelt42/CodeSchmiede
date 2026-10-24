<script lang="ts">
  /*
   * Filterzeile der Aufgabenliste am Rechner. Stufen und Sprachen kommen
   * aus der zentralen Konfiguration, Pfade aus dem PfadeStore.
   */
  import { konfig } from '../stores/KonfigStore.svelte';
  import { pfadeStore } from '../stores/PfadeStore.svelte';
  import { aufgabenFilter as f, OHNE_PFAD } from '../stores/AufgabenFilterStore.svelte';

  let { treffer }: { treffer: number } = $props();

  let pfadeSortiert = $derived([...pfadeStore.liste].sort((a, b) => a.titel.localeCompare(b.titel)));

  $effect(() => {
    void [f.suche, f.sprache, f.schwierigkeit, f.status, f.pfad];
    f.speichern();
  });
</script>

<div class="filter">
  <label class="suche">
    <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
    <input type="text" placeholder="Suchen (Titel, ID, #Tag)" bind:value={f.suche} />
    {#if f.suche}
      <button class="leeren" onclick={() => (f.suche = '')} aria-label="Suche leeren">
        <i class="fa-solid fa-xmark" aria-hidden="true"></i>
      </button>
    {/if}
  </label>
  <select class="wahl" bind:value={f.sprache} aria-label="Sprache">
    <option value="">Alle Sprachen</option>
    {#each konfig.daten.sprachen as s (s.id)}<option value={s.id}>{s.titel}</option>{/each}
  </select>
  <select class="wahl" bind:value={f.schwierigkeit} aria-label="Stufe">
    <option value="">Alle Stufen</option>
    {#each konfig.daten.schwierigkeiten as s (s.id)}<option value={s.id}>{s.titel}</option>{/each}
  </select>
  <select class="wahl" bind:value={f.status} aria-label="Status">
    <option value="">Alle Status</option>
    <option value="neu">Neu</option>
    <option value="in_arbeit">In Arbeit</option>
    <option value="geloest">Gelöst</option>
  </select>
  <select class="wahl" bind:value={f.pfad} aria-label="Pfad">
    <option value="">Alle Pfade</option>
    <option value={OHNE_PFAD}>Ohne Pfad</option>
    {#each pfadeSortiert as p (p.id)}<option value={p.id}>{p.titel}</option>{/each}
  </select>
  <span class="treffer"><span class="num">{treffer}</span> Treffer</span>
  {#if f.aktiv}
    <button class="knopf-klein" onclick={() => f.zuruecksetzen()}>
      <i class="fa-solid fa-xmark" aria-hidden="true"></i>Zurücksetzen
    </button>
  {/if}
</div>

<style>
  .wahl {
    max-width: 170px;
  }
</style>
