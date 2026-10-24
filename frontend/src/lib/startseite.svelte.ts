/*
 * Texte und Ziele der Startseite, geteilt von Rechner- und
 * Telefonansicht. Alles leitet sich aus AufgabenStore und ProgressStore
 * ab; die Ansichten zeigen es nur unterschiedlich an.
 */
import { aufgabenStore } from './stores/AufgabenStore.svelte';
import { progressStore } from './stores/ProgressStore.svelte';
import { route } from './stores/RouteStore.svelte';

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
  cta: string;
  oeffnen: () => void;
}

export function lead(): string {
  const g = progressStore.gesamt;
  if (!g) return 'Frischer Start in der Codeschmiede';
  return `${g.bestandene_submissions} von ${g.submissions_gesamt} Submissions bestanden`;
}

export function tagesziel(): StartKarte {
  const h = progressStore.heute;
  const faellig = h?.faellige_wiederholungen ?? [];
  let wert = '...';
  let unter = 'Lade ...';
  if (h) {
    if (faellig.length > 0) {
      wert = `${faellig.length} fällig`;
      unter = faellig.length === 1
        ? `Heute ist 1 Wiederholung fällig: ${titelVon(faellig[0])}`
        : `Heute sind ${faellig.length} Wiederholungen fällig`;
    } else if (h.vorgeschlagene_neue) {
      wert = `${progressStore.gesamt?.aufgaben_neu ?? 0} neu`;
      unter = `Vorschlag: ${titelVon(h.vorgeschlagene_neue)}`;
    } else {
      wert = 'erledigt';
      unter = 'Alle Aufgaben sind gelöst';
    }
  }
  return {
    icon: 'fa-bullseye',
    titel: 'Tagesziel',
    wert,
    unter,
    cta: faellig.length ? 'Wiederholen' : 'Aufgabe öffnen',
    oeffnen: () => oeffne(faellig[0] ?? h?.vorgeschlagene_neue),
  };
}

export function letzteAufgabe(): StartKarte {
  const id = progressStore.heute?.letzte_aufgabe;
  const p = id ? progressStore.proAufgabe[id] : undefined;
  let unter = 'Noch keine Aufgabe begonnen';
  if (id) {
    if (!p) unter = 'Direkt weitermachen';
    else if (p.status === 'geloest') unter = `Gelöst nach ${p.versuche} ${p.versuche === 1 ? 'Versuch' : 'Versuchen'}`;
    else unter = `In Arbeit, ${p.versuche} ${p.versuche === 1 ? 'Versuch' : 'Versuche'}`;
  }
  return {
    icon: 'fa-clock-rotate-left',
    titel: 'Letzte Aufgabe',
    wert: titelVon(id),
    unter,
    cta: id ? 'Weitermachen' : 'Aufgaben ansehen',
    oeffnen: () => oeffne(id),
  };
}

export function streak(): StartKarte {
  const s = progressStore.streak;
  let wert = '-';
  let unter = 'Lade ...';
  if (s) {
    wert = s.aktuell === 1 ? '1 Tag' : `${s.aktuell} Tage`;
    if (s.aktuell === 0) unter = 'Löse heute eine Aufgabe, um die Serie zu starten';
    else if (s.laengster > s.aktuell) unter = `Längste Serie: ${s.laengster} Tage`;
    else unter = 'Persönliche Bestmarke';
  }
  return {
    icon: 'fa-fire',
    titel: 'Streak',
    wert,
    unter,
    cta: s?.aktuell ? 'Heute weiter' : 'Erste Aufgabe',
    oeffnen: () => oeffne(progressStore.heute?.vorgeschlagene_neue),
  };
}

export function fortschrittProzent(): number {
  const g = progressStore.gesamt;
  if (!g || g.aufgaben_gesamt === 0) return 0;
  return (g.aufgaben_geloest / g.aufgaben_gesamt) * 100;
}

export async function ladeStart(): Promise<void> {
  await Promise.all([
    aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : Promise.resolve(),
    progressStore.gesamt ? Promise.resolve() : progressStore.ladeAlles(),
  ]);
}
