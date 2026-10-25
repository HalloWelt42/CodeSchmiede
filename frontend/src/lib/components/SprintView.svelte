<script lang="ts">
  /*
   * Ausgabe-Sprint (Spiel): Start, zehn Fragen gegen die Uhr, Auswertung.
   *
   * Die Runde stellt der Server (spiel/sprint.py); die richtige Antwort
   * kommt erst nach der Wahl zurück, die Erklärungen mit der Auswertung.
   * Die Uhr im Browser zeigt nur an, verbindlich ist die Frist des Servers.
   * Wählen mit Klick oder den Tasten 1 bis 4.
   */
  import { onDestroy } from 'svelte';
  import { spielApi, type SprintAbschluss, type SprintRunde } from '../api/SpielApi';
  import { fassung } from '../stores/FassungStore.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  interface SprintRegeln {
    fragen: number;
    sekunden: number;
    sterne: [number, number, number];
  }

  let { detail }: { detail: AufgabeDetail } = $props();
  let regeln = $derived(detail.extra?.['sprint'] as SprintRegeln);

  type Zustand = 'start' | 'frage' | 'auswertung';
  let zustand = $state<Zustand>('start');
  let runde = $state<SprintRunde | null>(null);
  let nr = $state(0);
  let kette = $state(0);
  let gewaehlt = $state<number | null>(null);
  let richtig = $state<number | null>(null);
  let rest = $state(0);
  let abschluss = $state<SprintAbschluss | null>(null);
  let fehler = $state<string | null>(null);
  let laeuft = $state(false);

  let frage = $derived(runde?.fragen[nr] ?? null);
  let besteSterne = $derived(progressStore.proAufgabe[detail.id]?.sterne ?? 0);

  // keine neue Fassung mitten in der Runde
  $effect(() => {
    if (zustand === 'frage') return fassung.halten();
  });

  let ende = 0;
  let takt: ReturnType<typeof setInterval> | undefined;
  onDestroy(() => clearInterval(takt));

  async function starten(): Promise<void> {
    fehler = null;
    laeuft = true;
    try {
      runde = await spielApi.sprintRunde(detail.id);
      nr = 0;
      kette = 0;
      gewaehlt = richtig = null;
      abschluss = null;
      ende = Date.now() + runde.sekunden * 1000;
      rest = runde.sekunden;
      zustand = 'frage';
      clearInterval(takt);
      takt = setInterval(ticken, 250);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laeuft = false;
    }
  }

  function ticken(): void {
    rest = Math.max(0, Math.ceil((ende - Date.now()) / 1000));
    if (rest === 0) void abschliessen();
  }

  async function waehlen(i: number): Promise<void> {
    if (!runde || gewaehlt !== null || zustand !== 'frage') return;
    gewaehlt = i;
    try {
      const r = await spielApi.sprintAntwort(runde.id, nr, i);
      richtig = r.richtige_wahl;
      kette = r.richtig ? kette + 1 : 0;
      setTimeout(weiter, r.richtig ? 450 : 1100);
    } catch (e) {
      // Frist abgelaufen oder Runde vorbei: auswerten, was da ist
      fehler = (e as Error).message;
      await abschliessen();
    }
  }

  function weiter(): void {
    if (zustand !== 'frage' || !runde) return;
    if (nr + 1 >= runde.fragen.length) {
      void abschliessen();
      return;
    }
    nr += 1;
    gewaehlt = richtig = null;
  }

  async function abschliessen(): Promise<void> {
    if (!runde || zustand !== 'frage') return;
    clearInterval(takt);
    zustand = 'auswertung';
    laeuft = true;
    try {
      abschluss = await spielApi.sprintAbschluss(runde.id);
      fehler = null;
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laeuft = false;
    }
  }

  function taste(e: KeyboardEvent): void {
    if (zustand === 'frage' && /^[1-9]$/.test(e.key) && frage && +e.key <= frage.optionen.length) {
      void waehlen(+e.key - 1);
    } else if (zustand !== 'frage' && e.key === 'Enter' && !laeuft && (e.target as HTMLElement).tagName !== 'BUTTON') {
      void starten();
    }
  }

  const sterneText = (n: number) => `${n} von 3 Sternen`;
</script>

<svelte:window onkeydown={taste} />

{#snippet sterne(anzahl: number)}
  <span class="sterne gross" title={sterneText(anzahl)}>
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

<div class="sprint">
  {#if zustand === 'start'}
    <div class="block start">
      <h2><i class="fa-solid fa-stopwatch" aria-hidden="true"></i>{detail.titel}</h2>
      <p>{regeln.fragen} kurze Schnipsel, {regeln.sekunden} Sekunden: Was gibt der Code aus? Richtige Antworten in Folge bilden eine Kette.</p>
      <div class="spickzettel">
        {#each regeln.sterne as schwelle, i (i)}{@render sterne(i + 1)}<span>mindestens {schwelle} von {regeln.fragen} richtig</span>{/each}
      </div>
      <div class="start-fuss">
        {#if besteSterne}<span class="dim">Bestwert {@render sterne(besteSterne)}</span>{/if}
        <button class="knopf voll" onclick={starten} disabled={laeuft}><i class="fa-solid fa-play" aria-hidden="true"></i>Runde starten</button>
      </div>
      {#if fehler}<p class="hinweis-box fehler">{fehler}</p>{/if}
    </div>
  {:else if zustand === 'frage' && runde && frage}
    <div class="sprint-kopf">
      <span>Frage <span class="num">{nr + 1} / {runde.fragen.length}</span></span>
      <span><i class="fa-regular fa-clock" aria-hidden="true"></i> <span class="num">{rest}</span> s</span>
      <span class="kette"><i class="fa-solid fa-link" aria-hidden="true"></i> Kette {kette}</span>
    </div>
    <div class="uhr"><span style:width="{(rest / runde.sekunden) * 100}%"></span></div>
    <div class="gruppe frage-titel">Was gibt dieser Code aus?</div>
    <pre class="schnipsel">{frage.code}</pre>
    <div class="antworten">
      {#each frage.optionen as option, i (i)}
        <button
          class="antwort"
          class:richtig={richtig === i}
          class:falsch={gewaehlt === i && richtig !== null && richtig !== i}
          disabled={gewaehlt !== null}
          onclick={() => waehlen(i)}
        ><kbd>{i + 1}</kbd><span>{option}</span></button>
      {/each}
    </div>
    {#if !geraet.telefon}<p class="dim tasten">Tasten 1 bis {frage.optionen.length} wählen eine Antwort</p>{/if}
  {:else}
    {#if laeuft}
      <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Runde wird ausgewertet ...</p>
    {:else if abschluss}
      {#if abschluss.belohnung}
        <BelohnungsBand belohnung={abschluss.belohnung} />
      {:else}
        <div class="block knapp">
          <b>Noch kein Stern</b>
          <span class="dim">Für den ersten Stern braucht es {regeln.sterne[0]} richtige Antworten.</span>
        </div>
      {/if}
      <p class="zusammenfassung">
        {@render sterne(abschluss.sterne)}
        <span><span class="num">{abschluss.treffer} von {abschluss.fragen}</span> richtig, längste Kette <span class="num">{abschluss.laengste_kette}</span>, <span class="num">{Math.round(abschluss.sekunden)}</span> s</span>
      </p>
      <div class="gruppe frage-titel">Auswertung</div>
      <div>
        {#each abschluss.auswertung as z, i (i)}
          {@const ok = z.gewaehlt === z.richtig}
          <div class="auswertung-zeile">
            <i class="fa-solid {ok ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>
            <div>
              <pre>{z.code}</pre>
              {#if ok}
                <span class="dim">{z.optionen[z.richtig]}</span>
              {:else}
                <span>Richtig: <b>{z.optionen[z.richtig]}</b>, {z.gewaehlt === null ? 'nicht beantwortet' : `gewählt: ${z.optionen[z.gewaehlt]}`}</span>
                <div class="erklaerung">{z.warum}</div>
              {/if}
            </div>
          </div>
        {/each}
      </div>
    {/if}
    {#if fehler && !abschluss}<p class="hinweis-box fehler">{fehler}</p>{/if}
    <div class="knoepfe">
      <button class="knopf voll" onclick={starten} disabled={laeuft}><i class="fa-solid fa-rotate" aria-hidden="true"></i>Neue Runde</button>
      <button class="knopf" onclick={() => route.setze('spiele')}><i class="fa-solid fa-arrow-left" aria-hidden="true"></i>Zu den Spielen</button>
    </div>
  {/if}
</div>

<style>
  .start h2 {
    margin: 0 0 var(--sp-2);
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-lg);
  }
  .start h2 i { color: var(--accent); }
  .start p { margin: 0 0 var(--sp-3); color: var(--fg-dim); }
  .start-fuss {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    margin-top: var(--sp-4);
  }
  .start-fuss .knopf { margin-left: auto; }
  .frage-titel { margin: 0; }
  .tasten {
    margin: 0;
    font-size: var(--fs-sm);
    text-align: center;
  }
  .knapp {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .zusammenfassung {
    margin: 0;
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    flex-wrap: wrap;
  }
  .knoepfe {
    display: flex;
    gap: var(--sp-2);
    flex-wrap: wrap;
  }
</style>
