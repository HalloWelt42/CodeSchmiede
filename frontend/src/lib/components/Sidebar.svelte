<script lang="ts">
  /*
   * Navigation am Rechner. Breit mit Beschriftung oder eingeklappt nur mit
   * Symbolen (Knopf in der Kopfleiste, bei jeder Fensterbreite); die Breite
   * gleitet, die Beschriftung blendet aus. Eingeklappt nennt der Hinweis
   * beim Überfahren den Bereich.
   */
  import { route } from '../stores/RouteStore.svelte';
  import { layout } from '../stores/LayoutStore.svelte';
  import { BEREICHE, istAktiv } from '../navigation';
</script>

<aside id="hauptnavigation" class="nav" class:schmal={!layout.navBreit}>
  {#each BEREICHE as bereich (bereich.id)}
    <button
      class="nav-btn"
      class:aktiv={istAktiv(bereich, route.aktiv)}
      onclick={() => route.setze(bereich.id)}
      aria-label={bereich.titel}
      title={layout.navBreit ? undefined : bereich.titel}
    >
      <i class="fa-solid {bereich.icon}" aria-hidden="true"></i>
      <span>{bereich.titel}</span>
    </button>
  {/each}
  <div class="nav-fuss">Lokal und abgeschottet</div>
</aside>

<style>
  .nav {
    --nav-dauer: 0.2s;
    width: 200px;
    flex: none;
    display: flex;
    flex-direction: column;
    gap: 2px;
    padding: var(--sp-2);
    overflow: hidden;
    background: var(--bg-card);
    border: 1px solid var(--border);
    transition: width var(--nav-dauer) ease, padding var(--nav-dauer) ease;
  }
  .nav-btn {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    height: var(--zeile-h);
    /* Symbol bleibt beim Gleiten an seinem Platz und steht eingeklappt mittig */
    padding: 0 0 0 9px;
    border: 1px solid transparent;
    border-radius: var(--radius-sm);
    background: transparent;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-align: left;
    white-space: nowrap;
  }
  .nav-btn i {
    flex: none;
    width: 18px;
    text-align: center;
  }
  .nav-btn span,
  .nav-fuss {
    transition: opacity var(--nav-dauer) ease, visibility var(--nav-dauer);
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
    white-space: nowrap;
  }
  .nav.schmal {
    width: 48px;
    padding: var(--sp-2) 4px;
  }
  .nav.schmal .nav-btn span,
  .nav.schmal .nav-fuss {
    opacity: 0;
    visibility: hidden;
  }
  @media (prefers-reduced-motion: reduce) {
    .nav {
      --nav-dauer: 0s;
    }
  }
</style>
