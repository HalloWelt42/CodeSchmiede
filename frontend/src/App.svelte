<script lang="ts">
  /*
   * Wurzel: Rechnerschale (Kopfleiste, Navigation, Inhalt, Fuß) oder
   * eigene Telefonschale, entschieden im GeraetStore. Den Inhalt nach
   * Route teilen sich beide (Inhalt.svelte).
   */
  import { onMount } from 'svelte';
  import { theme } from './lib/stores/ThemeStore.svelte';
  import { route } from './lib/stores/RouteStore.svelte';
  import { layout } from './lib/stores/LayoutStore.svelte';
  import { konfig } from './lib/stores/KonfigStore.svelte';
  import { fassung } from './lib/stores/FassungStore.svelte';
  import { geraet } from './lib/stores/GeraetStore.svelte';
  import Topbar from './lib/components/Topbar.svelte';
  import Sidebar from './lib/components/Sidebar.svelte';
  import Footer from './lib/components/Footer.svelte';
  import FassungsBand from './lib/components/FassungsBand.svelte';
  import Inhalt from './lib/components/Inhalt.svelte';
  import TelefonSchale from './lib/components/telefon/TelefonSchale.svelte';

  onMount(() => {
    theme.init();
    route.init();
    layout.init();
    konfig.init();
    const geraetEnde = geraet.init();
    const fassungEnde = fassung.verfolgen();
    return () => {
      geraetEnde();
      fassungEnde();
    };
  });
</script>

{#if geraet.telefon}
  <TelefonSchale />
{:else}
  <div class="app">
    <Topbar />
    <FassungsBand />
    <div class="koerper">
      <Sidebar />
      <main class="haupt">
        <Inhalt />
      </main>
    </div>
    <Footer />
  </div>
{/if}

<style>
  .app {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
    min-height: 0;
    overflow: hidden;
  }
  .koerper {
    flex: 1;
    min-height: 0;
    display: flex;
    gap: var(--sp-2);
    padding: var(--sp-2);
  }
  .haupt {
    flex: 1;
    min-width: 0;
    min-height: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--bg-card);
    border: 1px solid var(--border);
  }
</style>
