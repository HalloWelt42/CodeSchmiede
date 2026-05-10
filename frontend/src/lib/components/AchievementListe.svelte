<script lang="ts">
  /*
   * Zeigt alle Achievements als Grid. Erreichte mit Petrol-Akzent,
   * unerreichte gedimmt mit Fortschritts-Balken.
   */
  import { onMount } from 'svelte';
  import { progressApi } from '../api/ProgressApi';
  import type { Achievement } from '../api/ProgressApi';

  let liste = $state<Achievement[]>([]);
  let erreicht = $state(0);
  let gesamt = $state(0);
  let geladen = $state(false);

  onMount(async () => {
    try {
      const r = await progressApi.achievements();
      liste = r.eintraege;
      erreicht = r.erreicht_anzahl;
      gesamt = r.gesamt_anzahl;
    } catch {
      // ignorieren
    } finally {
      geladen = true;
    }
  });
</script>

<div class="achievements">
  <header class="kopf">
    <span class="titel">Achievements</span>
    <span class="zahlen num">{erreicht} / {gesamt}</span>
  </header>

  {#if geladen}
    <div class="grid">
      {#each liste as a (a.id)}
        <div class="kachel" class:erreicht={a.erreicht}>
          <i class="icon fa-solid {a.icon}" aria-hidden="true"></i>
          <div class="text">
            <strong>{a.titel}</strong>
            <small>{a.beschreibung}</small>
            {#if !a.erreicht && a.ziel > 1}
              <div class="balken">
                <span class="fuell" style="width: {(a.fortschritt / a.ziel) * 100}%"></span>
              </div>
              <small class="fortschritt num">{a.fortschritt} / {a.ziel}</small>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .achievements {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    border-radius: var(--radius-sm);
  }
  .kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: var(--sp-2);
    font-size: var(--fs-xs);
  }
  .titel {
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .zahlen {
    color: var(--accent);
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: var(--sp-2);
  }
  .kachel {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-2);
    display: flex;
    gap: var(--sp-2);
    align-items: flex-start;
    opacity: 0.55;
  }
  .kachel.erreicht {
    opacity: 1;
    border-color: var(--accent);
  }
  .icon {
    font-size: var(--fs-xl);
    color: var(--fg-mute);
    flex-shrink: 0;
    width: 32px;
    text-align: center;
  }
  .kachel.erreicht .icon {
    color: var(--accent);
  }
  .text {
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 0;
  }
  strong {
    font-size: var(--fs-sm);
    color: var(--fg);
  }
  small {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    font-family: var(--quick);
  }
  .balken {
    height: 4px;
    background: var(--bg);
    border: 1px solid var(--border);
    margin-top: 4px;
  }
  .fuell {
    display: block;
    height: 100%;
    background: var(--accent);
  }
  .fortschritt {
    color: var(--fg-mute);
  }
</style>
