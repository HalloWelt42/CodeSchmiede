<script lang="ts">
  /* Die Ziele des Tagesauftrags, erledigte abgehakt. */
  import type { Tagesauftrag } from '../../api/SpielApi';

  let { auftrag }: { auftrag: Tagesauftrag } = $props();
</script>

<div class="auftrag">
  {#each auftrag.ziele as z (z.id)}
    <div class="auftrag-ziel" class:erledigt={z.erledigt}>
      <i class="{z.erledigt ? 'fa-solid fa-circle-check' : 'fa-regular fa-circle'}" aria-hidden="true"></i>
      <span title={z.text}>{z.text}</span>
    </div>
  {/each}
</div>
