<script lang="ts">
  import { layout } from '../stores/LayoutStore.svelte';
  import { theme } from '../stores/ThemeStore.svelte';
  import { zoom } from '../stores/ZoomStore.svelte';
  import { zugang } from '../stores/ZugangStore.svelte';
  import KopfStand from './spiel/KopfStand.svelte';
</script>

<header class="topbar">
  <button
    class="ikon"
    onclick={() => layout.umschaltenNav()}
    aria-label={layout.navBreit ? 'Navigation einklappen' : 'Navigation ausklappen'}
    title={layout.navBreit ? 'Navigation einklappen' : 'Navigation ausklappen'}
    aria-expanded={layout.navBreit}
    aria-controls="hauptnavigation"
  >
    <i class="fa-solid {layout.navBreit ? 'fa-angles-left' : 'fa-angles-right'}" aria-hidden="true"></i>
  </button>
  <div class="marke">
    <i class="fa-solid fa-hammer" aria-hidden="true"></i>
    Codeschmiede
  </div>
  <div class="rechts">
    <KopfStand />
    {#if zugang.konto}
      <span class="konto">
        <i class="fa-solid {zugang.konto.geraet ? 'fa-link' : 'fa-user'}" aria-hidden="true"></i>{zugang.konto.name}
        <button class="ikon" onclick={() => zugang.abmelden()} aria-label="Abmelden" title="Abmelden">
          <i class="fa-solid fa-right-from-bracket" aria-hidden="true"></i>
        </button>
      </span>
    {/if}
    <div class="zoom" role="group" aria-label="Größe der Anzeige">
      <button class="ikon" onclick={() => zoom.kleiner()} disabled={zoom.kleinste} aria-label="Kleiner" title="Kleiner">
        <i class="fa-solid fa-magnifying-glass-minus" aria-hidden="true"></i>
      </button>
      <button class="prozent" onclick={() => zoom.zuruecksetzen()} title="Auf 100 % zurücksetzen" aria-label="Größe {zoom.prozent} %, zurücksetzen">
        {zoom.prozent} %
      </button>
      <button class="ikon" onclick={() => zoom.groesser()} disabled={zoom.groesste} aria-label="Größer" title="Größer">
        <i class="fa-solid fa-magnifying-glass-plus" aria-hidden="true"></i>
      </button>
    </div>
    <button class="ikon" onclick={() => theme.toggle()} aria-label="Theme wechseln">
      <i class="fa-solid {theme.modus === 'dark' ? 'fa-sun' : 'fa-moon'}" aria-hidden="true"></i>
    </button>
  </div>
</header>

<style>
  .topbar {
    flex: none;
    height: var(--kopf-h);
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: 0 var(--sp-3);
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
  }
  .marke {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-lg);
    font-weight: 600;
    letter-spacing: 0.02em;
  }
  .marke i { color: var(--accent); }
  .zoom { display: flex; align-items: center; gap: var(--sp-1); }
  .prozent {
    min-width: 4.5em;
    height: var(--knopf-h);
    padding: 0 var(--sp-1);
    border: none;
    background: transparent;
    color: var(--fg-dim);
    font: inherit;
    font-variant-numeric: tabular-nums;
    cursor: pointer;
  }
  .prozent:hover { color: var(--accent); }
  .rechts {
    margin-left: auto;
    display: flex;
    gap: var(--sp-2);
  }
</style>
