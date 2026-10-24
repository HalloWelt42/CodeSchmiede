<script lang="ts">
  /*
   * Inhalt nach Route -- geteilt von Rechner- und Telefonschale.
   * Bereiche, die nur am Rechner gelten (navigation.ts), fallen am
   * Telefon auf das Dashboard zurück.
   */
  import { route } from '../stores/RouteStore.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';
  import { BEREICHE } from '../navigation';
  import Dashboard from './Dashboard.svelte';
  import AufgabenListe from './AufgabenListe.svelte';
  import PfadListe from './PfadListe.svelte';
  import AufgabenDetail from './AufgabenDetail.svelte';
  import VerwaltungAnsicht from './VerwaltungAnsicht.svelte';

  let erlaubt = $derived(
    !geraet.telefon || BEREICHE.find((b) => b.id === route.aktiv)?.telefon !== false,
  );
</script>

{#if !erlaubt || route.aktiv === 'dashboard'}
  <Dashboard />
{:else if route.aktiv === 'aufgaben'}
  <AufgabenListe />
{:else if route.aktiv === 'pfade'}
  <PfadListe />
{:else if route.aktiv === 'verwaltung'}
  <VerwaltungAnsicht />
{:else if route.aktiv === 'aufgabe' && route.aufgabeId}
  {#key route.aufgabeId}
    <AufgabenDetail aufgabeId={route.aufgabeId} />
  {/key}
{/if}
