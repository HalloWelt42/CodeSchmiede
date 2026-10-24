<script lang="ts">
  /*
   * Drei-Spalten-Layout für die Aufgaben-Detail-Ansicht:
   *   Beschreibung | Editor + Probelauf | Output
   *
   * Header bietet Reset, Body laedt Detail asynchron, OutputBereich
   * zeigt Ergebnis nach Submit + Weiter-Button.
   */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { farbeZuCss } from '../types/Konfig';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import ConfirmModal from './ConfirmModal.svelte';
  import CssKlonView from './CssKlonView.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import LueckentextView from './LueckentextView.svelte';
  import OutputBereich from './OutputBereich.svelte';
  import OutputQuizView from './OutputQuizView.svelte';
  import ProbelaufBereich from './ProbelaufBereich.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import SqlAbfrageView from './SqlAbfrageView.svelte';

  let { aufgabeId }: { aufgabeId: string } = $props();

  let detail = $state<AufgabeDetail | null>(null);
  let ladenDetail = $state(false);
  let fehler = $state<string | null>(null);

  let code = $state('');
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let pruefen_laeuft = $state(false);
  let pruef_fehler = $state<string | null>(null);

  // Code, den der Server schon kennt (Starter, letzte Einreichung oder
  // zuletzt geprüft). Weicht der Editor davon ab oder läuft eine Prüfung,
  // wartet eine neue Fassung mit dem Neuladen.
  let gesicherter_code = $state('');
  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  let musterloesungen_frei = $state(false);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  // zählt Abgaben dieser Ansicht; der Verlauf lädt danach neu
  let abgaben = $state(0);

  let reset_modal_offen = $state(false);

  onMount(async () => {
    await lade();
  });

  async function lade(): Promise<void> {
    ladenDetail = true;
    fehler = null;
    try {
      const d = await aufgabenStore.ladeDetail(aufgabeId);
      if (!d) {
        fehler = 'Aufgabe nicht gefunden';
        return;
      }
      detail = d;
      musterloesungen_frei = d.musterloesungen_frei;
      // Default: Starter-Code. Eine vorherige Submission laden wir nur,
      // wenn der Nutzer noch nicht bestanden hat -- sonst stuende die
      // alte Loesung im Editor und Wiederholungen waeren trivialisiert.
      code = d.starter_code;
      try {
        const letzte = await aufgabenApi.letzteSubmission(d.id);
        if (letzte.code && !letzte.bestanden) code = letzte.code;
      } catch {
        // keine vorherige Submission -- bleibt Starter.
      }
      gesicherter_code = code;
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      ladenDetail = false;
    }
  }

  async function pruefe(): Promise<void> {
    if (!detail) return;
    pruefen_laeuft = true;
    pruef_fehler = null;
    const eingereicht = code;
    try {
      ergebnis = await submissionsApi.submit(detail.id, code);
      gesicherter_code = eingereicht;
      if (ergebnis.bestanden) musterloesungen_frei = true;
      await progressStore.ladeAlles();
      abgaben += 1;
    } catch (e) {
      pruef_fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function geheZuNaechster(): Promise<void> {
    if (!detail) return;
    try {
      const v = await progressApi.weiter(detail.id);
      if (v.naechste_id) {
        route.setze('aufgabe', v.naechste_id);
      } else {
        route.setze('aufgaben');
      }
    } catch {
      route.setze('aufgaben');
    }
  }

  function zurueck(): void {
    route.setze('aufgaben');
  }

  function resetAnfragen(): void {
    reset_modal_offen = true;
  }

  async function resetBestaetigt(): Promise<void> {
    if (!detail) {
      reset_modal_offen = false;
      return;
    }
    try {
      await progressApi.reset(detail.id);
      ergebnis = null;
      musterloesungen_frei = false;
      aktiver_tab = 'aufgabe';
      // Beim Reset zurück auf Starter-Boilerplate, nicht auf letzte
      // Submission -- der Nutzer will von vorn anfangen.
      code = detail.starter_code;
      gesicherter_code = code;
      await progressStore.ladeAlles();
    } catch (e) {
      pruef_fehler = (e as Error).message;
    } finally {
      reset_modal_offen = false;
    }
  }

  let aktProgress = $derived(progressStore.proAufgabe[aufgabeId]);

  let schwFarbe = $derived(
    detail ? farbeZuCss(konfig.schwierigkeitFarbe(detail.schwierigkeit)) : 'var(--accent)',
  );

</script>

<div class="detail">
  {#if ladenDetail}
    <div class="info">Lade Aufgabe ...</div>
  {:else if fehler}
    <div class="info fehler">Fehler: {fehler}</div>
  {:else if detail}
    <header class="kopf">
      <button class="kopf-btn" onclick={zurueck} title="Zurück zur Liste" aria-label="Zurück">
        <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
      </button>
      <div class="kopf-info">
        <span class="id">{detail.id}</span>
        <h1>{detail.titel}</h1>
      </div>
      <div class="kopf-meta">
        <span
          class="badge"
          style:color={schwFarbe}
          style:border-color={schwFarbe}
        >{konfig.schwierigkeitTitel(detail.schwierigkeit)}</span>
        <span class="badge sprache">{detail.sprache}</span>
        <span class="zeit">
          <i class="fa-regular fa-clock" aria-hidden="true"></i>
          {detail.schaetz_minuten} min
        </span>
        <span class="score num" title="Erreicht / Maximum">
          <i class="fa-solid fa-coins" aria-hidden="true"></i>
          {aktProgress?.punkte_erreicht ?? 0} / {detail.schwierigkeit_score}
        </span>
        {#if aktProgress && (aktProgress.versuche > 0 || aktProgress.hints_genutzt > 0)}
          <button class="kopf-btn warn" onclick={resetAnfragen} title="Aufgabe zurücksetzen" aria-label="Reset">
            <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>
          </button>
        {/if}
      </div>
    </header>

    {#if detail.gesperrt}
      <div class="sperre-banner">
        <i class="fa-solid fa-lock" aria-hidden="true"></i>
        <span>
          Diese Aufgabe ist gesperrt -- folgende Voraussetzungen sind noch nicht gelöst:
          {#each detail.voraussetzungen_offen as v, i}
            <button class="vor-link" onclick={() => route.setze('aufgabe', v)}>
              {aufgabenStore.findeKurz(v)?.titel ?? v}
            </button>{#if i < detail.voraussetzungen_offen.length - 1}, {/if}
          {/each}
        </span>
      </div>
    {/if}

    {#if detail.task_type === 'output_quiz'}
      <OutputQuizView {detail} />
    {:else if detail.task_type === 'lueckentext'}
      <LueckentextView {detail} />
    {:else if detail.task_type === 'css_klon'}
      <CssKlonView {detail} />
    {:else if detail.task_type === 'sql_abfrage'}
      <SqlAbfrageView {detail} />
    {:else}
      {#if detail.task_type === 'bug_finden'}
        <div class="bug-banner">
          <i class="fa-solid fa-bug" aria-hidden="true"></i>
          <span><strong>Bug finden!</strong> Im Editor steht Code mit einem Fehler. Finde ihn, fixe ihn, drück Prüfen.</span>
        </div>
      {/if}
    {@const aktuell = detail}
    <DreiSpaltenLayout>
      {#snippet links()}
        {#if aktuell.musterloesungen_anzahl > 0}
          <div class="tab-leiste" role="tablist">
            <button
              class="tab"
              class:aktiv={aktiver_tab === 'aufgabe'}
              role="tab"
              aria-selected={aktiver_tab === 'aufgabe'}
              onclick={() => (aktiver_tab = 'aufgabe')}
            >
              <i class="fa-solid fa-file-lines" aria-hidden="true"></i>
              Aufgabe
            </button>
            <button
              class="tab"
              class:aktiv={aktiver_tab === 'loesungen'}
              role="tab"
              aria-selected={aktiver_tab === 'loesungen'}
              onclick={() => (aktiver_tab = 'loesungen')}
            >
              <i class="fa-solid fa-lightbulb" aria-hidden="true"></i>
              Musterlösungen ({aktuell.musterloesungen_anzahl})
            </button>
          </div>
        {/if}
        <div class="tab-inhalt">
          {#if aktiver_tab === 'aufgabe'}
            <BeschreibungsBereich
              aufgabeId={aktuell.id}
              markdown={aktuell.beschreibung_md}
              hints={aktuell.hints}
              tests_sichtbar={aktuell.tests_sichtbar}
              anzahl_versteckt={aktuell.anzahl_versteckte_tests}
              quelle={aktuell.quelle}
              schwierigkeit_score={aktuell.schwierigkeit_score}
            />
          {:else}
            <MusterloesungenBereich aufgabeId={aktuell.id} bind:freigegeben={musterloesungen_frei} />
          {/if}
        </div>
      {/snippet}

      {#snippet mitte()}
        <div class="editor-kopf">
          <span class="label">Editor &middot; {aktuell.sprache}</span>
          <button class="pruefen" disabled={pruefen_laeuft || !code.trim()} onclick={pruefe}>
            {#if pruefen_laeuft}
              <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i>
              läuft ...
            {:else}
              <i class="fa-solid fa-play" aria-hidden="true"></i>
              Prüfen
            {/if}
          </button>
        </div>
        <div class="editor-host">
          <EditorBereich sprache={aktuell.sprache} bind:code />
        </div>
        <ProbelaufBereich aufgabeId={aktuell.id} {code} funktion={aktuell.funktion} />
      {/snippet}

      {#snippet rechts()}
        <OutputBereich
          ergebnis={ergebnis}
          fehler={pruef_fehler}
          laeuft={pruefen_laeuft}
          anzahl_versteckt={aktuell.anzahl_versteckte_tests}
          schwierigkeit_score={aktuell.schwierigkeit_score}
          onWeiter={geheZuNaechster}
        />

        <VerlaufBereich aufgabeId={aktuell.id} stand={abgaben} onUebernehmen={(c) => (code = c)} />
      {/snippet}
    </DreiSpaltenLayout>
    {/if}
  {/if}
</div>

<ConfirmModal
  offen={reset_modal_offen}
  titel="Aufgabe zurücksetzen?"
  nachricht="Status, Versuche, genutzte Hinweise und erreichte Punkte werden zurückgesetzt. Deine Submissions bleiben in der Historie. Streak und andere Aufgaben sind nicht betroffen."
  bestaetigen_text="Zurücksetzen"
  abbrechen_text="Abbrechen"
  danger={true}
  onBestaetigen={resetBestaetigt}
  onAbbrechen={() => (reset_modal_offen = false)}
/>

<style>
  .detail {
    display: flex;
    flex-direction: column;
    height: 100%;
    min-height: 0;
  }
  .info { padding: var(--sp-4); color: var(--fg-dim); }
  .info.fehler { color: var(--red); }

  .kopf {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-3) var(--sp-4);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card);
    flex-shrink: 0;
  }
  .kopf-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 36px;
    height: 36px;
    padding: 0;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .kopf-btn:hover { color: var(--accent); border-color: var(--accent); }
  .kopf-btn.warn:hover { color: var(--orange); border-color: var(--orange); }
  .kopf-info { display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0; }
  .id { font-family: var(--mono); font-size: var(--fs-xs); color: var(--fg-mute); }
  h1 { margin: 0; font-size: var(--fs-lg); font-weight: 600; }
  .kopf-meta { display: flex; align-items: center; gap: var(--sp-2); }
  .badge {
    padding: 2px 8px;
    border: 1px solid var(--border);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    border-radius: var(--radius-sm);
  }
  .badge.sprache { color: var(--accent); border-color: var(--accent); }

  .sperre-banner {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: var(--sp-3) var(--sp-4);
    background: color-mix(in srgb, var(--orange) 12%, transparent);
    border-bottom: 1px solid var(--orange);
    color: var(--fg);
    font-family: var(--quick);
    font-size: var(--fs-sm);
    flex-wrap: wrap;
  }
  .bug-banner {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: var(--sp-2) var(--sp-4);
    background: color-mix(in srgb, var(--red) 10%, transparent);
    border-bottom: 1px solid var(--red);
    color: var(--fg);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .bug-banner i { color: var(--red); }
  .sperre-banner i {
    color: var(--orange);
  }
  .vor-link {
    background: transparent;
    border: none;
    color: var(--accent);
    cursor: pointer;
    font-family: inherit;
    font-size: inherit;
    text-decoration: underline;
    padding: 0;
  }
  .vor-link:hover {
    color: var(--accent-strong);
  }
  .zeit {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .score {
    font-size: var(--fs-sm);
    color: var(--accent);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  .tab-leiste {
    display: flex;
    gap: 0;
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
  .tab.aktiv {
    color: var(--accent);
    border-bottom-color: var(--accent);
  }
  .tab-inhalt {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }
  .editor-kopf {
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
  .pruefen:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  .editor-host {
    flex: 1 1 auto;
    min-height: 0;
    overflow: hidden;
  }


</style>
