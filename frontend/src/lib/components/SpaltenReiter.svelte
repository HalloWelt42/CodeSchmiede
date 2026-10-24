<script lang="ts" generics="T extends string">
  /* Kleine Reiter oben in einer Spalte, etwa Aufgabe | Hinweise | Verlauf | Lösung. */
  interface Reiter {
    id: T;
    titel: string;
    icon?: string;
  }
  let { reiter, aktiv = $bindable() }: { reiter: Reiter[]; aktiv: T } = $props();
</script>

<div class="reiter-klein" role="tablist">
  {#each reiter as r (r.id)}
    <button class:aktiv={aktiv === r.id} role="tab" aria-selected={aktiv === r.id} onclick={() => (aktiv = r.id)}>
      {#if r.icon}<i class="fa-solid {r.icon}" aria-hidden="true"></i>{/if}{r.titel}
    </button>
  {/each}
</div>
