<script lang="ts">
  import { layout } from '../stores/LayoutStore.svelte';
  import { theme } from '../stores/ThemeStore.svelte';
</script>

<header class="topbar">
  <button
    class="ikon"
    onclick={() => layout.umschaltenNav()}
    aria-label={layout.navBreit ? 'Navigation schmal' : 'Navigation breit'}
  >
    <i class="fa-solid {layout.navBreit ? 'fa-angles-left' : 'fa-angles-right'}" aria-hidden="true"></i>
  </button>
  <div class="marke">
    <i class="fa-solid fa-hammer" aria-hidden="true"></i>
    Codeschmiede
  </div>
  <div class="rechts">
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
  .rechts {
    margin-left: auto;
    display: flex;
    gap: var(--sp-2);
  }
</style>
