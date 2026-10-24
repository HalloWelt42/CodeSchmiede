<script lang="ts">
  /*
   * Rahmen jeder Übersichtsseite: der Kopf (Titel, Aktionen, Reiter,
   * Kennzahlen, Filter) bleibt stehen, nur der Inhalt darunter rollt.
   * Die Seite selbst rollt nie.
   *
   * Nutzung:
   *   <Seite titel="Aufgaben">
   *     {#snippet lead()}...{/snippet}       optional, Zeile unter dem Titel
   *     {#snippet aktionen()}...{/snippet}   optional, rechts neben dem Titel
   *     {#snippet kopf()}...{/snippet}       optional, Reiter/Filter im festen Kopf
   *     ...Inhalt (rollt)
   *   </Seite>
   */
  import type { Snippet } from 'svelte';

  interface Props {
    titel: string;
    lead?: Snippet;
    aktionen?: Snippet;
    kopf?: Snippet;
    children: Snippet;
  }
  let { titel, lead, aktionen, kopf, children }: Props = $props();
</script>

<div class="seite">
  <header class="seiten-kopf">
    <div class="titelzeile">
      <div class="titel">
        <h1>{titel}</h1>
        {#if lead}<p class="lead">{@render lead()}</p>{/if}
      </div>
      {#if aktionen}<div class="aktionen">{@render aktionen()}</div>{/if}
    </div>
    {#if kopf}{@render kopf()}{/if}
  </header>
  <div class="rollfeld">
    {@render children()}
  </div>
</div>

<style>
  .seite {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    min-height: 0;
    min-width: 0;
  }
  .seiten-kopf {
    flex: none;
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
    padding: var(--sp-3) var(--sp-4);
    border-bottom: 1px solid var(--border);
  }
  .titelzeile {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    min-width: 0;
  }
  .titel {
    min-width: 0;
  }
  h1 {
    margin: 0;
    font-size: var(--fs-xl);
    font-weight: 600;
    line-height: 1.2;
  }
  .lead {
    margin: 2px 0 0;
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }
  .aktionen {
    margin-left: auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: var(--sp-2);
  }
  .rollfeld {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
    overflow-x: clip;
    padding: var(--sp-3) var(--sp-4) var(--sp-4);
  }

  :global([data-geraet='telefon']) .seiten-kopf {
    gap: var(--sp-2);
    padding: var(--sp-2) var(--sp-3);
  }
  :global([data-geraet='telefon']) .titelzeile {
    flex-wrap: wrap;
  }
  :global([data-geraet='telefon']) .rollfeld {
    padding: var(--sp-2) var(--sp-3) var(--sp-3);
  }
</style>
