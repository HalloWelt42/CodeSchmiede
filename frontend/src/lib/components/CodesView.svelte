<script lang="ts">
  /*
   * Codes knacken in der gemeinsamen Ansicht der Steuerungsspiele: links die Aufgabe, in der Mitte Python, rechts die
   * abgefangenen Nachrichten mit einer Werkbank zum Probieren von Hand. Nichts abzuspielen: "Ablauf" ruft das Programm
   * mit den sichtbaren Nachrichten auf, "Prüfen" auch mit den versteckten. Gerechnet und verglichen wird auf dem Server.
   */
  import { spielApi } from '../api/SpielApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { CodesAnsicht, CodesKennzahlen, CodesWiedergabe } from '../types/Codes';
  import CodeWerkbank from './steuerung/CodeWerkbank.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  const BEREIT: Record<string, string> = {
    DEUTSCH: 'Anteil je Buchstabe im Deutschen in Prozent, etwa DEUTSCH["E"]',
    PAARE: 'Anteil je Buchstabenpaar in Promille, _ für Wortanfang und -ende, etwa PAARE["_D"]',
  };

  // vor dem ersten Lauf gewählte Nachricht; danach wählen die Knöpfe unter der Werkbank
  let gewaehlt = $state(0);

  function prozent(anteil: number): string {
    return `${Math.round(anteil * 100)} %`;
  }

  function millisekunden(ms: number): string {
    return `${ms.toLocaleString('de-DE', { maximumFractionDigits: ms < 10 ? 1 : 0 })} ms`;
  }

  /** Das Ergebnis Zeichen für Zeichen, abweichende Zeichen markiert. */
  function vergleich(ergebnis: string, soll: string): [string, boolean][] {
    return [...ergebnis].map((c, i) => [c, c === soll[i]]);
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: CodesAnsicht)}
  <div class="gruppe">Aufrufe</div>
  <div class="spickzettel">
    {#each [...new Set(ansicht.nachrichten.map((n) => n.aufruf))] as aufruf (aufruf)}
      <code>{aufruf}</code><span>{ansicht.nachrichten.filter((n) => n.aufruf === aufruf).map((n) => n.name).join(', ')}</span>
    {/each}
    <code>{ansicht.funktion}(geheim)</code><span>dazu die versteckten Nachrichten</span>
  </div>
  {#if ansicht.bereit.length}
    <div class="gruppe">Steht bereit</div>
    <div class="spickzettel">
      {#each ansicht.bereit as name (name)}<code>{name}</code><span>{BEREIT[name] ?? ''}</span>{/each}
    </div>
  {/if}
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle Nachrichten richtig{ansicht.mindestens < 1 ? ` (ab ${prozent(ansicht.mindestens)} der Buchstaben)` : ''}, auch die versteckten</span>
    {@render sterne(2)}<span>alle zusammen in höchstens {ansicht.sterne.ms} ms</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.zeichen} Zeichen Code</span>
  </div>
{/snippet}

{#snippet szene(ansicht: CodesAnsicht, wiedergabe: CodesWiedergabe | null)}
  {@const nachricht = wiedergabe ?? ansicht.nachrichten[gewaehlt] ?? ansicht.nachrichten[0]}
  {#if !wiedergabe}
    <div class="ablaeufe">
      {#each ansicht.nachrichten as n, i (n.name)}
        <button class="chip" class:gewaehlt={i === gewaehlt} onclick={() => (gewaehlt = i)}>{n.name}</button>
      {/each}
    </div>
  {/if}
  <div class="gruppe">{nachricht.name}<span class="dim klein">{nachricht.aufruf}</span></div>
  <div class="text">{nachricht.eingabe}</div>
  {#if wiedergabe && wiedergabe.ergebnis !== null}
    {@const richtig = wiedergabe.ergebnis === wiedergabe.soll}
    <div class="gruppe">Dein Programm ergibt</div>
    <div class="text" class:klar={richtig}>
      {#each vergleich(wiedergabe.ergebnis, wiedergabe.soll) as [c, gleich], i (i)}<span class:falsch={!gleich}>{c}</span>{/each}
    </div>
    {#if !richtig}
      <div class="gruppe">Erwartet</div>
      <div class="text">{wiedergabe.soll}</div>
    {/if}
  {/if}
  <div class="gruppe">Von Hand probieren</div>
  {#key nachricht.eingabe}
    <CodeWerkbank verfahren={ansicht.verfahren} deutsch={ansicht.deutsch} geheim={nachricht.eingabe} />
  {/key}
  <p class="dim klein">Nur zum Verstehen: gewertet wird allein, was <code>{ansicht.funktion}</code> zurückgibt.</p>
{/snippet}

{#snippet kennzahlen(ansicht: CodesAnsicht, wiedergabe: CodesWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte" style:grid-template-columns="repeat(3, minmax(0, 1fr))">
    <div><span class="num" class:gut={k.anteil === 1} class:schlecht={k.anteil < ansicht.mindestens}>{prozent(k.anteil)}</span><small>Buchstaben richtig</small></div>
    <div><span class="num">{millisekunden(k.ms)}</span><small>Zeit</small></div>
    <div><span class="num" class:gut={k.zeichen <= ansicht.sterne.zeichen}>{k.zeichen}</span><small>Zeichen Code</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Nachrichten"
  symbol="fa-key"
  planTitel=""
  abspielen={false}
  ladeAnsicht={(id) => spielApi.codesNachrichten(id)}
  probieren={(id, code) => spielApi.codesLauf(id, code)}
  mitUnfall={(_: CodesKennzahlen) => false}
  {hilfe}
  {szene}
  {kennzahlen}
/>

<style>
  .klein {
    font-size: var(--fs-sm);
    text-transform: none;
    letter-spacing: 0;
    margin: 0;
  }
  .gruppe .klein {
    margin-left: var(--sp-2);
    font-family: var(--mono);
  }
  .text {
    font: 600 var(--fs-sm) var(--mono);
    letter-spacing: 0.08em;
    line-height: 1.7;
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
    overflow-wrap: anywhere;
    max-height: 220px;
    overflow-y: auto;
    flex-shrink: 0;
  }
  .text.klar { color: var(--green); }
  .falsch {
    color: var(--red);
    text-decoration: underline;
  }
</style>
