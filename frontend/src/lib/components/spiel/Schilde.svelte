<script lang="ts">
  /* Schutzschilde der Serie: erworbene voll, fehlende blass. */
  import type { SerienStand } from '../../api/SpielApi';

  let { serie }: { serie: SerienStand } = $props();
</script>

{#each { length: serie.schilde_max } as _, i (i)}
  <i class="fa-solid fa-shield-halved schild" class:leer={i >= serie.schilde} aria-hidden="true"></i>
{/each}
