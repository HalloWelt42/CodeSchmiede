<script lang="ts">
  /* Bild auf der Karte eines Spiels, aus Bausteinen der Oberfläche statt aus Bilddateien. */
  let { id }: { id: string } = $props();

  // kleines Raster wie im Entwurf: Wände, Spur, Kristall, Ziel
  const ROBOTER_BILD = ['.#..Z', '*#.#.', '***#.', '.#*K.', '#...#'].join('').split('');
</script>

{#if id === 'roboter-parcours'}
  <div class="welt mini" style:--zellen="5">
    {#each ROBOTER_BILD as z, i (i)}
      <div class="zelle" class:wand={z === '#'} class:spur={z === '*'}>
        {#if z === 'Z'}<div class="ziel"></div>{/if}
        {#if z === 'K'}<div class="kristall"></div>{/if}
      </div>
    {/each}
  </div>
{:else if id === 'ausgabe-sprint'}
  <div class="sprint-bild">
    <div class="num uhrzeit">0:42</div>
    <div class="code">print(3 * "ab")</div>
    <div class="kette"><i class="fa-solid fa-link" aria-hidden="true"></i> Kette 4</div>
  </div>
{:else if id === 'muster-jagd'}
  <div class="muster">
    <div class="akz">/\d{'{'}2{'}'}\.\d{'{'}2{'}'}/</div>
    <div><i class="fa-solid fa-check ok" aria-hidden="true"></i> <mark>24.10</mark>.2026</div>
    <div><i class="fa-solid fa-xmark nein" aria-hidden="true"></i> 2026-10-24</div>
  </div>
{:else}
  <i class="fa-solid fa-gamepad ersatz" aria-hidden="true"></i>
{/if}

<style>
  .muster {
    font-family: var(--mono);
    font-size: 11px;
    line-height: 1.8;
    padding: 8px;
    text-align: left;
  }
  .akz { color: var(--accent); }
  .ok { color: var(--green); }
  .nein { color: var(--red); }
  mark {
    background: color-mix(in srgb, var(--accent) 35%, transparent);
    color: var(--fg);
  }
  .mini { width: 96px; }
  .sprint-bild { text-align: center; }
  .uhrzeit {
    font-size: 34px;
    color: var(--accent);
  }
  .code {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--fg-dim);
  }
  .kette {
    margin-top: 6px;
    color: var(--orange);
    font-weight: 600;
    font-size: 12px;
  }
  .ersatz {
    font-size: 32px;
    color: var(--fg-mute);
  }
</style>
