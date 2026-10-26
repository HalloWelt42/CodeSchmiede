<script lang="ts">
  /*
   * Editor der Turingmaschine: die Übergangstabelle als Tabelle (je Regel Zustand, liest, schreibt, geht, danach)
   * oder als Text, darunter das Zustandsdiagramm. Beide Ansichten schreiben denselben Text; Kommentare und Unfertiges
   * bleiben als Textzeilen stehen. Die Regel des gezeigten Schritts ist hervorgehoben.
   */
  import { regeln, zerlege, zusammen, type Regel, type Richtung, type Zeile } from '../../steuerung/turingTabelle';
  import type { CodeZugriff } from '../../types/Steuerung';
  import type { TuringAnsicht } from '../../types/Turing';
  import EditorBereich from '../EditorBereich.svelte';
  import Zustandsdiagramm from './Zustandsdiagramm.svelte';

  interface Props {
    ansicht: TuringAnsicht;
    zugriff: CodeZugriff;
    /** Zeile der Regel im gezeigten Schritt */
    aktiveZeile: number | null;
    /** Zustand im gezeigten Schritt */
    aktiverZustand: string | null;
  }
  let { ansicht, zugriff, aktiveZeile, aktiverZustand }: Props = $props();

  const SCHLUESSEL = 'codeschmiede.turing.ansicht';
  const RICHTUNGEN: Richtung[] = ['L', 'R', 'N'];

  function gemerkt(): 'tabelle' | 'text' {
    try {
      return localStorage.getItem(SCHLUESSEL) === 'text' ? 'text' : 'tabelle';
    } catch {
      return 'tabelle';
    }
  }
  let ansichtArt = $state<'tabelle' | 'text'>(gemerkt());
  function waehle(neu: 'tabelle' | 'text'): void {
    ansichtArt = neu;
    try {
      localStorage.setItem(SCHLUESSEL, neu);
    } catch {
      // nur für diese Sitzung
    }
  }

  let zeilen = $derived(zerlege(zugriff.code));
  let zeichen = $derived([...ansicht.zeichen, '_']);

  function aendere(i: number, feld: keyof Omit<Regel, 'art'>, wert: string): void {
    const neu: Zeile[] = zeilen.map((z, k) => (k === i && z.art === 'regel' ? { ...z, [feld]: wert } : z));
    zugriff.code = zusammen(neu);
  }

  function loesche(i: number): void {
    zugriff.code = zusammen(zeilen.filter((_, k) => k !== i));
  }

  function dazu(): void {
    const letzte = regeln(zeilen).at(-1)?.regel;
    const zustand = letzte?.zustand ?? ansicht.start;
    const neu: Regel = { art: 'regel', zustand, liest: '_', schreibt: '_', geht: 'N', danach: ansicht.ende[0], kommentar: '' };
    const ohneLeerEnde = zeilen.at(-1)?.art === 'text' && (zeilen.at(-1) as { text: string }).text.trim() === '' ? zeilen.slice(0, -1) : zeilen;
    zugriff.code = zusammen([...ohneLeerEnde, neu]) + '\n';
  }
</script>

<div class="tabelle-rahmen">
  <div class="modus" role="group" aria-label="Ansicht der Tabelle">
    <button class:aktiv={ansichtArt === 'tabelle'} onclick={() => waehle('tabelle')}>Tabelle</button>
    <button class:aktiv={ansichtArt === 'text'} onclick={() => waehle('text')}>Text</button>
  </div>
  {#if ansichtArt === 'tabelle'}
    <table class="tabelle-ue">
      <thead><tr><th>Zustand</th><th>liest</th><th>schreibt</th><th>geht</th><th>danach</th><th></th></tr></thead>
      <tbody>
        {#each zeilen as z, i (i)}
          {#if z.art === 'regel'}
            <tr class:aktiv={aktiveZeile === i + 1}>
              <td><input class="feld zustand" value={z.zustand} aria-label="Zustand" onchange={(e) => aendere(i, 'zustand', e.currentTarget.value.trim())} /></td>
              <td>
                <select class="feld" value={z.liest} aria-label="liest" onchange={(e) => aendere(i, 'liest', e.currentTarget.value)}>
                  {#each zeichen as c (c)}<option value={c}>{c}</option>{/each}
                </select>
              </td>
              <td>
                <select class="feld" value={z.schreibt} aria-label="schreibt" onchange={(e) => aendere(i, 'schreibt', e.currentTarget.value)}>
                  {#each zeichen as c (c)}<option value={c}>{c}</option>{/each}
                </select>
              </td>
              <td>
                <select class="feld" value={z.geht} aria-label="geht" onchange={(e) => aendere(i, 'geht', e.currentTarget.value)}>
                  {#each RICHTUNGEN as r (r)}<option value={r}>{r}</option>{/each}
                </select>
              </td>
              <td><input class="feld zustand" value={z.danach} aria-label="danach" onchange={(e) => aendere(i, 'danach', e.currentTarget.value.trim())} /></td>
              <td><button class="ikon" title="Zeile löschen" onclick={() => loesche(i)}><i class="fa-solid fa-xmark" aria-hidden="true"></i></button></td>
            </tr>
          {:else if z.text.trim()}
            <tr class="text-zeile" class:unfertig={!z.text.trim().startsWith('#')}>
              <td colspan="6">{z.text.trim().startsWith('#') ? z.text.trim().slice(1).trim() : `${z.text.trim()} (keine Regel, im Text ändern)`}</td>
            </tr>
          {/if}
        {/each}
      </tbody>
    </table>
    <button class="knopf-klein zeile-dazu" onclick={dazu}><i class="fa-solid fa-plus" aria-hidden="true"></i>Zeile</button>
  {:else}
    <div class="text-host">
      <EditorBereich sprache="plaintext" bind:code={zugriff.code} />
    </div>
  {/if}
  <div class="gruppe diagramm-titel">Zustandsdiagramm</div>
  <Zustandsdiagramm {zeilen} start={ansicht.start} ende={ansicht.ende} {aktiveZeile} {aktiverZustand} />
</div>

<style>
  .tabelle-rahmen {
    height: 100%;
    overflow-y: auto;
    padding: var(--sp-2) var(--sp-3) var(--sp-3);
  }
  .tabelle-ue {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: var(--fs-sm);
  }
  .tabelle-ue th {
    text-align: left;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: .05em;
    color: var(--fg-dim);
    font-weight: 500;
    padding: 6px 4px;
    border-bottom: 1px solid var(--border);
  }
  .tabelle-ue td {
    padding: 3px 4px;
    border-bottom: 1px solid var(--border);
  }
  .tabelle-ue tr.aktiv td { background: color-mix(in srgb, var(--accent) 14%, transparent); }
  .text-zeile td {
    color: var(--fg-dim);
    font-family: var(--sans);
    font-size: var(--fs-sm);
  }
  .text-zeile.unfertig td { color: var(--red); }
  .feld {
    width: 100%;
    min-width: 44px;
    height: 28px;
    padding: 0 6px;
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    color: var(--fg);
    font: inherit;
    text-transform: none;
    letter-spacing: 0;
  }
  .feld.zustand { color: var(--accent); min-width: 80px; }
  .zeile-dazu { margin-top: var(--sp-2); }
  .text-host {
    height: 260px;
    border: 1px solid var(--border);
  }
  .diagramm-titel { margin-top: var(--sp-3); }
</style>
