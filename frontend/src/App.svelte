<script lang="ts">
  /*
   * Root-Layout (Topbar + Sidebar + Content + Footer).
   * Routing entscheidet ueber die Content-Komponente.
   */
  import { onMount } from 'svelte';
  import { theme } from './lib/stores/ThemeStore.svelte';
  import { route } from './lib/stores/RouteStore.svelte';
  import Topbar from './lib/components/Topbar.svelte';
  import Sidebar from './lib/components/Sidebar.svelte';
  import Footer from './lib/components/Footer.svelte';
  import Dashboard from './lib/components/Dashboard.svelte';
  import AufgabenListe from './lib/components/AufgabenListe.svelte';
  import PfadListe from './lib/components/PfadListe.svelte';
  import AufgabenDetail from './lib/components/AufgabenDetail.svelte';

  onMount(() => {
    theme.init();
    route.init();
  });
</script>

<div class="layout">
  <Topbar />
  <main class="body">
    <div class="sidebar-wrap"><Sidebar /></div>
    <section class="right">
      {#if route.aktiv === 'dashboard'}
        <Dashboard />
      {:else if route.aktiv === 'aufgaben'}
        <AufgabenListe />
      {:else if route.aktiv === 'pfade'}
        <PfadListe />
      {:else if route.aktiv === 'aufgabe' && route.aufgabeId}
        {#key route.aufgabeId}
          <AufgabenDetail aufgabeId={route.aufgabeId} />
        {/key}
      {/if}
    </section>
  </main>
  <Footer />
</div>

<style>
  .layout {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    min-height: 0;
    overflow: hidden;
  }
  .body {
    flex: 1 1 auto;
    min-height: 0;
    display: flex;
    gap: var(--sp-3);
    padding: var(--sp-4) var(--sp-3) var(--sp-3);
    overflow: hidden;
  }
  .right {
    flex: 1 1 auto;
    min-width: 0;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--bg-card);
    border: 1px solid var(--border);
  }
  .sidebar-wrap {
    display: contents;
  }

  @media (max-width: 900px) {
    .body {
      flex-direction: column;
      gap: var(--sp-2);
      padding: var(--sp-2);
      overflow-y: auto;
    }
  }
</style>
