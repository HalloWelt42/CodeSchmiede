<script lang="ts">
  /*
   * CSS-Aufgabe: links Aufgabe, Hinweise, Verlauf und Lösung, in der Mitte
   * der Editor mit Zeichenzahl, rechts Ziel über eigenem Ergebnis mit
   * Wertungsleiste (CssVergleich).
   *
   * Geprüft wird im Browser durch den IframeCssRunner (berechnete Stile
   * an den Prüfpunkten der Aufgabe); die Abgabe speichert
   * /submissions/lokal. Die Wertungsleiste zeigt den Anteil erfüllter
   * Prüfpunkte, die Zeichenzahl ohne Leerraum und den eigenen Bestwert.
   *
   * Frontmatter-Erweiterungen (im `extra`-Block des Detail-Modells):
   *   ziel_html: string                 # gemeinsames Markup
   *   ziel_css:  string                 # erzeugt das visuelle Ziel
   *   asserts:   list[CssAssert]        # bewertet das Ergebnis
   */
  import { onMount } from 'svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { route } from '../stores/RouteStore.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { iframeCssRunner } from '../sandbox/IframeCssRunner';
  import type { CssAssert, CssAssertErgebnis } from '../sandbox/IframeCssRunner';
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

  let { detail }: { detail: AufgabeDetail } = $props();

  let ziel_html = $derived((detail.extra?.['ziel_html'] as string) ?? '');
  let ziel_css = $derived((detail.extra?.['ziel_css'] as string) ?? '');
  let asserts = $derived<CssAssert[]>(
    (detail.extra?.['asserts'] as CssAssert[]) ?? [],
  );

  let code = $state('');
  // zählt Abgaben dieser Ansicht; der Verlauf lädt danach neu
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let assert_ergebnisse = $state<CssAssertErgebnis[]>([]);
  let fehler = $state<string | null>(null);
  // Startwert genügt: die Ansicht entsteht je Aufgabe neu ({#key} in der Schale).
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'hinweise' | 'verlauf' | 'loesung'>('aufgabe');
  // kürzeste bestandene eigene Abgabe (Zeichen ohne Leerraum)
  let bestwert = $state<number | null>(null);

  let zeichen = $derived([...code].filter((c) => !/\s/.test(c)).length);
  let erfuellt = $derived(assert_ergebnisse.filter((a) => a.bestanden).length);
  let prozent = $derived(assert_ergebnisse.length ? (erfuellt / assert_ergebnisse.length) * 100 : null);

  // Code, den der Server schon kennt (Starter, letzte Einreichung oder
  // zuletzt geprüft). Weicht der Editor davon ab oder läuft eine Prüfung,
  // wartet eine neue Fassung mit dem Neuladen.
  let gesicherter_code = $state('');
  $effect(() => {
    if (pruefen_laeuft || code !== gesicherter_code) return fassung.halten();
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
      const lauf = await iframeCssRunner.run(ziel_html, code, asserts);
      assert_ergebnisse = lauf.sichtbar;
      const pruefung = {
        bestanden: lauf.bestanden,
        sichtbar: lauf.sichtbar.map((s) => ({
          index: s.index,
          bestanden: s.bestanden,
          eingabe: [s.selector, s.property],
          erwartet: s.expected,
          tatsaechlich: s.tatsaechlich,
          fehler: s.fehler,
        })),
        versteckt_pass: 0,
        versteckt_fail: 0,
        laufzeit_ms: lauf.laufzeit_ms,
        stdout: '',
        stderr: '',
        timeout: false,
      };
      ergebnis = await submissionsApi.submitLokal(detail.id, code, pruefung);
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

  let ziel_srcdoc = $derived(buildSrcdoc(ziel_html, ziel_css));
  let live_srcdoc = $derived(buildSrcdoc(ziel_html, code));

  function buildSrcdoc(html: string, css: string): string {
    return `<!doctype html><html><head><meta charset="utf-8"><style>
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; background: #1a1d23; color: #e7ecf1; padding: 12px; }
${css}
</style></head><body>${html}</body></html>`;
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
    <CssVergleich zielSrcdoc={ziel_srcdoc} eigenSrcdoc={live_srcdoc}>
      {#snippet wertung()}
        <div class="wertung-leiste">
          <div class="ring" style:--wert={prozent ?? 0}><span>{prozent === null ? '-' : Math.round(prozent)}</span></div>
          <div class="wertung-text">
            {#if fehler}
              <b class="fehlertext">Prüfung gescheitert</b><span>{fehler}</span>
            {:else if prozent === null}
              <b>Noch nicht geprüft</b><span>{asserts.length} Prüfpunkte</span>
            {:else if erfuellt === assert_ergebnisse.length}
              <b>Alle Prüfpunkte erfüllt</b><span>{ergebnis?.bestanden ? `+${ergebnis.progress.punkte_erreicht} Punkte` : ''}</span>
            {:else}
              <b>{erfuellt} von {assert_ergebnisse.length} erfüllt</b><span>noch {assert_ergebnisse.length - erfuellt} offen</span>
            {/if}
          </div>
          <div class="wert-kachel"><span class="num">{zeichen}</span><small>Zeichen</small></div>
          <div class="wert-kachel"><span class="num gedimmt">{bestwert ?? '-'}</span><small>Bestwert</small></div>
        </div>
        {#if ergebnis?.bestanden}
          <button class="knopf primaer weiter" onclick={geheZuNaechster}>
            <i class="fa-solid fa-forward" aria-hidden="true"></i>Nächste Aufgabe
          </button>
        {/if}
        {#if assert_ergebnisse.some((a) => !a.bestanden)}
          <div class="pruefpunkte">
            {#each assert_ergebnisse.filter((a) => !a.bestanden) as a (a.index)}
              <div class="test-zeile">
                <i class="fa-solid fa-xmark nein" aria-hidden="true"></i>
                <span class="punkt">{a.selector} {a.property}: {a.tatsaechlich} <span class="fehlertext">statt {a.expected}</span></span>
              </div>
            {/each}
          </div>
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
  .wertung-leiste {
    display: grid;
    grid-template-columns: auto minmax(0, 1fr) auto auto;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg-card);
  }
  .ring {
    position: relative;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: conic-gradient(var(--accent) calc(var(--wert) * 1%), var(--bg-card-2) 0);
    display: grid;
    place-items: center;
  }
  .ring::before {
    content: "";
    position: absolute;
    inset: 6px;
    border-radius: 50%;
    background: var(--bg-card);
  }
  .ring span {
    position: relative;
    font-family: var(--num);
    font-weight: 700;
    font-size: 15px;
  }
  .wertung-text {
    min-width: 0;
    font-size: var(--fs-sm);
    line-height: 1.3;
    hyphens: auto;
    overflow-wrap: anywhere;
  }
  .wertung-text b { display: block; font-size: var(--fs-md); }
  .wertung-text span { color: var(--fg-dim); }
  .wert-kachel { text-align: right; }
  .wert-kachel .num { display: block; font-size: var(--fs-lg); }
  .wert-kachel .gedimmt { color: var(--fg-dim); }
  .wert-kachel small {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .weiter { align-self: flex-start; }
  .pruefpunkte { min-width: 0; }
  .punkt { min-width: 0; overflow-wrap: anywhere; }
</style>
