<script lang="ts">
  /*
   * Band unter der Kopfleiste, sobald der Server eine neue Fassung meldet.
   * Sagt, wann sie von selbst lädt, und bietet das sofortige Neuladen an.
   */
  import { fassung } from '../stores/FassungStore.svelte';
</script>

{#if fassung.neu}
  <div class="band" role="status">
    <i class="fa-solid fa-rotate" aria-hidden="true"></i>
    <span class="text">
      <strong>Neue Fassung {fassung.neu} ist da.</strong>
      {fassung.ruhig()
        ? 'Beim nächsten Seitenwechsel lädt die Codeschmiede sie von selbst.'
        : 'Sie lädt erst von selbst, wenn hier nichts mehr offen ist (Prüfung, ungeprüfter Code, Editor).'}
    </span>
    <button class="neu-laden" onclick={() => location.reload()}>
      <i class="fa-solid fa-rotate" aria-hidden="true"></i>
      Jetzt neu laden
    </button>
  </div>
{/if}

<style>
  .band {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    flex-wrap: wrap;
    padding: var(--sp-2) var(--sp-4);
    background: color-mix(in srgb, var(--accent) 10%, transparent);
    border-bottom: 1px solid var(--accent);
    color: var(--fg);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .band > i {
    color: var(--accent);
  }
  .text {
    flex: 1 1 auto;
    min-width: 0;
  }
  .neu-laden {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 6px 14px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .neu-laden:hover {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
</style>
