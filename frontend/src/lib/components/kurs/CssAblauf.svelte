<script lang="ts">
  /*
   * Ablauf eines CSS-Beispiels: das CSS Zeile für Zeile mit einem Schalter je Angabe, der Abspieler schaltet Angabe für
   * Angabe zu oder ab. Darunter die Bühne und das Kastenmodell eines Elements als farbige Ringe (Inhalt, padding,
   * border, margin) mit der Rechnung "Rand zu Rand". Gezeigt wird das erste Element der Bühne, das unter dem Zeiger
   * oder das angeklickte (bis zum nächsten Klick darauf).
   */
  import { erweitert, folge, kasten, weg, type Kasten, type Rechteck, type Seiten } from '../../css/kasten';
  import { ohne, zerlege, type Angabe, type Regel } from '../../css/regeln';
  import { zeilen } from '../../kurs/hervorheben';
  import CssBuehne from './CssBuehne.svelte';

  interface Props {
    html: string;
    css: string;
  }
  let { html, css }: Props = $props();

  let regeln = $derived(zerlege(css));
  let angaben = $derived(alle(regeln));
  /** abgeschaltete Angaben (Nummern); bei neuem CSS wieder alle an */
  let aus = $state(new Set<number>());
  $effect(() => {
    void css;
    aus = new Set();
  });
  let aktiv = $derived(ohne(css, regeln, aus));
  let quelle = $derived(css.replace(/\n$/, ''));
  let hervorgehoben = $derived(zeilen(quelle, 'css'));
  let zeilenAnfang = $derived(anfaenge(quelle));

  function alle(rs: Regel[]): Angabe[] {
    return rs.flatMap((r) => [...r.angaben, ...alle(r.innen)]).sort((a, b) => a.von - b.von);
  }
  function anfaenge(text: string): number[] {
    const a = [0];
    for (let i = 0; i < text.length; i++) if (text[i] === '\n') a.push(i + 1);
    return a;
  }
  function inZeile(nr: number): Angabe[] {
    const von = zeilenAnfang[nr];
    const bis = zeilenAnfang[nr + 1] ?? Infinity;
    return angaben.filter((a) => a.von >= von && a.von < bis);
  }

  function setze(nummern: number[], an: boolean) {
    const neu = new Set(aus);
    for (const nr of nummern) {
      if (an) neu.delete(nr);
      else neu.add(nr);
    }
    aus = neu;
  }
  function vor() {
    const a = angaben.find((x) => aus.has(x.nr));
    if (a) setze([a.nr], true);
  }
  function zurueck() {
    const a = [...angaben].reverse().find((x) => !aus.has(x.nr));
    if (a) setze([a.nr], false);
  }

  // ---- Kastenmodell ----
  let zeiger = $state<Kasten | null>(null);
  let gewaehlt = $state<number[] | null>(null);
  let erstes = $state<Kasten | null>(null);
  let festgehalten = $state<Kasten | null>(null);
  let gezeigt = $derived(festgehalten ?? zeiger ?? erstes);

  function beiLaden(dokument: Document) {
    zeiger = null;
    const ersterKasten = dokument.body.firstElementChild;
    erstes = ersterKasten ? kasten(ersterKasten) : null;
    const el = gewaehlt ? folge(dokument, gewaehlt) : null;
    festgehalten = el ? kasten(el) : null;
    if (!el) gewaehlt = null;
    const Element = dokument.defaultView?.Element;
    const ziel = (e: Event) => (Element && e.target instanceof Element && e.target !== dokument.body && e.target !== dokument.documentElement ? e.target : null);
    dokument.addEventListener('mouseover', (e) => {
      const t = ziel(e);
      zeiger = t ? kasten(t) : null;
    });
    dokument.documentElement.addEventListener('mouseleave', () => (zeiger = null));
    dokument.addEventListener('click', (e) => {
      const t = ziel(e);
      if (!t) return;
      const w = weg(t);
      const gleich = gewaehlt !== null && gewaehlt.join() === w.join();
      gewaehlt = gleich ? null : w;
      festgehalten = gleich ? null : kasten(t);
    });
  }

  const lage = (r: Rechteck) => `left:${r.x}px;top:${r.y}px;width:${Math.max(0, r.b)}px;height:${Math.max(0, r.h)}px`;
  // ein negativer Außenabstand zieht den Kasten nach außen, als Ring gibt es ihn nicht
  const breite = (n: number) => `${Math.max(0, n)}px`;
  const ring = (r: Rechteck, s: Seiten) => `${lage(r)};border-width:${breite(s.oben)} ${breite(s.rechts)} ${breite(s.unten)} ${breite(s.links)}`;
  const zahl = (n: number) => String(n).replace('.', ',');
</script>

{#snippet ringe(k: Kasten)}
  {@const paddingKante = erweitert(k.rand, k.border, -1)}
  <div class="kasten-ring margin" style={ring(erweitert(k.rand, k.margin), k.margin)}></div>
  <div class="kasten-ring border" style={ring(k.rand, k.border)}></div>
  <div class="kasten-ring padding" style={ring(paddingKante, k.padding)}></div>
  <div class="kasten-ring inhalt" style={lage(erweitert(paddingKante, k.padding, -1))}></div>
{/snippet}

<div class="css-ablauf">
  <div class="regel-liste" aria-label="CSS mit Schaltern">
    {#each hervorgehoben as zeile, i (i)}
      {@const hier = inZeile(i)}
      {@const ganzAus = hier.length > 0 && hier.every((a) => aus.has(a.nr))}
      <div class="regel" class:aus={ganzAus}>
        <span class="ln">{i + 1}</span><span class="text">{@html zeile}</span>
        {#if hier.length}
          <button class="schalter" aria-pressed={!ganzAus} title="Angabe ein oder aus" aria-label="{hier.map((a) => a.eigenschaft).join(', ')} ein oder aus"
            onclick={() => setze(hier.map((a) => a.nr), ganzAus)}></button>
        {:else}<span></span>{/if}
      </div>
    {/each}
  </div>

  <div class="abspieler">
    <button class="ikon" onclick={zurueck} disabled={aus.size === angaben.length} title="Angabe abschalten" aria-label="Letzte Angabe abschalten"><i class="fa-solid fa-backward-step" aria-hidden="true"></i></button>
    <button class="ikon" onclick={vor} disabled={aus.size === 0} title="Nächste Angabe zuschalten" aria-label="Nächste Angabe zuschalten"><i class="fa-solid fa-forward-step" aria-hidden="true"></i></button>
    <span class="dim">Angabe für Angabe zuschalten</span>
    <span class="num">{angaben.length - aus.size} / {angaben.length}</span>
  </div>

  <CssBuehne {html} css={aktiv} {beiLaden}>
    {#snippet ueber()}{#if gezeigt}{@render ringe(gezeigt)}{/if}{/snippet}
  </CssBuehne>

  <div class="legende"><span><b class="inhalt"></b>Inhalt</span><span><b class="padding"></b>padding</span><span><b class="border"></b>border</span><span><b class="margin"></b>margin</span></div>
  {#if gezeigt}
    {@const k = gezeigt}
    <p class="mass">
      <code>{k.name}</code>{festgehalten ? ' (festgehalten)' : ''}: Rand zu Rand {zahl(k.inhalt.b)} + {zahl(k.padding.links)} + {zahl(k.padding.rechts)} + {zahl(k.border.links)} + {zahl(k.border.rechts)} = {zahl(Math.round(k.rand.b * 10) / 10)} px breit, mit Außenabstand {zahl(Math.round((k.rand.b + k.margin.links + k.margin.rechts) * 10) / 10)} px
    </p>
  {/if}
  <p class="dim hinweis">Zeige auf ein Element der Bühne oder tippe es an, dann siehst du seine Kästen. Angetippt bleibt es stehen, bis du es noch einmal antippst.</p>
</div>

<style>
  .css-ablauf { display: flex; flex-direction: column; gap: var(--sp-3); }
  .regel-liste .text { white-space: pre; overflow: hidden; text-overflow: ellipsis; }
  .abspieler .dim { font-size: var(--fs-sm); }
  .abspieler .num { margin-left: auto; }
  .kasten-ring { position: absolute; box-sizing: border-box; border-style: solid; border-color: transparent; }
  .kasten-ring.margin { border-color: color-mix(in srgb, var(--kasten-margin) 45%, transparent); }
  .kasten-ring.border { border-color: color-mix(in srgb, var(--kasten-border) 60%, transparent); }
  .kasten-ring.padding { border-color: color-mix(in srgb, var(--kasten-padding) 45%, transparent); }
  .kasten-ring.inhalt { background: color-mix(in srgb, var(--kasten-inhalt) 40%, transparent); }
  .legende b.inhalt { background: var(--kasten-inhalt); }
  .legende b.padding { background: var(--kasten-padding); }
  .legende b.border { background: var(--kasten-border); }
  .legende b.margin { background: var(--kasten-margin); opacity: .6; }
  .mass { margin: 0; font-family: var(--mono); font-size: var(--fs-sm); color: var(--fg-dim); }
  .mass code { color: var(--fg); }
  .hinweis { margin: 0; font-size: var(--fs-sm); }
</style>
