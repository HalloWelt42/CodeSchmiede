/*
 * Texte und Ziele der Startseite, geteilt von Rechner- und
 * Telefonansicht. Alles leitet sich aus AufgabenStore, ProgressStore und
 * SpielStore ab; die Ansichten zeigen es nur unterschiedlich an.
 */
import { aufgabenStore } from './stores/AufgabenStore.svelte';
import { progressStore } from './stores/ProgressStore.svelte';
import { route } from './stores/RouteStore.svelte';
import { spielStore } from './stores/SpielStore.svelte';
import { zahl } from './spielanzeige';

function titelVon(id: string | null | undefined): string {
  if (!id) return '-';
  return aufgabenStore.findeKurz(id)?.titel ?? id;
}

function oeffne(id: string | null | undefined): void {
  if (id) route.setze('aufgabe', id);
  else route.setze('aufgaben');
}

export interface StartKarte {
  icon: string;
  titel: string;
  wert: string;
  unter: string;
  oeffnen: () => void;
}

export interface StartAktion {
  text: string;
  oeffnen: () => void;
}

export function lead(): string {
  const s = spielStore.stand?.stufe;
  if (!s) return 'Frischer Start in der Codeschmiede';
  return `Stufe ${s.stufe}, noch ${zahl(s.bis - s.punkte)} Punkte bis Stufe ${s.stufe + 1}`;
}

/** Weitermachen mit der letzten Aufgabe, sonst mit dem Vorschlag; nichts, wenn alles gelöst ist */
export function weitermachen(): StartAktion | null {
  const h = progressStore.heute;
  if (h?.letzte_aufgabe) {
    return { text: `Weitermachen: ${titelVon(h.letzte_aufgabe)}`, oeffnen: () => oeffne(h.letzte_aufgabe) };
  }
  if (h?.vorgeschlagene_neue) {
    return { text: `Loslegen: ${titelVon(h.vorgeschlagene_neue)}`, oeffnen: () => oeffne(h.vorgeschlagene_neue) };
  }
  return null;
}

export function wiederholungen(): StartAktion | null {
  const faellig = progressStore.heute?.faellige_wiederholungen ?? [];
  if (faellig.length === 0) return null;
  return {
    text: faellig.length === 1 ? '1 Wiederholung fällig' : `${faellig.length} Wiederholungen fällig`,
    oeffnen: () => oeffne(faellig[0]),
  };
}

export function letzteAufgabe(): StartKarte {
  const id = progressStore.heute?.letzte_aufgabe ?? progressStore.heute?.vorgeschlagene_neue;
  const p = id ? progressStore.proAufgabe[id] : undefined;
  let unter = 'Noch keine Aufgabe begonnen';
  if (id) {
    if (!p) unter = 'Neue Aufgabe';
    else if (p.status === 'geloest') unter = `Gelöst nach ${p.versuche} ${p.versuche === 1 ? 'Versuch' : 'Versuchen'}`;
    else unter = `In Arbeit, ${p.versuche} ${p.versuche === 1 ? 'Versuch' : 'Versuche'}`;
  }
  return {
    icon: 'fa-clock-rotate-left',
    titel: 'Weitermachen',
    wert: titelVon(id),
    unter,
    oeffnen: () => oeffne(id),
  };
}

export async function ladeStart(): Promise<void> {
  await Promise.all([
    aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : Promise.resolve(),
    progressStore.gesamt ? Promise.resolve() : progressStore.ladeAlles(),
  ]);
}
