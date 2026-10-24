<script lang="ts">
  /*
   * Eigene Schale für das Telefon: schmaler Kopf, Inhalt in voller
   * Breite, Reiterleiste ganz unten (ohne Abstand über dem Home-Balken).
   * Oben nur die sichere Zone des Geräts, damit nichts unter Uhr und
   * Kamera liegt.
   */
  import { route } from '../stores/RouteStore.svelte';
  import { theme } from '../stores/ThemeStore.svelte';
  import { BEREICHE, istAktiv } from '../navigation';
  import FassungsBand from './FassungsBand.svelte';
  import Inhalt from './Inhalt.svelte';

  const reiter = BEREICHE.filter((b) => b.telefon);
</script>

<div class="telefon">
  <header class="kopf">
    <div class="marke">
      <i class="fa-solid fa-hammer" aria-hidden="true"></i>
      <span>Codeschmiede</span>
    </div>
    <button
      class="hdr-btn icon-only"
      onclick={() => theme.toggle()}
      title={theme.modus === 'dark' ? 'Helles Theme' : 'Dunkles Theme'}
      aria-label="Theme wechseln"
    >
      <i class="fa-solid {theme.modus === 'dark' ? 'fa-sun' : 'fa-moon'}" aria-hidden="true"></i>
    </button>
  </header>
  <FassungsBand />
  <main class="inhalt">
    <Inhalt />
  </main>
  <nav class="reiter">
    {#each reiter as bereich (bereich.id)}
      <button
        class="reiter-btn"
        class:aktiv={istAktiv(bereich, route.aktiv)}
        onclick={() => route.setze(bereich.id)}
      >
        <i class="fa-solid {bereich.icon}" aria-hidden="true"></i>
        <span>{bereich.titel}</span>
      </button>
    {/each}
  </nav>
</div>

<style>
  .telefon {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100dvh;
    min-height: 0;
    overflow: hidden;
    background: var(--bg-card);
  }
  .kopf {
    flex: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: env(safe-area-inset-top) var(--sp-3) 0;
    height: calc(48px + env(safe-area-inset-top));
    border-bottom: 1px solid var(--border);
  }
  .marke {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-lg);
    font-weight: 600;
  }
  .marke i { color: var(--accent); }
  .inhalt {
    flex: 1 1 auto;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .reiter {
    flex: none;
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: minmax(0, 1fr);
    border-top: 1px solid var(--border);
    background: var(--bg-card);
  }
  .reiter-btn {
    height: 56px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3px;
    border: 0;
    border-radius: 0;
    background: transparent;
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    padding: 0;
  }
  .reiter-btn i { font-size: 18px; }
  .reiter-btn.aktiv {
    color: var(--accent);
    box-shadow: inset 0 2px 0 var(--accent);
  }
  .reiter-btn:hover:not(:disabled) {
    background: transparent;
    border-color: transparent;
  }
</style>
