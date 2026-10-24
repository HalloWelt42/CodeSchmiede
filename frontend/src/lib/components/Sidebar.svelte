<script lang="ts">
  /*
   * Navigation am Rechner. Breit mit Beschriftung oder schmal nur mit
   * Symbolen (Knopf in der Kopfleiste); unter 1200 px immer schmal,
   * damit der Inhalt Platz hat.
   */
  import { route } from '../stores/RouteStore.svelte';
  import { layout } from '../stores/LayoutStore.svelte';
  import { BEREICHE, istAktiv } from '../navigation';
</script>

<aside class="nav" class:schmal={!layout.navBreit}>
  {#each BEREICHE as bereich (bereich.id)}
    <button
      class="nav-btn"
      class:aktiv={istAktiv(bereich, route.aktiv)}
      onclick={() => route.setze(bereich.id)}
      aria-label={bereich.titel}
    >
      <i class="fa-solid {bereich.icon}" aria-hidden="true"></i>
      <span>{bereich.titel}</span>
    </button>
  {/each}
  <div class="nav-fuss">Lokal und abgeschottet</div>
</aside>

<style>
  .nav {
    width: 200px;
    flex: none;
    display: flex;
    flex-direction: column;
    gap: 2px;
    padding: var(--sp-2);
    background: var(--bg-card);
    border: 1px solid var(--border);
  }
  .nav-btn {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    height: var(--zeile-h);
    padding: 0 var(--sp-3);
    border: 1px solid transparent;
    border-radius: var(--radius-sm);
    background: transparent;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-align: left;
  }
  .nav-btn i {
    width: 18px;
    text-align: center;
  }
  .nav-btn:hover:not(:disabled) {
    background: var(--bg-card-2);
    border-color: transparent;
    color: var(--fg);
  }
  .nav-btn.aktiv,
  .nav-btn.aktiv:hover:not(:disabled) {
    color: var(--accent);
    border-color: var(--accent);
    background: color-mix(in srgb, var(--accent) 10%, transparent);
  }
  .nav-fuss {
    margin-top: auto;
    padding: var(--sp-2) var(--sp-3) 0;
    border-top: 1px solid var(--border);
    color: var(--fg-mute);
    font-size: var(--fs-xs);
  }
  .nav.schmal {
    width: 48px;
    padding: var(--sp-2) 4px;
  }
  .nav.schmal .nav-btn {
    justify-content: center;
    padding: 0;
  }
  .nav.schmal .nav-btn span,
  .nav.schmal .nav-fuss {
    display: none;
  }
  @media (max-width: 1199px) {
    .nav {
      width: 48px;
      padding: var(--sp-2) 4px;
    }
    .nav-btn {
      justify-content: center;
      padding: 0;
    }
    .nav-btn span,
    .nav-fuss {
      display: none;
    }
  }
</style>
