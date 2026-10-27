<script lang="ts">
  /*
   * Von Hand probieren, je Verfahren das passende Werkzeug: Verschiebung, Zuordnung, Schlüsselwort, Schalen, PIN.
   * Nur zum Verstehen; gewertet wird allein, was das Programm zurückgibt.
   */
  import {
    ABC,
    ersetzeZurueck,
    pruefwert,
    schaleAb,
    schiebe,
    vigenereZurueck,
    xorZurueck,
    zuordnungNachHaeufigkeit,
    type Schale,
  } from '../../steuerung/codes';
  import type { Verfahren } from '../../types/Codes';
  import Haeufigkeit from './Haeufigkeit.svelte';

  let { verfahren, deutsch, geheim }: { verfahren: Verfahren; deutsch: Record<string, number>; geheim: string } = $props();

  let verschiebung = $state(0);
  let wort = $state('');
  let zuordnung = $state<Record<string, string>>({});
  let schalen = $state<string[]>([]);
  let pin = $state('');
  let pin_wert = $state<string | null>(null);

  let innen = $derived(schalen.at(-1) ?? geheim);
  let vorschau = $derived.by((): string | null => {
    switch (verfahren) {
      case 'caesar':
        return schiebe(geheim, -verschiebung);
      case 'vigenere':
        return vigenereZurueck(geheim, wort);
      case 'ersetzung':
        return ersetzeZurueck(geheim, zuordnung);
      case 'xor':
        return xorZurueck(geheim, wort);
      case 'schichten':
        return schiebe(innen, -verschiebung);
      case 'pin':
        return null;
    }
  });
  // Buchstaben, deren Häufigkeit sich lohnt zu zeigen
  let mit_bild = $derived(vorschau !== null && ['caesar', 'vigenere', 'ersetzung', 'schichten'].includes(verfahren));
  // eine PIN aus vier Ziffern ist schon der Klartext (Probe des Prüfwerts)
  let ist_pin = $derived(/^\d{4}$/.test(geheim));

  function abziehen(art: Schale): void {
    const neu = schaleAb(innen, art);
    if (neu !== null) schalen = [...schalen, neu];
  }

  function setzeZuordnung(g: string, wert: string): void {
    const k = wert.toUpperCase().slice(-1);
    const neu = { ...zuordnung };
    if (k && ABC.includes(k)) neu[g] = k;
    else delete neu[g];
    zuordnung = neu;
  }

  $effect(() => {
    const eingabe = ist_pin ? geheim : pin;
    if (verfahren !== 'pin' || !/^\d{4}$/.test(eingabe)) {
      pin_wert = null;
      return;
    }
    let aktuell = true;
    void pruefwert(eingabe).then((w) => {
      if (aktuell) pin_wert = w;
    });
    return () => {
      aktuell = false;
    };
  });
</script>

{#if verfahren === 'caesar' || verfahren === 'schichten'}
  {#if verfahren === 'schichten'}
    <div class="zeile">
      <button class="knopf-klein" onclick={() => abziehen('hex')} disabled={schaleAb(innen, 'hex') === null}>Hex abziehen</button>
      <button class="knopf-klein" onclick={() => abziehen('base64')} disabled={schaleAb(innen, 'base64') === null}>Base64 abziehen</button>
      <button class="knopf-klein" onclick={() => (schalen = schalen.slice(0, -1))} disabled={!schalen.length}>
        <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Zurück
      </button>
      <span class="dim klein">{schalen.length} {schalen.length === 1 ? 'Schale' : 'Schalen'} ab</span>
    </div>
  {/if}
  <label class="zeile">
    <span>Verschiebung</span>
    <input class="regler" type="range" min="0" max="25" bind:value={verschiebung} />
    <span class="num wert">{verschiebung}</span>
  </label>
{:else if verfahren === 'vigenere' || verfahren === 'xor'}
  <label class="zeile">
    <span>Schlüssel</span>
    <input class="eingabe" type="text" bind:value={wort} placeholder={verfahren === 'vigenere' ? 'Wort aus A bis Z' : 'Wort'} spellcheck="false" />
  </label>
{:else if verfahren === 'ersetzung'}
  <div class="zeile">
    <button class="knopf-klein" onclick={() => (zuordnung = zuordnungNachHaeufigkeit(geheim, deutsch))}>Erste Vermutung</button>
    <button class="knopf-klein" onclick={() => (zuordnung = {})} disabled={!Object.keys(zuordnung).length}>Leeren</button>
  </div>
  <div class="zuordnung">
    {#each [...ABC] as g (g)}
      <label class="paar">
        <span class="num">{g}</span>
        <input value={zuordnung[g] ?? ''} oninput={(e) => setzeZuordnung(g, e.currentTarget.value)} maxlength="2" aria-label="Klarbuchstabe für {g}" />
      </label>
    {/each}
  </div>
{:else if verfahren === 'pin'}
  {#if ist_pin}
    <p class="dim klein">Prüfwert der PIN {geheim}:</p>
  {:else}
    <label class="zeile">
      <span>PIN</span>
      <input class="eingabe" type="text" inputmode="numeric" maxlength="4" bind:value={pin} placeholder="0000" />
    </label>
  {/if}
  {#if pin_wert}
    <div class="text klein-mono">{pin_wert}</div>
    {#if !ist_pin}
      <p class="ergebnis" class:passt={pin_wert === geheim}>
        <i class="fa-solid {pin_wert === geheim ? 'fa-lock-open' : 'fa-lock'}" aria-hidden="true"></i>
        {pin_wert === geheim ? 'passt' : 'passt nicht'}
      </p>
    {/if}
  {:else if (ist_pin || pin.length === 4) && !globalThis.crypto?.subtle}
    <p class="dim klein">Den Prüfwert rechnet der Browser nur über eine sichere Verbindung.</p>
  {/if}
{/if}

{#if vorschau !== null}
  <div class="text">{vorschau}</div>
{:else if verfahren === 'xor'}
  <p class="dim klein">Kein Hex-Text.</p>
{/if}
{#if mit_bild && vorschau}<Haeufigkeit text={vorschau} {deutsch} />{/if}

<style>
  .zeile {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-sm);
  }
  .zeile .regler {
    flex: 1;
    accent-color: var(--accent);
  }
  .zeile .eingabe {
    flex: 1;
    min-width: 0;
    font-family: var(--mono);
  }
  .wert { min-width: 2ch; text-align: right; }
  .klein { font-size: var(--fs-sm); margin: 0; }
  .text {
    font: 600 var(--fs-sm) var(--mono);
    letter-spacing: 0.08em;
    line-height: 1.7;
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
    overflow-wrap: anywhere;
    max-height: 220px;
    overflow-y: auto;
    flex-shrink: 0;
  }
  .klein-mono { letter-spacing: 0; font-weight: 400; }
  .zuordnung {
    flex-shrink: 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(44px, 1fr));
    gap: 4px;
  }
  .paar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    font-size: var(--fs-sm);
    color: var(--fg-dim);
  }
  .paar input {
    width: 100%;
    height: 32px;
    text-align: center;
    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--fg);
    font: 600 var(--fs-sm) var(--mono);
    text-transform: uppercase;
  }
  .ergebnis {
    margin: 0;
    color: var(--red);
    font-weight: 600;
  }
  .ergebnis.passt { color: var(--green); }
</style>
