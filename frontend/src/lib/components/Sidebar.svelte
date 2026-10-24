<script lang="ts">
  import { route } from '../stores/RouteStore.svelte';
  import { BEREICHE, istAktiv } from '../navigation';
</script>

<aside class="sidebar">
  <nav>
    {#each BEREICHE as bereich (bereich.id)}
      <button
        class="nav-btn"
        class:aktiv={istAktiv(bereich, route.aktiv)}
        onclick={() => route.setze(bereich.id)}
      >
        <i class="fa-solid {bereich.icon}" aria-hidden="true"></i>
        <span>{bereich.titel}</span>
      </button>
    {/each}
  </nav>

  <div class="hinweis">
    <small>Codeschmiede</small>
    <small class="dim">Lokal &amp; sandboxed</small>
  </div>
</aside>

<style>
  .sidebar {
    width: 200px;
    flex-shrink: 0;
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-2);
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
  }
  nav {
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
  }
  .nav-btn {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: transparent;
    border: 1px solid transparent;
    color: var(--fg-dim);
    text-align: left;
    border-radius: var(--radius-sm);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    cursor: pointer;
  }
  .nav-btn:hover {
    background: var(--bg-card-2);
    color: var(--fg);
    border-color: var(--border);
  }
  .nav-btn.aktiv {
    color: var(--accent);
    border-color: var(--accent);
    background: color-mix(in srgb, var(--accent) 10%, transparent);
  }
  .nav-btn i {
    width: 18px;
    text-align: center;
  }
  .hinweis {
    margin-top: auto;
    display: flex;
    flex-direction: column;
    gap: 2px;
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .hinweis .dim {
    color: var(--fg-mute);
    text-transform: none;
    letter-spacing: 0;
  }
</style>
