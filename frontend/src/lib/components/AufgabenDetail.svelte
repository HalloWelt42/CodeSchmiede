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
  import { route } from '../stores/RouteStore.svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import type { AufgabeDetail, Musterloesung } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import ConfirmModal from './ConfirmModal.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import OutputBereich from './OutputBereich.svelte';
  import ProbelaufBereich from './ProbelaufBereich.svelte';

  let { aufgabeId }: { aufgabeId: string } = $props();

  let detail = $state<AufgabeDetail | null>(null);
  let ladenDetail = $state(false);
  let fehler = $state<string | null>(null);

  let code = $state('');
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let pruefen_laeuft = $state(false);
  let pruef_fehler = $state<string | null>(null);

  let musterloesungen = $state<Musterloesung[] | null>(null);
  let zeige_loesungen = $state(false);

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
      // Letzte abgeschickte Lösung laden, falls vorhanden -- sonst
      // Starter-Boilerplate. Damit der Editor da weitermacht, wo der
      // Nutzer aufgehört hat.
      try {
        const letzte = await aufgabenApi.letzteSubmission(d.id);
        code = letzte.code ?? d.starter_code;
      } catch {
        code = d.starter_code;
      }
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
    try {
      ergebnis = await submissionsApi.submit(detail.id, code);
      if (ergebnis.bestanden && !musterloesungen) {
        musterloesungen = await aufgabenStore.ladeMusterloesungen(detail.id);
      }
      await progressStore.ladeAlles();
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

  function zurück(): void {
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
      musterloesungen = null;
      zeige_loesungen = false;
      // Beim Reset zurück auf Starter-Boilerplate, nicht auf letzte
      // Submission -- der Nutzer will von vorn anfangen.
      code = detail.starter_code;
      await progressStore.ladeAlles();
    } catch (e) {
      pruef_fehler = (e as Error).message;
    } finally {
      reset_modal_offen = false;
    }
  }

  let aktProgress = $derived(progressStore.proAufgabe[aufgabeId]);
</script>

<div class="detail">
  {#if ladenDetail}
    <div class="info">Lade Aufgabe ...</div>
  {:else if fehler}
    <div class="info fehler">Fehler: {fehler}</div>
  {:else if detail}
    <header class="kopf">
      <button class="kopf-btn" onclick={zurück} title="Zurück zur Liste" aria-label="Zurück">
        <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
      </button>
      <div class="kopf-info">
        <span class="id">{detail.id}</span>
        <h1>{detail.titel}</h1>
      </div>
      <div class="kopf-meta">
        <span class="badge schwierigkeit-{detail.schwierigkeit}">{detail.schwierigkeit}</span>
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

    <div class="spalten">
      <section class="spalte links">
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

      <section class="spalte mitte">
        <div class="editor-kopf">
          <span class="label">Editor &middot; {detail.sprache}</span>
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
          <EditorBereich sprache={detail.sprache} bind:code />
        </div>
        <ProbelaufBereich aufgabeId={detail.id} {code} funktion={detail.funktion} />
      </section>

      <section class="spalte rechts">
        <OutputBereich
          ergebnis={ergebnis}
          fehler={pruef_fehler}
          laeuft={pruefen_laeuft}
          anzahl_versteckt={detail.anzahl_versteckte_tests}
          schwierigkeit_score={detail.schwierigkeit_score}
          onWeiter={geheZuNaechster}
        />

        {#if ergebnis?.bestanden && musterloesungen}
          <div class="muster">
            <button class="muster-toggle" onclick={() => (zeige_loesungen = !zeige_loesungen)}>
              <i class="fa-solid {zeige_loesungen ? 'fa-chevron-down' : 'fa-chevron-right'}" aria-hidden="true"></i>
              Musterlösungen ({musterloesungen.length})
            </button>
            {#if zeige_loesungen}
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
        {/if}
      </section>
    </div>
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
  .badge.schwierigkeit-anfaenger { color: var(--green); border-color: var(--green); }
  .badge.schwierigkeit-mittel { color: var(--orange); border-color: var(--orange); }
  .badge.schwierigkeit-fortgeschritten,
  .badge.schwierigkeit-experte { color: var(--red); border-color: var(--red); }
  .badge.sprache { color: var(--accent); border-color: var(--accent); }
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

  .spalten {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1px;
    background: var(--border);
    flex: 1 1 auto;
    min-height: 0;
    overflow: hidden;
  }
  .spalte {
    display: flex;
    flex-direction: column;
    min-width: 0;
    min-height: 0;
    background: var(--bg-card);
    overflow: hidden;
  }
  .spalte.links { overflow-y: auto; }
  .spalte.mitte { background: var(--bg); }
  .spalte.rechts { overflow-y: auto; }

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

  .muster {
    border-top: 1px solid var(--border);
    padding: var(--sp-3);
  }
  .muster-toggle {
    background: transparent;
    border: none;
    color: var(--accent);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    cursor: pointer;
    padding: 0;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .muster-liste {
    margin-top: var(--sp-3);
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
    padding: var(--sp-1) 0;
  }
  .muster-eintrag pre {
    margin: var(--sp-2) 0 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    line-height: 1.5;
    color: var(--fg);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    overflow-x: auto;
    white-space: pre;
    border-radius: var(--radius-sm);
    max-height: 280px;
    overflow-y: auto;
  }
  .muster-eintrag pre code {
    background: transparent;
    border: none;
    padding: 0;
    color: inherit;
    font-size: inherit;
  }
</style>
