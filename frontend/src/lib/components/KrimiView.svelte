<script lang="ts">
  /*
   * SQL-Krimi (Spiel): Akte mit Frage und Pinnwand | Abfrage mit
   * Ergebnistabelle | Ermittlung.
   *
   * "Ausführen" zeigt das Ergebnis auf der Tatort-Datenbank und zählt nicht
   * als Versuch. "Prüfen" gibt ab: die Abfrage läuft dann auch auf der
   * Gegenprobe, einer anders befüllten Datenbank, in der dieselbe Frage
   * eine andere Antwort hat. Gelöste Kapitel hängen ihre Notiz an die
   * Pinnwand des Falls.
   *
   * Frontmatter-Felder (im `extra`-Block `krimi`, Antworten und Notiz
   * kommen nie hierher):
   *   dataset, gegenprobe, kapitel, frage, versuche
   */
  import { onMount } from 'svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { spielApi, type Ergebnistabelle, type Notiz } from '../api/SpielApi';
  import { sqlApi, type VorschauTabelle } from '../api/SqlApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { markdownRenderer } from '../markdown/MarkdownRenderer';
  import { fassung } from '../stores/FassungStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { spielStore } from '../stores/SpielStore.svelte';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import HinweisListe from './HinweisListe.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  interface KrimiLevel {
    dataset: string;
    gegenprobe: string;
    kapitel: number;
    frage: string;
    versuche: number;
  }

  /** mehr Zeilen zeigt die Ergebnistabelle nicht an */
  const ZEILEN_HOECHSTENS = 100;

  let { detail }: { detail: AufgabeDetail } = $props();
  let level = $derived(detail.extra?.['krimi'] as KrimiLevel);
  let akte = $derived(markdownRenderer.rendere(detail.beschreibung_md));
  let alsLevel = $derived(spielStore.levelVon(detail.id));
  let letztesKapitel = $derived(
    !!alsLevel?.level.gruppe_groesse && alsLevel.level.nummer_in_gruppe === alsLevel.level.gruppe_groesse,
  );

  type Reiter = 'akte' | 'tabellen' | 'hinweise' | 'loesungen';
  let aktiver_tab = $state<Reiter>('akte');
  let reiter = $derived([
    { id: 'akte' as Reiter, titel: 'Akte', icon: 'fa-folder-open' },
    { id: 'tabellen' as Reiter, titel: 'Tabellen', icon: 'fa-table' },
    ...(detail.hints.length ? [{ id: 'hinweise' as Reiter, titel: 'Hinweise', icon: 'fa-lightbulb' }] : []),
    ...(detail.musterloesungen_anzahl > 0 ? [{ id: 'loesungen' as Reiter, titel: 'Lösung', icon: 'fa-key' }] : []),
  ]);

  let code = $state('');
  let gesicherter_code = $state('');
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let ausfuehren_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);

  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  // --- Akte und Tabellen ---------------------------------------------------
  let pinnwand = $state<Notiz[]>([]);
  let tabellen = $state<VorschauTabelle[] | null>(null);
  let neueNotiz = $derived(ergebnis?.bestanden ? (pinnwand.find((n) => n.kapitel === level.kapitel) ?? null) : null);

  async function ladePinnwand(): Promise<void> {
    try {
      pinnwand = await spielApi.krimiPinnwand(detail.id);
    } catch {
      pinnwand = [];
    }
  }

  $effect(() => {
    if (aktiver_tab !== 'tabellen' || tabellen) return;
    sqlApi.vorschau(level.dataset).then(
      (t) => (tabellen = t),
      (e) => (fehler = (e as Error).message),
    );
  });

  onMount(async () => {
    code = detail.starter_code;
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code && !letzte.bestanden) code = letzte.code;
    } catch {
      // keine vorherige Abgabe
    }
    gesicherter_code = code;
    await ladePinnwand();
  });

  // --- Abfrage -------------------------------------------------------------
  let tabelle = $state<Ergebnistabelle | null>(null);
  let laufzeit = $state<number | null>(null);
  let abfrage_fehler = $state<string | null>(null);

  function zeige(t: Ergebnistabelle | null, ms: number | null, fehlertext: string | null): void {
    tabelle = t;
    laufzeit = ms;
    abfrage_fehler = fehlertext;
  }

  async function ausfuehren(): Promise<void> {
    ausfuehren_laeuft = true;
    fehler = null;
    try {
      const antwort = await spielApi.krimiAusfuehren(detail.id, code);
      zeige(antwort.fehler ? null : antwort.tabelle, antwort.laufzeit_ms, antwort.fehler);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      ausfuehren_laeuft = false;
    }
  }

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    const eingereicht = code;
    try {
      ergebnis = await submissionsApi.submit(detail.id, code);
      gesicherter_code = eingereicht;
      abgaben += 1;
      const tatort = ergebnis.pruefung.sichtbar[0];
      const tatsaechlich = (tatort?.tatsaechlich as Ergebnistabelle | null) ?? null;
      zeige(tatsaechlich, ergebnis.pruefung.laufzeit_ms, tatsaechlich ? null : ergebnis.pruefung.stderr || tatort?.fehler || null);
      if (ergebnis.bestanden) {
        musterloesungen_frei = true;
        await ladePinnwand();
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
      route.setze(v.naechste_id ? 'aufgabe' : 'spiele', v.naechste_id ?? undefined);
    } catch {
      route.setze('spiele');
    }
  }

  function zeilenText(anzahl: number): string {
    return anzahl === 1 ? '1 Zeile' : `${anzahl} Zeilen`;
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet datentabelle(spalten: string[], zeilen: unknown[][])}
  <div class="tabellen-rahmen">
    <table class="daten">
      <thead><tr>{#each spalten as s, i (i)}<th>{s}</th>{/each}</tr></thead>
      <tbody>
        {#each zeilen.slice(0, ZEILEN_HOECHSTENS) as zeile, i (i)}
          <tr>{#each zeile as wert, j (j)}<td class:leer={wert === null}>{wert ?? 'NULL'}</td>{/each}</tr>
        {/each}
      </tbody>
    </table>
  </div>
  {#if zeilen.length > ZEILEN_HOECHSTENS}
    <p class="dim klein">Angezeigt die ersten {ZEILEN_HOECHSTENS} von {zeilen.length} Zeilen.</p>
  {/if}
{/snippet}

<DreiSpaltenLayout
  mitteTitel="Abfrage, Tatort-Datenbank"
  rechtsTitel="Ermittlung"
  schritte={['Akte', 'Abfrage', 'Ermittlung']}
  zumEditor="Zur Abfrage"
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: code.trim() !== '' }}
>
  {#snippet links()}
    <SpaltenReiter {reiter} bind:aktiv={aktiver_tab} />
    <div class="rollfeld">
      {#if aktiver_tab === 'akte'}
        <div class="akte">
          <div class="kapitel">Kapitel {level.kapitel}</div>
          <div class="markdown">{@html akte}</div>
          <div class="frage"><i class="fa-solid fa-circle-question" aria-hidden="true"></i> {level.frage}</div>
          <div class="spickzettel">
            {@render sterne(1)}<span>Antwort eindeutig gefunden, auch in der Gegenprobe</span>
            {@render sterne(2)}<span>ohne Hinweis</span>
            {@render sterne(3)}<span>dazu {level.versuche === 1 ? 'im ersten Prüfversuch' : `in höchstens ${level.versuche} Prüfversuchen`}</span>
          </div>
          {#if pinnwand.length}
            <div class="gruppe">Pinnwand</div>
            <div class="pinnwand">
              {#each pinnwand as n (n.kapitel)}
                <div class="notiz" class:neu={n.kapitel === level.kapitel}><b>Kapitel {n.kapitel}</b>{n.text}</div>
              {/each}
            </div>
          {/if}
        </div>
      {:else if aktiver_tab === 'tabellen'}
        {#if !tabellen}
          <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Tabellen laden ...</p>
        {:else}
          <p class="dim klein">Die ersten Zeilen jeder Tabelle der Tatort-Datenbank.</p>
          {#each tabellen as t (t.name)}
            <div class="gruppe">{t.name} <span class="dim">({zeilenText(t.gesamt_zeilen)})</span></div>
            {@render datentabelle(t.spalten, t.zeilen)}
          {/each}
        {/if}
      {:else if aktiver_tab === 'hinweise'}
        <HinweisListe aufgabeId={detail.id} hints={detail.hints} schwierigkeit_score={detail.schwierigkeit_score} />
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <button class="knopf-klein" onclick={ausfuehren} disabled={ausfuehren_laeuft || pruefen_laeuft || !code.trim()}>
      <i class="fa-solid {ausfuehren_laeuft ? 'fa-spinner fa-spin' : 'fa-play'}" aria-hidden="true"></i>Ausführen
    </button>
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      <EditorBereich sprache="sql" bind:code />
    </div>
    <div class="ergebnis-feld">
      <div class="spalten-kopf">
        <span>Ergebnis</span>
        {#if tabelle}<span class="dim zaehler">{zeilenText(tabelle.zeilen.length)}{laufzeit !== null ? `, ${Math.round(laufzeit)} ms` : ''}</span>{/if}
      </div>
      <div class="ergebnis-innen">
        {#if abfrage_fehler}
          <p class="hinweis-box fehler">{abfrage_fehler}</p>
        {:else if tabelle && tabelle.zeilen.length}
          {@render datentabelle(tabelle.spalten, tabelle.zeilen)}
        {:else if tabelle}
          <p class="dim">Die Abfrage liefert keine Zeile.</p>
        {:else}
          <p class="dim klein">Ausführen zeigt nur das Ergebnis; erst Prüfen zählt als Versuch.</p>
        {/if}
      </div>
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld ermittlung">
      {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
      {#if neueNotiz}
        <div class="neue-notiz"><i class="fa-solid fa-thumbtack" aria-hidden="true"></i>Neue Notiz: <b>{neueNotiz.text}</b></div>
      {/if}
      {#if fehler}<p class="hinweis-box fehler">{fehler}</p>{/if}
      {#if pruefen_laeuft}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Abfrage läuft am Tatort und in der Gegenprobe ...</p>
      {:else if ergebnis}
        {@const p = ergebnis.pruefung}
        {@const tatort = p.sichtbar[0]}
        <div class="test-zeile">
          <i class="fa-solid {tatort?.bestanden ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>Tatort-Datenbank: {tatort?.bestanden ? 'Antwort eindeutig im Ergebnis' : 'Antwort nicht eindeutig'}
        </div>
        <div class="test-zeile">
          <i class="fa-solid {p.versteckt_pass ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>Gegenprobe (andere Befüllung): {p.versteckt_pass ? 'Antwort eindeutig im Ergebnis' : 'Antwort nicht eindeutig'}
        </div>
        {#if tatort?.fehler}
          <p class="dim klein">{tatort.fehler}</p>
        {:else if tatort?.bestanden && !p.versteckt_pass}
          <p class="dim klein">Am Tatort stimmt es, in der Gegenprobe nicht: die Abfrage trifft die Antwort nur zufällig. Frag nach den Bedingungen, nicht nach dem Namen.</p>
        {/if}
        <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
          <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
          {ergebnis.bestanden ? 'Gelöst' : 'Noch nicht gelöst'}
          {#if p.wertung}<span class="kopf-sterne">{@render sterne(p.wertung.sterne)}</span>{/if}
        </div>
        {#if ergebnis.bestanden}
          <button class="knopf primaer" onclick={geheZuNaechster}>
            <i class="fa-solid {letztesKapitel ? 'fa-flag-checkered' : 'fa-book-open'}" aria-hidden="true"></i>{letztesKapitel ? 'Fall abgeschlossen' : `Kapitel ${level.kapitel + 1} aufschlagen`}
          </button>
        {/if}
      {:else}
        <p class="dim klein">Prüfen lässt die Abfrage am Tatort und in der Gegenprobe laufen. In der Gegenprobe hat dieselbe Frage eine andere Antwort; es zählt nur eine Abfrage, die die Frage wirklich beantwortet.</p>
      {/if}
      <VerlaufBereich aufgabeId={detail.id} stand={abgaben} onUebernehmen={(c) => (code = c)} />
    </div>
  {/snippet}
</DreiSpaltenLayout>

<style>
  .editor-host {
    flex: none;
    height: 46%;
    min-height: 140px;
    overflow: hidden;
  }
  .ergebnis-feld {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    border-top: 1px solid var(--border);
    background: var(--bg-card);
  }
  .ergebnis-innen {
    flex: 1;
    min-height: 0;
    overflow-y: auto;
    overflow-x: clip;
    padding: var(--sp-3);
  }
  .zaehler {
    margin-left: auto;
    text-transform: none;
    letter-spacing: 0;
  }
  .tabellen-rahmen {
    max-width: 100%;
    overflow-x: auto;
  }
  .daten td.leer { color: var(--fg-dim); }
  .klein { font-size: var(--fs-sm); }
  .ermittlung {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .neue-notiz {
    display: flex;
    align-items: baseline;
    gap: var(--sp-2);
    font-size: var(--fs-sm);
  }
  .neue-notiz i { color: var(--gold); }
  .kopf-sterne { margin-left: auto; }
  .akte .spickzettel { margin-bottom: var(--sp-3); }
</style>
