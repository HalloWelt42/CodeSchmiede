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
  import DebuggerBereich from './DebuggerBereich.svelte';
  import { DebugSitzung } from '../debugger/sitzung.svelte';
  import CssKlonView from './CssKlonView.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import LueckentextView from './LueckentextView.svelte';
  import OutputBereich from './OutputBereich.svelte';
  import OutputQuizView from './OutputQuizView.svelte';
  import ProbelaufBereich from './ProbelaufBereich.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import SqlAbfrageView from './SqlAbfrageView.svelte';
  import MusterJagdView from './MusterJagdView.svelte';
  import SprintView from './SprintView.svelte';
  import KrimiView from './KrimiView.svelte';
  import AmpelView from './AmpelView.svelte';
  import AufzugView from './AufzugView.svelte';
  import TuringView from './TuringView.svelte';
  import SchaltungView from './SchaltungView.svelte';
  import CodesView from './CodesView.svelte';
  import TaktView from './TaktView.svelte';
  import KvView from './KvView.svelte';
  import RoboterView from './RoboterView.svelte';
  import { spielStore } from '../stores/SpielStore.svelte';

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
    if (pruefen_laeuft || code !== gesicherter_code || sitzung.aktiv) return fassung.halten();
  });

  // Debugger (nur am Rechner, Python und JavaScript): Lauf mit der Eingabe des Probelaufs, rechts als eigener Reiter
  const sitzung = new DebugSitzung();
  let rechter_tab = $state<'ergebnis' | 'debugger'>('ergebnis');
  /** Zeile, die der Debugger gerade zeigt */
  let debug_zeile = $state<number | null>(null);
  let mit_debugger = $derived(!geraet.telefon && (detail?.sprache === 'python' || detail?.sprache === 'javascript'));
  $effect(() => {
    if (!sitzung.aktiv) rechter_tab = 'ergebnis';
  });

  function debuggen(eingabe: unknown[], aufruf: string | null): void {
    rechter_tab = 'debugger';
    if (detail) void sitzung.starten(detail.id, code, eingabe, aufruf);
  }

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
    rechter_tab = 'ergebnis';
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
  // Level eines Spiels: Kopf mit Levelnummer und Sternen
  let alsLevel = $derived(spielStore.levelVon(aufgabeId));

  let schwFarbe = $derived(
    detail ? farbeZuCss(konfig.schwierigkeitFarbe(detail.schwierigkeit)) : 'var(--accent)',
  );

</script>

<div class="seite">
  {#if ladenDetail}
    <p class="leer-zeile">Lade Aufgabe ...</p>
  {:else if fehler}
    <p class="leer-zeile fehlertext">Fehler: {fehler}</p>
  {:else if detail}
    {@const aktuell = detail}
    <header class="a-kopf">
      <button class="ikon" onclick={zurueck} aria-label="Zurück zur Liste">
        <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
      </button>
      {#if alsLevel}
        {@const l = alsLevel.level}
        {@const gruppe = l.gruppe && l.gruppe !== alsLevel.spiel.titel ? l.gruppe : null}
        <span class="zelle-titel">
          <b>{alsLevel.spiel.levels_als === 'auswahl' ? aktuell.titel : `${alsLevel.spiel.level_wort} ${l.nummer_in_gruppe ?? l.nummer}: ${aktuell.titel}`}</b>
          <span class:meta-text={geraet.telefon}>{alsLevel.spiel.titel}{gruppe ? `, ${gruppe}` : ''}{geraet.telefon ? `, ${aktProgress?.punkte_erreicht ?? 0} / ${aktuell.schwierigkeit_score} Punkte` : gruppe ? '' : `, ${aktuell.id}`}</span>
        </span>
        <div class="meta">
          {#if !geraet.telefon}<span class="badge" style:color={schwFarbe}>{konfig.schwierigkeitTitel(aktuell.schwierigkeit)}</span>{/if}
          <span class="sterne gross" title="beste Wertung: {aktProgress?.sterne ?? 0} von 3 Sternen">
            {#each [1, 2, 3] as n (n)}<i class="fa-solid fa-star" class:aus={n > (aktProgress?.sterne ?? 0)} aria-hidden="true"></i>{/each}
          </span>
          {#if !geraet.telefon}<span class="num punkte"><i class="fa-solid fa-coins" aria-hidden="true"></i> {aktProgress?.punkte_erreicht ?? 0} / {aktuell.schwierigkeit_score}</span>{/if}
        </div>
      {:else if geraet.telefon}
        <span class="zelle-titel">
          <b>{aktuell.titel}</b>
          <span class="meta-text">
            {konfig.schwierigkeitTitel(aktuell.schwierigkeit)}, {konfig.sprache(aktuell.sprache)?.titel ?? aktuell.sprache},
            {aktuell.schaetz_minuten} min, {aktProgress?.punkte_erreicht ?? 0} / {aktuell.schwierigkeit_score} Punkte
          </span>
        </span>
      {:else}
        <span class="zelle-titel"><b>{aktuell.titel}</b><span>{aktuell.id}</span></span>
        <div class="meta">
          <span class="badge" style:color={schwFarbe}>{konfig.schwierigkeitTitel(aktuell.schwierigkeit)}</span>
          <span class="badge sprache">{konfig.sprache(aktuell.sprache)?.titel ?? aktuell.sprache}</span>
          <span><i class="fa-regular fa-clock" aria-hidden="true"></i> {aktuell.schaetz_minuten} min</span>
          <span class="num punkte"><i class="fa-solid fa-coins" aria-hidden="true"></i> {aktProgress?.punkte_erreicht ?? 0} / {aktuell.schwierigkeit_score}</span>
        </div>
      {/if}
      {#if aktProgress && (aktProgress.versuche > 0 || aktProgress.hints_genutzt > 0)}
        <button class="ikon warn" onclick={resetAnfragen} aria-label="Aufgabe zurücksetzen">
          <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>
        </button>
      {/if}
    </header>

    {#if aktuell.gesperrt}
      <div class="hinweis-box band">
        <i class="fa-solid fa-lock" aria-hidden="true"></i>
        <span>
          Gesperrt, erst lösen:
          {#each aktuell.voraussetzungen_offen as v, i (v)}
            <button class="verweis" onclick={() => route.setze('aufgabe', v)}>{aufgabenStore.findeKurz(v)?.titel ?? v}</button>{#if i < aktuell.voraussetzungen_offen.length - 1}, {/if}
          {/each}
        </span>
      </div>
    {/if}

    {#if aktuell.task_type === 'output_quiz'}
      <OutputQuizView detail={aktuell} />
    {:else if aktuell.task_type === 'lueckentext'}
      <LueckentextView detail={aktuell} />
    {:else if aktuell.task_type === 'css_klon'}
      <CssKlonView detail={aktuell} />
    {:else if aktuell.task_type === 'sql_abfrage' || aktuell.task_type === 'sql_aenderung'}
      <SqlAbfrageView detail={aktuell} />
    {:else if aktuell.task_type === 'muster_jagd'}
      <MusterJagdView detail={aktuell} />
    {:else if aktuell.task_type === 'ausgabe_sprint'}
      <SprintView detail={aktuell} />
    {:else if aktuell.task_type === 'roboter'}
      <RoboterView detail={aktuell} />
    {:else if aktuell.task_type === 'ampel'}
      <AmpelView detail={aktuell} />
    {:else if aktuell.task_type === 'aufzug'}
      <AufzugView detail={aktuell} />
    {:else if aktuell.task_type === 'turing'}
      <TuringView detail={aktuell} />
    {:else if aktuell.task_type === 'schaltung'}
      <SchaltungView detail={aktuell} />
    {:else if aktuell.task_type === 'codes'}
      <CodesView detail={aktuell} />
    {:else if aktuell.task_type === 'takt'}
      <TaktView detail={aktuell} />
    {:else if aktuell.task_type === 'kv'}
      <KvView detail={aktuell} />
    {:else if aktuell.task_type === 'sql_krimi'}
      <KrimiView detail={aktuell} />
    {:else}
      {#if aktuell.task_type === 'bug_finden'}
        <div class="hinweis-box band fehler">
          <i class="fa-solid fa-bug" aria-hidden="true"></i>
          <span><strong>Fehler finden:</strong> Im Editor steht Code mit einem Fehler. Finde und behebe ihn, dann Prüfen.</span>
        </div>
      {/if}
      <DreiSpaltenLayout
        mitteTitel="Editor, {konfig.sprache(aktuell.sprache)?.titel ?? aktuell.sprache}"
        rechtsTitel={sitzung.aktiv ? undefined : 'Ergebnis'}
        pruefen={{ aktion: pruefe, laeuft: pruefen_laeuft, moeglich: code.trim() !== '' }}
      >
        {#snippet links()}
          {#if aktuell.musterloesungen_anzahl > 0}
            <SpaltenReiter
              reiter={[
                { id: 'aufgabe', titel: 'Aufgabe', icon: 'fa-file-lines' },
                { id: 'loesungen', titel: `Musterlösungen (${aktuell.musterloesungen_anzahl})`, icon: 'fa-lightbulb' },
              ]}
              bind:aktiv={aktiver_tab}
            />
          {/if}
          <div class="rollfeld ohne-rand">
            {#if aktiver_tab === 'aufgabe'}
              <BeschreibungsBereich
                aufgabeId={aktuell.id}
                markdown={aktuell.beschreibung_md}
                hints={aktuell.hints}
                tests_sichtbar={aktuell.tests_sichtbar}
                anzahl_versteckt={aktuell.anzahl_versteckte_tests}
                quelle={aktuell.quelle}
                schwierigkeit_score={aktuell.schwierigkeit_score}
                programm={aktuell.task_type === 'programm'}
              />
            {:else}
              <MusterloesungenBereich aufgabeId={aktuell.id} bind:freigegeben={musterloesungen_frei} />
            {/if}
          </div>
        {/snippet}

        {#snippet mitte()}
          <div class="editor-host">
            <EditorBereich
              sprache={aktuell.sprache}
              bind:code
              markierteZeile={rechter_tab === 'debugger' ? debug_zeile : null}
              mitHaltepunkten={mit_debugger}
              bind:haltepunkte={sitzung.haltepunkte}
            />
          </div>
          {#if mit_debugger}
            <div class="rinnen-hinweis"><i class="fa-solid fa-circle" aria-hidden="true"></i> Klick links neben die Zeilennummer setzt oder löscht einen Haltepunkt.</div>
          {/if}
          <ProbelaufBereich
            aufgabeId={aktuell.id}
            {code}
            funktion={aktuell.funktion}
            programm={aktuell.task_type === 'programm'}
            sprache={aktuell.sprache}
            onDebuggen={mit_debugger ? debuggen : undefined}
            debugLaeuft={sitzung.laeuft}
          />
        {/snippet}

        {#snippet rechts()}
          {#if sitzung.aktiv}
            <SpaltenReiter
              reiter={[
                { id: 'ergebnis', titel: 'Ergebnis', icon: 'fa-square-check' },
                { id: 'debugger', titel: 'Debugger', icon: 'fa-bug' },
              ]}
              bind:aktiv={rechter_tab}
            />
          {/if}
          {#if rechter_tab === 'debugger'}
            <div class="rollfeld">
              <DebuggerBereich {sitzung} sprache={aktuell.sprache} {code} bind:zeile={debug_zeile} />
            </div>
          {:else}
          <div class="rollfeld">
            <OutputBereich
              {ergebnis}
              fehler={pruef_fehler}
              laeuft={pruefen_laeuft}
              anzahl_versteckt={aktuell.anzahl_versteckte_tests}
              programm={aktuell.task_type === 'programm'}
              onWeiter={geheZuNaechster}
            />
            <VerlaufBereich aufgabeId={aktuell.id} stand={abgaben} onUebernehmen={(c) => (code = c)} />
          </div>
          {/if}
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
  .a-kopf .punkte { color: var(--accent); }
  .a-kopf .ikon.warn { margin-left: var(--sp-1); }
  .meta-text {
    font-family: var(--sans);
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    white-space: normal;
  }
  .fehlertext { color: var(--red); }
  .band {
    flex: none;
    border-width: 0 0 1px;
    font-family: var(--quick);
  }
  .verweis {
    border: 0;
    padding: 0;
    background: transparent;
    color: var(--accent);
    font: inherit;
    text-decoration: underline;
  }
  .verweis:hover:not(:disabled) { background: transparent; color: var(--accent-strong); }
  .editor-host {
    flex: 1;
    min-height: 0;
    overflow: hidden;
  }
  .rinnen-hinweis {
    flex: none;
    padding: 4px var(--sp-3);
    border-top: 1px solid var(--border);
    color: var(--fg-mute);
    font-size: var(--fs-xs);
  }
  .rinnen-hinweis i { color: var(--ed-haltepunkt); font-size: 9px; vertical-align: 1px; }
</style>
