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
  import { route } from '../stores/RouteStore.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { sqlApi, type VorschauTabelle } from '../api/SqlApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

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
  // zählt Abgaben dieser Ansicht; der Verlauf lädt danach neu
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  // Startwert genügt: die Ansicht entsteht je Aufgabe neu ({#key} in der Schale).
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  // Code, den der Server schon kennt (Starter, letzte Einreichung oder
  // zuletzt geprüft). Weicht der Editor davon ab oder läuft eine Prüfung,
  // wartet eine neue Fassung mit dem Neuladen.
  let gesicherter_code = $state('');
  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  let schema_daten = $state<VorschauTabelle[] | null>(null);
  let schema_panel_offen = $state(false);
  let schema_position = $state({ x: 80, y: 80 });

  onMount(async () => {
    // Default: Starter-Code. Eine eigene laufende Submission laden wir nur,
    // wenn der Nutzer noch dran ist (also noch nicht bestanden hat). Sonst
    // sehen wir die alte Loesung im Editor und der Lerneffekt geht verloren.
    code = detail.starter_code;
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code && !letzte.bestanden) code = letzte.code;
    } catch {
      // keine vorherige Submission -- bleibt Starter.
    }
    gesicherter_code = code;
  });

  async function oeffneSchema(): Promise<void> {
    schema_panel_offen = true;
    if (schema_daten) return;
    try {
      schema_daten = await sqlApi.vorschau(dataset);
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  function startDrag(event: PointerEvent): void {
    // Klicks auf den Schliessen-Button NICHT als Drag interpretieren --
    // sonst nimmt setPointerCapture das Click-Event weg und das Panel
    // laesst sich nicht mehr zu machen.
    if ((event.target as HTMLElement).closest('.panel-schliessen')) return;
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
    const eingereicht = code;
    try {
      ergebnis = await submissionsApi.submit(detail.id, code);
      gesicherter_code = eingereicht;
      abgaben += 1;
      if (ergebnis.bestanden) musterloesungen_frei = true;
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

<DreiSpaltenLayout
  mitteTitel="SQL-Editor, Datensatz {dataset}"
  rechtsTitel="Ergebnis"
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: code.trim() !== '' }}
>
  {#snippet links()}
    {#if detail.musterloesungen_anzahl > 0}
      <SpaltenReiter
        reiter={[
          { id: 'aufgabe', titel: 'Aufgabe', icon: 'fa-file-lines' },
          { id: 'loesungen', titel: `Musterlösungen (${detail.musterloesungen_anzahl})`, icon: 'fa-lightbulb' },
        ]}
        bind:aktiv={aktiver_tab}
      />
    {/if}
    <div class="rollfeld ohne-rand">
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
            <div class="gruppe">Schema, Datensatz <code>{dataset}</code></div>
            <pre>{schema_hinweis}</pre>
          </div>
        {/if}
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <button class="knopf-klein" onclick={oeffneSchema}>
      <i class="fa-solid fa-table" aria-hidden="true"></i>Tabellen
    </button>
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      <EditorBereich sprache="sql" bind:code />
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld">
      {#if fehler}
        <p class="hinweis-box fehler">{fehler}</p>
      {:else if pruefen_laeuft}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Abfrage läuft in der Sandbox ...</p>
      {:else if ergebnis}
        {#if ergebnis.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
        <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
          <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
          {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
        </div>
        {#if ergebnis.pruefung?.stderr}
          <pre class="sql-fehler">{ergebnis.pruefung.stderr}</pre>
        {/if}
        {#if tatsaechlich}
          <div class="gruppe">Dein Ergebnis ({tatsaechlich.zeilen.length} Zeilen)</div>
          <table class="daten-tab">
            {#if tatsaechlich.spalten?.length}
              <thead><tr>{#each tatsaechlich.spalten as s}<th>{s}</th>{/each}</tr></thead>
            {/if}
            <tbody>
              {#each tatsaechlich.zeilen.slice(0, 50) as row}
                <tr>{#each row as v}<td>{v ?? 'NULL'}</td>{/each}</tr>
              {/each}
            </tbody>
          </table>
          {#if tatsaechlich.zeilen.length > 50}
            <p class="dim klein">{tatsaechlich.zeilen.length - 50} weitere Zeilen</p>
          {/if}
        {/if}
        {#if !ergebnis.bestanden}
          <details class="soll-block">
            <summary class="gruppe">Erwartetes Ergebnis ({erwartetes_ergebnis.length} Zeilen)</summary>
            <table class="daten-tab">
              {#if erwartete_spalten?.length}
                <thead><tr>{#each erwartete_spalten as s}<th>{s}</th>{/each}</tr></thead>
              {/if}
              <tbody>
                {#each erwartetes_ergebnis.slice(0, 50) as row}
                  <tr>{#each (row as unknown[]) as v}<td>{v ?? 'NULL'}</td>{/each}</tr>
                {/each}
              </tbody>
            </table>
          </details>
        {:else}
          <button class="knopf primaer" onclick={geheZuNaechster}>
            <i class="fa-solid fa-forward" aria-hidden="true"></i>Nächste Aufgabe
          </button>
        {/if}
      {:else}
        <p class="dim">Schreibe eine SELECT-Abfrage, dann <strong>Prüfen</strong>.</p>
      {/if}
      <VerlaufBereich aufgabeId={detail.id} stand={abgaben} onUebernehmen={(c) => (code = c)} />
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

  .schema {
    padding: 0 var(--sp-3) var(--sp-3);
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

  .daten-tab {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    margin-bottom: var(--sp-2);
  }
  .daten-tab th, .daten-tab td {
    border: 1px solid var(--border);
    padding: 4px 8px;
    text-align: left;
  }
  .daten-tab th {
    background: var(--bg-card-2);
    color: var(--accent);
  }
  .daten-tab td { color: var(--fg); }

  .soll-block {
    margin-top: var(--sp-3);
  }
  .soll-block summary { cursor: pointer; }
  .klein { font-size: var(--fs-xs); }

</style>
