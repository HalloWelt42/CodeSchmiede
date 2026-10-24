<script lang="ts">
  /* Startseite am Rechner: drei Karten, Gesamtfortschritt, Aktivität und Erfolge. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { fortschrittProzent, ladeStart, lead, letzteAufgabe, streak, tagesziel } from '../startseite.svelte';
  import AchievementListe from './AchievementListe.svelte';
  import EmptyState from './EmptyState.svelte';
  import Seite from './Seite.svelte';
  import StreakHeatmap from './StreakHeatmap.svelte';

  onMount(ladeStart);

  let karten = $derived([tagesziel(), letzteAufgabe(), streak()]);
</script>

{#if aufgabenStore.fehler && aufgabenStore.liste.length === 0}
  <EmptyState
    icon="fa-plug-circle-xmark"
    titel="Server nicht erreichbar"
    hinweis={`Die Aufgaben ließen sich nicht laden (${aufgabenStore.fehler}).`}
    ctaText="Erneut versuchen"
    ctaAction={() => aufgabenStore.ladeListe()}
  />
{:else if aufgabenStore.liste.length === 0 && !aufgabenStore.ladenListe}
  <EmptyState
    icon="fa-hammer"
    titel="Willkommen in der Codeschmiede"
    hinweis="Es sind noch keine Aufgaben vorhanden. Lege eine erste an unter aufgaben/python/NNN-id/aufgabe.md, die Vorlage steht in docs/AUFGABEN-FORMAT.md."
    ctaText="Aufgaben-Liste öffnen"
    ctaAction={() => route.setze('aufgaben')}
  />
{:else}
  <Seite titel="Willkommen zurück" lead={lead()}>
    <div class="karten">
      {#each karten as k (k.titel)}
        <button class="karte" onclick={k.oeffnen}>
          <span class="k-titel"><i class="fa-solid {k.icon}" aria-hidden="true"></i>{k.titel}</span>
          <span class="k-wert">{k.wert}</span>
          <span class="k-unter">{k.unter}</span>
          <span class="k-cta">{k.cta} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>
        </button>
      {/each}
    </div>

    {#if progressStore.gesamt && progressStore.gesamt.aufgaben_gesamt > 0}
      {@const g = progressStore.gesamt}
      <div class="block">
        <div class="block-kopf">
          <span>Gesamtfortschritt</span>
          <span class="num">{g.aufgaben_geloest} / {g.aufgaben_gesamt} gelöst</span>
        </div>
        <div class="balken"><span style:width="{fortschrittProzent()}%"></span></div>
        <div class="chips">
          <span class="chip gruen"><i class="fa-solid fa-check" aria-hidden="true"></i>{g.aufgaben_geloest} gelöst</span>
          <span class="chip orange"><i class="fa-solid fa-pen" aria-hidden="true"></i>{g.aufgaben_in_arbeit} in Arbeit</span>
          <span class="chip"><i class="fa-regular fa-circle" aria-hidden="true"></i>{g.aufgaben_neu} neu</span>
          <span class="chip akz"><i class="fa-solid fa-coins" aria-hidden="true"></i>{g.punkte_gesamt} / {g.punkte_maximal} Punkte</span>
        </div>
      </div>
    {/if}

    <div class="zwei">
      <StreakHeatmap />
      <AchievementListe />
    </div>
  </Seite>
{/if}
