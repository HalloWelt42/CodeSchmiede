<script lang="ts">
  /*
   * Generisches Bestaetigungs-Modal. Kein window.confirm, kein
   * Browser-Dialog -- alles im App-Stil. Tastatur: Esc schliesst,
   * Enter bestaetigt.
   */
  interface Props {
    offen: boolean;
    titel: string;
    nachricht: string;
    bestaetigen_text?: string;
    abbrechen_text?: string;
    danger?: boolean;
    onBestaetigen: () => void;
    onAbbrechen: () => void;
  }

  let {
    offen,
    titel,
    nachricht,
    bestaetigen_text = 'Bestätigen',
    abbrechen_text = 'Abbrechen',
    danger = false,
    onBestaetigen,
    onAbbrechen,
  }: Props = $props();

  function tastenanschlag(e: KeyboardEvent): void {
    if (!offen) return;
    if (e.key === 'Escape') {
      e.preventDefault();
      onAbbrechen();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      onBestaetigen();
    }
  }
</script>

<svelte:window on:keydown={tastenanschlag} />

{#if offen}
  <div class="overlay" onclick={onAbbrechen} role="presentation">
    <div class="dialog" onclick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
      <header>
        <i class="fa-solid {danger ? 'fa-triangle-exclamation' : 'fa-circle-question'}" aria-hidden="true"></i>
        <h2>{titel}</h2>
      </header>
      <p class="nachricht">{nachricht}</p>
      <footer>
        <button class="abbrechen" onclick={onAbbrechen}>{abbrechen_text}</button>
        <button class="bestaetigen" class:danger onclick={onBestaetigen}>{bestaetigen_text}</button>
      </footer>
    </div>
  </div>
{/if}

<style>
  .overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(2px);
  }
  .dialog {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-4);
    max-width: 460px;
    width: calc(100% - var(--sp-5));
    box-shadow: var(--shadow-lg);
  }
  header {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    margin-bottom: var(--sp-3);
  }
  header i {
    color: var(--orange);
    font-size: var(--fs-lg);
  }
  h2 {
    margin: 0;
    font-size: var(--fs-md);
    font-weight: 600;
    color: var(--fg);
  }
  .nachricht {
    margin: 0 0 var(--sp-4);
    color: var(--fg-dim);
    font-family: var(--quick);
    line-height: 1.6;
  }
  footer {
    display: flex;
    gap: var(--sp-2);
    justify-content: flex-end;
  }
  button {
    padding: 8px 16px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .abbrechen {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
  }
  .abbrechen:hover {
    border-color: var(--fg);
    color: var(--fg);
  }
  .bestaetigen {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
  }
  .bestaetigen:hover {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .bestaetigen.danger {
    background: color-mix(in srgb, var(--red) 14%, transparent);
    border-color: var(--red);
    color: var(--red);
  }
  .bestaetigen.danger:hover {
    background: color-mix(in srgb, var(--red) 22%, transparent);
  }
</style>
