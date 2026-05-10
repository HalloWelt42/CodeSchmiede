<script lang="ts">
  import ActionCard from './ActionCard.svelte';
  import { route } from '../stores/RouteStore.svelte';
</script>

<div class="dashboard">
  <header class="kopf">
    <h1>Willkommen zurück</h1>
    <p class="lead">
      Frischer Start in der Codeschmiede. Drei Aufgaben warten im Pfad
      <strong>Python-Grundlagen</strong>.
    </p>
  </header>

  <div class="cards">
    <ActionCard
      icon="fa-bullseye"
      titel="Tagesziel"
      wert="3 neu"
      hinweis="Heute keine Wiederholungen fällig. Schnapp dir eine frische Aufgabe."
      cta="Aufgaben öffnen"
      onClick={() => route.setze('aufgaben')}
    />

    <ActionCard
      icon="fa-clock-rotate-left"
      titel="Letzte Aufgabe"
      wert="-"
      hinweis="Noch keine Aufgabe begonnen. Starte mit FizzBuzz."
      cta="Pfad starten"
      onClick={() => route.setze('pfade')}
    />

    <ActionCard
      icon="fa-fire"
      titel="Streak"
      wert="0 Tage"
      hinweis="Löse heute deine erste Aufgabe, um die Serie zu starten."
      cta="Erste Aufgabe"
      onClick={() => route.setze('aufgaben')}
    />
  </div>
</div>

<style>
  .dashboard {
    padding: var(--sp-5) var(--sp-5) var(--sp-4);
    overflow-y: auto;
  }
  .kopf {
    margin-bottom: var(--sp-5);
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
    font-size: var(--fs-md);
    max-width: 720px;
  }
  .lead strong {
    color: var(--accent);
    font-weight: 600;
  }
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--sp-3);
  }
</style>
