<script lang="ts">
  /*
   * Verwaltungs-Übersicht aller Aufgaben.
   * Bewusst entkoppelt: eigener Endpoint /api/admin/aufgaben, eigener
   * Store, eigene Typen. Tabelle iteriert über alle Aufgaben und zeigt
   * pro Eintrag eine Zeile mit den Kern-Metadaten plus ausklappbare
   * Sektionen für Beschreibung, sichtbare Tests, versteckte Tests,
   * Hints, Frontmatter, Statistik.
   */
  import { onMount } from 'svelte';
  import { adminApi } from '../api/AdminApi';
  import type { PfadEintrag } from '../api/AdminApi';
  import { progressApi } from '../api/ProgressApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import type { VerwaltungsEintrag } from '../types/Admin';
  import { route } from '../stores/RouteStore.svelte';
  import AufgabeEditor from './AufgabeEditor.svelte';
  import ConfirmModal from './ConfirmModal.svelte';
  import PfadEditor from './PfadEditor.svelte';

  let eintraege = $state<VerwaltungsEintrag[]>([]);
  let laden = $state(false);
  let fehler = $state<string | null>(null);
  let suche = $state('');

  let editor_offen = $state(false);
  let editor_eintrag = $state<VerwaltungsEintrag | null>(null);
  let editor_vorlage = $state<VerwaltungsEintrag | null>(null);
  let loesch_eintrag = $state<VerwaltungsEintrag | null>(null);
  let reset_alles_bestaetigung = $state(false);

  async function reset_alles_anwenden(): Promise<void> {
    reset_alles_bestaetigung = false;
    try {
      await progressApi.resetAlles();
      await Promise.all([neuLaden(), progressStore.ladeAlles()]);
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  let aktiver_tab = $state<'aufgaben' | 'pfade'>('aufgaben');
  let pfade = $state<PfadEintrag[]>([]);
  let pfad_editor_offen = $state(false);
  let pfad_editor_eintrag = $state<PfadEintrag | null>(null);
  let pfad_loesch_eintrag = $state<PfadEintrag | null>(null);

  async function ladePfade(): Promise<void> {
    try {
      pfade = await adminApi.pfade();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  function pfad_neu(): void {
    pfad_editor_eintrag = null;
    pfad_editor_offen = true;
  }
  function pfad_bearbeiten(p: PfadEintrag): void {
    pfad_editor_eintrag = p;
    pfad_editor_offen = true;
  }
  function pfad_editor_schliessen(): void {
    pfad_editor_offen = false;
    pfad_editor_eintrag = null;
  }
  async function pfad_nach_speichern(): Promise<void> {
    pfad_editor_offen = false;
    pfad_editor_eintrag = null;
    await ladePfade();
  }
  function pfad_loesch_anfordern(p: PfadEintrag): void {
    pfad_loesch_eintrag = p;
  }
  async function pfad_loesch_bestaetigt(): Promise<void> {
    if (!pfad_loesch_eintrag) return;
    const id = pfad_loesch_eintrag.id;
    pfad_loesch_eintrag = null;
    try {
      await adminApi.pfadLoeschen(id);
      await ladePfade();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  function neu_oeffnen(): void {
    editor_eintrag = null;
    editor_vorlage = null;
    editor_offen = true;
  }

  function bearbeiten(e: VerwaltungsEintrag): void {
    editor_eintrag = e;
    editor_vorlage = null;
    editor_offen = true;
  }

  function duplizieren(e: VerwaltungsEintrag): void {
    editor_eintrag = null;
    editor_vorlage = e;
    editor_offen = true;
  }

  function editor_schliessen(): void {
    editor_offen = false;
    editor_eintrag = null;
    editor_vorlage = null;
  }

  async function nach_speichern(_id: string): Promise<void> {
    editor_offen = false;
    editor_eintrag = null;
    editor_vorlage = null;
    await neuLaden();
  }

  function loesch_anfordern(e: VerwaltungsEintrag): void {
    loesch_eintrag = e;
  }

  async function loesch_bestaetigt(): Promise<void> {
    if (!loesch_eintrag) return;
    const id = loesch_eintrag.id;
    loesch_eintrag = null;
    try {
      await adminApi.aufgabeLoeschen(id);
      await neuLaden();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  onMount(async () => {
    await Promise.all([neuLaden(), ladePfade()]);
  });

  async function neuLaden(): Promise<void> {
    laden = true;
    fehler = null;
    try {
      eintraege = await adminApi.aufgaben();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laden = false;
    }
  }

  function formatiere(wert: unknown): string {
    return JSON.stringify(wert);
  }

  let gefiltert = $derived(
    eintraege.filter((e) => {
      if (!suche.trim()) return true;
      const q = suche.trim().toLowerCase();
      const text = [
        e.id,
        e.titel,
        e.sprache,
        e.schwierigkeit,
        ...e.tags,
        ...e.pfade,
      ]
        .join(' ')
        .toLowerCase();
      return text.includes(q);
    }),
  );

  let aggregat = $derived({
    gesamt: eintraege.length,
    sprachen: new Set(eintraege.map((e) => e.sprache)).size,
    pfade: new Set(eintraege.flatMap((e) => e.pfade)).size,
    submissions: eintraege.reduce((s, e) => s + e.statistik.submissions_gesamt, 0),
  });
</script>

<div class="verwaltung">
  <header class="kopf">
    <div>
      <h1>Verwaltung</h1>
      <p class="lead">
        Vollständige Übersicht aller indizierten Aufgaben.
        Versteckte Tests sind hier sichtbar -- nur du siehst diese Ansicht.
      </p>
    </div>
    <div class="kopf-actions">
      {#if aktiver_tab === 'aufgaben'}
        <button class="primaer-btn" onclick={neu_oeffnen}>
          <i class="fa-solid fa-plus" aria-hidden="true"></i>
          Neue Aufgabe
        </button>
        <button class="reload-btn" onclick={neuLaden} disabled={laden}>
          <i class="fa-solid fa-rotate" aria-hidden="true"></i>
          {laden ? 'Lade ...' : 'Neu laden'}
        </button>
        <button class="danger-btn" onclick={() => (reset_alles_bestaetigung = true)} title="Alle Submissions, Punkte und Streak löschen">
          <i class="fa-solid fa-trash-can" aria-hidden="true"></i>
          Alles zurücksetzen
        </button>
      {:else}
        <button class="primaer-btn" onclick={pfad_neu}>
          <i class="fa-solid fa-plus" aria-hidden="true"></i>
          Neuer Pfad
        </button>
        <button class="reload-btn" onclick={ladePfade}>
          <i class="fa-solid fa-rotate" aria-hidden="true"></i>
          Neu laden
        </button>
      {/if}
    </div>
  </header>

  <nav class="tabs">
    <button
      class:aktiv={aktiver_tab === 'aufgaben'}
      onclick={() => (aktiver_tab = 'aufgaben')}
    >
      <i class="fa-solid fa-list-check" aria-hidden="true"></i>
      Aufgaben <span class="num">{eintraege.length}</span>
    </button>
    <button
      class:aktiv={aktiver_tab === 'pfade'}
      onclick={() => (aktiver_tab = 'pfade')}
    >
      <i class="fa-solid fa-route" aria-hidden="true"></i>
      Pfade <span class="num">{pfade.length}</span>
    </button>
  </nav>

  {#if fehler}
    <p class="fehler">Fehler: {fehler}</p>
  {/if}

  {#if aktiver_tab === 'aufgaben' && !laden && eintraege.length > 0}
    <section class="aggregat">
      <div class="kennzahl"><span class="num">{aggregat.gesamt}</span><small>Aufgaben</small></div>
      <div class="kennzahl"><span class="num">{aggregat.sprachen}</span><small>Sprachen</small></div>
      <div class="kennzahl"><span class="num">{aggregat.pfade}</span><small>Pfade</small></div>
      <div class="kennzahl"><span class="num">{aggregat.submissions}</span><small>Submissions</small></div>
    </section>

    <div class="suche-zeile">
      <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
      <input
        type="text"
        bind:value={suche}
        placeholder="Filter (ID, Titel, Sprache, Tag, Pfad)"
      />
      <span class="treffer num">{gefiltert.length} / {eintraege.length}</span>
    </div>

    <div class="tabelle">
      {#each gefiltert as e (e.id)}
        <article class="zeile status-{e.statistik.status}">
          <header class="zeilen-kopf">
            <div class="haupt">
              <span class="id">{e.id}</span>
              <span class="titel">{e.titel}</span>
            </div>

            <div class="meta">
              <span class="badge">{e.sprache}</span>
              <span class="badge schw-{e.schwierigkeit}">{e.schwierigkeit}</span>
              <span class="badge num">{e.schwierigkeit_score}</span>
              <span class="badge revision">rev {e.revision}</span>
              <span class="badge lizenz">{e.lizenz}</span>
              {#each e.pfade as pfad}
                <span class="badge pfad">{pfad}</span>
              {/each}
              <span class="badge stat-{e.statistik.status}">{e.statistik.status}</span>
            </div>

            <div class="aktionen">
              <button class="action" onclick={() => bearbeiten(e)} title="Bearbeiten" aria-label="Bearbeiten">
                <i class="fa-solid fa-pen-to-square" aria-hidden="true"></i>
              </button>
              <button class="action" onclick={() => duplizieren(e)} title="Duplizieren" aria-label="Duplizieren">
                <i class="fa-solid fa-clone" aria-hidden="true"></i>
              </button>
              <button class="action danger" onclick={() => loesch_anfordern(e)} title="Löschen" aria-label="Löschen">
                <i class="fa-solid fa-trash" aria-hidden="true"></i>
              </button>
              <button class="action" onclick={() => route.setze('aufgabe', e.id)} title="Aufgabe öffnen" aria-label="Öffnen">
                <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
              </button>
            </div>
          </header>

          <div class="kennzahlen-zeile">
            <span><i class="fa-solid fa-coins" aria-hidden="true"></i> <span class="num">{e.statistik.punkte_erreicht} / {e.schwierigkeit_score}</span> Punkte</span>
            <span><i class="fa-solid fa-arrow-rotate-right" aria-hidden="true"></i> <span class="num">{e.statistik.versuche}</span> Versuche</span>
            <span><i class="fa-solid fa-paper-plane" aria-hidden="true"></i> <span class="num">{e.statistik.submissions_gesamt}</span> Submissions ({e.statistik.bestandene_submissions} bestanden)</span>
            <span><i class="fa-solid fa-eye" aria-hidden="true"></i> <span class="num">{e.statistik.hints_genutzt}</span> / <span class="num">{e.hints.length}</span> Hints genutzt</span>
            <span><i class="fa-regular fa-clock" aria-hidden="true"></i> <span class="num">{e.schaetz_minuten}</span> min, Timeout <span class="num">{e.zeitlimit_sekunden}</span>s</span>
            <span><i class="fa-solid fa-puzzle-piece" aria-hidden="true"></i> <span class="num">{e.musterloesungen_anzahl}</span> Musterlösungen</span>
          </div>

          <details class="sektion">
            <summary>Beschreibung &middot; {e.beschreibung_md.length} Zeichen</summary>
            <pre class="markdown-quelle">{e.beschreibung_md}</pre>
          </details>

          <details class="sektion">
            <summary>Sichtbare Tests &middot; {e.tests_sichtbar.length}</summary>
            <ul class="test-liste">
              {#each e.tests_sichtbar as t, i (i)}
                <li>
                  <code>{e.funktion}({t.input.map(formatiere).join(', ')})</code>
                  <span class="zeichen">=</span>
                  <code class="erwartet">{formatiere(t.expected)}</code>
                </li>
              {/each}
            </ul>
          </details>

          <details class="sektion">
            <summary>
              Versteckte Tests &middot; {e.tests_versteckt.length}
              <span class="warn">
                <i class="fa-solid fa-eye-slash" aria-hidden="true"></i>
                nur in der Verwaltung sichtbar
              </span>
            </summary>
            <ul class="test-liste">
              {#each e.tests_versteckt as t, i (i)}
                <li>
                  <code>{e.funktion}({t.input.map(formatiere).join(', ')})</code>
                  <span class="zeichen">=</span>
                  <code class="erwartet">{formatiere(t.expected)}</code>
                </li>
              {/each}
            </ul>
          </details>

          <details class="sektion">
            <summary>Hints &middot; {e.hints.length}</summary>
            <ol class="hint-liste">
              {#each e.hints as h, i (i)}
                <li>
                  <span class="hint-kosten">-{h.kosten}</span>
                  <pre>{h.text}</pre>
                </li>
              {/each}
            </ol>
          </details>

          <details class="sektion">
            <summary>Frontmatter &middot; technische Daten</summary>
            <dl class="metadata">
              <dt>schema_version</dt><dd>{e.schema_version}</dd>
              <dt>task_type</dt><dd><code>{e.task_type}</code></dd>
              <dt>runner_type</dt><dd><code>{e.runner_type}</code></dd>
              <dt>funktion</dt><dd><code>{e.funktion ?? '-'}</code></dd>
              <dt>tags</dt><dd>{e.tags.join(', ') || '-'}</dd>
              <dt>voraussetzungen</dt><dd>{e.voraussetzungen.join(', ') || '-'}</dd>
              <dt>autor</dt><dd>{e.autor ?? '-'}</dd>
              <dt>erstellt_am</dt><dd>{e.erstellt_am ?? '-'}</dd>
              <dt>quelle.url</dt><dd>{e.quelle.url ?? '-'}</dd>
              <dt>quelle.notiz</dt><dd>{e.quelle.notiz ?? '-'}</dd>
              <dt>dateipfad</dt><dd><code>{e.dateipfad}</code></dd>
              <dt>hash</dt><dd><code>{e.hash.slice(0, 12)}…</code></dd>
            </dl>
          </details>

          <details class="sektion">
            <summary>Starter-Code &middot; {e.starter_code.length} Zeichen</summary>
            <pre class="code">{e.starter_code}</pre>
          </details>
        </article>
      {/each}
    </div>
  {:else if aktiver_tab === 'aufgaben' && !laden}
    <p class="info">Keine Aufgaben gefunden.</p>
  {/if}

  {#if aktiver_tab === 'pfade'}
    <div class="pfad-tabelle">
      {#if pfade.length === 0}
        <p class="info">Noch keine Pfade.</p>
      {:else}
        {#each pfade as p (p.id)}
          <article class="pfad-zeile">
            <header class="zeilen-kopf">
              <div class="haupt">
                <span class="id">{p.id}</span>
                <span class="titel">{p.titel}</span>
              </div>
              <div class="meta">
                <span class="badge num">{p.aufgaben_anzahl} Aufgaben</span>
              </div>
              <div class="aktionen">
                <button class="action" onclick={() => pfad_bearbeiten(p)} title="Bearbeiten" aria-label="Bearbeiten">
                  <i class="fa-solid fa-pen-to-square" aria-hidden="true"></i>
                </button>
                <button class="action danger" onclick={() => pfad_loesch_anfordern(p)} title="Löschen" aria-label="Löschen">
                  <i class="fa-solid fa-trash" aria-hidden="true"></i>
                </button>
              </div>
            </header>
            {#if p.beschreibung}
              <p class="pfad-beschreibung">{p.beschreibung}</p>
            {/if}
            <ol class="pfad-aufgaben">
              {#each p.reihenfolge as aid (aid)}
                <li>
                  <span class="num pos">{p.reihenfolge.indexOf(aid) + 1}.</span>
                  <code>{aid}</code>
                </li>
              {/each}
            </ol>
          </article>
        {/each}
      {/if}
    </div>
  {/if}
</div>

<AufgabeEditor
  offen={editor_offen}
  bearbeiten={editor_eintrag}
  vorlage={editor_vorlage}
  onSchliessen={editor_schliessen}
  onGespeichert={nach_speichern}
/>

<ConfirmModal
  offen={loesch_eintrag !== null}
  titel="Aufgabe löschen?"
  nachricht={loesch_eintrag
    ? `Aufgabe '${loesch_eintrag.id}' (${loesch_eintrag.titel}) wird komplett entfernt -- inkl. aller Musterlösungen. Submissions in der Historie bleiben erhalten.`
    : ''}
  bestaetigen_text="Löschen"
  abbrechen_text="Abbrechen"
  danger={true}
  onBestaetigen={loesch_bestaetigt}
  onAbbrechen={() => (loesch_eintrag = null)}
/>

<PfadEditor
  offen={pfad_editor_offen}
  bearbeiten={pfad_editor_eintrag}
  aufgaben={eintraege}
  onSchliessen={pfad_editor_schliessen}
  onGespeichert={pfad_nach_speichern}
/>

<ConfirmModal
  offen={reset_alles_bestaetigung}
  titel="Alles zurücksetzen?"
  nachricht="Alle Submissions, Fortschritte, Punkte und der Streak werden komplett gelöscht. Die Aufgaben-Dateien selbst bleiben erhalten -- du fängst von vorne an. Dieser Schritt ist nicht umkehrbar."
  bestaetigen_text="Komplett zurücksetzen"
  abbrechen_text="Abbrechen"
  danger={true}
  onBestaetigen={reset_alles_anwenden}
  onAbbrechen={() => (reset_alles_bestaetigung = false)}
/>

<ConfirmModal
  offen={pfad_loesch_eintrag !== null}
  titel="Pfad löschen?"
  nachricht={pfad_loesch_eintrag
    ? `Pfad '${pfad_loesch_eintrag.id}' (${pfad_loesch_eintrag.titel}) wird entfernt. Aufgaben selbst bleiben erhalten -- nur die Pfad-Zuordnung verschwindet.`
    : ''}
  bestaetigen_text="Löschen"
  abbrechen_text="Abbrechen"
  danger={true}
  onBestaetigen={pfad_loesch_bestaetigt}
  onAbbrechen={() => (pfad_loesch_eintrag = null)}
/>

<style>
  .verwaltung {
    padding: var(--sp-5);
    overflow-y: auto;
  }
  .kopf {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: var(--sp-3);
    margin-bottom: var(--sp-4);
  }
  h1 {
    margin: 0 0 var(--sp-2);
    font-size: var(--fs-xl);
    font-weight: 600;
  }
  .lead {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .kopf-actions {
    display: flex;
    gap: var(--sp-2);
    flex-shrink: 0;
    align-items: center;
  }
  .primaer-btn {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 6px 14px;
    font-size: var(--fs-xs);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .primaer-btn:hover {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .danger-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-mute);
    padding: 6px 14px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .danger-btn:hover {
    color: var(--red);
    border-color: var(--red);
  }
  .reload-btn {
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
    gap: 6px;
    flex-shrink: 0;
  }
  .reload-btn:hover:not(:disabled) {
    color: var(--accent);
    border-color: var(--accent);
  }
  .reload-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .fehler {
    color: var(--red);
    background: color-mix(in srgb, var(--red) 10%, transparent);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--red);
  }
  .info {
    color: var(--fg-dim);
    font-family: var(--quick);
  }

  .aggregat {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: var(--sp-2);
    margin-bottom: var(--sp-3);
  }
  .kennzahl {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .kennzahl .num {
    font-size: var(--fs-xl);
    color: var(--accent);
  }
  .kennzahl small {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .suche-zeile {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 6px var(--sp-3);
    margin-bottom: var(--sp-3);
    border-radius: var(--radius-sm);
  }
  .suche-zeile i {
    color: var(--fg-mute);
    font-size: var(--fs-sm);
  }
  .suche-zeile input {
    flex: 1;
    background: transparent;
    border: none;
    color: var(--fg);
    font-family: var(--sans);
    font-size: var(--fs-sm);
    padding: 4px;
  }
  .suche-zeile input:focus {
    outline: none;
  }
  .treffer {
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }

  .tabelle {
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
  }
  .zeile {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .zeile.status-geloest {
    border-left: 3px solid var(--green);
  }
  .zeile.status-in_arbeit {
    border-left: 3px solid var(--orange);
  }

  .zeilen-kopf {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    flex-wrap: wrap;
  }
  .haupt {
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 200px;
  }
  .id {
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg-mute);
  }
  .titel {
    font-size: var(--fs-md);
    font-weight: 600;
    color: var(--fg);
  }
  .meta {
    display: flex;
    align-items: center;
    gap: var(--sp-1);
    flex-wrap: wrap;
  }
  .badge {
    padding: 2px 8px;
    border: 1px solid var(--border);
    background: var(--bg-card);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
  }
  .badge.schw-anfaenger { color: var(--green); border-color: var(--green); }
  .badge.schw-mittel { color: var(--orange); border-color: var(--orange); }
  .badge.schw-fortgeschritten,
  .badge.schw-experte { color: var(--red); border-color: var(--red); }
  .badge.pfad { color: var(--accent); border-color: var(--accent); }
  .badge.revision { font-family: var(--mono); }
  .badge.lizenz { font-family: var(--mono); }
  .badge.stat-geloest { color: var(--green); }
  .badge.stat-in_arbeit { color: var(--orange); }
  .aktionen {
    display: flex;
    gap: var(--sp-1);
  }
  .action {
    width: 32px;
    height: 32px;
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .action:hover {
    color: var(--accent);
    border-color: var(--accent);
  }
  .action.danger:hover {
    color: var(--red);
    border-color: var(--red);
  }

  .tabs {
    display: flex;
    gap: var(--sp-1);
    border-bottom: 1px solid var(--border);
    margin-bottom: var(--sp-3);
  }
  .tabs button {
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    color: var(--fg-dim);
    padding: 8px 16px;
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-bottom: -1px;
  }
  .tabs button.aktiv {
    color: var(--accent);
    border-bottom-color: var(--accent);
  }
  .tabs .num {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
  }
  .tabs button.aktiv .num { color: var(--accent); }

  .pfad-tabelle {
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
  }
  .pfad-zeile {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .pfad-beschreibung {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .pfad-aufgaben {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
    gap: var(--sp-1);
  }
  .pfad-aufgaben li {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 2px 8px;
    font-size: var(--fs-xs);
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .pfad-aufgaben .pos {
    color: var(--fg-mute);
  }
  .pfad-aufgaben code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    padding: 0;
    color: var(--accent);
  }

  .kennzahlen-zeile {
    display: flex;
    flex-wrap: wrap;
    gap: var(--sp-3);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    padding: var(--sp-2) 0;
    border-top: 1px dashed var(--border);
  }
  .kennzahlen-zeile span {
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .kennzahlen-zeile .num {
    color: var(--fg);
  }

  .sektion {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-2) var(--sp-3);
    border-radius: var(--radius-sm);
  }
  .sektion summary {
    cursor: pointer;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 2px 0;
    list-style-position: inside;
  }
  .sektion summary:hover {
    color: var(--accent);
  }
  .sektion[open] summary {
    color: var(--accent);
    margin-bottom: var(--sp-2);
  }
  .sektion .warn {
    margin-left: var(--sp-2);
    color: var(--orange);
    font-size: var(--fs-xs);
    text-transform: none;
    letter-spacing: 0;
  }
  .markdown-quelle, .code {
    margin: 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    overflow-x: auto;
    white-space: pre-wrap;
    max-height: 320px;
    overflow-y: auto;
  }
  .test-liste, .hint-liste {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
  }
  .test-liste li, .hint-liste li {
    background: var(--bg);
    border: 1px solid var(--border);
    padding: 4px var(--sp-2);
    font-size: var(--fs-xs);
    display: flex;
    align-items: flex-start;
    gap: var(--sp-2);
  }
  .test-liste code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    color: var(--fg);
    padding: 0;
  }
  .test-liste .erwartet { color: var(--green); }
  .test-liste .zeichen { color: var(--fg-mute); }
  .hint-liste {
    counter-reset: hints;
  }
  .hint-liste li {
    flex-direction: column;
    gap: 4px;
    counter-increment: hints;
  }
  .hint-kosten {
    color: var(--orange);
    font-family: var(--mono);
    font-size: var(--fs-xs);
  }
  .hint-liste pre {
    margin: 0;
    font-family: var(--quick);
    font-size: var(--fs-sm);
    color: var(--fg);
    white-space: pre-wrap;
  }

  .metadata {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 4px var(--sp-3);
    margin: 0;
  }
  .metadata dt {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    font-family: var(--mono);
  }
  .metadata dd {
    margin: 0;
    color: var(--fg);
    font-size: var(--fs-xs);
    word-break: break-all;
  }
  .metadata code {
    font-family: var(--mono);
    background: var(--bg);
    border: 1px solid var(--border);
    padding: 1px 4px;
    color: var(--fg);
  }
</style>
