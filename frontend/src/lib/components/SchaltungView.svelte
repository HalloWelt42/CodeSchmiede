<script lang="ts">
  /*
   * Digitale Schaltungen in der gemeinsamen Ansicht der Steuerungsspiele: der Schaltplan als Editor, rechts die
   * Wahrheitstabelle statt einer Welt. Ohne Abspielen; jede Änderung rechnet sofort neu (auf dem Server, ohne Sandbox),
   * und die gewählte Zeile zeigt im Plan, welche Leitungen 1 führen.
   */
  import { spielApi } from '../api/SpielApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SchaltungAnsicht, SchaltungKennzahlen, SchaltungWiedergabe } from '../types/Schaltung';
  import type { CodeZugriff } from '../types/Steuerung';
  import SchaltplanEditor from './steuerung/SchaltplanEditor.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';
  import Wahrheitstabelle from './steuerung/Wahrheitstabelle.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  const BAUSTEINE: Record<string, string> = {
    UND: '1, wenn beide Eingänge 1 sind',
    ODER: '1, wenn mindestens einer 1 ist',
    XOR: '1, wenn genau einer 1 ist',
    NAND: '0 nur, wenn beide 1 sind',
    NOR: '1 nur, wenn beide 0 sind',
    NICHT: 'dreht um: aus 1 wird 0',
  };

  function werte(w: SchaltungWiedergabe | null, nr: number): Record<string, number> | null {
    return w ? (w.bilder[Math.max(0, nr)]?.[1] ?? null) : null;
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: SchaltungAnsicht)}
  <div class="gruppe">Bausteine</div>
  <div class="spickzettel">
    {#each ansicht.bausteine as b (b)}<code>{b}</code><span>{BAUSTEINE[b] ?? ''}</span>{/each}
    <code>0, 1</code><span>feste Werte, links unten im Plan</span>
  </div>
  <div class="gruppe">Plan als Text</div>
  <div class="spickzettel">
    <code>u1 = UND(A, B)</code><span>ein Baustein mit Namen und Eingängen</span>
    <code>S = u1</code><span>ein Ausgang hängt an einem Signal</span>
  </div>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>die ganze Wahrheitstabelle stimmt</span>
    {@render sterne(2)}<span>höchstens {ansicht.sterne.bausteine} {ansicht.sterne.bausteine === 1 ? 'Baustein' : 'Bausteine'}</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.tiefe} auf dem längsten Weg</span>
  </div>
{/snippet}

{#snippet editor(ansicht: SchaltungAnsicht, zugriff: CodeZugriff, wiedergabe: SchaltungWiedergabe | null, nr: number, springe: (s: number) => void)}
  <SchaltplanEditor {ansicht} {zugriff} werte={werte(wiedergabe, nr)} zeile={wiedergabe ? Math.max(0, nr) : -1} waehle={springe} />
{/snippet}

{#snippet szene(ansicht: SchaltungAnsicht, wiedergabe: SchaltungWiedergabe | null, nr: number, springe: (s: number) => void)}
  <Wahrheitstabelle {ansicht} {wiedergabe} zeile={nr} waehle={springe} />
{/snippet}

{#snippet kennzahlen(ansicht: SchaltungAnsicht, wiedergabe: SchaltungWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte" style:grid-template-columns="repeat(3, minmax(0, 1fr))">
    <div><span class="num" class:gut={k.richtig === k.zeilen} class:schlecht={k.richtig < k.zeilen}>{k.richtig} / {k.zeilen}</span><small>Zeilen richtig</small></div>
    <div><span class="num" class:gut={k.bausteine <= ansicht.sterne.bausteine}>{k.bausteine}</span><small>Bausteine</small></div>
    <div><span class="num" class:gut={k.tiefe <= ansicht.sterne.tiefe}>{k.tiefe}</span><small>Tiefe</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Wahrheitstabelle"
  symbol="fa-microchip"
  planTitel=""
  abspielen={false}
  live
  ladeAnsicht={(id) => spielApi.schaltungPlan(id)}
  probieren={(id, code) => spielApi.schaltungLauf(id, code)}
  mitteTitel={(code) => `Schaltplan, ${code.split('\n').filter((z) => /=\s*[A-Z]+\s*\(/.test(z.split('#')[0])).length} Bausteine`}
  mitUnfall={(_: SchaltungKennzahlen) => false}
  {hilfe}
  {editor}
  {szene}
  {kennzahlen}
/>
