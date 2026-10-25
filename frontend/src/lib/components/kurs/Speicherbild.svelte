<script lang="ts">
  /*
   * Speicher nach einer Zeile: je Aufrufrahmen die Namen mit ihren Werten. Einfache Werte als Kasten, Listen und
   * Tupel als Fächerreihe mit Nummern, Wörterbücher als Schubladen, Objekte mit ihren Attributen. Zeigen zwei Namen
   * auf dasselbe Objekt, steht das dabei. Gelb ist, was sich in diesem Schritt geändert hat.
   */
  import type { Schritt, Wert } from '../../api/KursApi';

  interface Props {
    schritt: Schritt | null;
    /** voriger Schritt: was sich seitdem geändert hat, leuchtet */
    vorher?: Schritt | null;
  }
  let { schritt, vorher = null }: Props = $props();

  function geaendert(rahmen: string, name: string, w: Wert): boolean {
    const alt = vorher?.rahmen.find((r) => r.name === rahmen)?.variablen[name];
    return !alt || alt.darstellung !== w.darstellung;
  }

  /** Namen, die auf dasselbe Objekt zeigen wie dieser (Verweis) */
  function teilen(name: string, w: Wert): string[] {
    if (w.kennung === null || !['liste', 'tupel', 'menge', 'woerterbuch', 'objekt'].includes(w.art)) return [];
    return (schritt?.rahmen ?? []).flatMap((r) => Object.entries(r.variablen).filter(([n, x]) => n !== name && x.kennung === w.kennung).map(([n]) => n));
  }

  /** Stelle in einer Liste, deren Inhalt der Wert eines einfachen Namens ist (etwa der Schleifenname) */
  function zeigtAuf(w: Wert): number {
    if (!schritt || !w.elemente) return -1;
    for (const r of schritt.rahmen) {
      for (const x of Object.values(r.variablen)) {
        if (x.art !== 'text' && x.art !== 'zahl') continue;
        const i = w.elemente.findIndex((e) => e.darstellung === x.darstellung);
        if (i >= 0) return i;
      }
    }
    return -1;
  }
</script>

<div class="speicher">
  <div class="speicher-titel"><span>Speicher</span>{#if schritt}<span>nach Zeile <b class="num">{schritt.zeile}</b></span>{/if}</div>
  {#if !schritt}
    <span class="dim" style="font-size:var(--fs-sm)">Noch nichts im Speicher.</span>
  {:else}
    {#each schritt.rahmen as r (r.name)}
      {#if schritt.rahmen.length > 1}<div class="gruppe">{r.name === 'Modul' ? 'Hauptprogramm' : `in ${r.name}()`}</div>{/if}
      {#each Object.entries(r.variablen) as [name, w] (name)}
        {@const neu = geaendert(r.name, name, w)}
        {@const geteilt = teilen(name, w)}
        <div class="speicher-zeile">
          <span class="speicher-name">{name}</span>
          <div>
            {#if w.elemente && (w.art === 'liste' || w.art === 'tupel' || w.art === 'menge')}
              {@const zeigt = zeigtAuf(w)}
              <div class="faecher" class:neu>
                {#each w.elemente as e, i (i)}
                  <div class="fach" class:zeigt={i === zeigt}><span>{e.darstellung}</span>{#if w.art !== 'menge'}<small>{i}</small>{/if}</div>
                {/each}
                {#if w.elemente.length === 0}<span class="kasten-wert leer">leer</span>{/if}
                {#if w.gekuerzt}<span class="dim">...</span>{/if}
              </div>
            {:else if w.paare}
              <div class="schubladen">
                {#each w.paare as [k, v] (k.darstellung)}
                  <div class="schublade"><span class="etikett">{k.darstellung}</span><span class="inhalt">{v.darstellung}</span></div>
                {/each}
                {#if w.paare.length === 0}<span class="kasten-wert leer">leer</span>{/if}
              </div>
            {:else if w.attribute}
              <div class="objekt"><b>{w.darstellung}</b>
                {#each Object.entries(w.attribute) as [a, v] (a)}<span><span class="speicher-name">{a}</span> {v.darstellung}</span>{/each}
              </div>
            {:else}
              <span class="kasten-wert" class:neu>{w.darstellung}</span>
            {/if}
            {#if geteilt.length}<small class="verweis"><i class="fa-solid fa-arrow-right-arrow-left" aria-hidden="true"></i> dasselbe wie {geteilt.join(', ')}</small>{/if}
          </div>
        </div>
      {/each}
    {/each}
    {#if schritt.rueckgabe}
      <div class="speicher-zeile"><span class="speicher-name">return</span><span class="kasten-wert neu">{schritt.rueckgabe.darstellung}</span></div>
    {/if}
  {/if}
</div>

<style>
  .faecher.neu .fach span { border-color: var(--gold); }
  .schubladen { display: flex; flex-direction: column; gap: 3px; }
  .schublade { display: grid; grid-template-columns: auto minmax(0, 1fr); border: 2px solid var(--s-a, var(--accent)); border-radius: 4px; font-family: var(--mono); font-size: 14px; }
  .schublade .etikett { padding: 2px 8px; background: color-mix(in srgb, var(--s-a, var(--accent)) 22%, var(--bg)); border-right: 2px solid var(--s-a, var(--accent)); }
  .schublade .inhalt { padding: 2px 8px; overflow-wrap: anywhere; }
  .objekt { display: flex; flex-direction: column; gap: 2px; padding: 4px 8px; border: 2px solid var(--s-b, var(--accent)); border-radius: 4px; font-family: var(--mono); font-size: 13px; }
  .verweis { display: block; margin-top: 2px; color: var(--fg-dim); font-size: var(--fs-xs); }
  .gruppe { margin-top: 0; }
</style>
