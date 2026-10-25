<script lang="ts">
  /*
   * Werkbank eines Beispiels: ausführen (erst nach der Vorhersage), am Rechner verändern und das Original
   * wiederherstellen. Der Lauf kommt aus der Sandbox; wie er sich zeigt, hängt an der Sprache: bei Python Ausgabe,
   * Ablauf und Speicherbild, bei SQL Ergebnis und Zwischentabellen auf dem Datensatz der Einführung.
   */
  import type { Snippet } from 'svelte';
  import { kursApi, type BeispielTeil, type Lauf } from '../../api/KursApi';
  import EditorBereich from '../EditorBereich.svelte';
  import CodeBlock from './CodeBlock.svelte';
  import PythonAblauf from './PythonAblauf.svelte';
  import SqlAblauf from './SqlAblauf.svelte';

  interface Props {
    einfuehrung: string;
    beispiel: BeispielTeil;
    sprache: string;
    /** Vorhersage steht noch aus */
    gesperrt: boolean;
    /** am Rechner: Code verändern erlaubt */
    bearbeitbar?: boolean;
    /** am Telefon zwischen Code und Ausführen, etwa die Vorhersage */
    vorAusfuehren?: Snippet;
  }
  let { einfuehrung, beispiel, sprache, gesperrt, bearbeitbar = true, vorAusfuehren }: Props = $props();

  let code = $state('');
  let lauf = $state<Lauf | null>(null);
  let laeuft = $state(false);
  let fehler = $state<string | null>(null);
  /** Zeile, die der Ablauf gerade zeigt */
  let zeile = $state<number | null>(null);

  // ohne Zeilenumbruch am Ende, sonst steht im Editor eine leere letzte Zeile
  let original = $derived(beispiel.code.replace(/\n$/, ''));

  // neues Beispiel: frischer Zustand
  $effect(() => {
    code = original;
    lauf = null;
    fehler = null;
    zeile = null;
  });

  let veraendert = $derived(code !== original);

  async function ausfuehren() {
    fehler = null;
    laeuft = true;
    try {
      lauf = await kursApi.ausfuehren(einfuehrung, beispiel.id, veraendert ? code : undefined);
    } catch (e) {
      fehler = e instanceof Error ? e.message : String(e);
    } finally {
      laeuft = false;
    }
  }
</script>

<div class="werkbank-inhalt">
  {#if !bearbeitbar}
    <CodeBlock {code} {sprache} jetzt={zeile} />
    {#if vorAusfuehren}{@render vorAusfuehren()}{/if}
  {/if}
  <div class="werkbank-zeile">
    <button class="knopf voll" onclick={ausfuehren} disabled={gesperrt || laeuft}><i class="fa-solid {laeuft ? 'fa-spinner fa-spin' : 'fa-play'}" aria-hidden="true"></i>Ausführen</button>
    {#if bearbeitbar && veraendert}
      <button class="knopf" onclick={() => (code = original)}><i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Original</button>
    {/if}
    <span class="zustand-hinweis rechts" class:veraendert>
      {#if !bearbeitbar}<i class="fa-solid fa-display" aria-hidden="true"></i>Verändern am Rechner{:else if veraendert}<i class="fa-solid fa-pen" aria-hidden="true"></i>verändert, nur zum Ausprobieren{:else}<i class="fa-solid fa-circle-check" aria-hidden="true"></i>Original{/if}
    </span>
  </div>

  {#if bearbeitbar}
    <div class="werkbank-editor"><EditorBereich {sprache} bind:code markierteZeile={zeile} /></div>
  {/if}

  {#if gesperrt}
    <div class="sperre"><i class="fa-solid fa-wand-magic-sparkles" aria-hidden="true"></i><span>Erst vorhersagen, dann ausführen.</span></div>
  {/if}

  {#if beispiel.eingabe.length}
    <div class="eingabe-zeile"><span class="dim">Eingabe für input():</span>{#each beispiel.eingabe as z, i (i)}<code>{z}</code>{/each}</div>
  {/if}
  {#if lauf?.art === 'sql'}
    <SqlAblauf {lauf} ablauf={beispiel.ablauf} bind:zeile />
  {:else if lauf}
    <PythonAblauf {lauf} ablauf={beispiel.ablauf} bind:zeile />
  {/if}
  {#if fehler}<div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div>{/if}
</div>

<style>
  .werkbank-inhalt { display: flex; flex-direction: column; gap: var(--sp-3); }
  .werkbank-inhalt > * { flex-shrink: 0; }
  .werkbank-editor { height: 220px; border: 1px solid var(--border); }
  .rechts { margin-left: auto; }
  .eingabe-zeile { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; font-size: var(--fs-sm); }
</style>
