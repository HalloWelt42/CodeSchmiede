<script lang="ts">
  /* Bild auf der Karte eines Spiels, aus Bausteinen der Oberfläche statt aus Bilddateien. */
  let { id }: { id: string } = $props();

  // kleines Raster wie im Entwurf: Wände, Spur, Kristall, Ziel
  const ROBOTER_BILD = ['.#..Z', '*#.#.', '***#.', '.#*K.', '#...#'].join('').split('');
</script>

{#if id === 'sql-krimi'}
  <div class="akte-bild">
    <div class="akte-text"><div class="kapitel">AKTE 1</div>SELECT ...<br />JOIN zeugen<br /><span class="fund">LK-447-B</span></div>
    <i class="fa-solid fa-magnifying-glass lupe" aria-hidden="true"></i>
  </div>
{:else if id === 'roboter-parcours'}
  <div class="welt mini" style:--zellen="5">
    {#each ROBOTER_BILD as z, i (i)}
      <div class="zelle" class:wand={z === '#'} class:spur={z === '*'}>
        {#if z === 'Z'}<div class="ziel"></div>{/if}
        {#if z === 'K'}<div class="kristall"></div>{/if}
      </div>
    {/each}
  </div>
{:else if id === 'ausgabe-sprint'}
  <div class="sprint-bild">
    <div class="num uhrzeit">0:42</div>
    <div class="code">print(3 * "ab")</div>
    <div class="kette"><i class="fa-solid fa-link" aria-hidden="true"></i> Kette 4</div>
  </div>
{:else if id === 'muster-jagd'}
  <div class="muster">
    <div class="akz">/\d{'{'}2{'}'}\.\d{'{'}2{'}'}/</div>
    <div><i class="fa-solid fa-check ok" aria-hidden="true"></i> <mark>24.10</mark>.2026</div>
    <div><i class="fa-solid fa-xmark nein" aria-hidden="true"></i> 2026-10-24</div>
  </div>
{:else if id === 'ampelschule'}
  <svg class="ampel-bild" viewBox="0 0 120 150" aria-hidden="true">
    <rect class="gras" x="0" y="0" width="120" height="150" />
    <rect class="strasse" x="0" y="52" width="120" height="46" />
    {#each [55, 63, 71, 79, 87] as y (y)}<rect class="zebra" x="52" {y} width="16" height="4" />{/each}
    <rect x="18" y="78" width="22" height="11" rx="3" fill="#60a5fa" />
    <rect x="80" y="60" width="22" height="11" rx="3" fill="#f59e0b" />
    <rect class="gehaeuse" x="40" y="104" width="10" height="28" rx="2" />
    <circle cx="45" cy="110" r="3.2" fill="var(--lampe-rot)" /><circle class="aus" cx="45" cy="118" r="3.2" /><circle class="aus" cx="45" cy="126" r="3.2" />
    <rect class="gehaeuse" x="72" y="18" width="9" height="20" rx="2" />
    <circle class="aus" cx="76.5" cy="24" r="3" /><circle cx="76.5" cy="32" r="3" fill="var(--lampe-gruen)" />
    <circle cx="60" cy="42" r="4" fill="var(--orange)" />
  </svg>
{:else if id === 'aufzugsteuerung'}
  <svg class="ampel-bild" viewBox="0 0 120 150" aria-hidden="true">
    <rect class="haus" x="14" y="12" width="92" height="126" />
    <rect class="schacht" x="50" y="12" width="26" height="126" />
    {#each [54, 96, 138] as y (y)}<line class="etage" x1="14" y1={y} x2="106" y2={y} />{/each}
    <rect class="kabine" x="53" y="60" width="20" height="33" />
    <path class="ruf" d="M 40 77 l 4 -6 l 4 6 z" /><path class="ruf" d="M 40 37 l 4 6 l 4 -6 z" />
    <circle cx="30" cy="88" r="4" fill="var(--orange)" /><circle cx="30" cy="46" r="4" fill="var(--orange)" />
  </svg>
{:else}
  <i class="fa-solid fa-gamepad ersatz" aria-hidden="true"></i>
{/if}

<style>
  .ampel-bild {
    width: 100%;
    height: 100%;
  }
  .ampel-bild .gras { fill: var(--szene-gras); }
  .ampel-bild .strasse { fill: var(--szene-strasse); }
  .ampel-bild .zebra { fill: var(--szene-markierung); }
  .ampel-bild .gehaeuse { fill: var(--signal-gehaeuse); }
  .ampel-bild .aus { fill: var(--lampe-aus); }
  .ampel-bild .haus { fill: var(--bg-card-2); }
  .ampel-bild .schacht { fill: color-mix(in srgb, var(--fg) 6%, var(--bg)); stroke: var(--border); }
  .ampel-bild .etage { stroke: var(--border-strong); }
  .ampel-bild .kabine { fill: var(--bg-card-2); stroke: var(--accent); stroke-width: 2; }
  .ampel-bild .ruf { fill: var(--gold); }
  .muster {
    font-family: var(--mono);
    font-size: 11px;
    line-height: 1.8;
    padding: 8px;
    text-align: left;
  }
  .akz { color: var(--accent); }
  .ok { color: var(--green); }
  .nein { color: var(--red); }
  mark {
    background: color-mix(in srgb, var(--accent) 35%, transparent);
    color: var(--fg);
  }
  .mini { width: 96px; }
  .akte-bild { position: absolute; inset: 0; }
  .akte-text {
    position: absolute;
    inset: 14px 18px;
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    padding: 8px;
    font-family: var(--mono);
    font-size: 10px;
    color: var(--fg-dim);
    line-height: 1.5;
    text-align: left;
  }
  .akte-text .kapitel { color: var(--orange); }
  .fund { background: color-mix(in srgb, var(--gold) 30%, transparent); color: var(--fg); }
  .lupe {
    position: absolute;
    right: 12px;
    bottom: 10px;
    font-size: 26px;
    color: var(--orange);
  }
  .sprint-bild { text-align: center; }
  .uhrzeit {
    font-size: 34px;
    color: var(--accent);
  }
  .code {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--fg-dim);
  }
  .kette {
    margin-top: 6px;
    color: var(--orange);
    font-weight: 600;
    font-size: 12px;
  }
  .ersatz {
    font-size: 32px;
    color: var(--fg-mute);
  }
</style>
