<script lang="ts">
  /*
   * SqlAbfrageView -- 3-Spalten-Layout fuer SQL-Aufgaben.
   *
   *   Aufgabe + Schema-Hinweis | SQL-Editor | Ergebnis-Tabelle + Soll-Vergleich
   *
   * Bewertung erfolgt im Backend: SQL_Pruefer laedt das Dataset frisch
   * in eine In-Memory-SQLite, fuehrt die User-Query aus und vergleicht
   * mit den erwarteten Zeilen aus dem Frontmatter.
   *
   * Frontmatter-Felder (im `extra`-Block):
   *   dataset:               z.B. "bibliothek" oder "shop"
   *   erwartete_spalten:     ["name", "alter"]
   *   erwartetes_ergebnis:   [["Anna", 34], ...]
   *   sortierung_egal:       bool
   *   schema_hinweis:        kurze Tabellenstruktur als Markdown
   */
  import { onMount } from 'svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import type { AufgabeDetail, Musterloesung } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  let dataset = $derived((detail.extra?.['dataset'] as string) ?? 'bibliothek');
  let schema_hinweis = $derived((detail.extra?.['schema_hinweis'] as string) ?? '');
  let erwartete_spalten = $derived<string[] | null>(
    (detail.extra?.['erwartete_spalten'] as string[]) ?? null,
  );
  let erwartetes_ergebnis = $derived<unknown[][]>(
    (detail.extra?.['erwartetes_ergebnis'] as unknown[][]) ?? [],
  );

  let code = $state('');
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  let musterloesungen = $state<Musterloesung[] | null>(null);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  interface SchemaTabelle {
    name: string;
    spalten: string[];
    zeilen: unknown[][];
    gesamt_zeilen: number;
  }
  let schema_daten = $state<SchemaTabelle[] | null>(null);
  let schema_panel_offen = $state(false);
  let schema_position = $state({ x: 80, y: 80 });

  onMount(async () => {
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      code = letzte.code ?? detail.starter_code;
    } catch {
      code = detail.starter_code;
    }
  });

  async function oeffneSchema(): Promise<void> {
    schema_panel_offen = true;
    if (schema_daten) return;
    try {
      const r = await fetch(`/api/sql/datasets/${dataset}/vorschau?limit=5`);
      if (r.ok) {
        const j = await r.json();
        schema_daten = j.tabellen;
      }
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  function startDrag(event: PointerEvent): void {
    const start_x = event.clientX;
    const start_y = event.clientY;
    const start_pos = { ...schema_position };
    const target = event.currentTarget as HTMLElement;
    target.setPointerCapture(event.pointerId);
    function bewegen(e: PointerEvent): void {
      schema_position = {
        x: Math.max(0, start_pos.x + (e.clientX - start_x)),
        y: Math.max(0, start_pos.y + (e.clientY - start_y)),
      };
    }
    function beenden(): void {
      target.releasePointerCapture(event.pointerId);
      window.removeEventListener('pointermove', bewegen);
      window.removeEventListener('pointerup', beenden);
    }
    window.addEventListener('pointermove', bewegen);
    window.addEventListener('pointerup', beenden);
  }

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    try {
      ergebnis = await submissionsApi.submit(detail.id, code);
      if (ergebnis.bestanden && !musterloesungen) {
        musterloesungen = await aufgabenStore.ladeMusterloesungen(detail.id);
      }
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function geheZuNaechster(): Promise<void> {
    try {
      const v = await progressApi.weiter(detail.id);
      route.setze(v.naechste_id ? 'aufgabe' : 'aufgaben', v.naechste_id ?? undefined);
    } catch {
      route.setze('aufgaben');
    }
  }

  // Ergebnis-Daten aus Pruefung extrahieren (sichtbar[0])
  let tatsaechlich = $derived(
    ergebnis?.pruefung?.sichtbar?.[0]?.tatsaechlich as
      | { spalten: string[]; zeilen: unknown[][] }
      | undefined,
  );
</script>

<DreiSpaltenLayout>
{#snippet links()}
    <div class="tab-leiste" role="tablist">
      <button
        class="tab"
        class:aktiv={aktiver_tab === 'aufgabe'}
        role="tab"
        onclick={() => (aktiver_tab = 'aufgabe')}
      >
        <i class="fa-solid fa-file-lines" aria-hidden="true"></i>
        Aufgabe
      </button>
      {#if musterloesungen && musterloesungen.length > 0}
        <button
          class="tab"
          class:aktiv={aktiver_tab === 'loesungen'}
          role="tab"
          onclick={() => (aktiver_tab = 'loesungen')}
        >
          <i class="fa-solid fa-lightbulb" aria-hidden="true"></i>
          Musterlösungen ({musterloesungen.length})
        </button>
      {/if}
    </div>
    <div class="tab-inhalt">
      {#if aktiver_tab === 'aufgabe'}
        <BeschreibungsBereich
          aufgabeId={detail.id}
          markdown={detail.beschreibung_md}
          hints={detail.hints}
          tests_sichtbar={[]}
          anzahl_versteckt={0}
          quelle={detail.quelle}
          schwierigkeit_score={detail.schwierigkeit_score}
        />
        {#if schema_hinweis}
          <div class="schema">
            <div class="schema-titel">Schema · Datensatz <code>{dataset}</code></div>
            <pre>{schema_hinweis}</pre>
          </div>
        {/if}
      {:else if musterloesungen}
        <div class="muster-liste">
          {#each musterloesungen as ml (ml.variante)}
            <details class="muster-eintrag" open>
              <summary>{ml.variante}</summary>
              <pre><code>{ml.code}</code></pre>
            </details>
          {/each}
        </div>
      {/if}
    </div>
{/snippet}

{#snippet mitte()}
    <div class="editor-kopf">
      <span class="label">SQL-Editor · Datensatz {dataset}</span>
      <div class="kopf-aktionen">
        <button class="schema-btn" onclick={oeffneSchema} title="Tabellen-Vorschau einblenden">
          <i class="fa-solid fa-table" aria-hidden="true"></i>
          Tabellen
        </button>
        <button class="pruefen" disabled={pruefen_laeuft || !code.trim()} onclick={pruefen}>
        {#if pruefen_laeuft}
          <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i>
          läuft ...
        {:else}
          <i class="fa-solid fa-play" aria-hidden="true"></i>
          Prüfen
        {/if}
        </button>
      </div>
    </div>
    <div class="editor-host">
      <EditorBereich sprache="sql" bind:code />
    </div>
{/snippet}

{#snippet rechts()}
    <div class="ergebnis-kopf">
      <span class="label">Ergebnis</span>
      {#if ergebnis?.bestanden}
        <button class="weiter" onclick={geheZuNaechster}>
          Weiter <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </button>
      {/if}
    </div>
    <div class="ergebnis-inhalt">
      {#if fehler}
        <div class="fehler">{fehler}</div>
      {:else if ergebnis}
        <div class="status" class:gut={ergebnis.bestanden} class:schlecht={!ergebnis.bestanden}>
          {#if ergebnis.bestanden}
            <i class="fa-solid fa-check" aria-hidden="true"></i> Bestanden
          {:else}
            <i class="fa-solid fa-xmark" aria-hidden="true"></i> Noch nicht bestanden
          {/if}
        </div>
        {#if ergebnis.pruefung?.stderr}
          <pre class="sql-fehler">{ergebnis.pruefung.stderr}</pre>
        {/if}
        {#if tatsaechlich}
          <div class="tabellen-titel">Dein Ergebnis ({tatsaechlich.zeilen.length} Zeilen)</div>
          <table class="tab">
            {#if tatsaechlich.spalten?.length}
              <thead>
                <tr>{#each tatsaechlich.spalten as s}<th>{s}</th>{/each}</tr>
              </thead>
            {/if}
            <tbody>
              {#each tatsaechlich.zeilen.slice(0, 50) as row}
                <tr>{#each row as v}<td>{v ?? 'NULL'}</td>{/each}</tr>
              {/each}
            </tbody>
          </table>
          {#if tatsaechlich.zeilen.length > 50}
            <div class="hinweis">... {tatsaechlich.zeilen.length - 50} weitere Zeilen</div>
          {/if}
        {/if}
        {#if !ergebnis.bestanden}
          <details class="soll-block">
            <summary>Erwartetes Ergebnis ({erwartetes_ergebnis.length} Zeilen)</summary>
            <table class="tab">
              {#if erwartete_spalten?.length}
                <thead>
                  <tr>{#each erwartete_spalten as s}<th>{s}</th>{/each}</tr>
                </thead>
              {/if}
              <tbody>
                {#each erwartetes_ergebnis.slice(0, 50) as row}
                  <tr>{#each (row as unknown[]) as v}<td>{v ?? 'NULL'}</td>{/each}</tr>
                {/each}
              </tbody>
            </table>
          </details>
        {/if}
      {:else}
        <div class="hinweis">Schreibe SELECT-SQL und drück <strong>Prüfen</strong>.</div>
      {/if}
    </div>
{/snippet}
</DreiSpaltenLayout>

{#if schema_panel_offen}
  <div
    class="schema-panel"
    style:left="{schema_position.x}px"
    style:top="{schema_position.y}px"
  >
    <div class="panel-kopf" role="toolbar" aria-label="Schema-Panel verschieben" onpointerdown={startDrag}>
      <span class="panel-titel">
        <i class="fa-solid fa-table" aria-hidden="true"></i>
        Datensatz · {dataset}
      </span>
      <span class="panel-hinweis">
        <i class="fa-solid fa-up-down-left-right" aria-hidden="true"></i>
        Header zum Verschieben · Ecke unten rechts zum Größe ändern
      </span>
      <button
        class="panel-schliessen"
        onclick={() => (schema_panel_offen = false)}
        aria-label="Schließen"
      ><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
    </div>
    <div class="panel-inhalt">
      {#if !schema_daten}
        <div class="laedt">Lädt ...</div>
      {:else}
        {#each schema_daten as t (t.name)}
          <details class="tab-block" open>
            <summary>
              <strong>{t.name}</strong>
              <span class="meta">({t.gesamt_zeilen} Zeilen)</span>
            </summary>
            <table class="vor-tab">
              <thead>
                <tr>{#each t.spalten as s}<th>{s}</th>{/each}</tr>
              </thead>
              <tbody>
                {#each t.zeilen as zeile}
                  <tr>{#each zeile as v}<td>{v ?? 'NULL'}</td>{/each}</tr>
                {/each}
              </tbody>
            </table>
          </details>
        {/each}
      {/if}
    </div>
  </div>
{/if}

<style>
  .tab-leiste {
    display: flex;
    border-bottom: 1px solid var(--border);
    background: var(--bg-card);
    flex-shrink: 0;
  }
  .tab {
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: var(--sp-2) var(--sp-3);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
    font-family: inherit;
  }
  .tab:hover { color: var(--accent); }
  .tab.aktiv { color: var(--accent); border-bottom-color: var(--accent); }

  .tab-inhalt {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }

  .schema {
    padding: var(--sp-3);
    border-top: 1px dashed var(--border);
  }
  .schema-titel {
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent);
    margin-bottom: var(--sp-2);
  }
  .schema pre {
    font-family: var(--mono);
    font-size: var(--fs-xs);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    overflow-x: auto;
  }

  .editor-kopf, .ergebnis-kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--sp-2) var(--sp-3);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card);
    flex-shrink: 0;
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
    gap: var(--sp-2);
  }
  .pruefen:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .pruefen:disabled { opacity: 0.5; cursor: not-allowed; }

  .kopf-aktionen {
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .schema-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    padding: 6px 12px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-1);
  }
  .schema-btn:hover {
    color: var(--accent);
    border-color: var(--accent);
  }

  .schema-panel {
    position: fixed;
    width: 480px;
    height: 520px;
    min-width: 320px;
    min-height: 240px;
    max-width: 95vw;
    max-height: 90vh;
    background: var(--bg-card);
    border: 1px solid var(--accent);
    border-radius: var(--radius-sm);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6);
    z-index: 100;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    resize: both;
  }
  .panel-kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 12px;
    background: color-mix(in srgb, var(--accent) 18%, var(--bg-card));
    border-bottom: 1px solid var(--border);
    cursor: move;
    user-select: none;
  }
  .panel-titel {
    color: var(--accent);
    font-size: var(--fs-sm);
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
    letter-spacing: 0.04em;
  }
  .panel-hinweis {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-left: auto;
    margin-right: 8px;
  }
  .panel-schliessen {
    background: transparent;
    border: none;
    color: var(--fg-dim);
    cursor: pointer;
    width: 28px;
    height: 28px;
    border-radius: var(--radius-sm);
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .panel-schliessen:hover {
    color: var(--red);
    background: rgba(255, 255, 255, 0.05);
  }
  .panel-inhalt {
    padding: var(--sp-3);
    overflow-y: auto;
    flex: 1 1 auto;
  }
  .laedt { color: var(--fg-dim); font-style: italic; }
  .tab-block {
    margin-bottom: var(--sp-3);
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: var(--sp-2);
  }
  .tab-block summary {
    cursor: pointer;
    color: var(--fg);
    font-size: var(--fs-sm);
    padding: 4px 0;
  }
  .tab-block summary .meta {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    margin-left: var(--sp-1);
  }
  .vor-tab {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    margin-top: var(--sp-2);
  }
  .vor-tab th, .vor-tab td {
    border: 1px solid var(--border);
    padding: 3px 6px;
    text-align: left;
    white-space: nowrap;
  }
  .vor-tab th {
    background: var(--bg-card-2);
    color: var(--accent);
    font-weight: 600;
  }
  .vor-tab td { color: var(--fg); }
  .editor-host { flex: 1 1 auto; min-height: 0; overflow: hidden; }

  .weiter {
    background: color-mix(in srgb, var(--green) 14%, transparent);
    border: 1px solid var(--green);
    color: var(--green);
    padding: 6px 12px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: var(--fs-xs);
    font-weight: 600;
  }

  .ergebnis-inhalt {
    padding: var(--sp-3);
    overflow-y: auto;
    flex: 1 1 auto;
    min-height: 0;
  }
  .fehler { color: var(--red); }
  .sql-fehler {
    background: var(--bg);
    border: 1px solid var(--red);
    border-radius: var(--radius-sm);
    padding: var(--sp-2);
    color: var(--red);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    white-space: pre-wrap;
    margin: var(--sp-2) 0;
  }
  .status {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    margin-bottom: var(--sp-3);
    font-weight: 600;
  }
  .status.gut { color: var(--green); border-color: var(--green); }
  .status.schlecht { color: var(--red); border-color: var(--red); }

  .tabellen-titel {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: var(--sp-2);
  }
  .tab {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    margin-bottom: var(--sp-2);
  }
  .tab th, .tab td {
    border: 1px solid var(--border);
    padding: 4px 8px;
    text-align: left;
  }
  .tab th {
    background: var(--bg-card-2);
    color: var(--accent);
  }
  .tab td { color: var(--fg); }
  .hinweis { color: var(--fg-dim); font-size: var(--fs-xs); }

  .soll-block {
    margin-top: var(--sp-3);
    border-top: 1px dashed var(--border);
    padding-top: var(--sp-2);
  }
  .soll-block summary {
    cursor: pointer;
    color: var(--accent);
    text-transform: uppercase;
    font-size: var(--fs-xs);
    letter-spacing: 0.05em;
    padding: var(--sp-1) 0;
  }

  .muster-liste {
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .muster-eintrag {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-2) var(--sp-3);
  }
  .muster-eintrag summary {
    cursor: pointer;
    color: var(--accent);
    text-transform: uppercase;
    font-size: var(--fs-xs);
    letter-spacing: 0.05em;
  }
  .muster-eintrag pre {
    margin: var(--sp-2) 0 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    overflow-x: auto;
    border-radius: var(--radius-sm);
    max-height: 280px;
    overflow-y: auto;
  }
</style>
