<script lang="ts">
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import ActionCard from './ActionCard.svelte';
  import EmptyState from './EmptyState.svelte';

  onMount(async () => {
    if (aufgabenStore.liste.length === 0) await aufgabenStore.ladeListe();
    if (!progressStore.gesamt) await progressStore.ladeAlles();
  });

  function findeTitel(id: string | null): string {
    if (!id) return '-';
    return aufgabenStore.findeKurz(id)?.titel ?? id;
  }

  function tageszielText(): string {
    const h = progressStore.heute;
    if (!h) return '...';
    const f = h.faellige_wiederholungen.length;
    if (f > 0) return `${f} fällig`;
    return progressStore.gesamt?.aufgaben_neu
      ? `${progressStore.gesamt.aufgaben_neu} neu`
      : 'erledigt';
  }

  function tageszielHinweis(): string {
    const h = progressStore.heute;
    if (!h) return 'Lade ...';
    if (h.faellige_wiederholungen.length > 0) {
      return `Heute sind ${h.faellige_wiederholungen.length} Wiederholungen fällig.`;
    }
    if (h.vorgeschlagene_neue) {
      return `Vorschlag: ${findeTitel(h.vorgeschlagene_neue)}.`;
    }
    return 'Alle Aufgaben sind gelöst.';
  }

  function letzteWert(): string {
    if (!progressStore.heute?.letzte_aufgabe) return '-';
    return findeTitel(progressStore.heute.letzte_aufgabe);
  }

  function letzteHinweis(): string {
    if (!progressStore.heute?.letzte_aufgabe) {
      return 'Noch keine Aufgabe begonnen.';
    }
    const p = progressStore.proAufgabe[progressStore.heute.letzte_aufgabe];
    if (!p) return 'Direkt weitermachen.';
    if (p.status === 'geloest') return `Gelöst nach ${p.versuche} Versuch(en).`;
    return `In Arbeit (${p.versuche} Versuch(e)).`;
  }

  function streakWert(): string {
    const s = progressStore.streak;
    if (!s) return '-';
    return s.aktuell === 1 ? '1 Tag' : `${s.aktuell} Tage`;
  }

  function streakHinweis(): string {
    const s = progressStore.streak;
    if (!s) return 'Lade ...';
    if (s.aktuell === 0) return 'Löse heute eine Aufgabe, um die Serie zu starten.';
    if (s.laengster > s.aktuell) return `Längste Serie: ${s.laengster} Tage.`;
    return 'Persönliche Bestmarke!';
  }

  function gesamtFortschrittsBalken(): { prozent: number; text: string } {
    const g = progressStore.gesamt;
    if (!g || g.aufgaben_gesamt === 0) return { prozent: 0, text: '0 / 0' };
    const prozent = Math.round((g.aufgaben_geloest / g.aufgaben_gesamt) * 100);
    return { prozent, text: `${g.aufgaben_geloest} / ${g.aufgaben_gesamt} gelöst` };
  }

  function oeffneVorgeschlagen(): void {
    const id = progressStore.heute?.vorgeschlagene_neue
      ?? progressStore.heute?.faellige_wiederholungen[0];
    if (id) route.setze('aufgabe', id);
    else route.setze('aufgaben');
  }

  function oeffneLetzte(): void {
    const id = progressStore.heute?.letzte_aufgabe;
    if (id) route.setze('aufgabe', id);
    else route.setze('aufgaben');
  }

  function oeffneStreak(): void {
    const id = progressStore.heute?.vorgeschlagene_neue;
    if (id) route.setze('aufgabe', id);
    else route.setze('aufgaben');
  }
</script>

<div class="dashboard">
  {#if aufgabenStore.liste.length === 0 && !aufgabenStore.ladenListe}
    <EmptyState
      icon="fa-hammer"
      titel="Willkommen in der Codeschmiede"
      hinweis="Es sind noch keine Aufgaben vorhanden. Lege eine erste an unter aufgaben/python/NNN-id/aufgabe.md -- die Vorlage steht in docs/AUFGABEN-FORMAT.md. Das Backend indiziert sie automatisch."
      ctaText="Aufgaben-Liste öffnen"
      ctaAction={() => route.setze('aufgaben')}
    />
  {:else}

  <header class="kopf">
    <h1>Willkommen zurück</h1>
    <p class="lead">
      {#if progressStore.gesamt}
        {progressStore.gesamt.bestandene_submissions} von
        {progressStore.gesamt.submissions_gesamt} Submissions bestanden.
      {:else}
        Frischer Start in der Codeschmiede.
      {/if}
    </p>
  </header>

  <div class="cards">
    <ActionCard
      icon="fa-bullseye"
      titel="Tagesziel"
      wert={tageszielText()}
      hinweis={tageszielHinweis()}
      cta={progressStore.heute?.faellige_wiederholungen.length ? 'Wiederholen' : 'Aufgabe öffnen'}
      onClick={oeffneVorgeschlagen}
    />

    <ActionCard
      icon="fa-clock-rotate-left"
      titel="Letzte Aufgabe"
      wert={letzteWert()}
      hinweis={letzteHinweis()}
      cta={progressStore.heute?.letzte_aufgabe ? 'Weitermachen' : 'Pfad starten'}
      onClick={oeffneLetzte}
    />

    <ActionCard
      icon="fa-fire"
      titel="Streak"
      wert={streakWert()}
      hinweis={streakHinweis()}
      cta={progressStore.streak?.aktuell ? 'Heute weiter' : 'Erste Aufgabe'}
      onClick={oeffneStreak}
    />
  </div>

  {#if progressStore.gesamt && progressStore.gesamt.aufgaben_gesamt > 0}
    {@const fb = gesamtFortschrittsBalken()}
    <section class="gesamt">
      <header class="gesamt-kopf">
        <span>Gesamtfortschritt</span>
        <span class="num dim">{fb.text}</span>
      </header>
      <div class="balken">
        <span class="fuell" style="width: {fb.prozent}%"></span>
      </div>
      <div class="aufschluesselung">
        <span class="chip status-geloest">
          <i class="fa-solid fa-check" aria-hidden="true"></i>
          {progressStore.gesamt.aufgaben_geloest} gelöst
        </span>
        <span class="chip status-in_arbeit">
          <i class="fa-solid fa-pen" aria-hidden="true"></i>
          {progressStore.gesamt.aufgaben_in_arbeit} in Arbeit
        </span>
        <span class="chip status-neu">
          <i class="fa-regular fa-circle" aria-hidden="true"></i>
          {progressStore.gesamt.aufgaben_neu} neu
        </span>
      </div>
    </section>
  {/if}
  {/if}
</div>

<style>
  .dashboard {
    padding: var(--sp-5);
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
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--sp-3);
    margin-bottom: var(--sp-5);
  }

  .gesamt {
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    padding: var(--sp-4);
    max-width: 720px;
  }
  .gesamt-kopf {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: var(--sp-2);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
  }
  .dim {
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }
  .balken {
    height: 10px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    overflow: hidden;
    margin-bottom: var(--sp-3);
  }
  .fuell {
    display: block;
    height: 100%;
    background: var(--accent);
    transition: width 0.4s ease-out;
  }
  .aufschluesselung {
    display: flex;
    gap: var(--sp-2);
    flex-wrap: wrap;
  }
  .chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px var(--sp-2);
    border: 1px solid var(--border);
    background: var(--bg-card);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    border-radius: var(--radius-sm);
  }
  .chip.status-geloest {
    color: var(--green);
    border-color: var(--green);
  }
  .chip.status-in_arbeit {
    color: var(--orange);
    border-color: var(--orange);
  }
  .chip.status-neu {
    color: var(--fg-mute);
  }
</style>
