<script lang="ts">
  /* Startseite am Telefon: Stufe mit Serie, Tagesauftrag, Weitermachen, letzte zwölf Wochen. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../../stores/AufgabenStore.svelte';
  import { route } from '../../stores/RouteStore.svelte';
  import { spielStore } from '../../stores/SpielStore.svelte';
  import { ladeStart, lead, letzteAufgabe, wiederholungen } from '../../startseite.svelte';
  import { schildText } from '../../spielanzeige';
  import EmptyState from '../EmptyState.svelte';
  import Seite from '../Seite.svelte';
  import StreakHeatmap from '../StreakHeatmap.svelte';
  import AuftragsZiele from '../spiel/AuftragsZiele.svelte';
  import Schilde from '../spiel/Schilde.svelte';
  import StufeAnzeige from '../spiel/StufeAnzeige.svelte';

  onMount(ladeStart);

  let karten = $derived.by(() => {
    const liste = [letzteAufgabe()];
    const faellig = wiederholungen();
    if (faellig) {
      liste.push({ icon: 'fa-rotate', titel: 'Wiederholen', wert: faellig.text, unter: 'Gelöstes auffrischen', oeffnen: faellig.oeffnen });
    }
    const e = spielStore.erfolge;
    if (e) {
      liste.push({
        icon: 'fa-medal',
        titel: 'Erfolge',
        wert: `${e.erreicht} von ${e.gesamt} erreicht`,
        unter: 'Meilensteine, Serie, Technik',
        oeffnen: () => route.setze('erfolge'),
      });
    }
    return liste;
  });
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
    {#if spielStore.stand}
      {@const stand = spielStore.stand}
      <div class="karte abstand">
        <StufeAnzeige stufe={stand.stufe} klein />
        <div class="serie" title={schildText(stand.serie)}>
          <i class="fa-solid fa-fire flamme" aria-hidden="true"></i><span class="num">{stand.serie.aktuell}</span>
          {stand.serie.aktuell === 1 ? 'Tag' : 'Tage'} Serie
          <span class="schilde"><Schilde serie={stand.serie} /></span>
        </div>
      </div>
      <div class="karte abstand">
        <span class="k-titel">
          <i class="fa-solid fa-bullseye" aria-hidden="true"></i>Tagesauftrag
          <span class="num zaehler">{stand.auftrag.ziele.filter((z) => z.erledigt).length} / {stand.auftrag.ziele.length}</span>
        </span>
        <AuftragsZiele auftrag={stand.auftrag} />
      </div>
    {/if}

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

    <StreakHeatmap wochen={12} />
  </Seite>
{/if}

<style>
  .abstand { margin-bottom: var(--sp-2); }
  .serie {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: var(--sp-2);
    font-size: var(--fs-sm);
  }
  .schilde {
    margin-left: auto;
    display: inline-flex;
    gap: 4px;
  }
  .zaehler {
    margin-left: auto;
    color: var(--fg);
  }
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
