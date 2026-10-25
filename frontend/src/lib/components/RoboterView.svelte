<script lang="ts">
  /*
   * Roboter-Parcours (Spiel): Aufgabe mit Befehlen und Sternen | Programm |
   * Welt mit abspielbarem Lauf.
   *
   * "Lauf" probiert das Programm in der sichtbaren Welt, "Prüfen" gibt ab
   * und läuft zusätzlich in den versteckten Welten. Den Weg rechnet der
   * Server nach; hier wird er nur abgespielt, die ausführende Zeile ist im
   * Editor markiert.
   *
   * Frontmatter-Felder (im `extra`-Block `roboter`):
   *   welt:    sichtbare Welt als Text (# Wand, . frei, Z Ziel, K Kristall, >^<v Start)
   *   sterne:  {schritte, zeichen}
   */
  import { onDestroy, onMount } from 'svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { spielApi, type RoboterLauf } from '../api/SpielApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { fassung } from '../stores/FassungStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  interface RoboterLevel {
    welt: string;
    sterne: { schritte: number; zeichen: number };
  }

  const BEFEHLE = ['gehe()', 'links()', 'rechts()', 'nimm()', 'wand_vorne()', 'kristall()', 'am_ziel()'];
  // Blickrichtung als Drehung des Symbols: Osten, Norden, Westen, Süden
  const DREHUNG = [0, -90, 180, 90];
  const TEMPI = [
    { ms: 450, text: 'langsam' },
    { ms: 250, text: 'normal' },
    { ms: 90, text: 'schnell' },
  ];

  let { detail }: { detail: AufgabeDetail } = $props();
  let level = $derived(detail.extra?.['roboter'] as RoboterLevel);
  let karte = $derived(level.welt.trim().split('\n').map((z) => z.trim()));
  let breite = $derived(karte[0].length);
  let hoehe = $derived(karte.length);
  let start = $derived.by(() => {
    for (let y = 0; y < hoehe; y++) {
      for (let x = 0; x < breite; x++) {
        const r = '>^<v'.indexOf(karte[y][x]);
        if (r >= 0) return { x, y, richtung: r };
      }
    }
    return { x: 0, y: 0, richtung: 0 };
  });

  let code = $state('');
  let gesicherter_code = $state('');
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let probe_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  let ausgabe = $state('');
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  // Zeichen wie beim Prüfen ungefähr: ohne Leerraum und ohne Kommentare
  let zeichen = $derived(code.split('\n').map((z) => z.replace(/#.*$/, '')).join('').replace(/\s/g, '').length);

  // --- Abspielen ---------------------------------------------------------
  let lauf = $state<RoboterLauf | null>(null);
  let schritt = $state(0);
  let tempo = $state(250);
  let takt: ReturnType<typeof setInterval> | undefined;
  onDestroy(() => clearInterval(takt));

  let lage = $derived(schritt > 0 && lauf ? lauf.schritte[schritt - 1] : { ...start, zeile: 0 });
  let spur = $derived(new Set(lauf ? [`${start.x},${start.y}`, ...lauf.schritte.slice(0, schritt).map((s) => `${s.x},${s.y}`)] : []));
  let genommen = $derived(
    new Set(lauf ? lauf.schritte.slice(0, schritt).filter((s) => s.befehl === 'nimm').map((s) => `${s.x},${s.y}`) : []),
  );
  let fertig = $derived(lauf !== null && schritt >= lauf.schritte.length);
  let abgestuerzt = $derived(fertig && lauf?.fehler != null && lauf.fehler.includes('Wand'));
  let markierteZeile = $derived(schritt > 0 && lauf ? lauf.schritte[schritt - 1].zeile || null : null);

  let stand = $derived.by(() => {
    if (!lauf) return 'Lauf zeigt den Weg in der sichtbaren Welt, Prüfen läuft auch in den versteckten.';
    if (!fertig) return `Schritt ${schritt} von ${lauf.schritte.length}`;
    if (lauf.fehler) return lauf.fehler;
    if (lauf.geschafft) return `Am Ziel nach ${lauf.schritte.length} Schritten${genommen.size ? ', Kristalle genommen' : ''}.`;
    if (lauf.am_ziel) return `Am Ziel, aber ${lauf.kristalle_offen === 1 ? 'ein Kristall liegt' : `${lauf.kristalle_offen} Kristalle liegen`} noch.`;
    return 'Das Programm ist zu Ende, der Roboter steht nicht im Ziel.';
  });

  function weiter(): boolean {
    if (!lauf || schritt >= lauf.schritte.length) return false;
    schritt += 1;
    return schritt < lauf.schritte.length;
  }

  function abspielen(): void {
    clearInterval(takt);
    if (fertig) schritt = 0;
    takt = setInterval(() => {
      if (!weiter()) clearInterval(takt);
    }, tempo);
  }

  function zeigeLauf(neu: RoboterLauf | null): void {
    clearInterval(takt);
    lauf = neu;
    schritt = 0;
    if (neu) abspielen();
  }

  onMount(async () => {
    code = detail.starter_code;
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code && !letzte.bestanden) code = letzte.code;
    } catch {
      // keine vorherige Abgabe
    }
    gesicherter_code = code;
  });

  async function probieren(): Promise<void> {
    probe_laeuft = true;
    fehler = null;
    try {
      const antwort = await spielApi.roboterLauf(detail.id, code);
      ausgabe = antwort.stdout;
      if (!antwort.laeufe) {
        fehler = antwort.timeout ? 'Zeit abgelaufen: das Programm endete nicht.' : antwort.stderr || 'Das Programm lief nicht bis zum Ende.';
      }
      zeigeLauf(antwort.laeufe?.[0] ?? null);
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
      zeigeLauf((ergebnis.pruefung.sichtbar[0]?.tatsaechlich as RoboterLauf | null) ?? null);
      if (!ergebnis.pruefung.sichtbar[0]?.tatsaechlich) fehler = ergebnis.pruefung.stderr || 'Das Programm lief nicht bis zum Ende.';
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
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

<DreiSpaltenLayout
  mitteTitel="Programm, {zeichen} Zeichen"
  rechtsTitel="Welt"
  schritte={['Aufgabe', 'Programm', 'Welt']}
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
        <div class="zusatz">
          <div class="gruppe">Befehle</div>
          <div class="befehle">{#each BEFEHLE as b (b)}<code>{b}</code>{/each}</div>
          <div class="gruppe">Sterne</div>
          <div class="spickzettel">
            {@render sterne(1)}<span>Ziel erreicht, Kristalle genommen, in allen Welten</span>
            {@render sterne(2)}<span>höchstens {level.sterne.schritte} Schritte in der sichtbaren Welt</span>
            {@render sterne(3)}<span>dazu höchstens {level.sterne.zeichen} Zeichen Code (Kommentare zählen nicht)</span>
          </div>
        </div>
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <button class="knopf-klein" onclick={probieren} disabled={probe_laeuft || pruefen_laeuft || !code.trim()}>
      <i class="fa-solid {probe_laeuft ? 'fa-spinner fa-spin' : 'fa-person-walking'}" aria-hidden="true"></i>Lauf
    </button>
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      <EditorBereich sprache="python" bind:code {markierteZeile} />
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld welt-rahmen">
      {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
      <div class="ablauf">
        <button class="knopf-klein" onclick={abspielen} disabled={!lauf}><i class="fa-solid fa-play" aria-hidden="true"></i>Abspielen</button>
        <button class="knopf-klein" onclick={() => { clearInterval(takt); weiter(); }} disabled={!lauf || fertig}><i class="fa-solid fa-forward-step" aria-hidden="true"></i>Schritt</button>
        <button class="knopf-klein" onclick={() => { clearInterval(takt); schritt = 0; }} disabled={!lauf}><i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Von vorn</button>
        <select class="wahl tempo" bind:value={tempo} aria-label="Tempo">
          {#each TEMPI as t (t.ms)}<option value={t.ms}>{t.text}</option>{/each}
        </select>
      </div>
      <div
        class="welt"
        style:--zellen={breite}
        style:aspect-ratio="{breite} / {hoehe}"
        style:width="min(100%, calc((100vh - 360px) * {breite} / {hoehe}))"
      >
        {#each karte as zeile, y (y)}
          {#each zeile.split('') as z, x (x)}
            {@const k = `${x},${y}`}
            <div class="zelle" class:wand={z === '#'} class:spur={spur.has(k)}>
              {#if z === 'Z'}<div class="ziel"></div>{/if}
              {#if z === 'K' && !genommen.has(k)}<div class="kristall"></div>{/if}
            </div>
          {/each}
        {/each}
        <div class="roboter" class:crash={abgestuerzt} style:left="{(lage.x * 100) / breite}%" style:top="{(lage.y * 100) / hoehe}%">
          <i class="fa-solid fa-robot" style:transform="rotate({DREHUNG[lage.richtung]}deg)" aria-hidden="true"></i>
        </div>
      </div>
      <p class="dim stand" class:fehlertext={fertig && !!lauf?.fehler}>{stand}</p>

      {#if fehler}<p class="hinweis-box fehler">{fehler}</p>{/if}
      {#if ergebnis && !pruefen_laeuft}
        {@const p = ergebnis.pruefung}
        <div class="welten">
          <span class="chip" class:ok={p.sichtbar[0]?.bestanden} class:nein={!p.sichtbar[0]?.bestanden}>
            <i class="fa-solid {p.sichtbar[0]?.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>sichtbare Welt
          </span>
          {#each { length: p.versteckt_pass } as _, i (i)}
            <span class="chip ok"><i class="fa-solid fa-check" aria-hidden="true"></i>versteckt</span>
          {/each}
          {#each { length: p.versteckt_fail } as _, i (i)}
            <span class="chip nein"><i class="fa-solid fa-xmark" aria-hidden="true"></i>versteckt</span>
          {/each}
        </div>
        <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
          <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
          {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
          {#if p.wertung}<span class="kopf-sterne">{@render sterne(p.wertung.sterne)}</span>{/if}
        </div>
        {#if ergebnis.bestanden}
          <button class="knopf primaer" onclick={geheZuNaechster}><i class="fa-solid fa-forward" aria-hidden="true"></i>Nächstes Level</button>
        {/if}
      {:else if pruefen_laeuft}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Programm läuft in allen Welten ...</p>
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
  .welt { align-self: center; }
  .tempo {
    height: 26px;
    margin-left: auto;
  }
  .stand {
    margin: 0;
    font-size: var(--fs-sm);
  }
  .fehlertext { color: var(--red); }
  .kopf-sterne { margin-left: auto; }
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
