<script lang="ts">
  /*
   * Linke Spalte der Aufgaben-Detail-Ansicht.
   * Rendert die Aufgabenbeschreibung als Markdown (mit KaTeX und
   * Mermaid), zeigt darunter die sichtbaren Tests, gestaffelte Hints
   * und die Quellen-/Lizenz-Info.
   */
  import { onMount, tick } from 'svelte';
  import { markdownRenderer } from '../markdown/MarkdownRenderer';
  import type { Hint, Quelle, TestFall } from '../types/Aufgabe';

  interface Props {
    markdown: string;
    hints: Hint[];
    tests_sichtbar: TestFall[];
    anzahl_versteckt: number;
    quelle: Quelle;
  }

  let { markdown, hints, tests_sichtbar, anzahl_versteckt, quelle }: Props = $props();

  let hintsOffen = $state<Set<number>>(new Set());
  let html = $state('');
  let host: HTMLDivElement | undefined = $state();

  $effect(() => {
    html = markdownRenderer.rendere(markdown);
    tick().then(() => {
      if (host) markdownRenderer.rendereMermaids(host);
    });
  });

  function toggleHint(i: number): void {
    const neu = new Set(hintsOffen);
    if (neu.has(i)) neu.delete(i);
    else neu.add(i);
    hintsOffen = neu;
  }

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
    <section class="block">
      <h3>Sichtbare Tests</h3>
      <ul class="tests">
        {#each tests_sichtbar as t, i (i)}
          <li><code>{formatiereTest(t)}</code></li>
        {/each}
      </ul>
      {#if anzahl_versteckt > 0}
        <p class="hinweis">
          Plus {anzahl_versteckt} verstecke
          {anzahl_versteckt === 1 ? 'Prüfung' : 'Prüfungen'} -- nur die Anzahl
          des Erfolgs wird zurückgemeldet.
        </p>
      {/if}
    </section>
  {/if}

  {#if hints.length > 0}
    <section class="block">
      <h3>Hinweise</h3>
      <ol class="hints">
        {#each hints as hint, i (i)}
          <li>
            <button
              class="hint-toggle"
              onclick={() => toggleHint(i)}
              class:offen={hintsOffen.has(i)}
            >
              <i class="fa-solid {hintsOffen.has(i) ? 'fa-eye' : 'fa-eye-slash'}" aria-hidden="true"></i>
              Hinweis {i + 1}
              {#if hint.kosten > 0}
                <span class="kosten">-{hint.kosten} Punkte</span>
              {:else}
                <span class="kosten frei">kostenlos</span>
              {/if}
            </button>
            {#if hintsOffen.has(i)}
              <div class="hint-text">
                {@html markdownRenderer.rendere(hint.text)}
              </div>
            {/if}
          </li>
        {/each}
      </ol>
    </section>
  {/if}

  {#if quelle.url || quelle.notiz}
    <section class="block fuss">
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
    padding: var(--sp-4);
    font-family: var(--quick);
    font-size: var(--fs-md);
    line-height: 1.65;
    color: var(--fg);
  }
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
    margin: var(--sp-4) 0 var(--sp-2);
    color: var(--fg);
  }
  .markdown :global(h3) {
    font-family: var(--sans);
    font-size: var(--fs-md);
    font-weight: 600;
    margin: var(--sp-3) 0 var(--sp-2);
    color: var(--fg);
  }
  .markdown :global(p) {
    margin: 0 0 var(--sp-3);
  }
  .markdown :global(ul),
  .markdown :global(ol) {
    margin: 0 0 var(--sp-3);
    padding-left: var(--sp-4);
  }
  .markdown :global(li) {
    margin: var(--sp-1) 0;
  }
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
  .markdown :global(pre code) {
    background: transparent;
    border: none;
    padding: 0;
    color: var(--fg);
    font-size: inherit;
  }
  .markdown :global(blockquote) {
    margin: 0 0 var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: var(--bg-card-2);
    color: var(--fg-dim);
    border-left: 3px solid var(--accent);
    font-style: normal;
  }
  .markdown :global(table) {
    border-collapse: collapse;
    margin: 0 0 var(--sp-3);
    font-family: var(--sans);
    font-size: var(--fs-sm);
  }
  .markdown :global(th),
  .markdown :global(td) {
    padding: var(--sp-1) var(--sp-3);
    border: 1px solid var(--border);
    text-align: left;
  }
  .markdown :global(th) {
    background: var(--bg-card-2);
    font-weight: 600;
  }
  .markdown :global(.mermaid) {
    margin: var(--sp-3) 0;
    text-align: center;
  }
  .markdown :global(.katex-display) {
    margin: var(--sp-3) 0 !important;
    overflow-x: auto;
  }
  .markdown :global(a) {
    color: var(--accent);
    text-decoration: underline;
  }

  .block {
    margin-top: var(--sp-4);
    padding-top: var(--sp-4);
    border-top: 1px solid var(--border);
  }
  .block.fuss {
    margin-top: var(--sp-5);
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }
  h3 {
    font-family: var(--sans);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    margin: 0 0 var(--sp-2);
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

  .hints {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .hint-toggle {
    width: 100%;
    text-align: left;
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-2) var(--sp-3);
    color: var(--fg-dim);
    cursor: pointer;
    font-size: var(--fs-sm);
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    border-radius: var(--radius-sm);
  }
  .hint-toggle:hover {
    border-color: var(--accent);
    color: var(--fg);
  }
  .hint-toggle.offen {
    color: var(--accent);
    border-color: var(--accent);
  }
  .hint-toggle .kosten {
    margin-left: auto;
    font-size: var(--fs-xs);
    color: var(--orange);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .hint-toggle .kosten.frei {
    color: var(--green);
  }
  .hint-text {
    margin: var(--sp-2) 0 0;
    padding: var(--sp-3);
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--fg);
    font-size: var(--fs-sm);
  }
  .dim {
    color: var(--fg-dim);
  }
</style>
