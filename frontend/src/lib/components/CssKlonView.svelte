<script lang="ts">
  /*
   * CssKlonView -- 3-Spalten-Layout fuer CSS-Klon-Aufgaben.
   *
   *   Beschreibung + Ziel-Vorschau | CSS-Editor | Live-Vorschau + Asserts
   *
   * Bewertung erfolgt clientseitig durch IframeCssRunner (Computed-Style-
   * Vergleich). Submission wird per /submissions/lokal gespeichert.
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
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { iframeCssRunner } from '../sandbox/IframeCssRunner';
  import type { CssAssert, CssAssertErgebnis } from '../sandbox/IframeCssRunner';
  import type { AufgabeDetail, Musterloesung } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import EditorBereich from './EditorBereich.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  let ziel_html = $derived((detail.extra?.['ziel_html'] as string) ?? '');
  let ziel_css = $derived((detail.extra?.['ziel_css'] as string) ?? '');
  let asserts = $derived<CssAssert[]>(
    (detail.extra?.['asserts'] as CssAssert[]) ?? [],
  );

  let code = $state('');
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let assert_ergebnisse = $state<CssAssertErgebnis[]>([]);
  let fehler = $state<string | null>(null);
  let musterloesungen = $state<Musterloesung[] | null>(null);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');

  onMount(async () => {
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      code = letzte.code ?? detail.starter_code;
    } catch {
      code = detail.starter_code;
    }
  });

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
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
      if (ergebnis.bestanden && !musterloesungen) {
        musterloesungen = await aufgabenStore.ladeMusterloesungen(detail.id);
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
      const v = await (await import('../api/ProgressApi')).progressApi.weiter(detail.id);
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

<DreiSpaltenLayout>
{#snippet links()}
    <div class="tab-leiste" role="tablist">
      <button
        class="tab"
        class:aktiv={aktiver_tab === 'aufgabe'}
        role="tab"
        onclick={() => (aktiver_tab = 'aufgabe')}
      >
        <i class="fa-solid fa-file-lines" aria-hidden="true"></i>
        Aufgabe
      </button>
      {#if musterloesungen && musterloesungen.length > 0}
        <button
          class="tab"
          class:aktiv={aktiver_tab === 'loesungen'}
          role="tab"
          onclick={() => (aktiver_tab = 'loesungen')}
        >
          <i class="fa-solid fa-lightbulb" aria-hidden="true"></i>
          Musterlösungen ({musterloesungen.length})
        </button>
      {/if}
    </div>
    <div class="tab-inhalt">
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
        <div class="ziel-block">
          <div class="ziel-titel">Ziel-Design</div>
          <iframe class="ziel-frame" title="Ziel-Design" sandbox="allow-same-origin" srcdoc={ziel_srcdoc}></iframe>
        </div>
      {:else if musterloesungen}
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
      <span class="label">CSS-Editor</span>
      <button class="pruefen" disabled={pruefen_laeuft || !code.trim()} onclick={pruefen}>
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
      <EditorBereich sprache="css" bind:code />
    </div>
{/snippet}

{#snippet rechts()}
    <div class="vorschau-kopf">
      <span class="label">Deine Lösung</span>
    </div>
    <iframe class="live-frame" title="Live-Vorschau" sandbox="allow-same-origin" srcdoc={live_srcdoc}></iframe>

    <div class="ergebnis-block">
      {#if fehler}
        <div class="fehler">{fehler}</div>
      {:else if ergebnis}
        <div class="status" class:gut={ergebnis.bestanden} class:schlecht={!ergebnis.bestanden}>
          {#if ergebnis.bestanden}
            <i class="fa-solid fa-check" aria-hidden="true"></i> Bestanden
            <button class="weiter" onclick={geheZuNaechster}>
              Weiter <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
            </button>
          {:else}
            <i class="fa-solid fa-xmark" aria-hidden="true"></i> Noch nicht bestanden
          {/if}
        </div>
        <ul class="asserts">
          {#each assert_ergebnisse as a (a.index)}
            <li class:bestanden={a.bestanden}>
              <span class="symbol">
                <i class="fa-solid {a.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
              </span>
              <span class="sel"><code>{a.selector}</code> · <em>{a.property}</em></span>
              {#if !a.bestanden}
                <span class="diff">erwartet <code>{a.expected}</code>, ist <code>{a.tatsaechlich}</code></span>
              {/if}
            </li>
          {/each}
        </ul>
      {:else}
        <div class="hinweis">Schreibe CSS und drück <strong>Prüfen</strong>.</div>
      {/if}
    </div>
{/snippet}
</DreiSpaltenLayout>

<style>
  .tab-leiste {
    display: flex;
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
  .tab.aktiv { color: var(--accent); border-bottom-color: var(--accent); }
  .tab-inhalt {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }

  .ziel-block { padding: var(--sp-3); border-top: 1px dashed var(--border); }
  .ziel-titel {
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent);
    margin-bottom: var(--sp-2);
  }
  .ziel-frame {
    width: 100%;
    height: 260px;
    border: 1px solid var(--border);
    background: var(--bg);
  }

  .editor-kopf, .vorschau-kopf {
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
  .pruefen:disabled { opacity: 0.5; cursor: not-allowed; }
  .editor-host { flex: 1 1 auto; min-height: 0; overflow: hidden; }

  .live-frame {
    width: 100%;
    height: 320px;
    border: none;
    background: var(--bg);
    flex-shrink: 0;
  }

  .ergebnis-block {
    padding: var(--sp-3);
    overflow-y: auto;
    flex: 1 1 auto;
    min-height: 0;
  }
  .fehler { color: var(--red); }
  .status {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    margin-bottom: var(--sp-3);
    font-weight: 600;
  }
  .status.gut { color: var(--green); border-color: var(--green); }
  .status.schlecht { color: var(--red); border-color: var(--red); }
  .weiter {
    margin-left: auto;
    background: color-mix(in srgb, var(--green) 14%, transparent);
    border: 1px solid var(--green);
    color: var(--green);
    padding: 6px 12px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: var(--fs-xs);
    font-weight: 600;
  }
  .asserts { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 4px; }
  .asserts li {
    display: grid;
    grid-template-columns: 24px 1fr;
    gap: var(--sp-2);
    padding: 6px var(--sp-2);
    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--red);
    font-size: var(--fs-xs);
  }
  .asserts li.bestanden { color: var(--green); border-color: color-mix(in srgb, var(--green) 35%, var(--border)); }
  .asserts li .symbol { text-align: center; }
  .asserts li .diff {
    grid-column: 2;
    color: var(--fg-dim);
    font-family: var(--mono);
  }
  .asserts li code {
    font-family: var(--mono);
    background: var(--bg-card);
    padding: 1px 4px;
    border-radius: 2px;
  }
  .hinweis { color: var(--fg-dim); }

  .muster-liste {
    padding: var(--sp-3);
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
  }
  .muster-eintrag pre {
    margin: var(--sp-2) 0 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    overflow-x: auto;
    border-radius: var(--radius-sm);
    max-height: 280px;
    overflow-y: auto;
  }
</style>
