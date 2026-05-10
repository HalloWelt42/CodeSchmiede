<script lang="ts">
  /*
   * LueckentextView -- Aufgaben mit Code-Templates und Platzhaltern.
   *
   * Template kommt im `detail.extra.lueckentext`-Block:
   *   template: "code mit ___1___ und ___2___ Platzhaltern"
   *   luecken: [{nummer: 1, hinweis?: "..."}, ...]
   *
   * Nutzer fuellt pro Platzhalter ein Feld, wir bauen JSON-Map und
   * schicken sie an /api/submissions; Backend setzt die Werte ein
   * und laesst die Tests laufen.
   */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { submissionsApi } from '../api/SubmissionsApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';

  interface Luecke {
    nummer: number;
    hinweis?: string;
  }

  interface Props {
    detail: AufgabeDetail;
  }

  let { detail }: Props = $props();

  let lueckentext = $derived(
    (detail.extra?.['lueckentext'] as { template?: string; luecken?: Luecke[] }) ?? {},
  );
  let template = $derived(lueckentext.template ?? '');
  let luecken = $derived<Luecke[]>(lueckentext.luecken ?? []);

  let werte = $state<Record<string, string>>({});

  $effect(() => {
    // Beim ersten Render mit leeren Werten initialisieren
    const neu: Record<string, string> = {};
    for (const l of luecken) {
      neu[String(l.nummer)] = werte[String(l.nummer)] ?? '';
    }
    werte = neu;
  });

  let vorschau_code = $derived(
    template.replace(/___(\d+)___/g, (_, n) => werte[n] ?? `___${n}___`),
  );

  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    try {
      // Code = JSON-Map. Backend entpackt + ersetzt im Template.
      const json = JSON.stringify(werte);
      ergebnis = await submissionsApi.submit(detail.id, json);
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  function alleAusgefuellt(): boolean {
    return luecken.every((l) => (werte[String(l.nummer)] ?? '').trim() !== '');
  }

  function neuStarten(): void {
    werte = {};
    ergebnis = null;
  }
</script>

<div class="lt">
  <section class="links">
    <BeschreibungsBereich
      aufgabeId={detail.id}
      markdown={detail.beschreibung_md}
      hints={detail.hints}
      tests_sichtbar={detail.tests_sichtbar}
      anzahl_versteckt={detail.anzahl_versteckte_tests}
      quelle={detail.quelle}
      schwierigkeit_score={detail.schwierigkeit_score}
    />
  </section>

  <section class="rechts">
    <header class="kopf">
      <span class="label">Lückentext &middot; {luecken.length} Felder</span>
      <button
        class="pruefen"
        disabled={pruefen_laeuft || !alleAusgefuellt()}
        onclick={pruefen}
      >
        {#if pruefen_laeuft}
          <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> läuft ...
        {:else}
          <i class="fa-solid fa-play" aria-hidden="true"></i> Prüfen
        {/if}
      </button>
    </header>

    <div class="luecken">
      {#each luecken as l (l.nummer)}
        <label class="luecke-feld">
          <span class="luecke-nr">___{l.nummer}___</span>
          <input
            type="text"
            class="mono"
            bind:value={werte[String(l.nummer)]}
            placeholder="..."
          />
          {#if l.hinweis}
            <small class="hinweis">{l.hinweis}</small>
          {/if}
        </label>
      {/each}
    </div>

    <details class="vorschau">
      <summary>Code-Vorschau</summary>
      <pre class="code">{vorschau_code}</pre>
    </details>

    {#if fehler}
      <div class="fehler-box">
        <i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>
        {fehler}
      </div>
    {/if}

    {#if ergebnis}
      <div class="ergebnis" class:bestanden={ergebnis.bestanden}>
        <i class="fa-solid {ergebnis.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
        <strong>{ergebnis.bestanden ? 'Bestanden!' : 'Noch nicht bestanden'}</strong>
        {#if ergebnis.bestanden}
          <span>+{ergebnis.progress.punkte_erreicht} Punkte</span>
        {/if}
      </div>
      {#if ergebnis.pruefung.sichtbar.length > 0}
        <ul class="test-liste">
          {#each ergebnis.pruefung.sichtbar as t (t.index)}
            <li class:ok={t.bestanden}>
              <i class="fa-solid {t.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
              <code>{detail.funktion ?? 'f'}({t.eingabe.map((x) => JSON.stringify(x)).join(', ')})</code>
              {#if t.bestanden}
                <span>= {JSON.stringify(t.tatsaechlich)}</span>
              {:else if t.fehler}
                <span class="fehlertext">{t.fehler}</span>
              {:else}
                <span>→ {JSON.stringify(t.tatsaechlich)} ≠ {JSON.stringify(t.erwartet)}</span>
              {/if}
            </li>
          {/each}
        </ul>
      {/if}
      <div class="aktionen">
        <button class="reset" onclick={neuStarten}>Reset</button>
        {#if ergebnis.bestanden}
          <button class="weiter" onclick={() => route.setze('aufgaben')}>
            Weiter <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
          </button>
        {/if}
      </div>
    {/if}
  </section>
</div>

<style>
  .lt {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: var(--border);
    flex: 1 1 auto;
    min-height: 0;
    overflow: hidden;
  }
  .links, .rechts {
    background: var(--bg-card);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    min-height: 0;
  }
  .rechts {
    background: var(--bg);
    padding: 0 0 var(--sp-3);
  }
  .kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--sp-2) var(--sp-3);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card);
  }
  .label {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .pruefen {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 6px 14px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .pruefen:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .pruefen:disabled { opacity: 0.5; cursor: not-allowed; }

  .luecken {
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .luecke-feld {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .luecke-nr {
    color: var(--accent);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .luecke-feld input {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 6px 10px;
    font-family: var(--mono);
    font-size: var(--fs-sm);
    border-radius: var(--radius-sm);
  }
  .luecke-feld input:focus {
    outline: 1px solid var(--accent);
    border-color: var(--accent);
  }
  .hinweis {
    color: var(--fg-mute);
    font-family: var(--quick);
    font-size: var(--fs-xs);
  }

  .vorschau {
    margin: 0 var(--sp-3) var(--sp-3);
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-2);
    border-radius: var(--radius-sm);
  }
  .vorschau summary {
    cursor: pointer;
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .code {
    margin: var(--sp-2) 0 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg);
    white-space: pre-wrap;
    overflow-x: auto;
  }

  .fehler-box {
    margin: 0 var(--sp-3);
    padding: var(--sp-2);
    background: color-mix(in srgb, var(--red) 12%, transparent);
    border: 1px solid var(--red);
    color: var(--red);
    font-size: var(--fs-sm);
    display: flex;
    gap: 8px;
    align-items: center;
  }

  .ergebnis {
    margin: 0 var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: color-mix(in srgb, var(--red) 12%, transparent);
    border: 1px solid var(--red);
    color: var(--fg);
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: var(--fs-md);
  }
  .ergebnis.bestanden {
    background: color-mix(in srgb, var(--green) 12%, transparent);
    border-color: var(--green);
  }
  .ergebnis i { color: var(--red); }
  .ergebnis.bestanden i { color: var(--green); }

  .test-liste {
    list-style: none;
    padding: 0;
    margin: 0 var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .test-liste li {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 4px 8px;
    font-size: var(--fs-xs);
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .test-liste li i { color: var(--red); }
  .test-liste li.ok i { color: var(--green); }
  .test-liste code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    padding: 0;
    color: var(--fg-dim);
  }
  .fehlertext {
    color: var(--red);
    font-family: var(--mono);
  }

  .aktionen {
    display: flex;
    gap: var(--sp-2);
    margin: 0 var(--sp-3);
  }
  .reset {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    padding: 6px 12px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .reset:hover { color: var(--accent); border-color: var(--accent); }
  .weiter {
    background: var(--green);
    border: 1px solid var(--green);
    color: var(--bg);
    padding: 6px 14px;
    font-size: var(--fs-xs);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .weiter:hover { filter: brightness(1.1); }
</style>
