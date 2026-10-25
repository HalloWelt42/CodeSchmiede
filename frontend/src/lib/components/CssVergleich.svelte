<script lang="ts">
  /*
   * Bildvergleich der CSS-Aufgabe: Ziel oben, eigenes Ergebnis darunter.
   *
   * Beide Bühnen zeigen dieselbe Fläche (BUEHNE_B x BUEHNE_H, wie die
   * Messung sie rastert), passend verkleinert. Ansichten: getrennt,
   * überblendet mit Schieberegler, Abweichung (das Bild der Messung:
   * gleich gedämpft, fehlt blau, zu viel rot). Das Mausrad zoomt beide Bühnen gemeinsam
   * zum Mauszeiger hin, gedämpft für Trackpad und Mac-Maus: die Stärke
   * folgt der Scrollweite, je Bildschirmbild wird höchstens einmal
   * gezoomt, ein Schritt ist auf 8 % begrenzt.
   */
  import type { Snippet } from 'svelte';
  import { BUEHNE_B, BUEHNE_H } from '../css/buehne';

  interface Props {
    zielSrcdoc: string;
    eigenSrcdoc: string;
    /** Abweichungsbild der letzten Messung */
    abweichung: ImageData | null;
    /** Wertungsleiste über dem Vergleich */
    wertung: Snippet;
  }
  let { zielSrcdoc, eigenSrcdoc, abweichung, wertung }: Props = $props();

  const ZOOM_MAX = 8;
  const SCHRITT_MAX = 1.08;

  type Modus = 'getrennt' | 'blenden' | 'abweichung';
  let modus = $state<Modus>('getrennt');
  let schnitt = $state(50);
  let zoom = $state(1);
  let ursprung = $state({ x: 50, y: 50 });
  let breite = $state(0);

  let massstab = $derived(breite / BUEHNE_B);
  let untenTitel = $derived(
    { getrennt: 'Deine Lösung', blenden: 'Ziel | Deine Lösung', abweichung: 'Abweichung: Blau fehlt, Rot zu viel' }[modus],
  );

  function setzeZoom(z: number, x?: number, y?: number): void {
    zoom = Math.min(ZOOM_MAX, Math.max(1, z));
    if (x !== undefined && y !== undefined) ursprung = { x, y };
  }

  let gesammelt = 0;
  let letzteLage: [number, number] = [50, 50];
  let geplant = false;

  function rad(e: WheelEvent): void {
    e.preventDefault();
    const r = (e.currentTarget as HTMLElement).getBoundingClientRect();
    gesammelt += e.deltaMode === 1 ? e.deltaY * 16 : e.deltaY;
    letzteLage = [((e.clientX - r.left) / r.width) * 100, ((e.clientY - r.top) / r.height) * 100];
    if (geplant) return;
    geplant = true;
    requestAnimationFrame(() => {
      const faktor = Math.min(SCHRITT_MAX, Math.max(1 / SCHRITT_MAX, Math.exp(-gesammelt * 0.0015)));
      setzeZoom(zoom * faktor, ...letzteLage);
      gesammelt = 0;
      geplant = false;
    });
  }

  function zeichne(leinwand: HTMLCanvasElement, bild: ImageData | null) {
    const male = (b: ImageData | null) => {
      const g = leinwand.getContext('2d');
      if (!g) return;
      if (b) g.putImageData(b, 0, 0);
      else g.clearRect(0, 0, leinwand.width, leinwand.height);
    };
    male(bild);
    return { update: male };
  }

  // Mausrad nur mit passive: false abfangbar, sonst rollt die Spalte mit
  function fangeRad(knoten: HTMLElement) {
    knoten.addEventListener('wheel', rad, { passive: false });
    return { destroy: () => knoten.removeEventListener('wheel', rad) };
  }
</script>

{#snippet rahmen(srcdoc: string, titel: string, klasse = '')}
  <div class="ebene {klasse}" style:width="{BUEHNE_B}px" style:height="{BUEHNE_H}px" style:transform="scale({massstab})">
    <iframe title={titel} sandbox="allow-same-origin" {srcdoc} tabindex="-1"></iframe>
  </div>
{/snippet}

<div class="vergleich">
  {@render wertung()}

  <div class="vergleich-kopf">
    <button class="knopf-klein" class:aktiv={modus === 'getrennt'} onclick={() => (modus = 'getrennt')}>Getrennt</button>
    <button class="knopf-klein" class:aktiv={modus === 'blenden'} onclick={() => (modus = 'blenden')}>Überblenden</button>
    <button class="knopf-klein" class:aktiv={modus === 'abweichung'} onclick={() => (modus = 'abweichung')}>Abweichung</button>
    <span class="zoom">
      <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
      <span class="num">{Math.round(zoom * 100)} %</span>
      <button class="knopf-klein" onclick={() => setzeZoom(1, 50, 50)}>1:1</button>
    </span>
  </div>

  <div class="buehne-rahmen">
    <div class="buehne-titel"><span>Ziel</span><span>{BUEHNE_B} × {BUEHNE_H}</span></div>
    <div class="buehne" bind:clientWidth={breite}>
      <div class="flaeche" style:transform-origin="{ursprung.x}% {ursprung.y}%" style:transform="scale({zoom})">
        {@render rahmen(zielSrcdoc, 'Ziel')}
      </div>
      <div class="fang" use:fangeRad></div>
    </div>
  </div>

  <div class="buehne-rahmen">
    <div class="buehne-titel"><span>{untenTitel}</span>{#if modus === 'getrennt'}<span>Mausrad zoomt beide</span>{/if}</div>
    <div class="buehne">
      <div class="flaeche" style:transform-origin="{ursprung.x}% {ursprung.y}%" style:transform="scale({zoom})" style:--schnitt-pos="{schnitt}%">
        {#if modus === 'abweichung'}
          <div class="ebene" style:width="{BUEHNE_B}px" style:height="{BUEHNE_H}px" style:transform="scale({massstab})">
            <canvas width={BUEHNE_B} height={BUEHNE_H} use:zeichne={abweichung}></canvas>
          </div>
        {:else}
          {#if modus === 'blenden'}{@render rahmen(zielSrcdoc, 'Ziel darunter')}{/if}
          {@render rahmen(eigenSrcdoc, 'Deine Lösung', modus === 'blenden' ? 'oben' : '')}
        {/if}
      </div>
      {#if modus === 'blenden'}<div class="schnittlinie" style:left="{schnitt}%"></div>{/if}
      <div class="fang" use:fangeRad></div>
    </div>
    {#if modus === 'blenden'}
      <input class="regler" type="range" min="0" max="100" bind:value={schnitt} aria-label="Überblendung verschieben" />
    {/if}
  </div>
</div>

<style>
  .vergleich {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
    padding: var(--sp-2) var(--sp-3) var(--sp-3);
    background: var(--bg);
    overflow-y: auto;
    overflow-x: clip;
  }
  .vergleich-kopf {
    display: flex;
    align-items: center;
    gap: 4px;
    flex-wrap: wrap;
  }
  .zoom {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .zoom .num {
    color: var(--fg);
    min-width: 44px;
    text-align: right;
    font-weight: 600;
  }
  .buehne-rahmen {
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: 0;
  }
  .buehne-titel {
    display: flex;
    justify-content: space-between;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--fg-dim);
  }
  /* so groß, dass beide Bühnen untereinander in die Spalte passen */
  .buehne {
    position: relative;
    width: min(100%, calc((100vh - 330px) / 2 * 1.5));
    aspect-ratio: 3 / 2;
    align-self: center;
    overflow: hidden;
    border: 1px solid var(--border);
    background: repeating-conic-gradient(var(--karo-a) 0 25%, var(--karo-b) 0 50%) 0 0 / 16px 16px;
  }
  .flaeche {
    position: absolute;
    inset: 0;
  }
  .ebene {
    position: absolute;
    left: 0;
    top: 0;
    transform-origin: 0 0;
  }
  .ebene iframe {
    width: 100%;
    height: 100%;
    border: 0;
    display: block;
  }
  .ebene.oben { clip-path: inset(0 0 0 var(--schnitt-pos, 50%)); }
  .ebene canvas { display: block; }
  .fang {
    position: absolute;
    inset: 0;
    cursor: zoom-in;
  }
  .schnittlinie {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--accent);
    pointer-events: none;
  }
  .regler {
    width: 100%;
    margin-top: 2px;
    accent-color: var(--accent);
  }
</style>
