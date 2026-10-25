<script lang="ts">
  /*
   * Sammelkarte eines Kapitels in der Farbfamilie seiner Sprache. Das Bild kommt aus dem Medienpool, sobald es
   * abgenommen ist; bis dahin steht ein Symbol. Verdeckt, solange das Kapitel nicht geschafft ist.
   */
  import type { KapitelSicht } from '../../api/KursApi';

  interface Props {
    kapitel: KapitelSicht;
    sprache: string;
    sprachTitel: string;
    breite?: number;
    /** Satz "Kann ich jetzt" auf der Karte */
    mitSatz?: boolean;
    offen?: boolean;
  }
  let { kapitel, sprache, sprachTitel, breite, mitSatz = false, offen }: Props = $props();
  let sichtbar = $derived(offen ?? (kapitel.stand === 'fertig' || kapitel.stand === 'uebersprungen'));
</script>

<div class="sammelkarte" class:verdeckt={!sichtbar} data-sprache={sprache} style={breite ? `--breite:${breite}px` : ''} title={kapitel.titel}>
  <div class="kopf"><span>{kapitel.titel}</span><span class="nr">{String(kapitel.nr).padStart(2, '0')}</span></div>
  <div class="bildfeld">
    {#if !sichtbar}
      <i class="fa-solid fa-lock" aria-hidden="true"></i>
    {:else if kapitel.bild?.url}
      <img src={kapitel.bild.url} alt="" />
    {:else}
      <i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>
    {/if}
  </div>
  {#if mitSatz && sichtbar}<div class="kann"><b>Kann ich jetzt</b>{kapitel.karte}</div>{/if}
  <div class="fuss-karte"><span>{sichtbar ? sprachTitel : 'noch verdeckt'}</span><span>{kapitel.stand === 'uebersprungen' ? 'Kurztest' : sichtbar ? 'Kapitel' : ''}</span></div>
</div>

<style>
  .bildfeld img { width: 92%; height: auto; }
</style>
