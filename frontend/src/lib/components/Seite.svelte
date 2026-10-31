<script lang="ts">
  /*
   * Rahmen jeder Übersichtsseite: der Kopf (Titel, Aktionen, Reiter,
   * Kennzahlen, Filter) bleibt stehen, nur der Inhalt darunter rollt.
   * Die Seite selbst rollt nie.
   *
   * Nutzung:
   *   <Seite titel="Aufgaben" lead="644 Aufgaben">
   *     {#snippet aktionen()}...{/snippet}   optional, rechts neben dem Titel
   *     {#snippet kopf()}...{/snippet}       optional, Reiter/Filter im festen Kopf
   *     ...Inhalt (rollt)
   *   </Seite>
   */
  import type { Snippet } from 'svelte';

  interface Props {
    titel: string;
    lead?: string;
    /** Inhalt ohne Innenabstand, etwa Tabellen, die bis an den Rand gehen */
    ohneRand?: boolean;
    aktionen?: Snippet;
    kopf?: Snippet;
    children: Snippet;
  }
  let { titel, lead, ohneRand = false, aktionen, kopf, children }: Props = $props();
</script>

<div class="seite">
  <header class="seiten-kopf">
    <div class="titelzeile">
      <h1>{titel}</h1>
      {#if lead}<span class="lead">{lead}</span>{/if}
      {#if aktionen}<div class="aktionen">{@render aktionen()}</div>{/if}
    </div>
    {#if kopf}{@render kopf()}{/if}
  </header>
  <div class="rollfeld" class:ohne-rand={ohneRand}>
    {@render children()}
  </div>
</div>

<style>
  :global([data-geraet='telefon']) .seiten-kopf {
    padding: var(--sp-2) var(--rahmen-rand);
  }
  :global([data-geraet='telefon']) .titelzeile {
    flex-wrap: wrap;
    row-gap: 2px;
  }
  :global([data-geraet='telefon']) .lead {
    flex-basis: 100%;
    white-space: normal;
  }
  :global([data-geraet='telefon']) .rollfeld:not(.ohne-rand) {
    padding: var(--sp-2) var(--rahmen-rand) var(--rahmen-rand);
  }
</style>
