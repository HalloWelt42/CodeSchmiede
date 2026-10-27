<script lang="ts">
  /*
   * KV-Werkstatt in der gemeinsamen Ansicht der Steuerungsspiele: in der Mitte das KV-Diagramm als Editor, rechts die
   * gewählte Belegung (bei den Segmenten a bis g als 7-Segment-Anzeige mit Soll), die ganze Tabelle mit Soll und Ist
   * und der Schaltplan, den die Formel ergibt. Ohne Abspielen; jede Änderung rechnet sofort neu (auf dem Server, ohne
   * Sandbox). Die vier Teilschritte sind in jedem Level dieselben.
   */
  import { spielApi } from '../api/SpielApi';
  import { istSiebenSegment } from '../steuerung/schaltplan';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { KvAnsicht, KvKennzahlen, KvWiedergabe } from '../types/Kv';
  import type { CodeZugriff } from '../types/Steuerung';
  import KvRaster from './steuerung/KvRaster.svelte';
  import SiebenSegment from './steuerung/SiebenSegment.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  /** bei vielen Ausgängen nur der Wert, falsche rot: sonst wird die Tabelle breiter als ein Telefon */
  function knapp(ansicht: KvAnsicht): boolean {
    return ansicht.ausgaenge.length > 3;
  }
  function bits(ansicht: KvAnsicht, b: number): string {
    const n = ansicht.eingaenge.length;
    return b.toString(2).padStart(n, '0');
  }
  function name(ansicht: KvAnsicht, b: number): string {
    return ansicht.namen[b] ?? bits(ansicht, b);
  }
  function ist(w: KvWiedergabe | null, b: number, a: string): number | null {
    return w?.bilder[b]?.[1][a] ?? null;
  }
  function falsch(ansicht: KvAnsicht, w: KvWiedergabe | null, b: number, a: string): boolean {
    const soll = ansicht.werte[a][b];
    const wert = ist(w, b, a);
    return wert != null && soll !== 'x' && String(wert) !== soll;
  }
  /** Blöcke im Text: Terme rechts vom = jeder Formelzeile (0 und leer zählen nicht) */
  function bloeckeIm(code: string): number {
    return code.split('\n').map((z) => /^\s*\w+\s*=(.*)$/.exec(z.split('#')[0])?.[1] ?? '')
      .flatMap((rechts) => rechts.split('+').map((term) => term.trim()))
      .filter((term) => term && term !== '0').length;
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: KvAnsicht)}
  <div class="gruppe">Zur Hand</div>
  <div class="spickzettel">
    <code>00 01 11 10</code><span>Reihenfolge an den Achsen: Nachbarn unterscheiden sich in genau einem Eingang</span>
    <code>Rand</code><span>links und rechts sind Nachbarn, oben und unten auch, bei vier Eingängen die vier Ecken</span>
    <code>Block</code><span>1, 2, 4, 8 oder 16 Felder; was im Block gleich bleibt, steht im Term</span>
    <code>x</code><span>egal: darf in einen Block, muss aber nicht</span>
    <code>!B</code><span>im Text: B ist 0, sonst überstrichen geschrieben</span>
  </div>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle vier Teilschritte stimmen</span>
    {@render sterne(2)}<span>höchstens {ansicht.sterne.bloecke} {ansicht.sterne.bloecke === 1 ? 'Block' : 'Blöcke'}</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.buchstaben} Buchstaben</span>
  </div>
{/snippet}

{#snippet editor(ansicht: KvAnsicht, zugriff: CodeZugriff, _: KvWiedergabe | null, nr: number, springe: (b: number) => void)}
  <KvRaster {ansicht} {zugriff} gewaehlt={Math.max(0, nr)} waehle={springe} />
{/snippet}

{#snippet szene(ansicht: KvAnsicht, wiedergabe: KvWiedergabe | null, nr: number, springe: (b: number) => void)}
  {@const b = Math.max(0, nr)}
  <div class="stand-rahmen">
    {#if istSiebenSegment(ansicht.ausgaenge)}
      <div class="paar"><SiebenSegment an={(s) => ist(wiedergabe, b, s) === 1} /><small>ist</small></div>
      <div class="paar"><SiebenSegment an={(s) => ansicht.werte[s][b] === '1'} /><small>soll</small></div>
    {/if}
    <div>
      <b class="gross-name">{ansicht.namen.length ? ansicht.namen[b] : bits(ansicht, b)}</b><br />
      <span class="dim num">{ansicht.eingaenge.join(' ')} = {bits(ansicht, b).split('').join(' ')}</span>
    </div>
  </div>
  <div class="tabelle-scroll">
    <table class="kv-tabelle">
      <thead>
        <tr>
          {#if ansicht.namen.length}<th></th>{/if}
          <th>{ansicht.eingaenge.join(' ')}</th>
          {#each ansicht.ausgaenge as a (a)}<th class="aus">{a}<small>{knapp(ansicht) ? 'ist' : 'soll / ist'}</small></th>{/each}
        </tr>
      </thead>
      <tbody>
        {#each Array.from({ length: 2 ** ansicht.eingaenge.length }, (_, i) => i) as i (i)}
          <tr class:jetzt={i === b} onclick={() => springe(i)}>
            {#if ansicht.namen.length}<td>{name(ansicht, i)}</td>{/if}
            <td>{bits(ansicht, i).split('').join(' ')}</td>
            {#each ansicht.ausgaenge as a (a)}
              {@const wert = ist(wiedergabe, i, a)}
              <td class="aus" class:nein={falsch(ansicht, wiedergabe, i, a)} class:ok={wert != null && !falsch(ansicht, wiedergabe, i, a)}>
                {#if knapp(ansicht)}{wert ?? ansicht.werte[a][i]}{:else}{ansicht.werte[a][i]} / {wert ?? '?'}{/if}
              </td>
            {/each}
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
  {#if wiedergabe}
    <div class="gruppe">So sähe die Schaltung aus<span class="dim klein">{wiedergabe.kennzahlen.bausteine} Bausteine, Tiefe {wiedergabe.kennzahlen.tiefe}</span></div>
    <pre class="plan">{wiedergabe.plan}</pre>
  {/if}
{/snippet}

{#snippet kennzahlen(ansicht: KvAnsicht, wiedergabe: KvWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte" style:grid-template-columns="repeat(2, minmax(0, 1fr))">
    <div><span class="num" class:gut={k.richtig === k.zeilen} class:schlecht={k.richtig < k.zeilen}>{k.richtig} / {k.zeilen}</span><small>Zeilen richtig</small></div>
    <div><span class="num" class:gut={k.bloecke <= ansicht.sterne.bloecke}>{k.bloecke}</span><small>Blöcke</small></div>
    <div><span class="num" class:gut={k.buchstaben <= ansicht.sterne.buchstaben}>{k.buchstaben}</span><small>Buchstaben</small></div>
    <div><span class="num">{k.bausteine}</span><small>Bausteine</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Tabelle"
  symbol="fa-table-cells"
  planTitel=""
  abspielen={false}
  live
  ladeAnsicht={(id) => spielApi.kvRaster(id)}
  probieren={(id, code) => spielApi.kvLauf(id, code)}
  mitteTitel={(code) => {
    const n = bloeckeIm(code);
    return `KV-Diagramm, ${n} ${n === 1 ? 'Block' : 'Blöcke'}`;
  }}
  mitUnfall={(_: KvKennzahlen) => false}
  {hilfe}
  {editor}
  {szene}
  {kennzahlen}
/>

<style>
  .stand-rahmen {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--sp-3);
    flex-shrink: 0;
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
  }
  .paar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .gross-name { font-size: 22px; }
  .tabelle-scroll {
    flex-shrink: 0;
    max-height: 360px;
    overflow: auto;
  }
  .kv-tabelle {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: 13px;
    text-align: center;
  }
  .kv-tabelle th {
    position: sticky;
    top: 0;
    background: var(--bg-card);
    font-weight: 600;
    color: var(--fg-dim);
    padding: 6px 4px;
    border-bottom: 1px solid var(--border);
  }
  .kv-tabelle th small {
    display: block;
    font-weight: 400;
    font-size: 10px;
    color: var(--fg-mute);
  }
  .kv-tabelle td {
    padding: 4px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
  }
  .kv-tabelle tr.jetzt td { background: color-mix(in srgb, var(--accent) 12%, transparent); }
  .aus { border-left: 1px solid var(--border); }
  .ok { color: var(--green); }
  .nein { color: var(--red); font-weight: 700; }
  .klein {
    margin-left: var(--sp-2);
    font-size: var(--fs-xs);
    text-transform: none;
    letter-spacing: 0;
  }
  .plan {
    flex-shrink: 0;
    margin: 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
    max-height: 200px;
    overflow: auto;
  }
</style>
