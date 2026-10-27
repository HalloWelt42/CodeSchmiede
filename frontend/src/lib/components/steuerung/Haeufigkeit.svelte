<script lang="ts">
  /* Balkenbild der Buchstaben A bis Z eines Texts, darüber die goldene Linie der Häufigkeit im Deutschen. */
  import { ABC, haeufigkeit } from '../../steuerung/codes';

  let { text, deutsch }: { text: string; deutsch: Record<string, number> } = $props();

  const HOEHE = 96;
  // Prozent je Bildpunkt: E liegt bei knapp 18 %
  const MASS = 4.6;
  const x = (i: number) => 8 + i * 17.6;

  let anteile = $derived(haeufigkeit(text));
  let linie = $derived([...ABC].map((b, i) => `${x(i) + 5.5},${HOEHE - (deutsch[b] ?? 0) * MASS}`).join(' '));
</script>

<svg class="haeufigkeit" viewBox="0 0 470 114" role="img" aria-label="Häufigkeit der Buchstaben im Text und im Deutschen">
  {#each [...ABC] as b, i (b)}
    {@const h = Math.min(HOEHE, anteile[b] * MASS)}
    <rect class="saeule" x={x(i)} width="11" y={HOEHE - h} height={h} />
    <text x={x(i) + 5.5} y="111" text-anchor="middle">{b}</text>
  {/each}
  <polyline class="deutsch" points={linie} />
</svg>
<div class="legende">
  <span class="l-text">im Text</span>
  <span class="l-deutsch">im Deutschen</span>
</div>

<style>
  .haeufigkeit {
    display: block;
    flex-shrink: 0;
    width: 100%;
    height: auto;
  }
  text {
    fill: var(--fg-dim);
    font: 600 13px var(--mono);
  }
  .saeule { fill: var(--accent); }
  .deutsch {
    fill: none;
    stroke: var(--gold);
    stroke-width: 1.6;
  }
  .legende {
    display: flex;
    flex-shrink: 0;
    gap: var(--sp-3);
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .legende span::before {
    content: '';
    display: inline-block;
    width: 10px;
    height: 10px;
    margin-right: 5px;
    vertical-align: -1px;
  }
  .l-text::before { background: var(--accent); }
  .l-deutsch::before {
    border: 2px solid var(--gold);
    width: 8px;
    height: 8px;
  }
</style>
