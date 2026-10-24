<script lang="ts">
  /*
   * Fuß mit der Fassung des Servers. Der FassungStore fragt
   * /api/healthz beim Start, jede Minute und beim Zurückkehren ab; das
   * Backend liest VERSION bei jedem Aufruf frisch.
   */
  import { fassung } from '../stores/FassungStore.svelte';
</script>

<footer class="fuss">
  <span><i class="fa-solid fa-hammer" aria-hidden="true"></i> Codeschmiede v{fassung.server ?? '...'}</span>
  <span>Lokal, ohne Tracking, ohne Werbung</span>
</footer>

<style>
  .fuss {
    flex: none;
    height: var(--fuss-h);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--sp-3);
    background: var(--bg-card);
    border-top: 1px solid var(--border);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }
  .fuss i { color: var(--accent); }
</style>
