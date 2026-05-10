<script lang="ts">
  /*
   * Footer mit Live-Version aus /api/healthz. Vite cached die VERSION
   * nur beim Build/Start, das Backend-Modul liest sie bei jedem Request
   * frisch -- also kommt der Footer immer aktuell.
   */
  import { onMount } from 'svelte';

  let version = $state<string | null>(null);

  onMount(async () => {
    try {
      const r = await fetch('/api/healthz');
      if (r.ok) {
        const j = await r.json();
        version = j.version;
      }
    } catch {
      // Backend nicht erreichbar -- bleibt bei "..."
    }
  });
</script>

<footer>
  <span class="links">
    <i class="fa-solid fa-hammer" aria-hidden="true"></i>
    Codeschmiede v{version ?? '...'}
  </span>
  <span class="rechts">Lokal, ohne Tracking, ohne Werbung</span>
</footer>

<style>
  footer {
    height: var(--footer-h);
    flex-shrink: 0;
    padding: 0 var(--sp-4);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--bg-card);
    border-top: 1px solid var(--border);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }
  .links {
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .links i {
    color: var(--accent);
  }
  .rechts {
    color: var(--fg-mute);
  }
</style>
