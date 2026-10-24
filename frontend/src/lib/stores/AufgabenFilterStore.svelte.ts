/*
 * Filter der Aufgabenliste, geteilt von Rechner- und Telefonansicht.
 * Die Auswahl bleibt im Browser gespeichert, damit sie nach Neuladen und
 * Seitenwechsel erhalten bleibt.
 */
import type { ProgressStatus } from '../api/ProgressApi';
import type { AufgabeKurz } from '../types/Aufgabe';
import { aufgabenStore } from './AufgabenStore.svelte';
import { progressStore } from './ProgressStore.svelte';

const SCHLUESSEL = 'codeschmiede.aufgaben_filter';
/** Pfadfilter für Aufgaben, die in keinem Pfad stehen */
export const OHNE_PFAD = '__ohne__';

const STATUS_WERTE: (ProgressStatus | '')[] = ['', 'neu', 'in_arbeit', 'geloest'];

class AufgabenFilterStore {
  suche = $state('');
  sprache = $state('');
  schwierigkeit = $state('');
  status = $state<ProgressStatus | ''>('');
  pfad = $state('');

  constructor() {
    try {
      const o = JSON.parse(localStorage.getItem(SCHLUESSEL) ?? '{}');
      if (typeof o.suche === 'string') this.suche = o.suche;
      if (typeof o.sprache === 'string') this.sprache = o.sprache;
      if (typeof o.schwierigkeit === 'string') this.schwierigkeit = o.schwierigkeit;
      if (STATUS_WERTE.includes(o.status)) this.status = o.status;
      if (typeof o.pfad === 'string') this.pfad = o.pfad;
    } catch {
      // ungültiger Eintrag: Standard bleibt
    }
  }

  speichern(): void {
    try {
      localStorage.setItem(SCHLUESSEL, JSON.stringify({
        suche: this.suche, sprache: this.sprache, schwierigkeit: this.schwierigkeit,
        status: this.status, pfad: this.pfad,
      }));
    } catch {
      // etwa privater Modus: Auswahl gilt nur bis zum Neuladen
    }
  }

  get aktiv(): boolean {
    return this.suche !== '' || this.sprache !== '' || this.schwierigkeit !== ''
      || this.status !== '' || this.pfad !== '';
  }

  zuruecksetzen(): void {
    this.suche = '';
    this.sprache = '';
    this.schwierigkeit = '';
    this.status = '';
    this.pfad = '';
  }

  /** Schlagwort als Suche setzen oder, wenn es schon gesetzt ist, wieder lösen */
  schlagwort(tag: string): void {
    this.suche = this.suche.trim() === `#${tag}` ? '' : `#${tag}`;
  }

  passt(a: AufgabeKurz): boolean {
    if (this.sprache && a.sprache !== this.sprache) return false;
    if (this.schwierigkeit && a.schwierigkeit !== this.schwierigkeit) return false;
    if (this.status && progressStore.status(a.id) !== this.status) return false;
    if (this.pfad === OHNE_PFAD && a.pfade.length > 0) return false;
    if (this.pfad && this.pfad !== OHNE_PFAD && !a.pfade.includes(this.pfad)) return false;
    const q = this.suche.trim().toLowerCase();
    if (q.startsWith('#')) return a.tags.some((t) => t.toLowerCase() === q.slice(1));
    if (q) return [a.id, a.titel, ...a.tags].join(' ').toLowerCase().includes(q);
    return true;
  }

  get treffer(): AufgabeKurz[] {
    return aufgabenStore.liste.filter((a) => this.passt(a));
  }
}

export const aufgabenFilter = new AufgabenFilterStore();
