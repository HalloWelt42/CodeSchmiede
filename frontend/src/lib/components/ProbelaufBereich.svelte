<script lang="ts">
  /*
   * Probelauf-Panel: eigene Eingabe testen, Funktion mit dem Input
   * aufrufen, Rückgabe + stdout anzeigen. Kein Test-Vergleich.
   */
  import { submissionsApi } from '../api/SubmissionsApi';
  import type { ProbelaufAntwort } from '../types/Submission';

  interface Props {
    aufgabeId: string;
    code: string;
    funktion: string | null;
  }

  let { aufgabeId, code, funktion }: Props = $props();

  let eingabe_text = $state('');
  let antwort = $state<ProbelaufAntwort | null>(null);
  let laeuft = $state(false);
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

  async function laufeAb(): Promise<void> {
    const args = parseEingabe();
    if (args === null) {
      fehler = 'Eingabe konnte nicht geparst werden. Beispiele: 7   "anna"   [1,2,3]   3, 5';
      return;
    }
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
  <header class="kopf">
    <span class="label">
      <i class="fa-solid fa-flask" aria-hidden="true"></i>
      Probelauf
    </span>
    <span class="hint">
      eigener Input -- ohne Bewertung
    </span>
  </header>

  <div class="eingabe-zeile">
    <span class="aufruf">
      {funktion ?? 'fn'}(
    </span>
    <input
      type="text"
      bind:value={eingabe_text}
      placeholder='z.B. 7  oder  "anna"  oder  [1,2,3]'
      onkeydown={(e) => { if (e.key === 'Enter') laufeAb(); }}
    />
    <span class="aufruf">)</span>
    <button
      class="laufe-button"
      onclick={laufeAb}
      disabled={laeuft || !code.trim()}
      title="Funktion mit diesem Input ausführen"
    >
      {#if laeuft}
        <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i>
      {:else}
        <i class="fa-solid fa-play" aria-hidden="true"></i>
      {/if}
      Lauf
    </button>
  </div>

  {#if fehler}
    <p class="meldung fehler">{fehler}</p>
  {/if}

  {#if antwort}
    {#if antwort.fehler}
      <div class="ergebnis fehler">
        <span class="ergebnis-label">Fehler</span>
        <code>{antwort.fehler}</code>
      </div>
    {:else}
      <div class="ergebnis ok">
        <span class="ergebnis-label">Rückgabe</span>
        <code class="rückgabe">{formatiere(antwort.rückgabe)}</code>
      </div>
    {/if}
    {#if antwort.stdout}
      <div class="stdout-block">
        <span class="ergebnis-label">stdout</span>
        <pre>{antwort.stdout}</pre>
      </div>
    {/if}
    <div class="meta">
      <span class="laufzeit num">{antwort.laufzeit_ms.toFixed(0)} ms</span>
      {#if antwort.timeout}
        <span class="badge timeout">Timeout</span>
      {/if}
    </div>
  {/if}
</div>

<style>
  .probelauf {
    border-top: 1px solid var(--border);
    background: var(--bg-card);
    padding: var(--sp-3);
    flex-shrink: 0;
    max-height: 240px;
    overflow-y: auto;
  }
  .kopf {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: var(--sp-2);
  }
  .label {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .label i {
    color: var(--accent);
  }
  .hint {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    font-family: var(--quick);
  }

  .eingabe-zeile {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    margin-bottom: var(--sp-2);
  }
  .aufruf {
    font-family: var(--mono);
    font-size: var(--fs-sm);
    color: var(--fg-dim);
  }
  input {
    flex: 1;
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--fg);
    font-family: var(--mono);
    font-size: var(--fs-sm);
    padding: 6px var(--sp-2);
    border-radius: var(--radius-sm);
  }
  input:focus {
    outline: none;
    border-color: var(--accent);
  }
  .laufe-button {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 6px 12px;
    font-size: var(--fs-xs);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    flex-shrink: 0;
  }
  .laufe-button:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .laufe-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .meldung {
    margin: var(--sp-2) 0 0;
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .meldung.fehler {
    color: var(--orange);
  }

  .ergebnis {
    margin-top: var(--sp-2);
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-sm);
  }
  .ergebnis.fehler {
    border-color: var(--red);
  }
  .ergebnis.fehler code {
    color: var(--red);
  }
  .ergebnis.ok {
    border-color: var(--green);
  }
  .ergebnis-label {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    flex-shrink: 0;
  }
  .ergebnis code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    padding: 0;
    color: var(--fg);
  }
  .rückgabe {
    color: var(--accent) !important;
  }

  .stdout-block {
    margin-top: var(--sp-2);
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
  }
  .stdout-block pre {
    margin: 4px 0 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg);
    white-space: pre-wrap;
    max-height: 80px;
    overflow-y: auto;
  }

  .meta {
    margin-top: var(--sp-2);
    display: flex;
    gap: var(--sp-2);
    align-items: center;
    color: var(--fg-mute);
    font-size: var(--fs-xs);
  }
  .badge.timeout {
    color: var(--orange);
    border: 1px solid var(--orange);
    padding: 2px 6px;
  }
</style>
