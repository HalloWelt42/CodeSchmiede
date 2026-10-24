<script lang="ts">
  /* Pfade am Rechner: nach Sprache gruppiert, aufklappbar mit allen Schritten. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { pfadeStore } from '../stores/PfadeStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { statusIcon, statusKlasse } from '../anzeige';
  import { nachSprache, pfadGeloest, pfadProzent, pfadSprache, pfadStand, type PfadStand } from '../pfade.svelte';
  import EmptyState from './EmptyState.svelte';
  import Seite from './Seite.svelte';

  onMount(async () => {
    await Promise.all([
      pfadeStore.liste.length === 0 ? pfadeStore.ladeListe() : null,
      aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : null,
      progressStore.gesamt ? null : progressStore.ladeAlles(),
    ]);
  });

  let suche = $state('');
  let sprache = $state('');
  let stand = $state<PfadStand | ''>('');
  let offen = $state<string | null>(null);

  let gefiltert = $derived(
    pfadeStore.liste.filter((p) => {
      if (sprache && pfadSprache(p) !== sprache) return false;
      if (stand && pfadStand(p) !== stand) return false;
      const q = suche.trim().toLowerCase();
      return !q || `${p.titel} ${p.beschreibung}`.toLowerCase().includes(q);
    }),
  );
  let gruppen = $derived(nachSprache(gefiltert, konfig.daten.sprachen.map((s) => s.id)));
</script>

<Seite titel="Pfade" lead="{pfadeStore.liste.length} didaktisch geordnete Reihen, nach Sprache gruppiert">
  {#snippet kopf()}
    <div class="filter">
      <label class="suche">
        <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
        <input type="text" placeholder="Pfad suchen" bind:value={suche} />
      </label>
      <select class="wahl" bind:value={sprache} aria-label="Sprache">
        <option value="">Alle Sprachen</option>
        {#each konfig.daten.sprachen as s (s.id)}<option value={s.id}>{s.titel}</option>{/each}
      </select>
      <select class="wahl" bind:value={stand} aria-label="Stand">
        <option value="">Alle Stände</option>
        <option value="offen">Nicht begonnen</option>
        <option value="begonnen">Begonnen</option>
        <option value="fertig">Abgeschlossen</option>
      </select>
    </div>
  {/snippet}

  {#if pfadeStore.laden}
    <p class="dim">Lade ...</p>
  {:else if pfadeStore.fehler}
    <EmptyState icon="fa-plug-circle-xmark" titel="Server nicht erreichbar" hinweis={pfadeStore.fehler} ctaText="Erneut versuchen" ctaAction={() => pfadeStore.ladeListe()} />
  {:else if gefiltert.length === 0}
    <EmptyState icon="fa-magnifying-glass" titel="Kein Pfad gefunden" hinweis="Passe Suche oder Auswahl an." />
  {:else}
    {#each gruppen as [sp, liste] (sp)}
      <div class="gruppe">{konfig.sprache(sp)?.titel ?? 'Sonstige'} <span class="num">{liste.length}</span></div>
      {#each liste as p (p.id)}
        {@const auf = offen === p.id}
        <div class="pfad" class:offen={auf}>
          <button class="pfad-zeile" onclick={() => (offen = auf ? null : p.id)} aria-expanded={auf}>
            <i class="fa-solid {auf ? 'fa-chevron-down' : 'fa-chevron-right'} chev" aria-hidden="true"></i>
            <b>{p.titel}</b>
            <span class="dim">{p.reihenfolge.length} Aufgaben</span>
            <span class="balken"><span style:width="{pfadProzent(p)}%"></span></span>
            <span class="dim num rechts-b">{pfadGeloest(p)} / {p.reihenfolge.length}</span>
          </button>
          {#if auf}
            <div class="schritte">
              <div class="pfad-text">{p.beschreibung}</div>
              {#each p.reihenfolge as id, i (id)}
                {@const st = progressStore.status(id)}
                <button class="schritt {statusKlasse(st)}" onclick={() => route.setze('aufgabe', id)}>
                  <span class="nr">{i + 1}</span>
                  <span class="t">{aufgabenStore.findeKurz(id)?.titel ?? id}</span>
                  <i class="fa-solid {statusIcon(st)}" aria-hidden="true"></i>
                </button>
              {/each}
            </div>
          {/if}
        </div>
      {/each}
    {/each}
  {/if}
</Seite>

<style>
  .pfad {
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    margin-bottom: 4px;
  }
  .pfad.offen { border-color: var(--accent); }
  .pfad-zeile {
    width: 100%;
    display: grid;
    grid-template-columns: 18px minmax(0, 1fr) 90px 140px 70px;
    gap: var(--sp-3);
    align-items: center;
    min-height: 40px;
    padding: 0 var(--sp-3);
    border: 0;
    border-radius: 0;
    background: transparent;
    color: var(--fg);
    font-size: var(--fs-md);
    text-align: left;
  }
  .pfad-zeile:hover:not(:disabled) { background: var(--bg-elev); border-color: transparent; }
  .pfad-zeile b {
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .pfad-zeile .dim { font-size: var(--fs-sm); }
  .chev { color: var(--fg-mute); font-size: 12px; }
  .schritte {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2px var(--sp-3);
    padding: var(--sp-2) var(--sp-3) var(--sp-3) 42px;
    border-top: 1px solid var(--border);
  }
  .pfad-text {
    grid-column: 1 / -1;
    font-size: var(--fs-sm);
    color: var(--fg-dim);
    margin-bottom: 4px;
    white-space: pre-line;
  }
  .schritt {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    min-height: 28px;
    min-width: 0;
    padding: 0 4px;
    border: 0;
    background: transparent;
    color: var(--fg);
    font-size: var(--fs-sm);
    text-align: left;
  }
  .schritt:hover:not(:disabled) { background: var(--bg-elev); border-color: transparent; }
  .nr {
    font-family: var(--num);
    font-size: 11px;
    color: var(--fg-mute);
    width: 20px;
    text-align: right;
    flex: none;
  }
  .t {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .schritt i {
    margin-left: auto;
    font-size: 11px;
    color: var(--fg-mute);
  }
  .schritt.geloest i { color: var(--green); }
  .schritt.arbeit i { color: var(--orange); }
</style>
