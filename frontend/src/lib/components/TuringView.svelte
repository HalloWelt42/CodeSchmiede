<script lang="ts">
  /*
   * Turingmaschine in der gemeinsamen Ansicht der Steuerungsspiele: statt Python eine Übergangstabelle mit
   * Zustandsdiagramm, rechts das Band mit Kopf und die Spur der Schritte. Gerechnet wird auf dem Server ohne Sandbox.
   */
  import { spielApi } from '../api/SpielApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { CodeZugriff } from '../types/Steuerung';
  import type { TuringAnsicht, TuringKennzahlen, TuringWiedergabe } from '../types/Turing';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';
  import TuringTabelle from './steuerung/TuringTabelle.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  const FENSTER = 15;

  function bild(w: TuringWiedergabe | null, nr: number) {
    return w && nr >= 0 ? w.bilder[nr] : null;
  }

  /** Felder rund um den Kopf: [Index, Zeichen] */
  function felder(band: string, von: number, kopf: number): [number, string][] {
    const anfang = Math.min(von, kopf) - 2;
    const ende = Math.max(von + band.length - 1, kopf) + 2;
    const mitte = Math.max(anfang, Math.min(kopf - Math.floor(FENSTER / 2), ende - FENSTER + 1));
    const liste: [number, string][] = [];
    for (let i = mitte; i < mitte + FENSTER && i <= ende + FENSTER; i++) {
      liste.push([i, i >= von && i < von + band.length ? band[i - von] : '_']);
    }
    return liste;
  }

  function ziel(w: TuringWiedergabe): string {
    return w.soll_zustand != null ? `hält in ${w.soll_zustand}` : `${w.soll || 'leer'}`;
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: TuringAnsicht)}
  <div class="gruppe">Band und Befehle</div>
  <div class="spickzettel">
    <code>{ansicht.zeichen.join(' ')} _</code><span>Zeichen auf dem Band, _ ist leer</span>
    <code>L R N</code><span>Kopf nach links, rechts, bleibt stehen</span>
    <code>{ansicht.start}</code><span>Startzustand; der Kopf steht am {ansicht.kopf === 'ende' ? 'letzten' : 'ersten'} Zeichen</span>
    <code>{ansicht.ende.join(', ')}</code><span>hier hält die Maschine an</span>
    <code>plus 1 -&gt; 0 L plus</code><span>eine Zeile als Text: Zustand liest -&gt; schreibt geht danach</span>
  </div>
  <div class="gruppe">Bänder</div>
  <div class="spickzettel">
    {#each ansicht.baender as b (b.name ?? b.band)}
      <code>{b.band || '(leer)'}</code><span>{b.soll_zustand != null ? `hält in ${b.soll_zustand}` : `wird ${b.soll || '(leer)'}`}</span>
    {/each}
  </div>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle Bänder richtig, je höchstens {ansicht.grenze} Schritte</span>
    {@render sterne(2)}<span>höchstens {ansicht.sterne.zustaende} {ansicht.sterne.zustaende === 1 ? 'Zustand' : 'Zustände'} (ohne {ansicht.ende.join(', ')})</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.zeilen} Zeilen</span>
  </div>
{/snippet}

{#snippet editor(ansicht: TuringAnsicht, zugriff: CodeZugriff, wiedergabe: TuringWiedergabe | null, nr: number)}
  {@const b = bild(wiedergabe, nr)}
  <TuringTabelle {ansicht} {zugriff} aktiveZeile={b?.[5] ?? null} aktiverZustand={b?.[4] ?? null} />
{/snippet}

{#snippet szene(ansicht: TuringAnsicht, wiedergabe: TuringWiedergabe | null, nr: number)}
  {@const b = bild(wiedergabe, nr) ?? bild(wiedergabe, 0)}
  {@const erstes = ansicht.baender[0]}
  {@const band = b ? b[1] : erstes.band}
  {@const von = b ? b[2] : 0}
  {@const kopf = b ? b[3] : ansicht.kopf === 'ende' ? Math.max(0, erstes.band.length - 1) : 0}
  {@const zustand = b ? b[4] : ansicht.start}
  <div class="band">
    {#each felder(band, von, kopf) as [i, c] (i)}
      <div class="zelle-b" class:leer={c === '_'} class:kopf={i === kopf}>
        {#if i === kopf}<span class="kopf-marke"><span>{zustand}</span><i class="fa-solid fa-caret-down" aria-hidden="true"></i></span>{/if}
        {c}
      </div>
    {/each}
  </div>
  {#if wiedergabe}
    <p class="ziel dim">Band {wiedergabe.start || '(leer)'}: soll {ziel(wiedergabe)}, ergibt {wiedergabe.ergebnis || '(leer)'}</p>
  {/if}
{/snippet}

{#snippet plan(_: TuringAnsicht, wiedergabe: TuringWiedergabe | null, __: number, zeit: number, springe: (s: number) => void)}
  <div class="spur">
    {#if wiedergabe}
      {#each wiedergabe.bilder.slice(1) as [n, band, von, kopf, zustand], i (n)}
        {@const vorher = wiedergabe.bilder[i]}
        {@const gelesen = vorher[3] >= vorher[2] && vorher[3] < vorher[2] + vorher[1].length ? vorher[1][vorher[3] - vorher[2]] : '_'}
        {@const geschrieben = vorher[3] >= von && vorher[3] < von + band.length ? band[vorher[3] - von] : '_'}
        <button class="spur-zeile" class:aktiv={n === zeit} onclick={() => springe(n)}>
          {n}: {vorher[4]} liest {gelesen}, schreibt {geschrieben}, geht {kopf < vorher[3] ? 'L' : kopf > vorher[3] ? 'R' : 'N'}, jetzt {zustand}
        </button>
      {/each}
    {:else}
      <span class="dim">Ablauf zeigt jeden Schritt.</span>
    {/if}
  </div>
{/snippet}

{#snippet kennzahlen(ansicht: TuringAnsicht, wiedergabe: TuringWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte" style:grid-template-columns="repeat(3, minmax(0, 1fr))">
    <div><span class="num">{k.schritte}</span><small>Schritte</small></div>
    <div><span class="num" class:gut={k.zustaende <= ansicht.sterne.zustaende}>{k.zustaende}</span><small>Zustände</small></div>
    <div><span class="num" class:gut={k.zeilen <= ansicht.sterne.zeilen}>{k.zeilen}</span><small>Zeilen</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Band"
  symbol="fa-tape"
  planTitel="Spur"
  planHinweis="Klick springt zum Schritt"
  takt={0.7}
  ladeAnsicht={(id) => spielApi.turingMaschine(id)}
  probieren={(id, code) => spielApi.turingLauf(id, code)}
  mitteTitel={(code) => `Übergangstabelle, ${code.split('\n').filter((z) => /->/.test(z.split('#')[0])).length} Zeilen`}
  zeitText={(zeit, dauer) => `Schritt ${zeit} von ${dauer}`}
  mitUnfall={(_: TuringKennzahlen) => false}
  {hilfe}
  {editor}
  {szene}
  {plan}
  {kennzahlen}
/>

<style>
  .band {
    display: flex;
    justify-content: center;
    gap: 3px;
    padding: 30px 0 6px;
  }
  .zelle-b {
    position: relative;
    width: 30px;
    height: 38px;
    display: grid;
    place-items: center;
    border: 1px solid var(--border-strong);
    background: var(--bg-card-2);
    font: 700 18px var(--mono);
  }
  .zelle-b.leer {
    color: var(--fg-mute);
    font-weight: 400;
  }
  .zelle-b.kopf { border-color: var(--accent); }
  .kopf-marke {
    position: absolute;
    top: -30px;
    left: 50%;
    transform: translateX(-50%);
    color: var(--accent);
    text-align: center;
    white-space: nowrap;
    font-size: 12px;
    line-height: 1.1;
  }
  .kopf-marke span {
    display: block;
    font: 600 11px var(--mono);
  }
  .ziel {
    margin: 0;
    font-size: var(--fs-sm);
    text-align: center;
  }
  .spur {
    max-height: 180px;
    overflow-y: auto;
    border: 1px solid var(--border);
    background: var(--bg);
    padding: 4px;
    font-family: var(--mono);
    font-size: 12px;
  }
  .spur-zeile {
    display: block;
    width: 100%;
    text-align: left;
    padding: 2px 4px;
    border: 0;
    background: transparent;
    color: var(--fg-dim);
    font: inherit;
    cursor: pointer;
  }
  .spur-zeile.aktiv {
    color: var(--accent);
    background: color-mix(in srgb, var(--accent) 10%, transparent);
  }
</style>
