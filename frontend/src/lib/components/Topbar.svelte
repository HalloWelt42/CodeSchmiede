<script lang="ts">
  import { theme } from '../stores/ThemeStore.svelte';
</script>

<header class="topbar">
  <div class="brand">
    <i class="fa-solid fa-hammer" aria-hidden="true"></i>
    <span class="name">Codeschmiede</span>
  </div>

  <div class="actions">
    <button
      class="hdr-btn icon-only"
      onclick={() => theme.toggle()}
      title={theme.modus === 'dark' ? 'Helles Theme' : 'Dunkles Theme'}
      aria-label="Theme wechseln"
    >
      <i class="fa-solid {theme.modus === 'dark' ? 'fa-sun' : 'fa-moon'}" aria-hidden="true"></i>
    </button>
  </div>
</header>

<style>
  .topbar {
    height: var(--header-h);
    flex-shrink: 0;
    padding: 0 var(--sp-4);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
  }
  .brand {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    color: var(--fg);
  }
  .brand i {
    color: var(--accent);
    font-size: var(--fs-lg);
  }
  .name {
    font-size: var(--fs-lg);
    font-weight: 600;
    letter-spacing: 0.02em;
  }
  .actions {
    display: flex;
    gap: var(--sp-2);
  }
</style>
