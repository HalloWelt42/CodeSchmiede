<script lang="ts">
  /*
   * Aufzugsteuerung (Steuerungsspiel) in der gemeinsamen Ansicht der Steuerungsspiele: dazu Sensoren, Befehle und
   * Sterne als Hilfe, das Haus im Schnitt, das Fahrdiagramm, die Kennzahlen und Gong, Tür und Einklemmen als Klang.
   */
  import { spielApi } from '../api/SpielApi';
  import { klang } from '../steuerung/klang.svelte';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { AufzugAnsicht, AufzugWiedergabe } from '../types/Aufzug';
  import AufzugSzene from './steuerung/AufzugSzene.svelte';
  import Fahrdiagramm from './steuerung/Fahrdiagramm.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';

  const DT = 0.25;
  const GRUNDSENSOREN: [string, string][] = [
    ['takt(lage)', 'fragt eine Kabine, sobald sie mit ihrem letzten Befehl fertig ist'],
    ['lage.etage', 'wo die Kabine steht, 0 ist das EG'],
    ['lage.tuer', '"offen" oder "zu"'],
    ['lage.rufe[1]', 'Etagen, an denen jemand nach oben will; lage.rufe[-1] nach unten'],
    ['lage.ziele', 'in der Kabine gedrückte Etagen'],
    ['lage.richtung', 'wohin sie zuletzt fuhr: 1, -1 oder 0'],
  ];
  // Sensoren, die ein Level dazu nennt
  const SENSOREN: Record<string, [string, string]> = {
    wartend: ['lage.wartend[3]', 'wie viele in Etage 3 warten'],
    lichtschranke: ['lage.lichtschranke', 'jemand steht in der Tür'],
    voll: ['lage.voll', 'kein Platz mehr; lage.drin zählt, wie viele drin sind'],
    ueberlast: ['lage.ueberlast', 'die Kabine ist zu schwer, die Tür darf nicht zu'],
    feuer: ['lage.feuer', 'Feueralarm: ohne Halt ins EG und dort stehen bleiben'],
    aufzuege: ['lage.aufzuege["b"]', 'eine Kabine (etage, richtung, tuer, ziele, drin); lage.aufzug ist die fragende'],
  };
  const BEFEHLE: [string, string][] = [
    ['"hoch", "runter"', 'eine Etage weiter, nur mit geschlossener Tür'],
    ['"auf"', 'Tür öffnen; erst steigen alle aus, dann ein'],
    ['"zu"', 'Tür schließen, nicht auf jemandem'],
    ['"warten"', 'eine Sekunde nichts tun'],
  ];

  let { detail }: { detail: AufgabeDetail } = $props();

  function tonZuBild(_: AufzugAnsicht, w: AufzugWiedergabe, nr: number): void {
    const t = w.bilder[nr][0];
    for (const e of w.ereignisse) {
      if (e.t <= t - DT || e.t > t) continue;
      if (e.art === 'offen') klang.spiele('gong');
      else if (e.art === 'auf') klang.spiele('tuer_auf');
      else if (e.art === 'zu') klang.spiele('tuer_zu');
      else if (e.grund === 'einklemmen') klang.spiele('blech_klein');
    }
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: AufzugAnsicht)}
  <div class="gruppe">Sensoren</div>
  <div class="spickzettel">
    {#each GRUNDSENSOREN as [name, text] (name)}<code>{name}</code><span>{text}</span>{/each}
    {#each ansicht.sensoren as sensor (sensor)}
      {#if SENSOREN[sensor]}<code>{SENSOREN[sensor][0]}</code><span>{SENSOREN[sensor][1]}</span>{/if}
    {/each}
  </div>
  <div class="gruppe">Befehle</div>
  <div class="spickzettel">
    {#each BEFEHLE as [name, text] (name)}<code>{name}</code><span>{text}</span>{/each}
  </div>
  <div class="gruppe">Haus</div>
  <p class="haus-text">
    {ansicht.haus.etagen} Etagen, {ansicht.haus.aufzuege.length === 1 ? 'eine Kabine' : `${ansicht.haus.aufzuege.length} Kabinen`}
    mit {ansicht.haus.plaetze} Plätzen, höchstens {ansicht.haus.last} kg.
  </p>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle Teilschritte, kein Verstoß, in allen Abläufen</span>
    {@render sterne(2)}<span>Fahrgäste warten im Mittel höchstens {ansicht.sterne.warten} s (erster sichtbarer Ablauf)</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.zeichen} Zeichen Code (Kommentare zählen nicht)</span>
  </div>
{/snippet}

{#snippet szene(ansicht: AufzugAnsicht, wiedergabe: AufzugWiedergabe | null, bild: number)}
  <AufzugSzene {ansicht} {wiedergabe} {bild} />
{/snippet}

{#snippet plan(ansicht: AufzugAnsicht, wiedergabe: AufzugWiedergabe | null, dauer: number, zeit: number, springe: (s: number) => void)}
  <Fahrdiagramm haus={ansicht.haus} {wiedergabe} {dauer} {zeit} onSpringe={springe} />
{/snippet}

{#snippet kennzahlen(ansicht: AufzugAnsicht, wiedergabe: AufzugWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte">
    <div><span class="num" class:gut={k.verstoesse === 0} class:schlecht={k.verstoesse > 0}>{k.verstoesse}</span><small>Verstöße</small></div>
    <div>
      <span class="num" class:gut={k.bedient === k.fahrgaeste} class:schlecht={k.bedient < k.fahrgaeste}>{k.bedient} / {k.fahrgaeste}</span>
      <small>Angekommen</small>
    </div>
    <div>
      <span class="num" class:gut={k.warten_mittel <= ansicht.sterne.warten}>{k.warten_mittel.toFixed(1).replace('.', ',')} s</span>
      <small>Warten im Mittel</small>
    </div>
    <div><span class="num">{Math.round(k.warten_max)} s</span><small>Warten max.</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Haus"
  symbol="fa-elevator"
  planTitel="Fahrdiagramm"
  ladeAnsicht={(id) => spielApi.aufzugHaus(id)}
  probieren={(id, code) => spielApi.aufzugLauf(id, code)}
  {tonZuBild}
  {hilfe}
  {szene}
  {plan}
  {kennzahlen}
/>

<style>
  .haus-text {
    margin: 0;
    font-size: var(--fs-sm);
  }
</style>
