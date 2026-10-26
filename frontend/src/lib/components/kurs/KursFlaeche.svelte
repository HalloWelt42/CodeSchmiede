<script lang="ts">
  /*
   * Rahmen um jede Kursseite (am Rechner und am Telefon): nur darin gelten
   * die Regeln aus styles/kurs.css. Ohne eigene Box, das Layout der Seite
   * bleibt unverändert.
   */
  import type { Snippet } from 'svelte';

  let { children }: { children: Snippet } = $props();
</script>

<div class="kursflaeche">{@render children()}</div>

<style>
  .kursflaeche {
    display: contents;
  }
</style>
