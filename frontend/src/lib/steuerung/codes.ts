/*
 * Die Verfahren von Codes knacken zum Probieren von Hand (Werkbank). Gerechnet wird wie im Backend
 * (backend/src/codeschmiede/steuerung/codes.py): nur A bis Z ändern sich, alles andere bleibt stehen.
 * Gewertet wird allein das Programm; was hier entsteht, ist nur zum Verstehen.
 */

export const ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function nummer(c: string): number {
  return ABC.indexOf(c);
}

export function schiebe(text: string, n: number): string {
  return [...text].map((c) => (nummer(c) >= 0 ? ABC[(((nummer(c) + n) % 26) + 26) % 26] : c)).join('');
}

/** Vigenère zurück: der n-te Buchstabe (nur A bis Z gezählt) rückt um den n-ten Buchstaben des Worts zurück. */
export function vigenereZurueck(text: string, wort: string): string {
  const w = [...wort.toUpperCase()].filter((c) => nummer(c) >= 0);
  if (!w.length) return text;
  let i = 0;
  return [...text].map((c) => (nummer(c) >= 0 ? schiebe(c, -nummer(w[i++ % w.length])) : c)).join('');
}

/** Ersetzung zurück: zuordnung[c] ist der Klarbuchstabe zum Geheimbuchstaben c; ohne Zuordnung bleibt ein Punkt. */
export function ersetzeZurueck(text: string, zuordnung: Record<string, string>): string {
  return [...text].map((c) => (nummer(c) >= 0 ? (zuordnung[c] ?? '·') : c)).join('');
}

/** Erste Vermutung: der häufigste Geheimbuchstabe wird der häufigste deutsche usw. */
export function zuordnungNachHaeufigkeit(text: string, deutsch: Record<string, number>): Record<string, string> {
  const zahl = zaehle(text);
  const geheim = [...ABC].sort((a, b) => zahl[b] - zahl[a]);
  const klar = [...ABC].sort((a, b) => (deutsch[b] ?? 0) - (deutsch[a] ?? 0));
  return Object.fromEntries(geheim.map((g, i) => [g, klar[i]]));
}

export function hexZuBytes(hex: string): Uint8Array | null {
  if (!/^([0-9a-f]{2})+$/i.test(hex)) return null;
  return Uint8Array.from(hex.match(/../g) ?? [], (b) => parseInt(b, 16));
}

const LESER = new TextDecoder('utf-8', { fatal: false });

export function bytesZuText(bytes: Uint8Array): string {
  return LESER.decode(bytes);
}

/** XOR zurück: jedes Byte mit dem Byte des Worts an derselben Stelle (reihum). */
export function xorZurueck(hex: string, wort: string): string | null {
  const daten = hexZuBytes(hex);
  const schluessel = new TextEncoder().encode(wort);
  if (!daten) return null;
  if (!schluessel.length) return bytesZuText(daten);
  return bytesZuText(daten.map((b, i) => b ^ schluessel[i % schluessel.length]));
}

export type Schale = 'hex' | 'base64';

/** Eine Schicht abziehen; null, wenn der Text nicht so aussieht. */
export function schaleAb(text: string, art: Schale): string | null {
  try {
    if (art === 'hex') {
      const bytes = hexZuBytes(text);
      return bytes ? bytesZuText(bytes) : null;
    }
    if (!/^[A-Za-z0-9+/]+={0,2}$/.test(text) || text.length % 4) return null;
    return bytesZuText(Uint8Array.from(atob(text), (c) => c.charCodeAt(0)));
  } catch {
    return null;
  }
}

/** Wie oft jeder Buchstabe A bis Z vorkommt. */
export function zaehle(text: string): Record<string, number> {
  const zahl: Record<string, number> = Object.fromEntries([...ABC].map((c) => [c, 0]));
  for (const c of text) if (c in zahl) zahl[c] += 1;
  return zahl;
}

/** Anteil je Buchstabe in Prozent, wie DEUTSCH. */
export function haeufigkeit(text: string): Record<string, number> {
  const zahl = zaehle(text);
  const summe = Object.values(zahl).reduce((a, b) => a + b, 0);
  return Object.fromEntries([...ABC].map((c) => [c, summe ? (100 * zahl[c]) / summe : 0]));
}

/** SHA-256 als Hex; null, wo der Browser es nicht anbietet (nur über https oder localhost). */
export async function pruefwert(pin: string): Promise<string | null> {
  if (!globalThis.crypto?.subtle) return null;
  const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(pin));
  return [...new Uint8Array(hash)].map((b) => b.toString(16).padStart(2, '0')).join('');
}
