<script lang="ts">
  /* Die fünf auffälligsten Erfolge: erreichte nach Rang, dann die nächsten. */
  import type { ErfolgsListe } from '../../api/SpielApi';
  import { pfadVon, route } from '../../stores/RouteStore.svelte';
  import { erfolgeNachStand, medaille, RANG_NAME } from '../../spielanzeige';

  let { erfolge, anzahl = 5 }: { erfolge: ErfolgsListe; anzahl?: number } = $props();
  let auswahl = $derived(erfolgeNachStand(erfolge.eintraege).slice(0, anzahl));
</script>

<div class="block">
  <div class="block-kopf">
    <span>Erfolge</span>
    <span><span class="num">{erfolge.erreicht} / {erfolge.gesamt}</span> <a href={pfadVon('erfolge')} onclick={(e) => { e.preventDefault(); route.setze('erfolge'); }}>alle</a></span>
  </div>
  {#each auswahl as e (e.id)}
    <div class="erfolg" class:da={e.erreicht} title={e.beschreibung}>
      <span class="medaille {medaille(e.rang)}"><i class="fa-solid {e.icon}" aria-hidden="true"></i></span>
      <span class="name">{e.titel}</span>
      <span class="dim num">{e.rang ? RANG_NAME[e.rang] : `${Math.min(e.wert, e.ziel)} / ${e.ziel}`}</span>
    </div>
  {/each}
</div>

<style>
  a { margin-left: 6px; }
</style>
