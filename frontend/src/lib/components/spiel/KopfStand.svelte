<script lang="ts">
  /* Stufe und Serie im Kopf der Rechneransicht. */
  import { spielStore, stufenAnteil } from '../../stores/SpielStore.svelte';
  import { zahl } from '../../spielanzeige';
  import Schilde from './Schilde.svelte';
</script>

{#if spielStore.stand}
  {@const s = spielStore.stand.stufe}
  {@const serie = spielStore.stand.serie}
  <span class="kopf-stand" title="Stufe {s.stufe}, {s.titel}: {zahl(s.punkte)} von {zahl(s.bis)} Punkten bis Stufe {s.stufe + 1}">
    <span class="mini-ring" style:--anteil={stufenAnteil(s)}><span>{s.stufe}</span></span>{s.titel}
  </span>
  <span
    class="kopf-stand"
    title="Serie: {serie.aktuell === 1 ? '1 Tag' : `${serie.aktuell} Tage`}, {serie.schilde} von {serie.schilde_max} Schutzschilden"
  >
    <i class="fa-solid fa-fire flamme" aria-hidden="true"></i><span class="num">{serie.aktuell}</span><Schilde {serie} />
  </span>
{/if}
