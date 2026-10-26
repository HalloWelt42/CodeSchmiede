<script lang="ts">
  /*
   * Ampelschule (Steuerungsspiel): Aufgabe mit Teilschritten, Sensoren und Sternen | Programm | Anlage mit
   * abspielbarem Ablauf, Signalplan, Kennzahlen und Abläufen.
   *
   * "Ablauf" probiert das Programm im sichtbaren Ablauf, "Prüfen" gibt ab und läuft zusätzlich in den versteckten.
   * Verkehr, Unfälle und Wartezeiten rechnet der Server nach; hier wird nur abgespielt. Misslingt ein versteckter
   * Ablauf, lässt er sich ab kurz vor der ersten Stelle abspielen.
   *
   * Was vom Level gebraucht wird (Teilschritte, Sensoren, Sterne), kommt geprüft mit der Anlage. Gibt es hier noch
   * kein Programm, beginnt das Level mit dem bestandenen Programm des Levels, auf dem es aufbaut.
   */
  import { onDestroy, onMount } from 'svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { spielApi } from '../api/SpielApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { Abspieler, TEMPI } from '../steuerung/abspieler.svelte';
  import { klang } from '../steuerung/klang.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import type { AmpelAnsicht, AmpelAuswertung, Wiedergabe } from '../types/Ampel';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';
  import AmpelSzene from './steuerung/AmpelSzene.svelte';
  import Signalplan from './steuerung/Signalplan.svelte';
  import Teilschritte from './steuerung/Teilschritte.svelte';

  const DT = 0.25;
  // Sensoren in lage, wie die Level-Datei sie nennt
  const SENSOREN: Record<string, [string, string]> = {
    taster: ['lage.taster["fuss"]', 'jemand wartet am Überweg dieser Gruppe; lage.taster allein: irgendwo'],
    schleife: ['lage.schleife["ns"]', 'ein Fahrzeug steht auf der Kontaktschleife vor der Haltlinie'],
    wartend: ['lage.wartend["ns"]', 'wie viele dort vor Rot warten'],
    frei: ['lage.frei["fuss"]', 'niemand Fremdes mehr auf den Flächen, die diese Gruppe kreuzt'],
    einsatz: ['lage.einsatz', 'Gruppe eines angemeldeten Einsatzfahrzeugs, sonst None'],
    nacht: ['lage.nacht', 'es ist Nacht'],
    stoerung: ['lage.stoerung', 'Gruppe mit gestörter Kontaktschleife, sonst None'],
  };
  const SIGNALE = { auto: '"gruen", "gelb", "rot", "rotgelb"', fuss: '"gruen", "rot"' };

  let { detail }: { detail: AufgabeDetail } = $props();

  let ansicht = $state<AmpelAnsicht | null>(null);
  let nachts = $derived(!!ansicht?.sensoren.includes('nacht'));
  let mitFuss = $derived(!!ansicht?.anlage.gruppen.some((g) => g.art === 'fuss'));
  let code = $state('');
  let gesicherter_code = $state('');
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let probe_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let auswertung = $state<AmpelAuswertung | null>(null);
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

  let wiedergabe = $derived<Wiedergabe | null>(
    auswertung?.wiedergaben.find((w) => w.name === gewaehlt) ?? auswertung?.wiedergaben[0] ?? null,
  );
  let dauer = $derived(wiedergabe?.dauer ?? ansicht?.dauer ?? 60);

  // --- Abspielen mit Ton ---------------------------------------------------
  const abspieler = new Abspieler(DT, tonZuBild);
  onDestroy(() => abspieler.anhalten());
  let zeit = $derived(wiedergabe && abspieler.bild >= 0 ? wiedergabe.bilder[abspieler.bild][0] : 0);

  function tonZuBild(nr: number): void {
    const w = wiedergabe;
    if (!w || !klang.an || nr < 0) return;
    const [t, jetzt] = w.bilder[nr];
    const vorher = new Set((w.bilder[nr - 1]?.[1] ?? []).map(([id]) => id));
    const arten = new Map(w.teilnehmer.map((x) => [x.id, x.art]));
    if (jetzt.some(([id]) => !vorher.has(id) && arten.get(id) === 'fuss')) klang.spiele('taster');
    for (const u of w.unfaelle) {
      if (u.t > t - DT && u.t <= t) klang.spiele(u.art === 'fuss' ? 'matsch' : 'blechschaden');
    }
    if (Math.abs(t - Math.round(t)) < 1e-6) {
      const s = Math.round(t);
      const signale = w.signale[s];
      if (!signale) return;
      const gruppen = ansicht?.anlage.gruppen ?? [];
      if (gruppen.some((g) => g.art === 'fuss' && signale[g.name] === 'gruen')) klang.spiele('ticken');
      if (gruppen.some((g) => g.art === 'auto' && signale[g.name] === 'gruen' && w.signale[s - 1]?.[g.name] !== 'gruen')) {
        klang.spiele('motor');
      }
    }
  }

  function zeige(name: string | null, ab = 0): void {
    gewaehlt = name;
    const w = auswertung?.wiedergaben.find((x) => x.name === name) ?? auswertung?.wiedergaben[0];
    if (!w) return;
    abspieler.laden(w.bilder.length, Math.round(ab / DT) - 1);
    abspieler.abspielen();
  }

  function neueAuswertung(neu: AmpelAuswertung | null): void {
    auswertung = neu;
    if (neu) zeige(neu.wiedergaben[0]?.name ?? null);
    else abspieler.laden(0);
  }

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
      ansicht = await spielApi.ampelAnlage(detail.id);
    } catch (e) {
      fehler = (e as Error).message;
    }
    code = await anfangscode(ansicht?.aufbauend_auf ?? null);
    gesicherter_code = code;
  });

  async function probieren(): Promise<void> {
    probe_laeuft = true;
    fehler = null;
    try {
      const antwort = await spielApi.ampelLauf(detail.id, code);
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
      const neu = (ergebnis.pruefung.sichtbar[0]?.tatsaechlich as AmpelAuswertung | null) ?? null;
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
  mitteTitel="Programm, {zeichen} Zeichen"
  rechtsTitel="Anlage"
  schritte={['Aufgabe', 'Programm', 'Anlage']}
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
          {@const s = ansicht.sterne}
          <div class="zusatz">
            <div class="gruppe">Teilschritte</div>
            <Teilschritte vorgaben={ansicht.teilschritte} staende={auswertung?.teilschritte ?? null} />
            <div class="gruppe">Sensoren</div>
            <div class="spickzettel">
              <code>takt(lage)</code><span>läuft jede Sekunde und gibt das Signal je Gruppe zurück</span>
              <code>lage.sekunde</code><span>Zeit seit dem Start</span>
              {#each ansicht.sensoren as sensor (sensor)}
                {#if SENSOREN[sensor]}<code>{SENSOREN[sensor][0]}</code><span>{SENSOREN[sensor][1]}</span>{/if}
              {/each}
            </div>
            <div class="gruppe">Signale</div>
            <div class="spickzettel">
              {#each ansicht.anlage.gruppen as g (g.name)}
                <code>"{g.name}"</code>
                <span>{g.text}: {g.art === 'auto' && nachts ? `${SIGNALE.auto}, "gelb_blinkt"` : g.art === 'fuss' && nachts ? `${SIGNALE.fuss}, "aus"` : SIGNALE[g.art]}</span>
              {/each}
            </div>
            <div class="gruppe">Sterne</div>
            <div class="spickzettel">
              {@render sterne(1)}<span>alle Teilschritte, kein Unfall, kein Verstoß, in allen Abläufen</span>
              {@render sterne(2)}<span>
                {[
                  s.fuss != null ? `Fußgänger warten höchstens ${s.fuss} s` : null,
                  s.autos != null ? `Fahrzeuge im Mittel höchstens ${String(s.autos).replace('.', ',')} s` : null,
                ].filter(Boolean).join(', ')} (erster sichtbarer Ablauf)
              </span>
              {@render sterne(3)}<span>dazu höchstens {s.zeichen} Zeichen Code (Kommentare zählen nicht)</span>
            </div>
          </div>
        {/if}
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <button class="knopf-klein" onclick={probieren} disabled={probe_laeuft || pruefen_laeuft || !code.trim()}>
      <i class="fa-solid {probe_laeuft ? 'fa-spinner fa-spin' : 'fa-traffic-light'}" aria-hidden="true"></i>Ablauf
    </button>
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      <EditorBereich sprache="python" bind:code />
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld anlage-rahmen">
      {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
      <div class="ablauf-leiste">
        <button class="knopf-klein" onclick={() => abspieler.abspielen()} disabled={!wiedergabe || abspieler.laeuft}>
          <i class="fa-solid fa-play" aria-hidden="true"></i>Abspielen
        </button>
        <button class="knopf-klein" onclick={() => abspieler.anhalten()} disabled={!abspieler.laeuft}>
          <i class="fa-solid fa-pause" aria-hidden="true"></i>Anhalten
        </button>
        <button class="knopf-klein" onclick={() => abspieler.springe(-1)} disabled={!wiedergabe}>
          <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Von vorn
        </button>
        <button class="knopf-klein" class:aktiv={klang.an} onclick={() => klang.umschalten()} title="Klänge beim Abspielen">
          <i class="fa-solid {klang.an ? 'fa-volume-high' : 'fa-volume-xmark'}" aria-hidden="true"></i>Ton {klang.an ? 'an' : 'aus'}
        </button>
        <select
          class="wahl tempo"
          value={abspieler.tempo}
          onchange={(e) => abspieler.setzeTempo(+(e.currentTarget as HTMLSelectElement).value)}
          aria-label="Tempo"
        >
          {#each TEMPI as t (t)}<option value={t}>{t}-fach</option>{/each}
        </select>
        <span class="num zeit">{uhr(zeit)} / {uhr(dauer)}</span>
      </div>

      {#if ansicht}
        <AmpelSzene {ansicht} {wiedergabe} bild={abspieler.bild} />
        <div class="gruppe">
          Signalplan{#if wiedergabe}<span class="dim klein">{wiedergabe.name}, Klick springt zur Sekunde</span>{/if}
        </div>
        <Signalplan
          gruppen={ansicht.anlage.gruppen}
          {wiedergabe}
          {dauer}
          {zeit}
          onSpringe={(s) => abspieler.springe(Math.round(s / DT) - 1)}
        />
      {:else if !fehler}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Anlage wird geladen ...</p>
      {/if}

      {#if wiedergabe}
        {@const k = wiedergabe.kennzahlen}
        <div class="sim-werte" style:grid-template-columns="repeat({mitFuss ? 4 : 3}, minmax(0, 1fr))">
          <div><span class="num" class:gut={k.unfaelle === 0} class:schlecht={k.unfaelle > 0}>{k.unfaelle}</span><small>Unfälle</small></div>
          <div><span class="num" class:gut={k.verstoesse === 0} class:schlecht={k.verstoesse > 0}>{k.verstoesse}</span><small>Verstöße</small></div>
          {#if mitFuss}
            <div>
              <span class="num" class:gut={ansicht?.sterne.fuss != null && k.fuss_max <= ansicht.sterne.fuss}>{Math.round(k.fuss_max)} s</span>
              <small>Fußgänger max.</small>
            </div>
          {/if}
          <div>
            <span class="num" class:gut={ansicht?.sterne.autos != null && k.autos_mittel <= ansicht.sterne.autos}>
              {k.autos_mittel.toFixed(1).replace('.', ',')} s
            </span>
            <small>Fahrzeuge im Mittel</small>
          </div>
        </div>
      {/if}

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
                <i class="fa-solid {a.ok ? 'fa-check' : a.kennzahlen.unfaelle ? 'fa-car-burst' : 'fa-xmark'}" aria-hidden="true"></i>
                {a.name}{#if !a.ok && a.erste_stelle != null}, {uhr(a.erste_stelle)}{/if}
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
  .anlage-rahmen {
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
