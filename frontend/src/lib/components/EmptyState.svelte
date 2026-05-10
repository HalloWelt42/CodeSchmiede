<script lang="ts">
  /*
   * Generischer Empty-State. Verwendet beim Erststart (DB leer), bei
   * leerer Suche oder bei Fehlern.
   */
  interface Props {
    icon?: string;
    titel: string;
    hinweis?: string;
    ctaText?: string;
    ctaAction?: () => void;
  }

  let { icon = 'fa-flask', titel, hinweis, ctaText, ctaAction }: Props = $props();
</script>

<div class="empty">
  <i class="fa-solid {icon}" aria-hidden="true"></i>
  <h2>{titel}</h2>
  {#if hinweis}
    <p class="hinweis">{hinweis}</p>
  {/if}
  {#if ctaText && ctaAction}
    <button class="cta" onclick={ctaAction}>{ctaText}</button>
  {/if}
</div>

<style>
  .empty {
    padding: var(--sp-6) var(--sp-5);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: var(--sp-3);
    text-align: center;
    color: var(--fg-dim);
    max-width: 480px;
    margin: var(--sp-5) auto;
  }
  i {
    font-size: var(--fs-xxl);
    color: var(--fg-mute);
    margin-bottom: var(--sp-2);
  }
  h2 {
    margin: 0;
    color: var(--fg);
    font-size: var(--fs-lg);
    font-weight: 600;
  }
  .hinweis {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
    line-height: 1.6;
  }
  .cta {
    margin-top: var(--sp-3);
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: var(--sp-2) var(--sp-4);
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .cta:hover {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
</style>
