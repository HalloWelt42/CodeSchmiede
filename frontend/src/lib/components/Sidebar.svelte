<script lang="ts">
  import { route, type Route } from '../stores/RouteStore.svelte';

  interface NavEintrag {
    id: Route;
    titel: string;
    icon: string;
  }

  const eintraege: NavEintrag[] = [
    { id: 'dashboard', titel: 'Dashboard', icon: 'fa-house' },
    { id: 'aufgaben', titel: 'Aufgaben', icon: 'fa-list-check' },
    { id: 'pfade', titel: 'Pfade', icon: 'fa-route' },
  ];

  function istAktiv(eintrag: NavEintrag): boolean {
    if (eintrag.id === route.aktiv) return true;
    // Aufgaben-Detail soll den Aufgaben-Eintrag aktiv markieren
    if (eintrag.id === 'aufgaben' && route.aktiv === 'aufgabe') return true;
    return false;
  }
</script>

<aside class="sidebar">
  <nav>
    {#each eintraege as eintrag (eintrag.id)}
      <button
        class="nav-btn"
        class:aktiv={istAktiv(eintrag)}
        onclick={() => route.setze(eintrag.id)}
      >
        <i class="fa-solid {eintrag.icon}" aria-hidden="true"></i>
        <span>{eintrag.titel}</span>
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
    width: 220px;
    flex-shrink: 0;
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-3);
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
    padding: var(--sp-3);
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
