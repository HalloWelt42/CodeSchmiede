<script lang="ts">
  /*
   * Verwaltung aller Aufgaben und Pfade.
   * Bewusst entkoppelt: eigener Endpunkt /api/admin/aufgaben, eigene
   * Typen. Eine Tabellenzeile je Aufgabe mit den Kernwerten; ein Klick
   * klappt die Zeile auf (Tests samt versteckten, Beschreibung, Hinweise,
   * Startcode, technische Daten). Die Einzelheiten lädt erst das
   * Aufklappen nach.
   */
  import { onMount } from 'svelte';
  import { adminApi } from '../api/AdminApi';
  import type { Befund, PfadEintrag } from '../api/AdminApi';
  import { progressApi } from '../api/ProgressApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import type { VerwaltungsEintrag } from '../types/Admin';
  import { route } from '../stores/RouteStore.svelte';
  import { farbeZuCss } from '../types/Konfig';
  import Seite from './Seite.svelte';
  import AufgabeEditor from './AufgabeEditor.svelte';
  import ConfirmModal from './ConfirmModal.svelte';
  import CssBestandMessung from './CssBestandMessung.svelte';
  import PfadEditor from './PfadEditor.svelte';

  let eintraege = $state<VerwaltungsEintrag[]>([]);
  let laden = $state(false);
  let fehler = $state<string | null>(null);

  // Filter-Zustand: persistent in localStorage. Hunderte Aufgaben werden
  // sonst muehsam zu durchsuchen; mit gespeicherten Filtern bleibt der
  // Workspace zwischen Sessions konsistent.
  const FILTER_KEY = 'codeschmiede.verwaltung_filter';
  interface VFilter {
    suche: string;
    sprache: string;
    schwierigkeit: string;
    pfad: string;
  }
  function ladeFilter(): VFilter {
    try {
      const r = localStorage.getItem(FILTER_KEY);
      if (r) {
        const o = JSON.parse(r);
        return {
          suche: typeof o.suche === 'string' ? o.suche : '',
          sprache: typeof o.sprache === 'string' ? o.sprache : '',
          schwierigkeit: typeof o.schwierigkeit === 'string' ? o.schwierigkeit : '',
          pfad: typeof o.pfad === 'string' ? o.pfad : '',
        };
      }
    } catch { /* ungueltig -> Default */ }
    return { suche: '', sprache: '', schwierigkeit: '', pfad: '' };
  }
  const initF = ladeFilter();
  let suche = $state(initF.suche);
  let sprache = $state(initF.sprache);
  let schwierigkeit = $state(initF.schwierigkeit);
  let pfad = $state(initF.pfad);
  $effect(() => {
    try {
      localStorage.setItem(
        FILTER_KEY,
        JSON.stringify({ suche, sprache, schwierigkeit, pfad }),
      );
    } catch { /* z.B. private mode */ }
  });

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

  let befunde = $state<Befund[]>([]);
  let befundeOffen = $state(false);
  async function ladeBefunde(): Promise<void> {
    try {
      befunde = await adminApi.befunde();
    } catch {
      befunde = [];
    }
  }

  onMount(async () => {
    await Promise.all([neuLaden(), ladePfade(), ladeBefunde()]);
  });

  // aufgeklappte Zeile und ihr Reiter
  type AusklappReiter = 'tests' | 'text' | 'hints' | 'start' | 'technik';
  let offenId = $state<string | null>(null);
  let ausklappReiter = $state<AusklappReiter>('tests');
  let offenerPfad = $state<string | null>(null);

  function umschalten(e: VerwaltungsEintrag): void {
    if (offenId === e.id) {
      offenId = null;
      return;
    }
    offenId = e.id;
    ausklappReiter = 'tests';
    void detail_nachladen(e);
  }

  // Slim-Liste initial -- pro Eintrag deutlich kleiner. Detail-Sektionen
  // (beschreibung, tests, hints) werden beim Aufklappen on-demand
  // nachgeladen. Spart bei 300+ Aufgaben mehrere hundert KB beim Start.
  const details_geladen = new Set<string>();

  async function neuLaden(): Promise<void> {
    laden = true;
    fehler = null;
    details_geladen.clear();
    try {
      eintraege = await adminApi.aufgabenSlim();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laden = false;
    }
  }

  async function detail_nachladen(eintrag: VerwaltungsEintrag): Promise<void> {
    if (details_geladen.has(eintrag.id)) return;
    details_geladen.add(eintrag.id);
    try {
      const voll = await adminApi.aufgabe(eintrag.id);
      eintraege = eintraege.map((e) => (e.id === voll.id ? voll : e));
    } catch (e) {
      details_geladen.delete(eintrag.id); // bei Fehler nochmal versuchen
      fehler = (e as Error).message;
    }
  }


  function formatiere(wert: unknown): string {
    return JSON.stringify(wert);
  }

  let gefiltert = $derived(
    eintraege.filter((e) => {
      if (sprache && e.sprache !== sprache) return false;
      if (schwierigkeit && e.schwierigkeit !== schwierigkeit) return false;
      if (pfad === '__ohne__' && e.pfade.length > 0) return false;
      if (pfad && pfad !== '__ohne__' && !e.pfade.includes(pfad)) return false;
      const q = suche.trim().toLowerCase();
      if (q) {
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
        if (!text.includes(q)) return false;
      }
      return true;
    }),
  );

  let filter_aktiv = $derived(
    suche.length > 0 || sprache !== '' || schwierigkeit !== '' || pfad !== '',
  );

  function filterZuruecksetzen(): void {
    suche = '';
    sprache = '';
    schwierigkeit = '';
    pfad = '';
  }

  let pfade_sortiert = $derived(
    [...new Set(eintraege.flatMap((e) => e.pfade))].sort(),
  );

  let aggregat = $derived({
    gesamt: eintraege.length,
    sprachen: new Set(eintraege.map((e) => e.sprache)).size,
    pfade: new Set(eintraege.flatMap((e) => e.pfade)).size,
    submissions: eintraege.reduce((s, e) => s + e.statistik.submissions_gesamt, 0),
    geloest: eintraege.filter((e) => e.statistik.status === 'geloest').length,
  });
</script>

<Seite
  titel="Verwaltung"
  lead={aktiver_tab === 'aufgaben' ? 'Alle eingelesenen Aufgaben mit versteckten Tests, nur hier sichtbar' : 'Pfade: Reihenfolge der Aufgaben'}
  ohneRand
>
  {#snippet aktionen()}
    {#if aktiver_tab === 'aufgaben'}
      <button class="knopf primaer" onclick={neu_oeffnen}><i class="fa-solid fa-plus" aria-hidden="true"></i>Neue Aufgabe</button>
      <button class="knopf" onclick={() => { void neuLaden(); void ladeBefunde(); }} disabled={laden}>
        <i class="fa-solid fa-rotate" aria-hidden="true"></i>{laden ? 'Lade ...' : 'Neu laden'}
      </button>
      <button class="knopf gefahr" onclick={() => (reset_alles_bestaetigung = true)}>
        <i class="fa-solid fa-trash-can" aria-hidden="true"></i>Alles zurücksetzen
      </button>
    {:else}
      <button class="knopf primaer" onclick={pfad_neu}><i class="fa-solid fa-plus" aria-hidden="true"></i>Neuer Pfad</button>
      <button class="knopf" onclick={ladePfade}><i class="fa-solid fa-rotate" aria-hidden="true"></i>Neu laden</button>
    {/if}
  {/snippet}

  {#snippet kopf()}
    <nav class="reiter">
      <button class:aktiv={aktiver_tab === 'aufgaben'} onclick={() => (aktiver_tab = 'aufgaben')}>
        <i class="fa-solid fa-list-check" aria-hidden="true"></i>Aufgaben <span class="num">{eintraege.length}</span>
      </button>
      <button class:aktiv={aktiver_tab === 'pfade'} onclick={() => (aktiver_tab = 'pfade')}>
        <i class="fa-solid fa-route" aria-hidden="true"></i>Pfade <span class="num">{pfade.length}</span>
      </button>
    </nav>
    {#if fehler}
      <p class="hinweis-box fehler"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>{fehler}</p>
    {/if}
    {#if befunde.length > 0}
      <button class="hinweis-box befunde-knopf" onclick={() => (befundeOffen = !befundeOffen)}>
        <i class="fa-solid fa-clipboard-list" aria-hidden="true"></i>
        Bestandsprüfung: {befunde.length} {befunde.length === 1 ? 'Befund' : 'Befunde'}
        <i class="fa-solid {befundeOffen ? 'fa-chevron-up' : 'fa-chevron-down'} rechts" aria-hidden="true"></i>
      </button>
      {#if befundeOffen}
        <ul class="befunde">
          {#each befunde as b, i (i)}<li><code>{b.ort}</code> {b.meldung}</li>{/each}
        </ul>
      {/if}
    {/if}
    {#if aktiver_tab === 'aufgaben'}<CssBestandMessung />{/if}
    {#if aktiver_tab === 'aufgaben' && eintraege.length > 0}
      <div class="kennzahlen">
        <div class="kennzahl"><span class="num">{aggregat.gesamt}</span><small>Aufgaben</small></div>
        <div class="kennzahl"><span class="num">{aggregat.sprachen}</span><small>Sprachen</small></div>
        <div class="kennzahl"><span class="num">{aggregat.pfade}</span><small>Pfade</small></div>
        <div class="kennzahl"><span class="num">{aggregat.submissions}</span><small>Submissions</small></div>
        <div class="kennzahl"><span class="num">{aggregat.geloest}</span><small>gelöst</small></div>
      </div>
      <div class="filter">
        <label class="suche">
          <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
          <input type="text" bind:value={suche} placeholder="Suchen (ID, Titel, Tag, Pfad)" />
        </label>
        <select class="wahl" bind:value={sprache} aria-label="Sprache">
          <option value="">Alle Sprachen</option>
          {#each konfig.daten.sprachen as s (s.id)}<option value={s.id}>{s.titel}</option>{/each}
        </select>
        <select class="wahl" bind:value={schwierigkeit} aria-label="Stufe">
          <option value="">Alle Stufen</option>
          {#each konfig.daten.schwierigkeiten as st (st.id)}<option value={st.id}>{st.titel}</option>{/each}
        </select>
        <select class="wahl" bind:value={pfad} aria-label="Pfad">
          <option value="">Alle Pfade</option>
          <option value="__ohne__">Ohne Pfad</option>
          {#each pfade_sortiert as p (p)}<option value={p}>{p}</option>{/each}
        </select>
        <span class="treffer"><span class="num">{gefiltert.length}</span> Aufgaben</span>
        {#if filter_aktiv}
          <button class="knopf-klein" onclick={filterZuruecksetzen}><i class="fa-solid fa-xmark" aria-hidden="true"></i>Zurücksetzen</button>
        {/if}
      </div>
    {/if}
  {/snippet}

  {#if aktiver_tab === 'aufgaben'}
    {#if laden && eintraege.length === 0}
      <p class="leer-zeile">Lade Aufgaben ...</p>
    {:else if gefiltert.length === 0}
      <p class="leer-zeile">Keine Aufgaben gefunden.</p>
    {:else}
      <div class="tabelle">
        <div class="t-kopf cols">
          <span>Aufgabe</span><span>Stufe</span><span>Sprache</span><span class="rechts-b">Rev</span>
          <span class="rechts-b">Tests</span><span class="rechts-b">Hints</span><span class="rechts-b">Muster</span>
          <span class="rechts-b">Versuche</span><span></span>
        </div>
        {#each gefiltert as e (e.id)}
          {@const auf = offenId === e.id}
          <div
            class="t-zeile cols"
            class:offen={auf}
            role="button"
            tabindex="0"
            aria-expanded={auf}
            onclick={() => umschalten(e)}
            onkeydown={(ev) => { if (ev.key === 'Enter') umschalten(e); }}
          >
            <span class="zelle-titel"><b>{e.titel}</b><span>{e.id}</span></span>
            <span><span class="badge" style:color={farbeZuCss(konfig.schwierigkeitFarbe(e.schwierigkeit))}>{konfig.schwierigkeitTitel(e.schwierigkeit)}</span></span>
            <span><span class="badge sprache">{konfig.sprache(e.sprache)?.titel ?? e.sprache}</span></span>
            <span class="rechts-b num">{e.revision}</span>
            <span class="rechts-b num">{e.tests_sichtbar.length}+{e.tests_versteckt.length}</span>
            <span class="rechts-b num">{e.hints.length}</span>
            <span class="rechts-b num">{e.musterloesungen_anzahl}</span>
            <span class="rechts-b num">{e.statistik.versuche}</span>
            <span class="zeilen-aktionen">
              <button class="ikon" onclick={(ev) => { ev.stopPropagation(); bearbeiten(e); }} aria-label="Bearbeiten"><i class="fa-solid fa-pen" aria-hidden="true"></i></button>
              <button class="ikon" onclick={(ev) => { ev.stopPropagation(); duplizieren(e); }} aria-label="Duplizieren"><i class="fa-solid fa-copy" aria-hidden="true"></i></button>
              <button class="ikon gefahr" onclick={(ev) => { ev.stopPropagation(); loesch_anfordern(e); }} aria-label="Löschen"><i class="fa-solid fa-trash-can" aria-hidden="true"></i></button>
              <button class="ikon" onclick={(ev) => { ev.stopPropagation(); route.setze('aufgabe', e.id); }} aria-label="Öffnen"><i class="fa-solid fa-arrow-right" aria-hidden="true"></i></button>
            </span>
          </div>
          {#if auf}
            <div class="ausklapp">
              <nav>
                <button class:aktiv={ausklappReiter === 'tests'} onclick={() => (ausklappReiter = 'tests')}>Tests <span class="num">{e.tests_sichtbar.length} + {e.tests_versteckt.length}</span></button>
                <button class:aktiv={ausklappReiter === 'text'} onclick={() => (ausklappReiter = 'text')}>Beschreibung</button>
                <button class:aktiv={ausklappReiter === 'hints'} onclick={() => (ausklappReiter = 'hints')}>Hints <span class="num">{e.hints.length}</span></button>
                <button class:aktiv={ausklappReiter === 'start'} onclick={() => (ausklappReiter = 'start')}>Starter-Code</button>
                <button class:aktiv={ausklappReiter === 'technik'} onclick={() => (ausklappReiter = 'technik')}>Technische Daten</button>
              </nav>
              <div class="inhalt">
                {#if !details_geladen.has(e.id) && e.beschreibung_md === ''}
                  <p class="dim">Lade ...</p>
                {:else if ausklappReiter === 'tests'}
                  <table class="testtab">
                    <thead><tr><th>Art</th><th>Eingabe</th><th>Erwartet</th></tr></thead>
                    <tbody>
                      {#each e.tests_sichtbar as t, i (i)}
                        <tr><td class="dim">sichtbar</td><td>{e.funktion ?? ''}({t.input.map(formatiere).join(', ')})</td><td>{formatiere(t.expected)}</td></tr>
                      {/each}
                      {#each e.tests_versteckt as t, i (i)}
                        <tr><td class="warnmarke">versteckt</td><td>{e.funktion ?? ''}({t.input.map(formatiere).join(', ')})</td><td>{formatiere(t.expected)}</td></tr>
                      {/each}
                    </tbody>
                  </table>
                {:else if ausklappReiter === 'text'}
                  <pre class="quelle">{e.beschreibung_md}</pre>
                {:else if ausklappReiter === 'hints'}
                  {#each e.hints as h, i (i)}
                    <p class="hint"><span class="badge">{h.kosten} Punkte</span> {h.text}</p>
                  {:else}
                    <p class="dim">Keine Hinweise.</p>
                  {/each}
                {:else if ausklappReiter === 'start'}
                  <pre class="quelle code">{e.starter_code}</pre>
                {:else}
                  <dl class="technik">
                    <dt>schema_version</dt><dd>{e.schema_version}</dd>
                    <dt>revision</dt><dd>{e.revision}</dd>
                    <dt>task_type</dt><dd><code>{e.task_type}</code></dd>
                    <dt>runner_type</dt><dd><code>{e.runner_type}</code></dd>
                    <dt>funktion</dt><dd><code>{e.funktion ?? '-'}</code></dd>
                    <dt>zeitlimit</dt><dd>{e.zeitlimit_sekunden} s</dd>
                    <dt>tags</dt><dd>{e.tags.join(', ') || '-'}</dd>
                    <dt>pfade</dt><dd>{e.pfade.join(', ') || '-'}</dd>
                    <dt>voraussetzungen</dt><dd>{e.voraussetzungen.join(', ') || '-'}</dd>
                    <dt>lizenz</dt><dd>{e.lizenz}</dd>
                    <dt>autor</dt><dd>{e.autor ?? '-'}</dd>
                    <dt>erstellt_am</dt><dd>{e.erstellt_am ?? '-'}</dd>
                    <dt>quelle</dt><dd>{e.quelle.url ?? '-'} {e.quelle.notiz ?? ''}</dd>
                    <dt>statistik</dt><dd>{e.statistik.submissions_gesamt} Submissions, {e.statistik.bestandene_submissions} bestanden, {e.statistik.punkte_erreicht} / {e.schwierigkeit_score} Punkte, {e.statistik.hints_genutzt} Hints genutzt</dd>
                    <dt>dateipfad</dt><dd><code>{e.dateipfad}</code></dd>
                    <dt>hash</dt><dd><code>{e.hash.slice(0, 12)}</code></dd>
                  </dl>
                {/if}
              </div>
            </div>
          {/if}
        {/each}
      </div>
    {/if}
  {:else}
    {#if pfade.length === 0}
      <p class="leer-zeile">Noch keine Pfade.</p>
    {:else}
      <div class="tabelle">
        <div class="t-kopf cols-pfade">
          <span>Pfad</span><span class="rechts-b">Aufgaben</span><span></span>
        </div>
        {#each pfade as p (p.id)}
          {@const auf = offenerPfad === p.id}
          <div
            class="t-zeile cols-pfade"
            class:offen={auf}
            role="button"
            tabindex="0"
            aria-expanded={auf}
            onclick={() => (offenerPfad = auf ? null : p.id)}
            onkeydown={(ev) => { if (ev.key === 'Enter') offenerPfad = auf ? null : p.id; }}
          >
            <span class="zelle-titel"><b>{p.titel}</b><span>{p.id}</span></span>
            <span class="rechts-b num">{p.aufgaben_anzahl}</span>
            <span class="zeilen-aktionen">
              <button class="ikon" onclick={(ev) => { ev.stopPropagation(); pfad_bearbeiten(p); }} aria-label="Bearbeiten"><i class="fa-solid fa-pen" aria-hidden="true"></i></button>
              <button class="ikon gefahr" onclick={(ev) => { ev.stopPropagation(); pfad_loesch_anfordern(p); }} aria-label="Löschen"><i class="fa-solid fa-trash-can" aria-hidden="true"></i></button>
            </span>
          </div>
          {#if auf}
            <div class="pfad-ausklapp">
              {#if p.beschreibung}<p class="dim">{p.beschreibung}</p>{/if}
              <ol>
                {#each p.reihenfolge as aid (aid)}<li><code>{aid}</code></li>{/each}
              </ol>
            </div>
          {/if}
        {/each}
      </div>
    {/if}
  {/if}
</Seite>

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
    ? `Aufgabe '${loesch_eintrag.id}' (${loesch_eintrag.titel}) wird mit allen Musterlösungen entfernt. Submissions in der Historie bleiben erhalten.`
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
  nachricht="Alle Submissions, Fortschritte, Punkte und der Streak werden komplett gelöscht. Die Aufgaben-Dateien selbst bleiben erhalten, du fängst von vorne an. Dieser Schritt ist nicht umkehrbar."
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
    ? `Pfad '${pfad_loesch_eintrag.id}' (${pfad_loesch_eintrag.titel}) wird entfernt. Aufgaben selbst bleiben erhalten, nur die Zuordnung zum Pfad verschwindet.`
    : ''}
  bestaetigen_text="Löschen"
  abbrechen_text="Abbrechen"
  danger={true}
  onBestaetigen={pfad_loesch_bestaetigt}
  onAbbrechen={() => (pfad_loesch_eintrag = null)}
/>

<style>
  /* feste Spalten wachsen mit der Schrift (--schrift-zoom), damit Kopf und Werte nicht über den Rand ragen */
  .cols {
    --z: var(--schrift-zoom, 1);
    grid-template-columns: minmax(0, 2.4fr) calc(124px * var(--z)) calc(80px * var(--z)) calc(44px * var(--z)) calc(64px * var(--z)) calc(52px * var(--z)) calc(52px * var(--z)) calc(70px * var(--z)) calc(112px * var(--z));
  }
  .cols-pfade {
    grid-template-columns: minmax(0, 1fr) 80px 60px;
  }
  .befunde-knopf {
    width: 100%;
    text-align: left;
    cursor: pointer;
    border-radius: 0;
  }
  .befunde-knopf .rechts { margin-left: auto; }
  .befunde {
    margin: 0;
    padding: var(--sp-2) var(--sp-3) var(--sp-2) var(--sp-5);
    max-height: 160px;
    overflow-y: auto;
    font-size: var(--fs-sm);
    border: 1px solid var(--border);
  }
  .ausklapp {
    display: grid;
    grid-template-columns: 170px minmax(0, 1fr);
    min-height: 220px;
    border-bottom: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    background: var(--bg);
  }
  .ausklapp nav {
    display: flex;
    flex-direction: column;
    gap: 2px;
    padding: var(--sp-2);
    border-right: 1px solid var(--border);
  }
  .ausklapp nav button {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 30px;
    padding: 0 var(--sp-2);
    border: 0;
    border-radius: var(--radius-sm);
    background: transparent;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
    text-align: left;
  }
  .ausklapp nav button:hover:not(:disabled) { background: var(--bg-card-2); color: var(--fg); }
  .ausklapp nav button.aktiv { background: var(--bg-card-2); color: var(--accent); }
  .ausklapp .inhalt {
    min-width: 0;
    padding: var(--sp-3) var(--sp-4);
    max-height: 420px;
    overflow-y: auto;
  }
  .testtab {
    width: 100%;
    border-collapse: collapse;
    font-size: var(--fs-sm);
  }
  .testtab th, .testtab td {
    padding: 5px var(--sp-2);
    border-bottom: 1px solid var(--border);
    text-align: left;
    vertical-align: top;
  }
  .testtab th {
    color: var(--fg-mute);
    font-weight: 500;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .testtab td {
    font-family: var(--mono);
    font-size: 12px;
    overflow-wrap: anywhere;
  }
  .quelle {
    margin: 0;
    font-family: var(--mono);
    font-size: 12px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  .hint {
    margin: 0 0 var(--sp-2);
    font-family: var(--quick);
  }
  .technik {
    display: grid;
    grid-template-columns: 150px minmax(0, 1fr);
    gap: 4px var(--sp-3);
    margin: 0;
    font-size: var(--fs-sm);
  }
  .technik dt { color: var(--fg-mute); font-family: var(--mono); font-size: 12px; }
  .technik dd { margin: 0; overflow-wrap: anywhere; }
  .pfad-ausklapp {
    padding: var(--sp-2) var(--sp-4) var(--sp-3) calc(var(--sp-4) + 3px);
    border-bottom: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    background: var(--bg);
    font-size: var(--fs-sm);
  }
  .pfad-ausklapp p { margin: 0 0 var(--sp-2); }
  .pfad-ausklapp ol {
    margin: 0;
    padding-left: var(--sp-5);
    columns: 3 220px;
  }
</style>
