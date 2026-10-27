<script lang="ts">
  /* Eine Ziffer der 7-Segment-Anzeige: Segmente a (oben) bis g (Mitte), leuchtend, wo `an` es sagt. */
  import { SEGMENTE } from '../../steuerung/schaltplan';

  let { an }: { an: (segment: string) => boolean } = $props();

  // Lage der Segmente als Polygon in einer Ziffer von 60 mal 100
  const FORM: Record<string, string> = {
    a: '12,6 48,6 42,12 18,12',
    b: '50,8 50,46 44,42 44,14',
    c: '50,54 50,92 44,86 44,58',
    d: '12,94 48,94 42,88 18,88',
    e: '10,54 10,92 16,86 16,58',
    f: '10,8 10,46 16,42 16,14',
    g: '12,50 18,46 42,46 48,50 42,54 18,54',
  };
</script>

<svg class="sieben" viewBox="0 0 60 100" role="img" aria-label="7-Segment-Anzeige">
  {#each SEGMENTE as s (s)}<polygon class="segment" class:an={an(s)} points={FORM[s]} />{/each}
</svg>

<style>
  .sieben {
    flex-shrink: 0;
    width: 60px;
    height: 100px;
    background: #0b0d10;
    border: 1px solid var(--border-strong);
    padding: 4px;
  }
  .segment { fill: #2b1a12; }
  .segment.an { fill: #ff6b3d; filter: drop-shadow(0 0 3px #ff6b3d); }
</style>
