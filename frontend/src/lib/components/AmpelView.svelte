<script lang="ts">
  /*
   * Ampelschule (Steuerungsspiel) in der gemeinsamen Ansicht der Steuerungsspiele: dazu Sensoren, Signale und
   * Sterne als Hilfe, die Anlage von oben, der Signalplan, die Kennzahlen und die Klänge des Verkehrs.
   */
  import { spielApi } from '../api/SpielApi';
  import { klang } from '../steuerung/klang.svelte';
  import type { AmpelAnsicht, Kennzahlen, Wiedergabe } from '../types/Ampel';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import AmpelSzene from './steuerung/AmpelSzene.svelte';
  import Signalplan from './steuerung/Signalplan.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';

  const DT = 0.25;
  // Sensoren in lage, wie die Level-Datei sie nennt
  const SENSOREN: Record<string, [string, string]> = {
    taster: ['lage.taster["fuss"]', 'jemand wartet am Überweg dieser Gruppe; lage.taster allein: irgendwo'],
    schleife: ['lage.schleife["ns"]', 'ein Fahrzeug steht auf der Kontaktschleife vor der Haltlinie'],
    wartend: ['lage.wartend["ns"]', 'wie viele dort vor Rot warten'],
    frei: ['lage.frei["fuss"]', 'niemand Fremdes mehr auf den Flächen, die diese Gruppe kreuzt'],
    einsatz: ['lage.einsatz', 'Gruppe eines angemeldeten Einsatzfahrzeugs, sonst None'],
    nacht: ['lage.nacht', 'es ist Nacht'],
    stoerung: ['lage.stoerung', 'Gruppe mit gestörter Kontaktschleife, sonst None'],
  };
  const SIGNALE = { auto: '"gruen", "gelb", "rot", "rotgelb"', fuss: '"gruen", "rot"' };

  let { detail }: { detail: AufgabeDetail } = $props();

  function mitFuss(ansicht: AmpelAnsicht): boolean {
    return ansicht.anlage.gruppen.some((g) => g.art === 'fuss');
  }

  function signale(ansicht: AmpelAnsicht, art: 'auto' | 'fuss'): string {
    if (!ansicht.sensoren.includes('nacht')) return SIGNALE[art];
    return `${SIGNALE[art]}, ${art === 'auto' ? '"gelb_blinkt"' : '"aus"'}`;
  }

  function tonZuBild(ansicht: AmpelAnsicht, w: Wiedergabe, nr: number): void {
    const [t, jetzt] = w.bilder[nr];
    const vorher = new Set((w.bilder[nr - 1]?.[1] ?? []).map(([id]) => id));
    const arten = new Map(w.teilnehmer.map((x) => [x.id, x.art]));
    if (jetzt.some(([id]) => !vorher.has(id) && arten.get(id) === 'fuss')) klang.spiele('taster');
    for (const u of w.unfaelle) {
      if (u.t > t - DT && u.t <= t) klang.spiele(u.art === 'fuss' ? 'matsch' : 'blechschaden');
    }
    if (Math.abs(t - Math.round(t)) > 1e-6) return;
    const s = Math.round(t);
    const jetztSignale = w.signale[s];
    if (!jetztSignale) return;
    const gruppen = ansicht.anlage.gruppen;
    if (gruppen.some((g) => g.art === 'fuss' && jetztSignale[g.name] === 'gruen')) klang.spiele('ticken');
    if (gruppen.some((g) => g.art === 'auto' && jetztSignale[g.name] === 'gruen' && w.signale[s - 1]?.[g.name] !== 'gruen')) {
      klang.spiele('motor');
    }
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: AmpelAnsicht)}
  {@const s = ansicht.sterne}
  <div class="gruppe">Sensoren</div>
  <div class="spickzettel">
    <code>takt(lage)</code><span>läuft jede Sekunde und gibt das Signal je Gruppe zurück</span>
    <code>lage.sekunde</code><span>Zeit seit dem Start</span>
    {#each ansicht.sensoren as sensor (sensor)}
      {#if SENSOREN[sensor]}<code>{SENSOREN[sensor][0]}</code><span>{SENSOREN[sensor][1]}</span>{/if}
    {/each}
  </div>
  <div class="gruppe">Signale</div>
  <div class="spickzettel">
    {#each ansicht.anlage.gruppen as g (g.name)}
      <code>"{g.name}"</code><span>{g.text}: {signale(ansicht, g.art)}</span>
    {/each}
  </div>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle Teilschritte, kein Unfall, kein Verstoß, in allen Abläufen</span>
    {@render sterne(2)}<span>
      {[
        s.fuss != null ? `Fußgänger warten höchstens ${s.fuss} s` : null,
        s.autos != null ? `Fahrzeuge im Mittel höchstens ${String(s.autos).replace('.', ',')} s` : null,
      ].filter(Boolean).join(', ')} (erster sichtbarer Ablauf)
    </span>
    {@render sterne(3)}<span>dazu höchstens {s.zeichen} Zeichen Code (Kommentare zählen nicht)</span>
  </div>
{/snippet}

{#snippet szene(ansicht: AmpelAnsicht, wiedergabe: Wiedergabe | null, bild: number)}
  <AmpelSzene {ansicht} {wiedergabe} {bild} />
{/snippet}

{#snippet plan(ansicht: AmpelAnsicht, wiedergabe: Wiedergabe | null, dauer: number, zeit: number, springe: (s: number) => void)}
  <Signalplan gruppen={ansicht.anlage.gruppen} {wiedergabe} {dauer} {zeit} onSpringe={springe} />
{/snippet}

{#snippet kennzahlen(ansicht: AmpelAnsicht, wiedergabe: Wiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  {@const fuss = mitFuss(ansicht)}
  <div class="sim-werte" style:grid-template-columns="repeat({fuss ? 4 : 3}, minmax(0, 1fr))">
    <div><span class="num" class:gut={k.unfaelle === 0} class:schlecht={k.unfaelle > 0}>{k.unfaelle}</span><small>Unfälle</small></div>
    <div><span class="num" class:gut={k.verstoesse === 0} class:schlecht={k.verstoesse > 0}>{k.verstoesse}</span><small>Verstöße</small></div>
    {#if fuss}
      <div>
        <span class="num" class:gut={ansicht.sterne.fuss != null && k.fuss_max <= ansicht.sterne.fuss}>{Math.round(k.fuss_max)} s</span>
        <small>Fußgänger max.</small>
      </div>
    {/if}
    <div>
      <span class="num" class:gut={ansicht.sterne.autos != null && k.autos_mittel <= ansicht.sterne.autos}>
        {k.autos_mittel.toFixed(1).replace('.', ',')} s
      </span>
      <small>Fahrzeuge im Mittel</small>
    </div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Anlage"
  symbol="fa-traffic-light"
  planTitel="Signalplan"
  ladeAnsicht={(id) => spielApi.ampelAnlage(id)}
  probieren={(id, code) => spielApi.ampelLauf(id, code)}
  {tonZuBild}
  mitUnfall={(k: Kennzahlen) => k.unfaelle > 0}
  {hilfe}
  {szene}
  {plan}
  {kennzahlen}
/>
