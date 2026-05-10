<script lang="ts">
  import { mockPfad, mockAufgaben } from '../mocks/aufgaben';

  function findeTitel(id: string): string {
    return mockAufgaben.find((a) => a.id === id)?.titel ?? id;
  }
</script>

<div class="liste">
  <header class="kopf">
    <h1>Pfade</h1>
    <p class="lead">Didaktisch geordnete Aufgaben-Reihen.</p>
  </header>

  <article class="pfad-karte">
    <header class="pfad-kopf">
      <i class="fa-solid fa-route" aria-hidden="true"></i>
      <div class="info">
        <span class="titel">{mockPfad.titel}</span>
        <span class="anzahl num">{mockPfad.reihenfolge.length} Aufgaben</span>
      </div>
    </header>

    <p class="beschreibung">{mockPfad.beschreibung}</p>

    <ol class="schritte">
      {#each mockPfad.reihenfolge as id, i (id)}
        <li>
          <span class="nummer num">{i + 1}</span>
          <div class="text">
            <span class="aufgabe-id">{id}</span>
            <span class="aufgabe-titel">{findeTitel(id)}</span>
          </div>
          <i class="fa-solid fa-circle status-neu" aria-hidden="true"></i>
        </li>
      {/each}
    </ol>

    <div class="fortschritt">
      <span class="balken"><span class="fuell" style="width: 0%"></span></span>
      <span class="dim num">0 / {mockPfad.reihenfolge.length} gelöst</span>
    </div>
  </article>
</div>

<style>
  .liste {
    padding: var(--sp-5) var(--sp-5) var(--sp-4);
    overflow-y: auto;
  }
  .kopf {
    margin-bottom: var(--sp-4);
  }
  h1 {
    margin: 0 0 var(--sp-2);
    font-size: var(--fs-xl);
    font-weight: 600;
  }
  .lead {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .dim {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }

  .pfad-karte {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-4);
    max-width: 760px;
  }
  .pfad-kopf {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    margin-bottom: var(--sp-3);
  }
  .pfad-kopf i {
    color: var(--accent);
    font-size: var(--fs-xl);
  }
  .info {
    display: flex;
    align-items: baseline;
    gap: var(--sp-3);
    flex: 1;
  }
  .titel {
    font-size: var(--fs-lg);
    font-weight: 600;
  }
  .anzahl {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .beschreibung {
    color: var(--fg-dim);
    font-family: var(--quick);
    margin: 0 0 var(--sp-4);
    line-height: 1.65;
  }
  .schritte {
    list-style: none;
    padding: 0;
    margin: 0 0 var(--sp-4);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
    counter-reset: schritte;
  }
  .schritte li {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    background: var(--bg-card);
    border: 1px solid var(--border);
  }
  .nummer {
    width: 32px;
    height: 32px;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-elev);
    color: var(--accent);
    border: 1px solid var(--border);
    font-size: var(--fs-md);
  }
  .text {
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    min-width: 0;
  }
  .aufgabe-id {
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg-mute);
  }
  .aufgabe-titel {
    font-size: var(--fs-md);
    font-weight: 500;
  }
  .status-neu {
    color: var(--fg-mute);
    font-size: 10px;
  }
  .fortschritt {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
  }
  .balken {
    flex: 1;
    height: 8px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    overflow: hidden;
  }
  .fuell {
    display: block;
    height: 100%;
    background: var(--accent);
  }
</style>
