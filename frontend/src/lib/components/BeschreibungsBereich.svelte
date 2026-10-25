<script lang="ts">
  /*
   * Linke Spalte der Aufgaben-Detail-Ansicht.
   * Markdown-Beschreibung (mit KaTeX und Mermaid), darunter sichtbare
   * Tests, gestaffelte Hinweise (HinweisListe) und die Quelle.
   */
  import { onMount, tick } from 'svelte';
  import { markdownRenderer } from '../markdown/MarkdownRenderer';
  import HinweisListe from './HinweisListe.svelte';
  import type { Hint, Quelle, TestFall } from '../types/Aufgabe';

  interface Props {
    aufgabeId: string;
    markdown: string;
    hints: Hint[];
    tests_sichtbar: TestFall[];
    anzahl_versteckt: number;
    quelle: Quelle;
    schwierigkeit_score: number;
    /** Programm-Aufgabe: Tests sind Eingabezeilen und erwartete Ausgabe */
    programm?: boolean;
  }

  let { aufgabeId, markdown, hints, tests_sichtbar, anzahl_versteckt, quelle, schwierigkeit_score, programm = false }: Props = $props();

  let html = $state('');
  let host: HTMLDivElement | undefined = $state();

  $effect(() => {
    html = markdownRenderer.rendere(markdown);
    tick().then(() => {
      if (host) markdownRenderer.rendereMermaids(host);
    });
  });

  function formatiereTest(t: TestFall): string {
    const args = t.input.map((x) => JSON.stringify(x)).join(', ');
    return `f(${args}) = ${JSON.stringify(t.expected)}`;
  }

</script>

<div class="beschreibungs-bereich">
  <div class="markdown" bind:this={host}>
    {@html html}
  </div>

  {#if tests_sichtbar.length > 0}
    <section class="abschnitt">
      <details>
        <summary>
          <h3>Sichtbare Tests &middot; {tests_sichtbar.length}</h3>
          <i class="fa-solid fa-chevron-down summary-chevron" aria-hidden="true"></i>
        </summary>
        <ul class="tests">
          {#each tests_sichtbar as t, i (i)}
            {#if programm}
              <li class="programm-test">
                {#if t.input.length}<span class="etikett">Eingabe</span><pre>{t.input.join('\n')}</pre>{/if}
                <span class="etikett">Erwartete Ausgabe</span><pre>{String(t.expected).replace(/\n$/, '')}</pre>
              </li>
            {:else}
              <li><code>{formatiereTest(t)}</code></li>
            {/if}
          {/each}
        </ul>
        {#if anzahl_versteckt > 0}
          <p class="hinweis">
            Dazu {anzahl_versteckt} versteckte
            {anzahl_versteckt === 1 ? 'Prüfung' : 'Prüfungen'}; zurück kommt nur, wie viele bestanden sind.
          </p>
        {/if}
      </details>
    </section>
  {/if}

  {#if hints.length > 0}
    <section class="abschnitt">
      <HinweisListe {aufgabeId} {hints} {schwierigkeit_score} />
    </section>
  {/if}

  {#if quelle.url || quelle.notiz}
    <section class="abschnitt fuss">
      <h3>Quelle</h3>
      {#if quelle.url}
        <p><a href={quelle.url} target="_blank" rel="noopener noreferrer">{quelle.url}</a></p>
      {/if}
      {#if quelle.notiz}
        <p class="dim">{quelle.notiz}</p>
      {/if}
    </section>
  {/if}
</div>

<style>
  .beschreibungs-bereich {
    padding: var(--sp-3);
    font-family: var(--quick);
    font-size: var(--fs-md);
    line-height: 1.55;
    color: var(--fg);
  }
  /* Der Titel steht schon im Kopf der Aufgabe */
  .markdown > :global(h1:first-child) { display: none; }
  .markdown :global(h1) {
    font-family: var(--sans);
    font-size: var(--fs-xl);
    font-weight: 600;
    margin: 0 0 var(--sp-3);
    color: var(--fg);
  }
  .markdown :global(h2) {
    font-family: var(--sans);
    font-size: var(--fs-lg);
    font-weight: 600;
    margin: var(--sp-3) 0 var(--sp-1);
    color: var(--fg);
  }
  .markdown :global(h3) {
    font-family: var(--sans);
    font-size: var(--fs-md);
    font-weight: 600;
    margin: var(--sp-3) 0 var(--sp-2);
    color: var(--fg);
  }
  .markdown :global(p) { margin: 0 0 var(--sp-2); }
  .markdown :global(ul), .markdown :global(ol) { margin: 0 0 var(--sp-3); padding-left: var(--sp-4); }
  .markdown :global(li) { margin: var(--sp-1) 0; }
  .markdown :global(code) {
    font-family: var(--mono);
    font-size: 0.92em;
    background: var(--bg);
    padding: 1px 6px;
    border: 1px solid var(--border);
    border-radius: 4px;
    color: var(--accent);
  }
  .markdown :global(pre) {
    background: var(--bg);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    margin: 0 0 var(--sp-3);
    overflow-x: auto;
    font-family: var(--mono);
    font-size: var(--fs-sm);
  }
  .markdown :global(pre code) { background: transparent; border: none; padding: 0; color: var(--fg); font-size: inherit; }
  .markdown :global(blockquote) {
    margin: 0 0 var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: var(--bg-card-2);
    color: var(--fg-dim);
    border-left: 3px solid var(--accent);
  }
  .markdown :global(table) { border-collapse: collapse; margin: 0 0 var(--sp-3); font-family: var(--sans); font-size: var(--fs-sm); }
  .markdown :global(th), .markdown :global(td) { padding: var(--sp-1) var(--sp-3); border: 1px solid var(--border); text-align: left; }
  .markdown :global(th) { background: var(--bg-card-2); font-weight: 600; }
  .markdown :global(.mermaid) { margin: var(--sp-3) 0; text-align: center; }
  .markdown :global(.katex-display) { margin: var(--sp-3) 0; overflow-x: auto; }
  .markdown :global(a) { color: var(--accent); text-decoration: underline; }

  .abschnitt { margin-top: var(--sp-3); padding-top: var(--sp-3); border-top: 1px solid var(--border); }
  .abschnitt.fuss { margin-top: var(--sp-4); color: var(--fg-dim); font-size: var(--fs-sm); }
  h3 {
    font-family: var(--sans);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    margin: 0 0 var(--sp-2);
  }

  details summary {
    list-style: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  details summary::-webkit-details-marker {
    display: none;
  }
  details summary h3 {
    margin: 0;
  }
  .summary-chevron {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    transition: transform 0.15s;
  }
  details[open] .summary-chevron {
    transform: rotate(180deg);
    color: var(--accent);
  }
  details > *:not(summary) {
    margin-top: var(--sp-2);
  }
  .tests {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
  }
  .tests code {
    font-family: var(--mono);
    font-size: var(--fs-sm);
    background: var(--bg);
    padding: 4px var(--sp-2);
    border: 1px solid var(--border);
    color: var(--fg);
    display: inline-block;
  }
  .hinweis {
    margin: var(--sp-2) 0 0;
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    font-style: italic;
  }

  .dim { color: var(--fg-dim); }
  .programm-test { display: flex; flex-direction: column; gap: 4px; }
  .programm-test .etikett { font-size: var(--fs-xs); text-transform: uppercase; letter-spacing: .05em; color: var(--fg-mute); }
  .programm-test pre { margin: 0; padding: var(--sp-2) var(--sp-3); background: var(--bg); border: 1px solid var(--border); font-family: var(--mono); font-size: 13px; white-space: pre-wrap; }
</style>
