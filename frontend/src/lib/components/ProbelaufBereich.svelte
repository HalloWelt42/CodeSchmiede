<script lang="ts">
  /*
   * Probelauf-Panel: eigene Eingabe testen, Funktion mit dem Input
   * aufrufen, Rückgabe + stdout anzeigen. Kein Test-Vergleich.
   * Mit `onDebuggen` gibt es daneben den Debugger mit derselben Eingabe.
   */
  import { submissionsApi } from '../api/SubmissionsApi';
  import { fassung } from '../stores/FassungStore.svelte';
  import type { ProbelaufAntwort } from '../types/Submission';

  interface Props {
    aufgabeId: string;
    code: string;
    funktion: string | null;
    /** Programm-Aufgabe: Eingabezeilen für input() oder prompt() statt Funktionsargumente */
    programm?: boolean;
    sprache?: string;
    /** Debugger anbieten: bekommt die Eingabe und den Aufruf als Text (bei Programmen null) */
    onDebuggen?: (eingabe: unknown[], aufruf: string | null) => void;
    debugLaeuft?: boolean;
  }

  let { aufgabeId, code, funktion, programm = false, sprache = 'python', onDebuggen, debugLaeuft = false }: Props = $props();
  let eingabeBefehl = $derived(sprache === 'javascript' ? 'prompt()' : 'input()');

  let eingabe_text = $state('');
  let antwort = $state<ProbelaufAntwort | null>(null);
  let laeuft = $state(false);
  // Während des Probelaufs wartet eine neue Fassung mit dem Neuladen.
  $effect(() => {
    if (laeuft) return fassung.halten();
  });
  let fehler = $state<string | null>(null);

  function parseEingabe(): unknown[] | null {
    const text = eingabe_text.trim();
    if (text === '') return [];
    try {
      const wert = JSON.parse(`[${text}]`);
      return Array.isArray(wert) ? wert : [wert];
    } catch {
      return null;
    }
  }

  /** Argumente oder Eingabezeilen; null mit Meldung, wenn sie sich nicht lesen lassen */
  function eingabe(): unknown[] | null {
    const args = programm ? (eingabe_text ? eingabe_text.split('\n') : []) : parseEingabe();
    if (args === null) fehler = 'Eingabe konnte nicht geparst werden. Beispiele: 7   "anna"   [1,2,3]   3, 5';
    return args;
  }

  function debuggen(): void {
    const args = eingabe();
    if (args === null || !onDebuggen) return;
    fehler = null;
    onDebuggen(args, programm ? null : `${funktion ?? 'f'}(${eingabe_text.trim()})`);
  }

  async function laufeAb(): Promise<void> {
    const args = eingabe();
    if (args === null) return;
    laeuft = true;
    fehler = null;
    try {
      antwort = await submissionsApi.probelauf(aufgabeId, code, args);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laeuft = false;
    }
  }

  function formatiere(wert: unknown): string {
    return JSON.stringify(wert);
  }
</script>

<div class="probelauf">
  <div class="zeile">
    <div class="eingabe">
    {#if programm}
    <textarea
      rows="3"
      bind:value={eingabe_text}
      placeholder="Eingaben für {eingabeBefehl}, eine je Zeile (leer lassen, wenn das Programm nichts fragt)"
      aria-label="Eingaben für den Probelauf"
    ></textarea>
    {:else}
    <span class="aufruf">{funktion ?? 'f'}(</span>
    <input
      type="text"
      bind:value={eingabe_text}
      placeholder='Probelauf ohne Wertung, etwa 7 oder "anna" oder [1, 2, 3]'
      aria-label="Eingabe für den Probelauf"
      onkeydown={(e) => { if (e.key === 'Enter') laufeAb(); }}
    />
    <span class="aufruf">)</span>
    {/if}
    </div>
    <div class="knoepfe">
    <button class="knopf" onclick={laufeAb} disabled={laeuft || !code.trim()}>
      <i class="fa-solid {laeuft ? 'fa-spinner fa-spin' : 'fa-play'}" aria-hidden="true"></i>Lauf
    </button>
    {#if onDebuggen}
      <button class="knopf debug" onclick={debuggen} disabled={debugLaeuft || !code.trim()} title="Lauf Schritt für Schritt mit Speicher, hält an den Haltepunkten">
        <i class="fa-solid {debugLaeuft ? 'fa-spinner fa-spin' : 'fa-bug'}" aria-hidden="true"></i>Debuggen
      </button>
    {/if}
    </div>
  </div>

  {#if fehler}
    <p class="meldung">{fehler}</p>
  {/if}
  {#if antwort}
    <div class="antwort">
      {#if antwort.fehler}
        <span class="marke">Fehler</span><code class="fehlertext">{antwort.fehler}</code>
      {:else if !programm}
        <span class="marke">Rückgabe</span><code class="rueckgabe">{formatiere(antwort.rueckgabe)}</code>
      {:else}
        <span class="marke">Ausgabe</span>
      {/if}
      <span class="laufzeit num">{antwort.laufzeit_ms.toFixed(0)} ms{antwort.timeout ? ', Zeit überschritten' : ''}</span>
    </div>
    {#if antwort.stdout}
      <pre class="ausgabe">{antwort.stdout}</pre>
    {/if}
  {/if}
</div>

<style>
  .probelauf {
    flex: none;
    border-top: 1px solid var(--border);
    background: var(--bg-card);
    padding: var(--sp-2) var(--sp-3);
    max-height: 45vh;   /* Eingabe dreizeilig plus Ausgabe; vorher 220 px, dann rollte die Eingabe unter den Hinweis */
    overflow-y: auto;
    font-family: var(--mono);
    font-size: 12px;
  }
  /* ist die Spalte schmal, rutschen die Knöpfe unter die Eingabe */
  .zeile {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--sp-2);
  }
  .eingabe {
    flex: 1 1 200px;
    min-width: 0;
    display: flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .knoepfe {
    flex: none;
    display: flex;
    gap: var(--sp-2);
    margin-left: auto;
  }
  .aufruf { color: var(--fg-dim); white-space: nowrap; }
  input, textarea {
    flex: 1;
    min-width: 0;
    height: 28px;
    padding: 0 var(--sp-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--bg);
    font-family: var(--mono);
    font-size: 12px;
  }
  textarea { height: auto; min-height: calc(3 * 1.5em + 2 * var(--sp-2) + 2px); padding: var(--sp-2) var(--sp-3); font-size: var(--fs-sm); line-height: 1.5; resize: vertical; color: var(--fg); align-self: stretch; }
  input:focus, textarea:focus { outline: none; border-color: var(--accent); }
  .knopf { height: 28px; }
  .knopf.debug { color: var(--gold); border-color: color-mix(in srgb, var(--gold) 60%, var(--border)); }
  .knopf.debug:hover:not(:disabled) { color: var(--gold); border-color: var(--gold); }
  .meldung {
    margin: var(--sp-2) 0 0;
    color: var(--orange);
    font-family: var(--sans);
    font-size: var(--fs-xs);
  }
  .antwort {
    margin-top: var(--sp-2);
    display: flex;
    align-items: baseline;
    gap: var(--sp-2);
    min-width: 0;
  }
  .marke {
    color: var(--fg-mute);
    font-family: var(--sans);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    flex: none;
  }
  .antwort code {
    background: transparent;
    border: 0;
    padding: 0;
    overflow-wrap: anywhere;
  }
  .rueckgabe { color: var(--accent); }
  .fehlertext { color: var(--red); }
  .laufzeit {
    margin-left: auto;
    color: var(--fg-mute);
    font-weight: 500;
    white-space: nowrap;
  }
  .ausgabe {
    margin: var(--sp-1) 0 0;
    padding: var(--sp-1) var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    white-space: pre-wrap;
    max-height: 80px;
    overflow-y: auto;
  }
</style>
