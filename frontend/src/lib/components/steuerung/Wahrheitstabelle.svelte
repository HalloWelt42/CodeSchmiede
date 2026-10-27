<script lang="ts">
  /*
   * Wahrheitstabelle der Schaltung: je Belegung der Eingänge Soll und Ist jedes Ausgangs, falsche Werte rot. Ein Klick
   * wählt die Zeile; der Plan zeigt dann, welche Leitungen 1 führen. Heißen die Ausgänge a bis g, steht darüber eine
   * 7-Segment-Anzeige mit der gewählten Zeile.
   */
  import { istSiebenSegment } from '../../steuerung/schaltplan';
  import type { SchaltungAnsicht, SchaltungWiedergabe } from '../../types/Schaltung';
  import SiebenSegment from './SiebenSegment.svelte';

  interface Props {
    ansicht: SchaltungAnsicht;
    wiedergabe: SchaltungWiedergabe | null;
    zeile: number;
    waehle: (zeile: number) => void;
  }
  let { ansicht, wiedergabe, zeile, waehle }: Props = $props();

  let zeilen = $derived(Array.from({ length: 2 ** ansicht.eingaenge.length }, (_, i) => i));
  let siebenSegment = $derived(istSiebenSegment(ansicht.ausgaenge));
  let gewaehlt = $derived(Math.max(0, zeile));

  function bit(nr: number, i: number): number {
    return (nr >> (ansicht.eingaenge.length - 1 - i)) & 1;
  }
  function ist(nr: number, a: string): number | null {
    return wiedergabe?.bilder[nr]?.[1][a] ?? null;
  }
  function falsch(nr: number, a: string): boolean {
    const soll = ansicht.soll[a][nr];
    const wert = ist(nr, a);
    return wert != null && soll !== 'x' && String(wert) !== soll;
  }
  function leuchtet(s: string): boolean {
    const wert = ist(gewaehlt, s);
    return wert != null ? wert === 1 : ansicht.soll[s][gewaehlt] === '1';
  }
</script>

{#if siebenSegment}
  <div class="anzeige-rahmen">
    <SiebenSegment an={leuchtet} />
    <span class="dim">Zeile {gewaehlt}: {ansicht.eingaenge.map((e, i) => `${e} = ${bit(gewaehlt, i)}`).join(', ')}</span>
  </div>
{/if}
<div class="tabelle-scroll">
  <table class="wahrheit">
    <thead>
      <tr>
        {#each ansicht.eingaenge as e (e)}<th>{e}</th>{/each}
        {#each ansicht.ausgaenge as a (a)}<th class="aus">{a}<small>soll / ist</small></th>{/each}
      </tr>
    </thead>
    <tbody>
      {#each zeilen as nr (nr)}
        <tr class:jetzt={nr === gewaehlt} onclick={() => waehle(nr)}>
          {#each ansicht.eingaenge as e, i (e)}<td>{bit(nr, i)}</td>{/each}
          {#each ansicht.ausgaenge as a (a)}
            {@const wert = ist(nr, a)}
            <td class="aus" class:nein={falsch(nr, a)} class:ok={wert != null && !falsch(nr, a)}>
              {ansicht.soll[a][nr] === 'x' ? '-' : ansicht.soll[a][nr]} / {wert ?? '?'}
            </td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
  .anzeige-rahmen {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    font-size: var(--fs-sm);
  }
  .tabelle-scroll {
    max-height: 420px;
    overflow: auto;
  }
  .wahrheit {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: 13px;
    text-align: center;
  }
  .wahrheit th {
    position: sticky;
    top: 0;
    background: var(--bg-card);
    font-weight: 600;
    color: var(--fg-dim);
    padding: 6px 4px;
    border-bottom: 1px solid var(--border);
  }
  .wahrheit th small {
    display: block;
    font-weight: 400;
    font-size: 10px;
    color: var(--fg-mute);
  }
  .wahrheit td {
    padding: 4px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
  }
  .wahrheit tr.jetzt td { background: color-mix(in srgb, var(--accent) 12%, transparent); }
  .aus { border-left: 1px solid var(--border); }
  .ok { color: var(--green); }
  .nein { color: var(--red); font-weight: 700; }
</style>
