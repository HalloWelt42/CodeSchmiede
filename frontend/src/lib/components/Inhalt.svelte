<script lang="ts">
  /*
   * Inhalt nach Route. Übersichten gibt es je Gerät als eigene Ansicht,
   * die Aufgabe selbst ist geteilt (ihre Spalten werden am Telefon zu
   * drei Schritten). Bereiche, die nur am Rechner gelten
   * (navigation.ts), fallen am Telefon auf die Startseite zurück.
   */
  import { route } from '../stores/RouteStore.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';
  import { BEREICHE } from '../navigation';
  import Dashboard from './Dashboard.svelte';
  import ErfolgeSeite from './ErfolgeSeite.svelte';
  import SpieleSeite from './SpieleSeite.svelte';
  import TelefonSpiele from './telefon/TelefonSpiele.svelte';
  import AufgabenListe from './AufgabenListe.svelte';
  import PfadListe from './PfadListe.svelte';
  import AufgabenDetail from './AufgabenDetail.svelte';
  import VerwaltungAnsicht from './VerwaltungAnsicht.svelte';
  import TelefonStart from './telefon/TelefonStart.svelte';
  import TelefonAufgaben from './telefon/TelefonAufgaben.svelte';
  import TelefonPfade from './telefon/TelefonPfade.svelte';

  let erlaubt = $derived(
    !geraet.telefon || BEREICHE.find((b) => b.id === route.aktiv)?.telefon !== false,
  );
</script>

{#if route.aktiv === 'aufgabe' && route.aufgabeId}
  {#key route.aufgabeId}
    <AufgabenDetail aufgabeId={route.aufgabeId} />
  {/key}
{:else if route.aktiv === 'erfolge'}
  <ErfolgeSeite />
{:else if geraet.telefon}
  {#if route.aktiv === 'aufgaben'}
    <TelefonAufgaben />
  {:else if route.aktiv === 'pfade'}
    <TelefonPfade />
  {:else if route.aktiv === 'spiele'}
    <TelefonSpiele />
  {:else}
    <TelefonStart />
  {/if}
{:else if !erlaubt || route.aktiv === 'dashboard'}
  <Dashboard />
{:else if route.aktiv === 'aufgaben'}
  <AufgabenListe />
{:else if route.aktiv === 'pfade'}
  <PfadListe />
{:else if route.aktiv === 'spiele'}
  <SpieleSeite />
{:else if route.aktiv === 'verwaltung'}
  <VerwaltungAnsicht />
{/if}
