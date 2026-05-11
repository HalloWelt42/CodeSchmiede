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
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { webWorkerRunner } from '../sandbox/WebWorkerRunner';
  import { farbeZuCss } from '../types/Konfig';
  import type { AufgabeDetail, Musterloesung } from '../types/Aufgabe';
  import type { SubmissionAntwort, VerlaufEintrag } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import ConfirmModal from './ConfirmModal.svelte';
  import CssKlonView from './CssKlonView.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import LueckentextView from './LueckentextView.svelte';
  import OutputBereich from './OutputBereich.svelte';
  import OutputQuizView from './OutputQuizView.svelte';
  import ProbelaufBereich from './ProbelaufBereich.svelte';
  import SqlAbfrageView from './SqlAbfrageView.svelte';

  let { aufgabeId }: { aufgabeId: string } = $props();

  let detail = $state<AufgabeDetail | null>(null);
  let ladenDetail = $state(false);
  let fehler = $state<string | null>(null);

  let code = $state('');
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let pruefen_laeuft = $state(false);
  let pruef_fehler = $state<string | null>(null);

  let musterloesungen = $state<Musterloesung[] | null>(null);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  let verlauf = $state<VerlaufEintrag[]>([]);
  let zeige_verlauf = $state(false);
  let verlauf_geladen = $state(false);

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
      if (detail.sprache === 'javascript') {
        ergebnis = await pruefe_lokal();
      } else {
        ergebnis = await submissionsApi.submit(detail.id, code);
      }
      if (ergebnis.bestanden && !musterloesungen) {
        musterloesungen = await aufgabenStore.ladeMusterloesungen(detail.id);
      }
      await progressStore.ladeAlles();
      if (verlauf_geladen) {
        await ladeVerlauf();
      }
    } catch (e) {
      pruef_fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function pruefe_lokal(): Promise<SubmissionAntwort> {
    if (!detail) throw new Error('kein detail');
    // tests_versteckt liegt clientseitig nicht vor (Anti-Hardcoding).
    // Wir nutzen daher nur tests_sichtbar. Die Backend-Pruefung wuerde
    // weiterhin funktionieren -- aber JS hat keinen Backend-Runner.
    // Konsequenz: bei JS-Aufgaben werden nur sichtbare Tests bewertet.
    // Deep-Clone via JSON, damit Svelte-Reactive-Proxies in plain Objects
    // landen -- structuredClone (postMessage) versteht Proxies nicht.
    const tests = JSON.parse(JSON.stringify(
      detail.tests_sichtbar.map((t) => ({ input: t.input, expected: t.expected })),
    ));
    const lauf = await webWorkerRunner.run(
      code,
      detail.funktion ?? 'main',
      tests,
      [],
      (detail.zeitlimit_sekunden ?? 5) * 1000,
    );
    const pruefung = {
      bestanden: lauf.bestanden,
      sichtbar: lauf.sichtbar.map((s) => ({
        index: s.index,
        bestanden: s.bestanden,
        eingabe: s.eingabe,
        erwartet: s.erwartet,
        tatsaechlich: s.tatsaechlich,
        fehler: s.fehler,
      })),
      versteckt_pass: 0,
      versteckt_fail: 0,
      laufzeit_ms: lauf.laufzeit_ms,
      stdout: lauf.stdout,
      stderr: lauf.stderr,
      timeout: lauf.timeout,
    };
    return await submissionsApi.submitLokal(detail.id, code, pruefung);
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

  async function ladeVerlauf(): Promise<void> {
    if (!detail) return;
    try {
      verlauf = await aufgabenApi.submissionsVerlauf(detail.id, 20);
      verlauf_geladen = true;
    } catch (e) {
      pruef_fehler = (e as Error).message;
    }
  }

  async function umschalteVerlauf(): Promise<void> {
    zeige_verlauf = !zeige_verlauf;
    if (zeige_verlauf && !verlauf_geladen) {
      await ladeVerlauf();
    }
  }

  function uebernehmeAusVerlauf(eintrag: VerlaufEintrag): void {
    code = eintrag.code;
    zeige_verlauf = false;
  }

  function formatiereDatum(iso: string): string {
    const d = new Date(iso);
    return d.toLocaleString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
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
      aktiver_tab = 'aufgabe';
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
    <DreiSpaltenLayout>
      {#snippet links()}
        {#if musterloesungen && musterloesungen.length > 0}
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
              Musterlösungen ({musterloesungen.length})
            </button>
          </div>
        {/if}
        <div class="tab-inhalt">
          {#if aktiver_tab === 'aufgabe'}
            <BeschreibungsBereich
              aufgabeId={detail.id}
              markdown={detail.beschreibung_md}
              hints={detail.hints}
              tests_sichtbar={detail.tests_sichtbar}
              anzahl_versteckt={detail.anzahl_versteckte_tests}
              quelle={detail.quelle}
              schwierigkeit_score={detail.schwierigkeit_score}
            />
          {:else if aktiver_tab === 'loesungen' && musterloesungen}
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
      {/snippet}

      {#snippet rechts()}
        <OutputBereich
          ergebnis={ergebnis}
          fehler={pruef_fehler}
          laeuft={pruefen_laeuft}
          anzahl_versteckt={detail.anzahl_versteckte_tests}
          schwierigkeit_score={detail.schwierigkeit_score}
          onWeiter={geheZuNaechster}
        />

        <div class="muster verlauf">
          <button class="muster-toggle" onclick={umschalteVerlauf}>
            <i class="fa-solid {zeige_verlauf ? 'fa-chevron-down' : 'fa-chevron-right'}" aria-hidden="true"></i>
            Verlauf{verlauf_geladen ? ` (${verlauf.length})` : ''}
          </button>
          {#if zeige_verlauf}
            {#if !verlauf_geladen}
              <div class="verlauf-info">Lade Verlauf ...</div>
            {:else if verlauf.length === 0}
              <div class="verlauf-info leer">Noch keine Submissions vorhanden.</div>
            {:else}
              <ul class="verlauf-liste">
                {#each verlauf as v (v.id)}
                  <li class:bestanden={v.bestanden}>
                    <button
                      type="button"
                      class="verlauf-eintrag"
                      onclick={() => uebernehmeAusVerlauf(v)}
                      title="Diesen Code in den Editor übernehmen"
                    >
                      <span class="verlauf-status">
                        <i class="fa-solid {v.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
                      </span>
                      <span class="verlauf-zeit">{formatiereDatum(v.zeitstempel)}</span>
                      <span class="verlauf-metrik num">{v.laufzeit_ms.toFixed(0)} ms</span>
                      <span class="verlauf-metrik num">{v.codelaenge_zeichen} Z.</span>
                    </button>
                  </li>
                {/each}
              </ul>
            {/if}
          {/if}
        </div>
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
  .tab-inhalt > .muster-liste {
    padding: var(--sp-3);
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

  .verlauf {
    border-top: 1px dashed var(--border);
  }
  .verlauf-info {
    margin-top: var(--sp-2);
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .verlauf-info.leer {
    color: var(--fg-mute);
  }
  .verlauf-liste {
    list-style: none;
    padding: 0;
    margin: var(--sp-3) 0 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .verlauf-eintrag {
    width: 100%;
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 6px var(--sp-2);
    cursor: pointer;
    display: grid;
    grid-template-columns: 24px 1fr 70px 70px;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-xs);
    text-align: left;
  }
  .verlauf-eintrag:hover {
    border-color: var(--accent);
  }
  .verlauf-status {
    color: var(--red);
    text-align: center;
  }
  .verlauf-liste li.bestanden .verlauf-status { color: var(--green); }
  .verlauf-zeit {
    font-family: var(--mono);
    color: var(--fg-dim);
  }
  .verlauf-metrik {
    color: var(--fg);
    text-align: right;
  }
</style>
