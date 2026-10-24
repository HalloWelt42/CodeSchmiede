<script lang="ts">
  /* Startseite am Telefon: Karten als Zeilen, knapper Fortschritt, letzte zwölf Wochen. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../../stores/AufgabenStore.svelte';
  import { progressStore } from '../../stores/ProgressStore.svelte';
  import { fortschrittProzent, ladeStart, lead, letzteAufgabe, streak, tagesziel } from '../../startseite.svelte';
  import EmptyState from '../EmptyState.svelte';
  import Seite from '../Seite.svelte';
  import StreakHeatmap from '../StreakHeatmap.svelte';

  onMount(ladeStart);

  let karten = $derived([
    tagesziel(),
    { ...letzteAufgabe(), titel: 'Weitermachen' },
    streak(),
  ]);
</script>

{#if aufgabenStore.fehler && aufgabenStore.liste.length === 0}
  <EmptyState
    icon="fa-plug-circle-xmark"
    titel="Server nicht erreichbar"
    hinweis={`Die Aufgaben ließen sich nicht laden (${aufgabenStore.fehler}).`}
    ctaText="Erneut versuchen"
    ctaAction={() => aufgabenStore.ladeListe()}
  />
{:else}
  <Seite titel="Willkommen zurück" lead={lead()}>
    <div class="t-karten">
      {#each karten as k (k.titel)}
        <button class="karte" onclick={k.oeffnen}>
          <i class="fa-solid {k.icon}" aria-hidden="true"></i>
          <span class="text">
            <span class="k-titel">{k.titel}</span>
            <span class="k-wert">{k.wert}</span>
            <span class="k-unter">{k.unter}</span>
          </span>
          <i class="fa-solid fa-chevron-right mute" aria-hidden="true"></i>
        </button>
      {/each}
    </div>

    {#if progressStore.gesamt && progressStore.gesamt.aufgaben_gesamt > 0}
      {@const g = progressStore.gesamt}
      <div class="block">
        <div class="block-kopf"><span>Fortschritt</span><span class="num">{g.aufgaben_geloest} / {g.aufgaben_gesamt}</span></div>
        <div class="balken"><span style:width="{fortschrittProzent()}%"></span></div>
        <div class="chips">
          <span class="chip gruen">{g.aufgaben_geloest} gelöst</span>
          <span class="chip orange">{g.aufgaben_in_arbeit} in Arbeit</span>
          <span class="chip akz">{g.punkte_gesamt} Punkte</span>
        </div>
      </div>
    {/if}

    <StreakHeatmap wochen={12} />
  </Seite>
{/if}

<style>
  .text {
    min-width: 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .karte > i:last-child {
    font-size: 14px;
  }
</style>
