<script lang="ts">
  /*
   * Kursübersicht am Rechner: Sprachen als Reiter, Kapitel in Blöcken mit Stand, rechts das gewählte Kapitel mit
   * Lernzielen, Ablauf (Einführung, Übungen, Projekt), Vertiefung und den Wegen hinein (Einführung, Üben, Merkblatt,
   * Kurztest). Gesperrte Kapitel lassen sich per Kurztest überspringen.
   */
  import { onMount } from 'svelte';
  import type { KapitelSicht } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import Sammelkarte from './Sammelkarte.svelte';

  onMount(() => {
    void kursStore.laden(true);
  });

  const MARKE: Record<KapitelSicht['stand'], [string, string]> = {
    fertig: ['fa-circle-check', 'Fertig'],
    uebersprungen: ['fa-forward', 'Per Kurztest'],
    aktuell: ['fa-circle-play', 'Weiter hier'],
    offen: ['fa-circle', 'Offen'],
    zu: ['fa-lock', 'Noch zu'],
  };

  let gewaehlt = $state<string | null>(null);
  let kurs = $derived(kursStore.kurs);
  let alle = $derived(kursStore.alleKapitel(kurs));
  let kapitel = $derived(alle.find((k) => k.einfuehrung === gewaehlt) ?? kursStore.weiter ?? alle[0] ?? null);
  let geschafft = $derived(alle.filter((k) => k.stand === 'fertig' || k.stand === 'uebersprungen').length);

  function anteil(k: KapitelSicht): number {
    const gesamt = k.abschnitte + k.uebungen.length + k.projekt.length;
    if (k.stand === 'fertig' || k.stand === 'uebersprungen' || !gesamt) return k.stand === 'zu' || k.stand === 'offen' ? 0 : 100;
    const erledigt = k.abschnitte_fertig + [...k.uebungen, ...k.projekt].filter((u) => u.geloest).length;
    return Math.round((100 * erledigt) / gesamt);
  }
  const standText = (k: KapitelSicht) =>
    k.stand === 'zu' ? `Einführung, ${k.uebungen.length} Übungen${k.kurztest ? ', Kurztest' : ''}`
      : k.stand === 'uebersprungen' ? 'per Kurztest übersprungen, Einführung lesbar'
      : `Einführung ${k.abschnitte_fertig} von ${k.abschnitte}, Übungen ${k.uebungen.filter((u) => u.geloest).length} von ${k.uebungen.length}`;
  const naechsteUebung = (k: KapitelSicht) => [...k.uebungen, ...k.projekt].find((u) => !u.geloest) ?? k.uebungen[0];
</script>

<div class="seite" data-sprache={kursStore.sprache}>
  <header class="seiten-kopf">
    <div class="titelzeile">
      <h1>Kurs</h1>
      <span class="lead">Von null an, eine neue Sache nach der anderen: erst die Einführung, dann üben</span>
      {#if kursStore.weiter}
        {@const w = kursStore.weiter}
        <div class="aktionen"><button class="knopf voll kuerzbar" onclick={() => route.setze('einfuehrung', w.einfuehrung)}><i class="fa-solid fa-play" aria-hidden="true"></i><span>Weiter: {w.titel}</span></button></div>
      {/if}
    </div>
    <div class="titelzeile kurs-kopf">
      <div class="sprach-reiter">
        {#each kursStore.kurse as k (k.sprache)}
          <button data-sprache={k.sprache} class:aktiv={k.sprache === kursStore.sprache} onclick={() => { kursStore.waehleSprache(k.sprache); gewaehlt = null; }}><span class="punkt"></span>{k.titel}</button>
        {/each}
      </div>
      {#if kurs}
        <div class="kennzahlen">
          <div class="kennzahl"><span class="num">{geschafft}</span><small>Kapitel fertig</small></div>
          <div class="kennzahl"><span class="num">{alle.length}</span><small>Kapitel</small></div>
        </div>
      {/if}
    </div>
  </header>

  {#if kursStore.fehler}
    <div class="rollfeld"><div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{kursStore.fehler}</span></div></div>
  {:else if kursStore.geladen && !kurs}
    <div class="rollfeld"><p class="dim">Noch kein Kurs eingelesen.</p></div>
  {:else if kurs}
    <div class="kurs-seite">
      <section class="spalte">
        <div class="rollfeld">
          {#each kurs.bloecke as b (b.titel)}
            <div class="kapitel-block">
              <div class="gruppe">{b.titel} <span class="num">{b.kapitel.length}</span></div>
              {#each b.kapitel as k (k.einfuehrung)}
                <button class="kapitel" class:gewaehlt={k.einfuehrung === kapitel?.einfuehrung} class:zu={k.stand === 'zu'} onclick={() => (gewaehlt = k.einfuehrung)}>
                  <span class="mini-karte" class:leer={k.stand === 'zu'}>
                    {#if k.stand !== 'zu' && k.bild?.url}<img src={k.bild.url} alt="" />{:else}<i class="fa-solid {k.stand === 'zu' ? 'fa-lock' : 'fa-graduation-cap'}" aria-hidden="true"></i>{/if}
                  </span>
                  <span class="kapitel-text">
                    <b><span class="nr">{k.nr}</span>{k.titel}</b>
                    <span class="kapitel-stand"><span class="balken"><span style="width:{anteil(k)}%"></span></span>{standText(k)}</span>
                  </span>
                  <span class="kapitel-marke {k.stand}"><i class="fa-solid {MARKE[k.stand][0]}" aria-hidden="true"></i>{MARKE[k.stand][1]}</span>
                </button>
              {/each}
            </div>
          {/each}
        </div>
      </section>

      <section class="spalte">
        <div class="rollfeld">
          {#if kapitel}
            {@const k = kapitel}
            {@const zu = k.stand === 'zu'}
            <div class="detail-kopf">
              <Sammelkarte kapitel={k} sprache={kursStore.sprache} sprachTitel={kurs.titel} breite={112} />
              <div>
                <div class="kapitel-marke {k.stand}"><i class="fa-solid {MARKE[k.stand][0]}" aria-hidden="true"></i>Kapitel {k.nr}, {MARKE[k.stand][1]}</div>
                <h2>{k.titel}</h2>
                <p>{k.kurz}</p>
              </div>
            </div>
            <div class="block">
              <div class="block-kopf"><span>Danach kannst du</span></div>
              <ul class="lernziele">{#each k.lernziele as z (z)}<li><i class="fa-solid fa-check" aria-hidden="true"></i><span>{z}</span></li>{/each}</ul>
            </div>
            <div class="block">
              <div class="block-kopf"><span>Ablauf des Kapitels</span></div>
              <div class="schritt-liste">
                <div class="schritt" class:zu><span class="t">Einführung, {k.abschnitte} Abschnitte</span><span class="art">{k.abschnitte_fertig} fertig</span>
                  <i class="fa-solid {k.abschnitte_fertig === k.abschnitte ? 'fa-circle-check' : 'fa-book-open'}" aria-hidden="true"></i></div>
                {#each k.uebungen as u, i (u.id)}
                  <button class="schritt uebung" class:zu={!k.uebungen_offen} disabled={!k.uebungen_offen} onclick={() => route.setze('aufgabe', u.id, k.einfuehrung)}>
                    <span class="t">Übung {i + 1}: {u.titel}</span>
                    <i class="fa-solid {u.geloest ? 'fa-circle-check' : k.uebungen_offen ? 'fa-circle' : 'fa-lock'}" style={u.geloest ? 'color:var(--green)' : ''} aria-hidden="true"></i>
                  </button>
                {/each}
                {#each k.projekt as u (u.id)}
                  <button class="schritt uebung" class:zu={!k.uebungen_offen} disabled={!k.uebungen_offen} onclick={() => route.setze('aufgabe', u.id, k.einfuehrung)}>
                    <span class="t">Kapitelprojekt: {u.titel}</span><span class="art">Projekt wächst</span>
                    <i class="fa-solid {u.geloest ? 'fa-circle-check' : k.uebungen_offen ? 'fa-circle' : 'fa-lock'}" aria-hidden="true"></i>
                  </button>
                {/each}
              </div>
            </div>
            {#if k.vertiefung.length}
              <div class="block">
                <div class="block-kopf"><span>Vertiefung aus dem Bestand, freiwillig</span></div>
                <div class="chips">{#each k.vertiefung as v (v.id)}<button class="chip" disabled={!k.uebungen_offen} onclick={() => route.setze('aufgabe', v.id, k.einfuehrung)}>{v.titel}</button>{/each}</div>
              </div>
            {/if}
            <div class="detail-aktionen" style="margin-top:var(--sp-3)">
              {#if zu}
                {#if k.kurztest}<button class="knopf primaer" onclick={() => route.setze('kurztest', k.einfuehrung)}><i class="fa-solid fa-forward" aria-hidden="true"></i>Kann ich schon: Kurztest</button>{/if}
                <span class="dim" style="font-size:var(--fs-sm);align-self:center">Öffnet sich nach Kapitel {k.nr - 1}</span>
              {:else}
                <button class="knopf voll" onclick={() => route.setze('einfuehrung', k.einfuehrung)}><i class="fa-solid fa-book-open" aria-hidden="true"></i>Einführung</button>
                <button class="knopf" disabled={!k.uebungen_offen || !k.uebungen.length} onclick={() => { const u = naechsteUebung(k); if (u) route.setze('aufgabe', u.id, k.einfuehrung); }}><i class="fa-solid fa-code" aria-hidden="true"></i>Üben</button>
                <button class="knopf" onclick={() => route.setze('merkblatt', k.einfuehrung)}><i class="fa-solid fa-note-sticky" aria-hidden="true"></i>Merkblatt</button>
                {#if k.kurztest && k.stand !== 'fertig' && k.stand !== 'uebersprungen'}<button class="knopf" onclick={() => route.setze('kurztest', k.einfuehrung)}><i class="fa-solid fa-forward" aria-hidden="true"></i>Kurztest</button>{/if}
              {/if}
            </div>
          {/if}
        </div>
      </section>
    </div>
  {/if}
</div>

<style>
  .kurs-kopf { flex-wrap: wrap; gap: var(--sp-2); }
  .kurs-kopf .kennzahlen { margin-left: auto; }
  .kapitel { width: 100%; text-align: left; color: var(--fg); font: inherit; }
  .kapitel:hover:not(:disabled) { color: var(--fg); background: var(--bg-card-2); }
  .mini-karte img { width: 100%; height: 100%; object-fit: contain; }
  .uebung { width: 100%; background: transparent; color: var(--fg); cursor: pointer; text-align: left; font: inherit; font-size: var(--fs-sm); }
  .uebung:hover:not(:disabled) { background: var(--bg-card-2); color: var(--fg); }
  .chip { cursor: pointer; background: transparent; }
</style>
