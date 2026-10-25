<script lang="ts">
  /* Stufe als Ring mit Titel und Punkten bis zur nächsten Stufe. */
  import type { StufenStand } from '../../api/SpielApi';
  import { stufenAnteil } from '../../stores/SpielStore.svelte';
  import { zahl } from '../../spielanzeige';

  let { stufe, klein = false }: { stufe: StufenStand; klein?: boolean } = $props();
  let anteil = $derived(stufenAnteil(stufe));
</script>

<div class="stufe">
  <div class="stufe-ring" class:klein style:--anteil={anteil}>
    <b>{stufe.stufe}</b>{#if !klein}<small>Stufe</small>{/if}
  </div>
  <div class="stufe-text">
    <b>{stufe.titel}</b>
    {#if klein}
      <span><span class="num">{zahl(stufe.punkte)}</span> / <span class="num">{zahl(stufe.bis)}</span> Punkte</span>
    {:else}
      <span><span class="num">{zahl(stufe.punkte)}</span> von <span class="num">{zahl(stufe.bis)}</span> Punkten bis Stufe {stufe.stufe + 1}</span>
    {/if}
    <div class="balken"><span style:width="{anteil}%"></span></div>
    {#if !klein && stufe.naechster_titel}
      <span>Stufe {stufe.naechster_titel_ab_stufe} macht dich zum {stufe.naechster_titel}</span>
    {/if}
  </div>
</div>

<style>
  .balken { margin-top: 4px; }
  .stufe-ring.klein { width: 60px; height: 60px; }
  .stufe-ring.klein b { font-size: 20px; }
</style>
