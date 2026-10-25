<script lang="ts">
  /*
   * Ein Teil eines Abschnitts im Lesetext: Markdown, Alltagsbeispiel mit eigener Zeichnung, Merksatz, Falle,
   * Augenzwinkern, Zeichnung, Diagramm (gebautes SVG, eingebettet, damit es die Farben des Themas trägt), Beispiel mit
   * Vorhersage oder Frage.
   */
  import type { Antwort, TeilSicht, Urteil } from '../../api/KursApi';
  import { markdownRenderer } from '../../markdown/MarkdownRenderer';
  import CodeBlock from './CodeBlock.svelte';
  import FrageBlock from './FrageBlock.svelte';

  interface Props {
    teil: TeilSicht;
    sprache: string;
    senden: (a: Antwort) => Promise<Urteil>;
    beiUrteil: (element: string, u: Urteil) => void;
    /** Beispiel in der Werkbank zeigen (am Rechner) */
    beispielWaehlen?: (id: string) => void;
    gewaehltesBeispiel?: string | null;
  }
  let { teil, sprache, senden, beiUrteil, beispielWaehlen, gewaehltesBeispiel = null }: Props = $props();

  let svg = $state('');
  $effect(() => {
    if (teil.art !== 'diagramm' || !teil.url) return;
    let aktuell = true;
    void fetch(teil.url).then((r) => (r.ok ? r.text() : '')).then((t) => { if (aktuell) svg = t; });
    return () => { aktuell = false; };
  });
</script>

{#if teil.art === 'text'}
  <div class="md-text">{@html markdownRenderer.rendere(teil.markdown)}</div>
{:else if teil.art === 'alltag'}
  <div class="alltag" class:ohne-bild={!teil.zeichnung}>
    {#if teil.zeichnung}<div class="zeichnung"><img src={teil.zeichnung} alt="" /></div>{/if}
    <div><span class="marke-klein">Aus dem Leben</span>{@html markdownRenderer.rendere(teil.text)}</div>
  </div>
{:else if teil.art === 'merke'}
  <div class="merksatz"><b>Merke:</b> {@html markdownRenderer.rendere(teil.text)}</div>
{:else if teil.art === 'falle'}
  <div class="falle-block"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><div><b>{teil.titel}</b>{@html markdownRenderer.rendere(teil.text)}</div></div>
{:else if teil.art === 'augenzwinkern'}
  <div class="augenzwinkern"><i class="fa-solid fa-face-smile-wink" aria-hidden="true"></i><span>{teil.text}</span></div>
{:else if teil.art === 'zeichnung'}
  <figure class="zeichnung-gross"><img src={teil.url} alt={teil.unterschrift} />{#if teil.unterschrift}<figcaption>{teil.unterschrift}</figcaption>{/if}</figure>
{:else if teil.art === 'diagramm'}
  <div class="schema">
    {#if teil.titel}<div class="schema-titel"><span>{teil.titel}</span></div>{/if}
    {#if svg}<div class="diagramm">{@html svg}</div>{:else if !teil.url}<span class="dim">Diagramm wird noch gebaut.</span>{/if}
  </div>
{:else if teil.art === 'beispiel'}
  <div class="beispiel-im-text" class:gewaehlt={gewaehltesBeispiel === teil.id}>
    <div class="schema-titel">
      <span>Beispiel</span>
      {#if beispielWaehlen}<button class="knopf-klein" onclick={() => beispielWaehlen?.(teil.id)}><i class="fa-solid fa-play" aria-hidden="true"></i>In der Werkbank</button>{/if}
    </div>
    <CodeBlock code={teil.code} {sprache} />
  </div>
  {#if teil.vorhersage}
    <FrageBlock element={teil.id} {sprache} vorhersage={teil.vorhersage} {senden} beiUrteil={(u) => beiUrteil(teil.id, u)} />
  {/if}
{:else if teil.art === 'frage'}
  <FrageBlock element={teil.frage.id} {sprache} frage={teil.frage} {senden} beiUrteil={(u) => beiUrteil(teil.frage.id, u)} />
{/if}

<style>
  .alltag.ohne-bild { grid-template-columns: minmax(0, 1fr); }
  .alltag img, .zeichnung-gross img { width: 100%; height: auto; display: block; }
  .zeichnung-gross { margin: 0; display: flex; flex-direction: column; align-items: center; gap: var(--sp-1); }
  .zeichnung-gross img { max-width: 420px; }
  .zeichnung-gross figcaption { font-size: var(--fs-sm); color: var(--fg-dim); font-family: var(--sans); }
  .falle-block { display: grid; grid-template-columns: 22px minmax(0, 1fr); gap: var(--sp-2); padding: var(--sp-3); border-left: 4px solid var(--orange); background: color-mix(in srgb, var(--orange) 8%, var(--bg-card-2)); }
  .falle-block i { color: var(--orange); margin-top: 5px; }
  .falle-block b { font-family: var(--sans); display: block; }
  .beispiel-im-text { display: flex; flex-direction: column; gap: var(--sp-1); }
  .beispiel-im-text.gewaehlt :global(.code) { border-color: var(--accent); }
  .md-text :global(p), .merksatz :global(p), .alltag :global(p), .falle-block :global(p) { margin: 0 0 var(--sp-2); }
  .md-text :global(p:last-child), .merksatz :global(p:last-child), .alltag :global(p:last-child), .falle-block :global(p:last-child) { margin-bottom: 0; }
  .merksatz :global(p) { display: inline; }
</style>
