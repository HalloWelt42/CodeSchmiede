<script lang="ts">
  /* Bild auf der Karte eines Spiels, aus Bausteinen der Oberfläche statt aus Bilddateien. */
  let { id }: { id: string } = $props();
</script>

{#if id === 'muster-jagd'}
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
  .ersatz {
    font-size: 32px;
    color: var(--fg-mute);
  }
</style>
