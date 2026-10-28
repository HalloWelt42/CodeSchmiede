<script lang="ts">
  /*
   * Eigene Schale für das Telefon: schmaler Kopf, Inhalt in voller
   * Breite, Reiterleiste ganz unten (ohne Abstand über dem Home-Balken).
   * Oben nur die sichere Zone des Geräts, damit nichts unter Uhr und
   * Kamera liegt.
   */
  import { route } from '../../stores/RouteStore.svelte';
  import { theme } from '../../stores/ThemeStore.svelte';
  import { zugang } from '../../stores/ZugangStore.svelte';
  import { BEREICHE, istAktiv } from '../../navigation';
  import FassungsBand from '../FassungsBand.svelte';
  import Inhalt from '../Inhalt.svelte';

  const reiter = BEREICHE.filter((b) => b.telefon);
</script>

<div class="telefon">
  <header class="t-kopf">
    <div class="marke">
      <i class="fa-solid fa-hammer" aria-hidden="true"></i>
      Codeschmiede
    </div>
    <div class="rechts">
      {#if zugang.konto}
        <button class="ikon" onclick={() => zugang.abmelden()} aria-label="Abmelden {zugang.konto.name}">
          <i class="fa-solid fa-right-from-bracket" aria-hidden="true"></i>
        </button>
      {/if}
      <button class="ikon" onclick={() => theme.toggle()} aria-label="Theme wechseln">
        <i class="fa-solid {theme.modus === 'dark' ? 'fa-sun' : 'fa-moon'}" aria-hidden="true"></i>
      </button>
    </div>
  </header>
  <FassungsBand />
  <main class="t-inhalt">
    <Inhalt />
  </main>
  <nav class="t-reiter">
    {#each reiter as bereich (bereich.id)}
      <button class:aktiv={istAktiv(bereich, route.aktiv, route.kursId)} onclick={() => route.setze(bereich.id)}>
        <i class="fa-solid {bereich.icon}" aria-hidden="true"></i>
        {bereich.titel}
      </button>
    {/each}
  </nav>
</div>

<style>
  .telefon {
    flex: 1;
    display: flex;
    flex-direction: column;
    width: 100%;
    min-height: 0;
    overflow: hidden;
    background: var(--bg-card);
  }
  .t-kopf {
    flex: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: calc(48px + env(safe-area-inset-top));
    padding: env(safe-area-inset-top) var(--sp-3) 0;
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
  .rechts {
    display: flex;
    gap: var(--sp-2);
  }
  .t-inhalt {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .t-reiter {
    flex: none;
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: minmax(0, 1fr);
    border-top: 1px solid var(--border);
    background: var(--bg-card);
  }
  .t-reiter button {
    height: 56px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3px;
    padding: 0;
    border: 0;
    border-radius: 0;
    background: transparent;
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }
  .t-reiter button i { font-size: 18px; }
  .t-reiter button:hover:not(:disabled) { background: transparent; }
  .t-reiter button.aktiv {
    color: var(--accent);
    box-shadow: inset 0 2px 0 var(--accent);
  }
</style>
