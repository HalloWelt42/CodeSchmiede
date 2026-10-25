<script lang="ts">
  /*
   * CSS-Aufgabe: links Aufgabe, Hinweise, Verlauf und Lösung, in der Mitte
   * der Editor mit Zeichenzahl, rechts Ziel über eigenem Ergebnis mit
   * Wertungsleiste (CssVergleich).
   *
   * Gewertet wird nach dem Bild: der Browser rastert Ziel und eigenes
   * Ergebnis und misst die Deckung (css/deckung.ts), schon beim Tippen.
   * Prüfen schickt die Messung ab; Bestehen, Sterne und Punkte (Deckung
   * und Kürze) entscheidet der Server und meldet sie zurück.
   *
   * Frontmatter-Erweiterungen (im `extra`-Block des Detail-Modells):
   *   ziel_html: string                 # gemeinsames Markup
   *   ziel_css:  string                 # erzeugt das Zielbild
   */
  import { onMount } from 'svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { route } from '../stores/RouteStore.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { buehnenDokument } from '../css/buehne';
  import { rastere, vergleiche, type Vergleich } from '../css/deckung';
  import { prozentZahl } from '../spielanzeige';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import CssVergleich from './CssVergleich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import HinweisListe from './HinweisListe.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import EditorBereich from './EditorBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  /** so lange nach dem letzten Tastendruck wird gemessen */
  const MESSEN_NACH_MS = 300;

  let { detail }: { detail: AufgabeDetail } = $props();

  let ziel_html = $derived((detail.extra?.['ziel_html'] as string) ?? '');
  let ziel_css = $derived((detail.extra?.['ziel_css'] as string) ?? '');

  let code = $state('');
  // zählt Abgaben dieser Ansicht; der Verlauf lädt danach neu
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  // Startwert genügt: die Ansicht entsteht je Aufgabe neu ({#key} in der Schale).
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'hinweise' | 'verlauf' | 'loesung'>('aufgabe');
  // kürzeste bestandene eigene Abgabe (Zeichen ohne Leerraum)
  let bestwert = $state<number | null>(null);

  let zeichen = $derived([...code].filter((c) => !/\s/.test(c)).length);
  let gewertet = $derived(ergebnis?.pruefung.wertung ?? null);

  // Code, den der Server schon kennt (Starter, letzte Einreichung oder
  // zuletzt geprüft). Weicht der Editor davon ab oder läuft eine Prüfung,
  // wartet eine neue Fassung mit dem Neuladen.
  let gesicherter_code = $state('');
  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
  });

  // --- Messung -------------------------------------------------------------
  let messung = $state<Vergleich | null>(null);
  let messfehler = $state<string | null>(null);
  let zielBild: Promise<ImageData> | null = null;
  // nur die jüngste Messung zählt, ältere kommen womöglich später an
  let messNummer = 0;

  async function miss(css: string): Promise<Vergleich> {
    zielBild ??= rastere(ziel_html, ziel_css);
    const [ziel, eigen] = await Promise.all([zielBild, rastere(ziel_html, css)]);
    return vergleiche(ziel, eigen);
  }

  $effect(() => {
    const css = code;
    const nummer = ++messNummer;
    const zeit = setTimeout(async () => {
      try {
        const neu = await miss(css);
        if (nummer === messNummer) [messung, messfehler] = [neu, null];
      } catch (e) {
        if (nummer === messNummer) messfehler = (e as Error).message || 'Das Bild ließ sich nicht messen.';
      }
    }, MESSEN_NACH_MS);
    return () => clearTimeout(zeit);
  });

  let deckung = $derived(messung?.deckung ?? null);
  let urteil = $derived.by(() => {
    if (deckung === null) return '';
    if (deckung >= 0.9995) return 'Deckungsgleich';
    if (deckung >= 0.99) return 'Fast deckungsgleich';
    if (deckung >= 0.95) return 'Nah dran';
    if (deckung >= 0.8) return 'Auf dem Weg';
    return 'Noch weit weg';
  });

  onMount(async () => {
    // Default Starter. Vorherige Submission nur laden, wenn der Nutzer
    // noch dran ist (nicht bestanden) -- sonst stuende die alte Loesung
    // im Editor und der Lerneffekt waere weg.
    code = detail.starter_code;
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code && !letzte.bestanden) code = letzte.code;
    } catch {
      // keine vorherige Submission -- bleibt Starter.
    }
    gesicherter_code = code;
    await ladeBestwert();
  });

  async function ladeBestwert(): Promise<void> {
    try {
      const verlauf = await aufgabenApi.submissionsVerlauf(detail.id, 20);
      const laengen = verlauf.filter((v) => v.bestanden && v.codelaenge_zeichen !== null).map((v) => v.codelaenge_zeichen as number);
      bestwert = laengen.length ? Math.min(...laengen) : null;
    } catch {
      bestwert = null;
    }
  }

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    const eingereicht = code;
    try {
      const start = performance.now();
      messung = await miss(eingereicht);
      messfehler = null;
      ergebnis = await submissionsApi.submitLokal(detail.id, eingereicht, {
        deckung: messung.deckung,
        laufzeit_ms: performance.now() - start,
      });
      gesicherter_code = eingereicht;
      abgaben += 1;
      if (ergebnis.bestanden) musterloesungen_frei = true;
      await Promise.all([progressStore.ladeAlles(), ladeBestwert()]);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function geheZuNaechster(): Promise<void> {
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

  let ziel_srcdoc = $derived(buehnenDokument(ziel_html, ziel_css));
  let live_srcdoc = $derived(buehnenDokument(ziel_html, code));

  /** Punkte eines Teils, bezogen auf die Punkte der Aufgabe */
  function punkte(anteil: number): number {
    return Math.round(detail.schwierigkeit_score * anteil);
  }
</script>

<DreiSpaltenLayout
  raster="css"
  mitteTitel="CSS-Editor"
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: code.trim() !== '' }}
>
  {#snippet links()}
    <SpaltenReiter
      reiter={[
        { id: 'aufgabe', titel: 'Aufgabe' },
        { id: 'hinweise', titel: 'Hinweise' },
        { id: 'verlauf', titel: 'Verlauf' },
        { id: 'loesung', titel: 'Lösung' },
      ]}
      bind:aktiv={aktiver_tab}
    />
    <div class="rollfeld ohne-rand">
      {#if aktiver_tab === 'aufgabe'}
        <BeschreibungsBereich
          aufgabeId={detail.id}
          markdown={detail.beschreibung_md}
          hints={[]}
          tests_sichtbar={[]}
          anzahl_versteckt={0}
          quelle={detail.quelle}
          schwierigkeit_score={detail.schwierigkeit_score}
        />
      {:else if aktiver_tab === 'hinweise'}
        <div class="innen">
          {#if detail.hints.length}
            <HinweisListe aufgabeId={detail.id} hints={detail.hints} schwierigkeit_score={detail.schwierigkeit_score} />
          {:else}
            <p class="dim">Zu dieser Aufgabe gibt es keine Hinweise.</p>
          {/if}
        </div>
      {:else if aktiver_tab === 'verlauf'}
        <div class="innen">
          <VerlaufBereich aufgabeId={detail.id} stand={abgaben} anfangsOffen onUebernehmen={(c) => (code = c)} />
        </div>
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <span class="num" title="Zeichen ohne Leerraum">{zeichen} Zeichen</span>
  {/snippet}

  {#snippet mitte()}
    <div class="editor-host">
      <EditorBereich sprache="css" bind:code />
    </div>
  {/snippet}

  {#snippet rechts()}
    <CssVergleich zielSrcdoc={ziel_srcdoc} eigenSrcdoc={live_srcdoc} abweichung={messung?.abweichung ?? null}>
      {#snippet wertung()}
        <div class="wertung-leiste">
          <div class="ring" style:--wert={(deckung ?? 0) * 100}><span>{deckung === null ? '-' : prozentZahl(deckung)}</span></div>
          <div class="wertung-text">
            {#if fehler || messfehler}
              <b class="fehlertext">Messung gescheitert</b><span>{fehler ?? messfehler}</span>
            {:else if deckung === null}
              <b>Wird gemessen</b><span>Deckung mit dem Ziel in Prozent</span>
            {:else}
              <b>{urteil}</b><span>{deckung >= 0.9995 ? 'kein Bildpunkt weicht ab' : `noch ${prozentZahl(1 - deckung)} % Abweichung`}</span>
            {/if}
          </div>
          <div class="wert-kachel"><span class="num">{zeichen}</span><small>Zeichen</small></div>
          <div class="wert-kachel"><span class="num gedimmt">{bestwert ?? '-'}</span><small>Bestwert</small></div>
        </div>
        {#if gewertet && gewertet.teile.length === 2}
          {@const [deckungsteil, kuerze] = gewertet.teile}
          <div class="punkte-teile" title="Punkte des letzten Prüfens, bezogen auf die Punkte der Aufgabe">
            <span><span class="num">{punkte(deckungsteil.anteil)}</span> / {punkte(deckungsteil.moeglich)} {deckungsteil.text}</span>
            <span class="balken"><span style:width="{(deckungsteil.anteil / deckungsteil.moeglich) * 100}%"></span></span>
            <span><span class="num">{punkte(kuerze.anteil)}</span> / {punkte(kuerze.moeglich)} {kuerze.text}{#if kuerze.bedingung} <span class="dim">{kuerze.bedingung}</span>{/if}</span>
            <span class="sterne" title="{gewertet.sterne} von 3 Sternen">
              {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > gewertet.sterne} aria-hidden="true"></i>{/each}
            </span>
          </div>
          <div class="spickzettel">
            {#each gewertet.kriterien as k, i (i)}
              <i class="fa-solid {k.erreicht ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i><span>{i + 1}. Stern: {k.text}</span>
            {/each}
          </div>
        {/if}
        {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
        {#if ergebnis?.bestanden}
          <button class="knopf primaer weiter" onclick={geheZuNaechster}>
            <i class="fa-solid fa-forward" aria-hidden="true"></i>Nächste Aufgabe
          </button>
        {/if}
      {/snippet}
    </CssVergleich>
  {/snippet}
</DreiSpaltenLayout>

<style>
  .innen { padding: var(--sp-3); }
  .editor-host {
    flex: 1;
    min-height: 0;
    overflow: hidden;
  }
  .fehlertext { color: var(--red); }
  .weiter { align-self: flex-start; }
  .spickzettel .ok { color: var(--green); }
  .spickzettel .nein { color: var(--fg-dim); }
</style>
