<script lang="ts">
  /*
   * Werkbank eines Beispiels: ausführen (erst nach der Vorhersage), am Rechner verändern und das Original
   * wiederherstellen, den Lauf Zeile für Zeile abspielen und den Speicher nach jeder Zeile zeigen. Die Aufzeichnung
   * kommt aus dem echten Lauf in der Sandbox.
   */
  import { onDestroy, type Snippet } from 'svelte';
  import { kursApi, type Aufzeichnung, type BeispielTeil } from '../../api/KursApi';
  import EditorBereich from '../EditorBereich.svelte';
  import CodeBlock from './CodeBlock.svelte';
  import Speicherbild from './Speicherbild.svelte';

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
  let lauf = $state<Aufzeichnung | null>(null);
  let schritt = $state(0);
  let laeuft = $state(false);
  let fehler = $state<string | null>(null);
  let takt = $state<ReturnType<typeof setInterval> | null>(null);

  // ohne Zeilenumbruch am Ende, sonst steht im Editor eine leere letzte Zeile
  let original = $derived(beispiel.code.replace(/\n$/, ''));

  // neues Beispiel: frischer Zustand
  $effect(() => {
    code = original;
    lauf = null;
    schritt = 0;
    fehler = null;
  });

  let veraendert = $derived(code !== original);
  /** Speicherbild nur, wenn der Lauf überhaupt Namen anlegt */
  let mitSpeicher = $derived(schritteMitNamen());
  let schritte = $derived(lauf?.schritte ?? []);
  let aktuell = $derived(schritt > 0 ? schritte[schritt - 1] : null);
  function schritteMitNamen(): boolean {
    return (lauf?.schritte ?? []).some((s) => s.rahmen.some((r) => Object.keys(r.variablen).length > 0));
  }
  let ausgabeBisher = $derived(lauf ? schritte.slice(0, schritt).map((s) => s.ausgabe).join('') : '');

  async function ausfuehren() {
    anhalten();
    fehler = null;
    laeuft = true;
    try {
      lauf = await kursApi.ausfuehren(einfuehrung, beispiel.id, veraendert ? code : undefined);
      schritt = lauf.schritte.length;
    } catch (e) {
      fehler = e instanceof Error ? e.message : String(e);
    } finally {
      laeuft = false;
    }
  }

  function anhalten() {
    if (takt) clearInterval(takt);
    takt = null;
  }

  function abspielen() {
    if (takt) return anhalten();
    if (schritt >= schritte.length) schritt = 0;
    takt = setInterval(() => {
      if (schritt >= schritte.length) return anhalten();
      schritt += 1;
    }, 1000);
  }

  onDestroy(anhalten);
</script>

<div class="werkbank-inhalt">
  {#if !bearbeitbar}
    <CodeBlock {code} {sprache} jetzt={aktuell?.zeile ?? null} />
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
    <div class="werkbank-editor"><EditorBereich {sprache} bind:code markierteZeile={aktuell?.zeile ?? null} /></div>
  {/if}

  {#if gesperrt}
    <div class="sperre"><i class="fa-solid fa-wand-magic-sparkles" aria-hidden="true"></i><span>Erst vorhersagen, dann ausführen.</span></div>
  {/if}

  {#if beispiel.eingabe.length}
    <div class="eingabe-zeile"><span class="dim">Eingabe für input():</span>{#each beispiel.eingabe as z, i (i)}<code>{z}</code>{/each}</div>
  {/if}
  {#if lauf}
    <pre class="ausgabe">{#if ausgabeBisher}{ausgabeBisher}{:else}<span class="leer">Noch keine Ausgabe</span>{/if}</pre>
    {#if lauf.fehler && schritt === schritte.length}
      <div class="erklaerung schlecht"><i class="fa-solid fa-bug" aria-hidden="true"></i><span>{lauf.fehler}{lauf.fehlerzeile ? ` (Zeile ${lauf.fehlerzeile})` : ''}</span></div>
    {/if}
    {#if beispiel.ablauf && schritte.length}
      <div class="block-kopf"><span>Ablauf Schritt für Schritt</span><span class="dim">aus dem echten Lauf</span></div>
      <div class="abspieler">
        <button class="ikon" onclick={() => { anhalten(); schritt = Math.max(0, schritt - 1); }} aria-label="Schritt zurück"><i class="fa-solid fa-backward-step" aria-hidden="true"></i></button>
        <button class="ikon" onclick={abspielen} aria-label={takt ? 'Anhalten' : 'Abspielen'}><i class="fa-solid {takt ? 'fa-pause' : 'fa-play'}" aria-hidden="true"></i></button>
        <button class="ikon" onclick={() => { anhalten(); schritt = Math.min(schritte.length, schritt + 1); }} aria-label="Schritt vor"><i class="fa-solid fa-forward-step" aria-hidden="true"></i></button>
        <input class="regler" type="range" min="0" max={schritte.length} bind:value={schritt} oninput={anhalten} aria-label="Schritt" />
        <span class="num">{schritt} / {schritte.length}</span>
      </div>
      {#if lauf.gekuerzt}<span class="dim" style="font-size:var(--fs-xs)">Aufzeichnung nach {schritte.length} Schritten gekürzt; der Code lief trotzdem zu Ende.</span>{/if}
      {#if mitSpeicher}<Speicherbild schritt={aktuell} vorher={schritt > 1 ? schritte[schritt - 2] : null} />{/if}
    {/if}
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
