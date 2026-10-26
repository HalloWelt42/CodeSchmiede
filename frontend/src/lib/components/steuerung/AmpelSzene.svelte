<script lang="ts">
  /*
   * Ampelschule von oben: die Anlage, wie das Backend sie zeichnet (Flächen, Striche, Pfeile, Signale, Taster),
   * darüber die Teilnehmer eines Bilds der Wiedergabe. Fahrzeuge stehen mit der Front an ihrer Strecke auf dem Weg;
   * Unfälle bis zum Bild zeigen verbeultes Blech mit Rauch und einen Matschfleck. Nachts liegt ein Schleier darüber,
   * gelbes Blinken blinkt im Halbsekundentakt.
   */
  import { Linie } from '../../steuerung/linie';
  import type { AmpelAnsicht, Bewegung, Punkt, Signal, Wiedergabe } from '../../types/Ampel';

  interface Props {
    ansicht: AmpelAnsicht;
    wiedergabe: Wiedergabe | null;
    bild: number;
  }
  let { ansicht, wiedergabe, bild }: Props = $props();

  const FARBEN = ['#2dd4bf', '#60a5fa', '#f59e0b', '#a78bfa', '#f472b6', '#94a3b8', '#34d399', '#fb7185'];
  const PFEIL: Record<Bewegung, string> = {
    gerade: 'M0 8 L0 -8 M-3 -5 L0 -8 L3 -5',
    rechts: 'M0 8 L0 0 Q0 -5 6 -5 M3 -8 L6 -5 L3 -2',
    links: 'M0 8 L0 0 Q0 -5 -6 -5 M-3 -8 L-6 -5 L-3 -2',
  };
  const FLECK = 'M -9 -2 C -11 -9 -2 -12 3 -9 C 9 -11 13 -4 10 1 C 14 6 6 11 1 9 C -4 13 -12 8 -9 3 Z';
  const SPRITZER = [[14, -8, 2.4], [-14, 9, 2], [16, 8, 1.6], [-4, -15, 1.8], [7, 15, 1.4]];

  let anlage = $derived(ansicht.anlage);
  let linien = $derived(new Map(anlage.wege.map((w) => [w.id, new Linie(w.punkte)])));
  let wegGruppe = $derived(new Map(anlage.wege.map((w) => [w.id, w.gruppe])));
  let leute = $derived(new Map((wiedergabe?.teilnehmer ?? []).map((t) => [t.id, t])));

  let aufnahme = $derived(wiedergabe && bild >= 0 ? wiedergabe.bilder[bild] : null);
  let zeit = $derived(aufnahme?.[0] ?? 0);
  let sekunde = $derived(Math.max(0, Math.ceil(zeit - 1e-6) - 1));
  let signale = $derived<Record<string, Signal> | null>(wiedergabe && aufnahme ? (wiedergabe.signale[sekunde] ?? null) : null);
  let blinkt = $derived(Math.floor(zeit * 2) % 2 === 0);
  let unfaelle = $derived((wiedergabe?.unfaelle ?? []).filter((u) => u.t <= zeit + 1e-6));
  let kaputt = $derived(new Set(unfaelle.flatMap((u) => u.ids)));
  let nachts = $derived((wiedergabe?.nacht ?? []).some(([von, bis]) => von <= sekunde && sekunde < bis));

  interface Figur {
    id: number;
    art: string;
    x: number;
    y: number;
    winkel: number;
    laenge: number;
    breite: number;
    kaputt: boolean;
  }

  let figuren = $derived.by(() => {
    const liste: Figur[] = [];
    for (const [id, s] of aufnahme?.[1] ?? []) {
      const t = leute.get(id);
      const linie = t && linien.get(t.weg);
      if (!t || !linie) continue;
      const masse = ansicht.arten[t.art];
      if (t.art === 'fuss') {
        const [x, y] = linie.punkt(s);
        liste.push({ id, art: t.art, x, y, winkel: 0, laenge: masse.laenge, breite: masse.breite, kaputt: false });
        continue;
      }
      const [fx, fy] = linie.punkt(s);
      const [hx, hy] = linie.punkt(s - masse.laenge);
      liste.push({
        id,
        art: t.art,
        x: (fx + hx) / 2,
        y: (fy + hy) / 2,
        winkel: (Math.atan2(fy - hy, fx - hx) * 180) / Math.PI,
        laenge: masse.laenge,
        breite: masse.breite,
        kaputt: kaputt.has(id),
      });
    }
    return liste;
  });

  // Taster leuchtet, solange an seiner Gruppe jemand am Bordstein wartet
  let gedrueckt = $derived.by(() => {
    const gruppen = new Set<string>();
    for (const f of figuren) {
      if (f.art !== 'fuss') continue;
      const t = leute.get(f.id);
      const gruppe = t && wegGruppe.get(t.weg);
      const s = aufnahme?.[1].find(([id]) => id === f.id)?.[1] ?? 0;
      if (gruppe && s <= 0 && signale?.[gruppe] !== 'gruen') gruppen.add(gruppe);
    }
    return gruppen;
  });

  function lampen(art: 'auto' | 'fuss', z: Signal | undefined): Record<string, boolean> {
    if (art === 'fuss') return { rot: z === 'rot', gruen: z === 'gruen' };
    return {
      rot: z === 'rot' || z === 'rotgelb',
      gelb: z === 'gelb' || z === 'rotgelb' || (z === 'gelb_blinkt' && blinkt),
      gruen: z === 'gruen',
    };
  }

  function punkte(liste: Punkt[]): string {
    return liste.map(([x, y]) => `${x},${y}`).join(' ');
  }

  function farbe(f: Figur): string {
    if (f.art === 'lkw') return '#e2e8f0';
    if (f.art === 'einsatz') return '#f8fafc';
    return FARBEN[f.id % FARBEN.length];
  }
</script>

<svg class="szene" viewBox="0 0 {anlage.breite} {anlage.hoehe}" role="img" aria-label="Anlage von oben">
  {#each anlage.zeichnung.flaechen as f, i (i)}
    <polygon class={f.klasse} points={punkte(f.punkte)} />
  {/each}
  {#each anlage.zeichnung.striche as s, i (i)}
    <polyline class={s.klasse} points={punkte(s.punkte)} />
  {/each}
  {#each anlage.zeichnung.pfeile as p, i (i)}
    <g transform="translate({p.x} {p.y}) rotate({p.drehung})">
      {#each p.richtungen as r (r)}<path class="pfeil" d={PFEIL[r]} />{/each}
    </g>
  {/each}

  {#each unfaelle.filter((u) => u.art === 'fuss') as u, k (u.t + ':' + u.ids.join())}
    <g class="matsch" transform="translate({u.x} {u.y}) rotate({k * 67})">
      <path d={FLECK} />
      {#each SPRITZER as [cx, cy, r], j (j)}<circle {cx} {cy} {r} />{/each}
    </g>
  {/each}

  {#each figuren as f (f.id)}
    {#if f.art === 'fuss'}
      <circle class="fussgaenger" cx={f.x} cy={f.y} r="4" />
    {:else}
      <g transform="translate({f.x} {f.y}) rotate({f.winkel})">
        <rect class="fahrzeug" class:verbeult={f.kaputt} x={-f.laenge / 2} y={-f.breite / 2} width={f.laenge} height={f.breite}
          rx={f.art === 'lkw' ? 2 : 4} fill={farbe(f)} />
        {#if f.art === 'lkw'}
          <rect class="fuehrerhaus" x={f.laenge / 2 - 13} y={-f.breite / 2} width="13" height={f.breite} rx="2" />
        {/if}
        <rect class="scheibe" x={f.laenge / 2 - 9} y={-f.breite / 2 + 2} width="5" height={f.breite - 4} rx="1.5" />
        {#if f.art === 'einsatz'}
          <rect class="blaulicht" class:aus={!blinkt} x="-3" y={-f.breite / 2 + 1} width="6" height={f.breite - 2} rx="1" />
        {/if}
        {#if f.kaputt}
          {#each [0, 1, 2] as k (k)}<circle class="rauch" cx={f.laenge / 2 - 4 - k * 5} cy={-f.breite / 2 - 4 - k * 4} r={4 + k * 2} />{/each}
        {/if}
      </g>
    {/if}
  {/each}

  <!-- nachts dunkel, nur die Lampen leuchten -->
  {#if nachts}<rect class="nacht" x="0" y="0" width={anlage.breite} height={anlage.hoehe} />{/if}
  {#each anlage.zeichnung.signale as s, i (i)}
    {@const an = lampen(s.art, signale?.[s.gruppe])}
    {#if s.art === 'auto'}
      <g transform="rotate({s.drehung} {s.x} {s.y})">
        <rect class="gehaeuse" x={s.x - 6.5} y={s.y - 17} width="13" height="34" rx="2.5" />
        {#each ['rot', 'gelb', 'gruen'] as l, k (l)}<circle class="lampe {l}" class:an={an[l]} cx={s.x} cy={s.y - 10.5 + k * 10.5} r="4.2" />{/each}
      </g>
    {:else}
      <g transform="rotate({s.drehung} {s.x} {s.y})">
        <rect class="gehaeuse" x={s.x - 6} y={s.y - 12} width="12" height="24" rx="2.5" />
        {#each ['rot', 'gruen'] as l, k (l)}<circle class="lampe {l}" class:an={an[l]} cx={s.x} cy={s.y - 5.5 + k * 11} r="4" />{/each}
      </g>
    {/if}
  {/each}
  {#each anlage.zeichnung.taster as t, i (i)}
    <rect class="taster" class:an={gedrueckt.has(t.gruppe)} x={t.x - 4.5} y={t.y - 4.5} width="9" height="9" rx="2" />
  {/each}
</svg>
