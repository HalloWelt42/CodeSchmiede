<script lang="ts">
  /*
   * Inhalt des Reiters "Musterlösungen" -- gemeinsam für alle
   * Aufgabentypen. Der Server gibt die Lösungen erst nach dem Bestehen
   * oder nach dem Aufgeben frei; vorher steht hier, was Aufgeben kostet.
   *
   * `freigegeben` setzt die Elternansicht nach einem Bestehen auf true;
   * nach dem Aufgeben setzt der Bereich es selbst.
   */
  import { aufgabenApi } from '../api/AufgabenApi';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import type { Musterloesung } from '../types/Aufgabe';
  import ConfirmModal from './ConfirmModal.svelte';

  interface Props {
    aufgabeId: string;
    freigegeben: boolean;
  }
  let { aufgabeId, freigegeben = $bindable() }: Props = $props();

  let loesungen = $state<Musterloesung[] | null>(null);
  let fehler = $state<string | null>(null);
  let nachfrage_offen = $state(false);

  $effect(() => {
    if (freigegeben && loesungen === null) {
      aufgabenStore
        .ladeMusterloesungen(aufgabeId)
        .then((ml) => (loesungen = ml))
        .catch((e) => (fehler = (e as Error).message));
    }
  });

  async function aufgeben(): Promise<void> {
    nachfrage_offen = false;
    try {
      await aufgabenApi.aufgeben(aufgabeId);
      freigegeben = true;
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }
</script>

{#if fehler}
  <p class="fehler">{fehler}</p>
{:else if !freigegeben}
  <div class="aufgeben">
    <i class="fa-solid fa-lock" aria-hidden="true"></i>
    <p>Die Musterlösungen gibt es nach dem Bestehen. Wer sie vorher ansieht, gibt die Aufgabe auf: ein späteres Bestehen bringt dann keine Punkte mehr.</p>
    <button class="aufgeben-btn" onclick={() => (nachfrage_offen = true)}>
      <i class="fa-solid fa-flag" aria-hidden="true"></i>
      Aufgeben und Lösungen ansehen
    </button>
  </div>
{:else if loesungen}
  <div class="muster-liste">
    {#each loesungen as ml (ml.variante)}
      <details class="muster-eintrag" open>
        <summary>{ml.variante}</summary>
        <pre><code>{ml.code}</code></pre>
      </details>
    {/each}
  </div>
{/if}

<ConfirmModal
  offen={nachfrage_offen}
  titel="Aufgabe aufgeben?"
  nachricht="Du siehst die Musterlösungen sofort. Bestehst du die Aufgabe danach, gibt es dafür keine Punkte mehr. Bereits erreichte Punkte bleiben."
  bestaetigen_text="Aufgeben"
  abbrechen_text="Weiter üben"
  danger={true}
  onBestaetigen={aufgeben}
  onAbbrechen={() => (nachfrage_offen = false)}
/>

<style>
  .fehler {
    margin: var(--sp-3);
    color: var(--red);
  }
  .aufgeben {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--sp-3);
    padding: var(--sp-4);
    color: var(--fg-dim);
  }
  .aufgeben > i { color: var(--fg-mute); font-size: var(--fs-lg); }
  .aufgeben p { margin: 0; font-family: var(--quick); }
  .aufgeben-btn {
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
    border-color: var(--orange);
    color: var(--orange);
  }
  .muster-liste {
    padding: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .muster-eintrag {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-2) var(--sp-3);
  }
  .muster-eintrag summary {
    cursor: pointer;
    color: var(--accent);
    text-transform: uppercase;
    font-size: var(--fs-xs);
    letter-spacing: 0.05em;
    padding: var(--sp-1) 0;
  }
  .muster-eintrag pre {
    margin: var(--sp-2) 0 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    line-height: 1.5;
    color: var(--fg);
    background: var(--bg);
    padding: var(--sp-2);
    border: 1px solid var(--border);
    overflow-x: auto;
    white-space: pre;
    border-radius: var(--radius-sm);
    max-height: 280px;
    overflow-y: auto;
  }
  .muster-eintrag pre code {
    background: transparent;
    border: none;
    padding: 0;
    color: inherit;
    font-size: inherit;
  }
</style>
