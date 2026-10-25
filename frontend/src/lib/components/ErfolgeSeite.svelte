<script lang="ts">
  /* Alle Erfolge nach Gruppen; erreichte mit Medaille, offene blass mit Stand. */
  import { onMount } from 'svelte';
  import type { ErfolgsGruppe, Rang } from '../api/SpielApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { spielStore } from '../stores/SpielStore.svelte';
  import { medaille } from '../spielanzeige';
  import Seite from './Seite.svelte';

  const GRUPPEN: { id: ErfolgsGruppe; titel: string }[] = [
    { id: 'meilensteine', titel: 'Meilensteine' },
    { id: 'serie', titel: 'Serie' },
    { id: 'technik', titel: 'Technik' },
    { id: 'spiele', titel: 'Spiele' },
  ];
  const RAENGE: { id: Rang; titel: string }[] = [
    { id: 'gold', titel: 'Gold' },
    { id: 'silber', titel: 'Silber' },
    { id: 'bronze', titel: 'Bronze' },
  ];

  onMount(() => {
    if (!spielStore.erfolge) void progressStore.ladeAlles();
  });

  let liste = $derived(spielStore.erfolge);
  let lead = $derived(liste ? `${liste.erreicht} von ${liste.gesamt} erreicht; Meilensteine haben drei Stufen` : 'Lade ...');
</script>

<Seite titel="Erfolge" {lead}>
  {#snippet kopf()}
    {#if liste}
      <div class="kennzahlen">
        {#each RAENGE as r (r.id)}
          <div class="kennzahl"><span class="num {r.id}">{liste.eintraege.filter((e) => e.rang === r.id).length}</span><small>{r.titel}</small></div>
        {/each}
        <div class="kennzahl"><span class="num offen">{liste.gesamt - liste.erreicht}</span><small>offen</small></div>
      </div>
    {/if}
  {/snippet}

  {#if liste}
    {#each GRUPPEN as g (g.id)}
      {@const eintraege = liste.eintraege.filter((e) => e.gruppe === g.id)}
      {#if eintraege.length > 0}
        <div class="gruppe">{g.titel}</div>
        <div class="kachel-raster">
          {#each eintraege as e (e.id)}
            <div class="erfolg-kachel" class:gesperrt={!e.erreicht}>
              <span class="gross-medaille {medaille(e.rang)}"><i class="fa-solid {e.icon}" aria-hidden="true"></i></span>
              <div>
                <b>{e.titel}</b>
                <small>{e.beschreibung}</small>
                {#if e.rang !== 'gold' && e.ziel > 1}
                  <div class="balken"><span style:width="{Math.min(100, (e.wert / e.ziel) * 100)}%"></span></div>
                {/if}
              </div>
            </div>
          {/each}
        </div>
      {/if}
    {/each}
  {/if}
</Seite>

<style>
  .num.gold { color: var(--gold); }
  .num.silber { color: var(--silber); }
  .num.bronze { color: var(--bronze); }
  .num.offen { color: var(--fg); }
</style>
