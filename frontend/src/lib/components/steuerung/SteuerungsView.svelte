<script lang="ts" generics="A extends AnsichtBasis, W extends WiedergabeBasis, K">
  /*
   * Gemeinsame Ansicht der Steuerungsspiele: Aufgabe mit Teilschritten und Hilfe | Programm | Welt mit
   * abspielbarem Ablauf, Ablaufplan, Kennzahlen und Abläufen.
   *
   * "Ablauf" probiert das Programm in den sichtbaren Abläufen, "Prüfen" gibt ab und läuft zusätzlich in den
   * versteckten. Was geschieht, rechnet der Server nach; hier wird nur abgespielt. Misslingt ein versteckter Ablauf,
   * lässt er sich ab kurz vor der ersten Stelle abspielen. Gibt es hier noch kein Programm, beginnt das Level mit dem
   * bestandenen Programm des Levels, auf dem es aufbaut.
   *
   * Jedes Spiel bringt mit: wie es Ansicht und Probelauf holt, die Hilfe (Sensoren, Befehle, Sterne), die Szene,
   * den Ablaufplan, die Kennzahlen und die Klänge je Bild. Wer kein Python schreibt (Turingmaschine), bringt auch
   * seinen Editor mit; der bekommt den Code zum Lesen und Schreiben und das gezeigte Bild.
   */
  import { onDestroy, onMount, type Snippet } from 'svelte';
  import { aufgabenApi } from '../../api/AufgabenApi';
  import { progressApi } from '../../api/ProgressApi';
  import { submissionsApi } from '../../api/SubmissionsApi';
  import { Abspieler, TEMPI } from '../../steuerung/abspieler.svelte';
  import { klang } from '../../steuerung/klang.svelte';
  import { fassung } from '../../stores/FassungStore.svelte';
  import { progressStore } from '../../stores/ProgressStore.svelte';
  import { route } from '../../stores/RouteStore.svelte';
  import type { AufgabeDetail } from '../../types/Aufgabe';
  import type { AnsichtBasis, Auswertung, CodeZugriff, Laeufe, WiedergabeBasis } from '../../types/Steuerung';
  import type { SubmissionAntwort } from '../../types/Submission';
  import BeschreibungsBereich from '../BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from '../DreiSpaltenLayout.svelte';
  import EditorBereich from '../EditorBereich.svelte';
  import MusterloesungenBereich from '../MusterloesungenBereich.svelte';
  import SpaltenReiter from '../SpaltenReiter.svelte';
  import VerlaufBereich from '../VerlaufBereich.svelte';
  import BelohnungsBand from '../spiel/BelohnungsBand.svelte';
  import Teilschritte from './Teilschritte.svelte';

  // Sekunden je Bild der Aufzeichnung, wenn das Spiel nichts anderes sagt
  const DT = 0.25;

  interface Props {
    detail: AufgabeDetail;
    /** Name der Welt: "Anlage", "Haus" */
    welt: string;
    /** Symbol des Knopfs "Ablauf" */
    symbol: string;
    planTitel: string;
    ladeAnsicht: (aufgabeId: string) => Promise<A>;
    probieren: (aufgabeId: string, code: string) => Promise<Laeufe<W, K>>;
    /** Klänge zu einem Bild der Wiedergabe (nur, wenn der Ton an ist) */
    tonZuBild?: (ansicht: A, wiedergabe: W, nr: number) => void;
    /** ob ein misslungener Ablauf einen Unfall hatte (eigenes Symbol) */
    mitUnfall?: (kennzahlen: K) => boolean;
    hilfe: Snippet<[A]>;
    szene: Snippet<[A, W | null, number, (sekunde: number) => void]>;
    plan?: Snippet<[A, W | null, number, number, (sekunde: number) => void]>;
    kennzahlen: Snippet<[A, W]>;
    /** eigener Editor statt Python; bekommt den Code, die Wiedergabe und das gezeigte Bild */
    editor?: Snippet<[A, CodeZugriff, W | null, number, (sekunde: number) => void]>;
    /** Titel der mittleren Spalte; ab Werk "Programm, n Zeichen" */
    mitteTitel?: (code: string) => string;
    /** Anzeige der Zeit; ab Werk Minuten und Sekunden */
    zeitText?: (zeit: number, dauer: number) => string;
    /** Sekunden je Bild beim Abspielen in 1-fach */
    takt?: number;
    /** Hinweis neben dem Titel des Ablaufplans */
    planHinweis?: string;
    /** ohne Abspielen (Schaltungen): keine Leiste, das Bild ist eine Auswahl */
    abspielen?: boolean;
    /** jede Änderung am Code rechnet sofort neu (Spiele ohne Sandbox); die gezeigte Stelle bleibt dabei stehen */
    live?: boolean;
    /** Anzeige der ersten falschen Stelle an einem Ablauf; ab Werk Minuten und Sekunden */
    stelleText?: (stelle: number) => string;
  }
  let {
    detail, welt, symbol, planTitel, ladeAnsicht, probieren, tonZuBild, mitUnfall, hilfe, szene, plan, kennzahlen,
    editor, mitteTitel, zeitText, takt = DT, planHinweis = 'Klick springt zur Sekunde', abspielen = true, live = false,
    stelleText,
  }: Props = $props();

  let ansicht = $state<A | null>(null);
  let code = $state('');
  let gesicherter_code = $state('');
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let probe_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let auswertung = $state<Auswertung<W, K> | null>(null);
  let fehler = $state<string | null>(null);
  let ausgabe = $state('');
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');
  let gewaehlt = $state<string | null>(null);

  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  // Zeichen wie beim Prüfen ungefähr: ohne Leerraum und ohne Kommentare
  let zeichen = $derived(code.split('\n').map((z) => z.replace(/#.*$/, '')).join('').replace(/\s/g, '').length);
  const zugriff: CodeZugriff = {
    get code() {
      return code;
    },
    set code(neu: string) {
      code = neu;
    },
  };

  let wiedergabe = $derived<W | null>(
    auswertung?.wiedergaben.find((w) => w.name === gewaehlt) ?? auswertung?.wiedergaben[0] ?? null,
  );
  let dauer = $derived(wiedergabe?.dauer ?? ansicht?.dauer ?? 60);

  // svelte-ignore state_referenced_locally
  const abspieler = new Abspieler(takt, (nr) => {
    if (klang.an && ansicht && wiedergabe && nr >= 0) tonZuBild?.(ansicht, wiedergabe, nr);
  });
  onDestroy(() => abspieler.anhalten());
  let zeit = $derived(wiedergabe && abspieler.bild >= 0 ? wiedergabe.bilder[abspieler.bild][0] : 0);

  /** Das letzte Bild, das bis zu dieser Zeit gezeigt wird (-1 vor dem ersten). */
  function bildBei(w: W, sekunde: number): number {
    let nr = -1;
    while (nr + 1 < w.bilder.length && w.bilder[nr + 1][0] <= sekunde + 1e-6) nr += 1;
    return nr;
  }

  function zeige(name: string | null, ab = 0): void {
    gewaehlt = name;
    const w = auswertung?.wiedergaben.find((x) => x.name === name) ?? auswertung?.wiedergaben[0];
    if (!w) return;
    abspieler.laden(w.bilder.length, ab > 0 ? bildBei(w, ab) : -1);
    abspieler.abspielen();
  }

  function springe(sekunde: number): void {
    if (wiedergabe) abspieler.springe(bildBei(wiedergabe, sekunde));
  }

  function neueAuswertung(neu: Auswertung<W, K> | null): void {
    auswertung = neu;
    if (!abspielen || live) {
      // die Auswahl bleibt stehen, solange es sie noch gibt
      const n = (neu?.wiedergaben.find((w) => w.name === gewaehlt) ?? neu?.wiedergaben[0])?.bilder.length ?? 0;
      abspieler.laden(n, n ? Math.min(Math.max(abspieler.bild, 0), n - 1) : -1);
      return;
    }
    if (neu) zeige(neu.wiedergaben[0]?.name ?? null);
    else abspieler.laden(0);
  }

  // Spiele ohne Sandbox rechnen bei jeder Änderung neu, kurz nach dem letzten Tastendruck
  $effect(() => {
    if (!live || !ansicht) return;
    void code;
    const uhr = setTimeout(() => probelauf(), 350);
    return () => clearTimeout(uhr);
  });

  /** Eigenes letztes Programm, sonst das bestandene des Levels davor, sonst der Startcode. */
  async function anfangscode(aufbauend_auf: string | null): Promise<string> {
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code) return letzte.bestanden ? detail.starter_code : letzte.code;
      if (aufbauend_auf) {
        const vorher = await aufgabenApi.letzteSubmission(aufbauend_auf);
        if (vorher.code && vorher.bestanden) return vorher.code;
      }
    } catch {
      // ohne frühere Abgaben gilt der Startcode
    }
    return detail.starter_code;
  }

  onMount(async () => {
    try {
      ansicht = await ladeAnsicht(detail.id);
    } catch (e) {
      fehler = (e as Error).message;
    }
    code = await anfangscode(ansicht?.aufbauend_auf ?? null);
    gesicherter_code = code;
  });

  async function probelauf(): Promise<void> {
    probe_laeuft = true;
    fehler = null;
    try {
      const antwort = await probieren(detail.id, code);
      ausgabe = antwort.stdout;
      if (!antwort.auswertung) {
        fehler = antwort.timeout ? 'Zeit abgelaufen: das Programm endete nicht.' : antwort.stderr || 'Das Programm lief nicht bis zum Ende.';
      }
      neueAuswertung(antwort.auswertung);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      probe_laeuft = false;
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
      ausgabe = ergebnis.pruefung.stdout;
      if (ergebnis.bestanden) musterloesungen_frei = true;
      const neu = (ergebnis.pruefung.sichtbar[0]?.tatsaechlich as Auswertung<W, K> | null) ?? null;
      if (!neu) fehler = ergebnis.pruefung.stderr || 'Das Programm lief nicht bis zum Ende.';
      neueAuswertung(neu);
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

  function uhr(s: number): string {
    return `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  }

  let ausgewaehlterStand = $derived(auswertung?.ablaeufe.find((a) => a.name === (wiedergabe?.name ?? '')) ?? null);
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

<DreiSpaltenLayout
  mitteTitel={mitteTitel ? mitteTitel(code) : `Programm, ${zeichen} Zeichen`}
  rechtsTitel={welt}
  schritte={['Aufgabe', 'Programm', welt]}
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: code.trim() !== '' }}
>
  {#snippet links()}
    {#if detail.musterloesungen_anzahl > 0}
      <SpaltenReiter
        reiter={[
          { id: 'aufgabe', titel: 'Aufgabe', icon: 'fa-file-lines' },
          { id: 'loesungen', titel: 'Musterlösung', icon: 'fa-lightbulb' },
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
        {#if ansicht}
          <div class="zusatz">
            <div class="gruppe">Teilschritte</div>
            <Teilschritte vorgaben={ansicht.teilschritte} staende={auswertung?.teilschritte ?? null} />
            {@render hilfe(ansicht)}
          </div>
        {/if}
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    {#if !live}
      <button class="knopf-klein" onclick={probelauf} disabled={probe_laeuft || pruefen_laeuft || !code.trim()}>
        <i class="fa-solid {probe_laeuft ? 'fa-spinner fa-spin' : symbol}" aria-hidden="true"></i>Ablauf
      </button>
    {/if}
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      {#if editor && ansicht}
        {@render editor(ansicht, zugriff, wiedergabe, abspieler.bild, springe)}
      {:else}
        <EditorBereich sprache="python" bind:code />
      {/if}
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld welt-rahmen">
      {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
      {#if abspielen}<div class="ablauf-leiste">
        <button class="knopf-klein" onclick={() => abspieler.abspielen()} disabled={!wiedergabe || abspieler.laeuft}>
          <i class="fa-solid fa-play" aria-hidden="true"></i>Abspielen
        </button>
        <button class="knopf-klein" onclick={() => abspieler.anhalten()} disabled={!abspieler.laeuft}>
          <i class="fa-solid fa-pause" aria-hidden="true"></i>Anhalten
        </button>
        <button class="knopf-klein" onclick={() => abspieler.springe(-1)} disabled={!wiedergabe}>
          <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Von vorn
        </button>
        {#if tonZuBild}
          <button class="knopf-klein" class:aktiv={klang.an} onclick={() => klang.umschalten()} title="Klänge beim Abspielen">
            <i class="fa-solid {klang.an ? 'fa-volume-high' : 'fa-volume-xmark'}" aria-hidden="true"></i>Ton {klang.an ? 'an' : 'aus'}
          </button>
        {/if}
        <select
          class="wahl tempo"
          value={abspieler.tempo}
          onchange={(e) => abspieler.setzeTempo(+(e.currentTarget as HTMLSelectElement).value)}
          aria-label="Tempo"
        >
          {#each TEMPI as t (t)}<option value={t}>{t}-fach</option>{/each}
        </select>
        <span class="num zeit">{zeitText ? zeitText(zeit, dauer) : `${uhr(zeit)} / ${uhr(dauer)}`}</span>
      </div>{/if}

      {#if ansicht}
        {@render szene(ansicht, wiedergabe, abspieler.bild, springe)}
        {#if plan}
          <div class="gruppe">
            {planTitel}{#if wiedergabe}<span class="dim klein">{wiedergabe.name}, {planHinweis}</span>{/if}
          </div>
          {@render plan(ansicht, wiedergabe, dauer, zeit, springe)}
        {/if}
      {:else if !fehler}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> {welt} wird geladen ...</p>
      {/if}

      {#if ansicht && wiedergabe}{@render kennzahlen(ansicht, wiedergabe)}{/if}

      {#if auswertung}
        <div class="ablaeufe">
          {#each auswertung.ablaeufe as a (a.name)}
            {@const abspielbar = auswertung.wiedergaben.some((w) => w.name === a.name)}
            {#if abspielbar}
              <button
                class="chip"
                class:ok={a.ok}
                class:nein={!a.ok}
                class:gewaehlt={wiedergabe?.name === a.name}
                onclick={() => zeige(a.name, Math.max(0, (a.erste_stelle ?? 0) - 8))}
                title={a.ok ? 'abspielen' : 'ab kurz vor der ersten Stelle abspielen'}
              >
                <i class="fa-solid {a.ok ? 'fa-check' : mitUnfall?.(a.kennzahlen) ? 'fa-car-burst' : 'fa-xmark'}" aria-hidden="true"></i>
                {a.name}{#if !a.ok && a.erste_stelle != null}, {(stelleText ?? uhr)(a.erste_stelle)}{/if}
              </button>
            {:else}
              <span class="chip" class:ok={a.ok} class:nein={!a.ok}>
                <i class="fa-solid {a.ok ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>{a.name}
              </span>
            {/if}
          {/each}
        </div>
        {#if ausgewaehlterStand?.erster_befund}
          <p class="befund">{ausgewaehlterStand.erster_befund}</p>
        {/if}
      {/if}

      {#if fehler}<p class="hinweis-box fehler">{fehler}</p>{/if}
      {#if wiedergabe?.fehler}<p class="hinweis-box fehler">{wiedergabe.fehler}</p>{/if}
      {#if ergebnis && !pruefen_laeuft}
        {@const p = ergebnis.pruefung}
        <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
          <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
          {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
          {#if p.wertung}<span class="kopf-sterne">{@render sterne(p.wertung.sterne)}</span>{/if}
        </div>
        {#if ergebnis.bestanden}
          <button class="knopf primaer" onclick={geheZuNaechster}><i class="fa-solid fa-forward" aria-hidden="true"></i>Nächstes Level</button>
        {/if}
      {:else if pruefen_laeuft}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Programm läuft in allen Abläufen ...</p>
      {/if}
      {#if ausgabe}
        <div class="gruppe">Ausgabe</div>
        <pre class="ausgabe">{ausgabe}</pre>
      {/if}
      <VerlaufBereich aufgabeId={detail.id} stand={abgaben} onUebernehmen={(c) => (code = c)} />
    </div>
  {/snippet}
</DreiSpaltenLayout>

<style>
  .zusatz { padding: 0 var(--sp-4) var(--sp-4); }
  .editor-host {
    flex: 1;
    min-height: 0;
    overflow: hidden;
  }
  .welt-rahmen {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .tempo { height: 26px; }
  .zeit {
    margin-left: auto;
    font-size: var(--fs-sm);
  }
  .klein {
    font-size: var(--fs-xs);
    text-transform: none;
    letter-spacing: 0;
  }
  .befund {
    margin: 0;
    font-size: var(--fs-sm);
    color: var(--red);
  }
  .kopf-sterne { margin-left: auto; }
  .knopf-klein.aktiv { color: var(--accent); border-color: var(--accent); }
  .ausgabe {
    margin: 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
    white-space: pre-wrap;
    max-height: 140px;
    overflow-y: auto;
  }
</style>
