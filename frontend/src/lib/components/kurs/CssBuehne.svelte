<script lang="ts">
  /*
   * Die Bühne der CSS-Beispiele: dieselbe Fläche wie bei den CSS-Aufgaben (css/buehne.ts), passend zur Spalte
   * verkleinert. Ohne Skripte; wer die Elemente darin braucht (Kästen in der Werkbank), bekommt das Dokument nach
   * jedem Laden über beiLaden. Darüber liegt, was die Werkbank zeichnet (ueber), in den Maßen der Bühne.
   */
  import type { Snippet } from 'svelte';
  import { BUEHNE_B, BUEHNE_H, buehnenDokument } from '../../css/buehne';

  interface Props {
    html: string;
    css: string;
    titel?: string;
    beiLaden?: (dokument: Document) => void;
    ueber?: Snippet;
  }
  let { html, css, titel = 'Bühne', beiLaden, ueber }: Props = $props();

  let breite = $state(0);
  let massstab = $derived(Math.min(1, breite / BUEHNE_B) || 0);
  let srcdoc = $derived(buehnenDokument(html, css));

  function geladen(e: Event) {
    const dokument = (e.currentTarget as HTMLIFrameElement).contentDocument;
    if (dokument) beiLaden?.(dokument);
  }
</script>

<div class="css-buehne" bind:clientWidth={breite} style:height="{BUEHNE_H * massstab}px">
  <div class="flaeche" style:width="{BUEHNE_B}px" style:height="{BUEHNE_H}px" style:transform="scale({massstab})">
    <iframe title={titel} sandbox="allow-same-origin" {srcdoc} tabindex="-1" onload={geladen}></iframe>
    {#if ueber}<div class="ueber">{@render ueber()}</div>{/if}
  </div>
</div>

<style>
  .css-buehne { position: relative; width: 100%; max-width: 600px; overflow: hidden; border: 1px solid var(--border); }
  .flaeche { position: absolute; left: 0; top: 0; transform-origin: 0 0; }
  .flaeche iframe { width: 100%; height: 100%; border: 0; display: block; }
  .ueber { position: absolute; inset: 0; pointer-events: none; }
</style>
