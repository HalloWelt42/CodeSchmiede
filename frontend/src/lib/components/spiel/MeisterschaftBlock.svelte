<script lang="ts">
  /* Meisterschaft je Sprache und für die Spiele mit Rang. */
  import type { BereichStand } from '../../api/SpielApi';
  import { konfig } from '../../stores/KonfigStore.svelte';
  import { medaille, RANG_NAME } from '../../spielanzeige';

  let { bereiche }: { bereiche: BereichStand[] } = $props();
  let raenge = $derived(konfig.daten.spiel?.raenge);
  const prozent = (anteil: number) => Math.floor(anteil * 100);
</script>

<div class="block">
  <div class="block-kopf"><span>Meisterschaft</span><span>Anteil der erreichbaren Punkte</span></div>
  <div class="meister">
    {#each bereiche as b (b.id)}
      <span class="medaille {medaille(b.rang)}" title={b.rang ? RANG_NAME[b.rang] : 'noch kein Rang'}><i class="fa-solid fa-medal" aria-hidden="true"></i></span>
      <span>{b.titel}</span>
      <span class="balken"><span style:width="{prozent(b.anteil)}%"></span></span>
      <span class="num" title="{b.punkte} von {b.moeglich} Punkten">{prozent(b.anteil)} %</span>
    {/each}
  </div>
  {#if raenge}
    <!-- geschützte Leerzeichen: "ab 25 %" bricht nie auseinander -->
    <p class="regel dim">Bronze ab&nbsp;{prozent(raenge.bronze)}&nbsp;%, Silber ab&nbsp;{prozent(raenge.silber)}&nbsp;%, Gold ab&nbsp;{prozent(raenge.gold)}&nbsp;%</p>
  {/if}
</div>

<style>
  .regel { font-size: var(--fs-xs); margin: var(--sp-2) 0 0; }
</style>
