<script lang="ts">
  /*
   * Linke Spalte der Aufgaben-Detail-Ansicht.
   * Markdown-Beschreibung (mit KaTeX und Mermaid), darunter sichtbare
   * Tests, gestaffelte Hints (Klick meldet "geoeffnet" ans Backend),
   * Quellen-/Lizenz-Info.
   */
  import { onMount, tick } from 'svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { markdownRenderer } from '../markdown/MarkdownRenderer';
  import type { Hint, Quelle, TestFall } from '../types/Aufgabe';

  interface Props {
    aufgabeId: string;
    markdown: string;
    hints: Hint[];
    tests_sichtbar: TestFall[];
    anzahl_versteckt: number;
    quelle: Quelle;
    schwierigkeit_score: number;
  }

  let { aufgabeId, markdown, hints, tests_sichtbar, anzahl_versteckt, quelle, schwierigkeit_score }: Props = $props();

  let html = $state('');
  let host: HTMLDivElement | undefined = $state();

  $effect(() => {
    html = markdownRenderer.rendere(markdown);
    tick().then(() => {
      if (host) markdownRenderer.rendereMermaids(host);
    });
  });

  // Welche Hints sind aktuell aufgeklappt? (lokal pro Sicht)
  let offen = $state<Set<number>>(new Set());

  // Wieviele Hints schon "verbraucht" (via API getrackt) -- aus Progress
  let geseheneAnzahl = $derived(progressStore.proAufgabe[aufgabeId]?.hints_genutzt ?? 0);

  async function toggleHint(i: number): Promise<void> {
    const neu = new Set(offen);
    const istOffen = neu.has(i);
    if (istOffen) {
      neu.delete(i);
      offen = neu;
      return;
    }
    neu.add(i);
    offen = neu;
    if (i + 1 > geseheneAnzahl) {
      try {
        await aufgabenApi.hintGeoeffnet(aufgabeId, i);
        await progressStore.ladeAlles();
      } catch {
        // tolerieren -- UI bleibt offen
      }
    }
  }

  function formatiereTest(t: TestFall): string {
    const args = t.input.map((x) => JSON.stringify(x)).join(', ');
    return `f(${args}) = ${JSON.stringify(t.expected)}`;
  }

  // Aktuell maximal noch erreichbare Punkte
  let restPunkte = $derived(() => {
    const verbrauchteKosten = hints.slice(0, geseheneAnzahl).reduce((s, h) => s + h.kosten, 0);
    return Math.max(0, schwierigkeit_score - verbrauchteKosten);
  });
</script>

<div class="beschreibungs-bereich">
  <div class="markdown" bind:this={host}>
    {@html html}
  </div>

  {#if tests_sichtbar.length > 0}
    <section class="block">
      <details>
        <summary>
          <h3>Sichtbare Tests &middot; {tests_sichtbar.length}</h3>
          <i class="fa-solid fa-chevron-down summary-chevron" aria-hidden="true"></i>
        </summary>
        <ul class="tests">
          {#each tests_sichtbar as t, i (i)}
            <li><code>{formatiereTest(t)}</code></li>
          {/each}
        </ul>
        {#if anzahl_versteckt > 0}
          <p class="hinweis">
            Plus {anzahl_versteckt} versteckte
            {anzahl_versteckt === 1 ? 'Prüfung' : 'Prüfungen'} -- nur die Anzahl
            des Erfolgs wird zurückgemeldet.
          </p>
        {/if}
      </details>
    </section>
  {/if}

  {#if hints.length > 0}
    <section class="block">
      <header class="block-kopf">
        <h3>Hinweise</h3>
        <span class="punkte-rest num" title="Aktuell noch erreichbare Punkte">
          {restPunkte()} / {schwierigkeit_score} Punkte
        </span>
      </header>
      <ol class="hints">
        {#each hints as hint, i (i)}
          {@const istGeseht = i < geseheneAnzahl}
          {@const istOffen = offen.has(i)}
          <li>
            <button
              class="hint-toggle"
              onclick={() => toggleHint(i)}
              class:offen={istOffen}
              class:gesehen={istGeseht && !istOffen}
            >
              <i class="fa-solid {istOffen ? 'fa-eye' : istGeseht ? 'fa-eye-low-vision' : 'fa-eye-slash'}" aria-hidden="true"></i>
              Hinweis {i + 1}
              {#if istGeseht}
                <span class="status-text">bereits gesehen</span>
              {/if}
              {#if hint.kosten > 0}
                <span class="kosten">-{hint.kosten} Punkte</span>
              {:else}
                <span class="kosten frei">kostenlos</span>
              {/if}
            </button>
            {#if istOffen}
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
  .markdown :global(p) { margin: 0 0 var(--sp-3); }
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
  .markdown :global(.katex-display) { margin: var(--sp-3) 0 !important; overflow-x: auto; }
  .markdown :global(a) { color: var(--accent); text-decoration: underline; }

  .block { margin-top: var(--sp-4); padding-top: var(--sp-4); border-top: 1px solid var(--border); }
  .block.fuss { margin-top: var(--sp-5); color: var(--fg-dim); font-size: var(--fs-sm); }
  .block-kopf {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: var(--sp-2);
  }
  h3 {
    font-family: var(--sans);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    margin: 0 0 var(--sp-2);
  }
  .punkte-rest {
    font-size: var(--fs-sm);
    color: var(--accent);
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
  .hint-toggle:hover { border-color: var(--accent); color: var(--fg); }
  .hint-toggle.offen { color: var(--accent); border-color: var(--accent); }
  .hint-toggle.gesehen { border-color: var(--fg-mute); }
  .hint-toggle.gesehen i { color: var(--fg-mute); }
  .status-text {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
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
  .dim { color: var(--fg-dim); }
</style>
