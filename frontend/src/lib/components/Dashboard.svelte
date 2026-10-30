<script lang="ts">
  /* Startseite am Rechner: Stufe, Serie und Tagesauftrag, Meisterschaft und Erfolge, Aktivität. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { spielStore } from '../stores/SpielStore.svelte';
  import { kursStore } from '../stores/KursStore.svelte';
  import { oeffneKapitel, weiterText } from '../kurs/weiter';
  import { ladeStart, lead, weitermachen, wiederholungen } from '../startseite.svelte';
  import { schildText, serieUnter, tage } from '../spielanzeige';
  import EmptyState from './EmptyState.svelte';
  import Seite from './Seite.svelte';
  import StreakHeatmap from './StreakHeatmap.svelte';
  import AuftragsZiele from './spiel/AuftragsZiele.svelte';
  import ErfolgeBlock from './spiel/ErfolgeBlock.svelte';
  import MeisterschaftBlock from './spiel/MeisterschaftBlock.svelte';
  import Schilde from './spiel/Schilde.svelte';
  import StufeAnzeige from './spiel/StufeAnzeige.svelte';

  onMount(() => {
    ladeStart();
    void kursStore.laden(true);
  });

  let weiter = $derived(weitermachen());
  let faellig = $derived(wiederholungen());
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
    {#snippet aktionen()}
      {#if kursStore.weiter}
        {@const k = kursStore.weiter}
        <button class="knopf voll kuerzbar kurs-knopf" onclick={() => oeffneKapitel(k)} title="Kurs, Kapitel {k.nr}: {k.titel}, {weiterText(k)}"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i><span>Kurs: {k.titel}</span></button>
      {/if}
      {#if weiter}
        <button class="knopf primaer kuerzbar" onclick={weiter.oeffnen} title={weiter.text}><i class="fa-solid fa-play" aria-hidden="true"></i><span>{weiter.text}</span></button>
      {/if}
      {#if faellig}
        <button class="knopf" onclick={faellig.oeffnen}><i class="fa-solid fa-rotate" aria-hidden="true"></i>{faellig.text}</button>
      {/if}
    {/snippet}

    {#if spielStore.stand}
      {@const stand = spielStore.stand}
      <div class="karten">
        <div class="karte">
          <span class="k-titel"><i class="fa-solid fa-hammer" aria-hidden="true"></i>Stufe</span>
          <StufeAnzeige stufe={stand.stufe} />
        </div>
        <div class="karte">
          <span class="k-titel"><i class="fa-solid fa-fire" aria-hidden="true"></i>Serie</span>
          <span class="k-wert"><span class="num">{stand.serie.aktuell}</span> {stand.serie.aktuell === 1 ? 'Tag' : 'Tage'}</span>
          <span class="k-unter" title="längste Serie: {tage(stand.serie.laengste)}">{serieUnter(stand.serie)}</span>
          {#if stand.serie.schilde_max > 0}
            <span class="k-unter schilde"><Schilde serie={stand.serie} /> {schildText(stand.serie)}</span>
          {/if}
        </div>
        <div class="karte">
          <span class="k-titel">
            <i class="fa-solid fa-bullseye" aria-hidden="true"></i>Tagesauftrag
            <span class="num zaehler">{stand.auftrag.ziele.filter((z) => z.erledigt).length} / {stand.auftrag.ziele.length}</span>
          </span>
          <AuftragsZiele auftrag={stand.auftrag} />
          <span class="k-cta">
            {#if stand.auftrag.gutgeschrieben}
              Erledigt, +{stand.auftrag.bonus} Punkte gutgeschrieben
            {:else}
              Alle {stand.auftrag.ziele.length === 3 ? 'drei' : stand.auftrag.ziele.length}: +{stand.auftrag.bonus} Punkte
            {/if}
          </span>
        </div>
      </div>

      <div class="zwei">
        <MeisterschaftBlock bereiche={stand.meisterschaft} />
        {#if spielStore.erfolge}<ErfolgeBlock erfolge={spielStore.erfolge} />{/if}
      </div>
    {/if}

    <StreakHeatmap />
  </Seite>
{/if}

<style>
  /* drei Knöpfe im Kopf: der Kurs gibt zuerst nach */
  .kurs-knopf { max-width: clamp(120px, 14vw, 300px); }
  .schilde {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .zaehler {
    margin-left: auto;
    color: var(--fg);
  }
</style>
