/*
 * Wo es im Kurs weitergeht, einzige Stelle für alle Ansichten: "Weiter hier" eines Kapitels sowie "Nächste Aufgabe"
 * und "zurück" einer geöffneten Aufgabe. Die Regel steht auf dem Server (kurs/weiter.py): Einführung, offene Übungen,
 * Kapitelprojekt, dann das nächste Kapitel mit Offenem, am Ende die Kursübersicht. Nur Aufgaben außerhalb jedes Kurses
 * nehmen den allgemeinen Vorschlag (Pfad, dann Schwierigkeit).
 */
import { kursApi, type KapitelSicht, type KursWeiter } from '../api/KursApi';
import { progressApi } from '../api/ProgressApi';
import { route } from '../stores/RouteStore.svelte';

function geheZuSchritt(schritt: KursWeiter): boolean {
  if (schritt.art === 'aufgabe' && schritt.aufgabe_id) {
    route.setze('aufgabe', schritt.aufgabe_id, schritt.einfuehrung ?? undefined);
  } else if (schritt.art === 'kapitel' && schritt.einfuehrung) {
    route.setze('einfuehrung', schritt.einfuehrung);
  } else if (schritt.art === 'kurs') {
    route.setze('kurs');
  } else {
    return false;
  }
  return true;
}

export async function geheZurNaechstenAufgabe(aufgabeId: string): Promise<void> {
  const kapitel = route.kursId;
  try {
    if (geheZuSchritt(await kursApi.weiter(aufgabeId, kapitel))) return;
    const v = await progressApi.weiter(aufgabeId);
    if (v.naechste_id) route.setze('aufgabe', v.naechste_id);
    else route.setze('aufgaben');
  } catch {
    if (kapitel) route.setze('einfuehrung', kapitel);
    else route.setze('aufgaben');
  }
}

/** Zurück dorthin, woher die Aufgabe kam: ins Kurskapitel oder zur Aufgabenliste */
export function zurueckVonAufgabe(): void {
  if (route.kursId) route.setze('einfuehrung', route.kursId);
  else route.setze('aufgaben');
}

/** "Weiter hier": zum ersten offenen Element des Kapitels, sonst in seine Einführung */
export function oeffneKapitel(k: KapitelSicht): void {
  if (!k.offen || !geheZuSchritt(k.offen)) route.setze('einfuehrung', k.einfuehrung);
}

/** Was im Kapitel als Nächstes offen ist, kurz: "Übung 4 von 7: Punkte steigen", "Kapitelprojekt: ...", "Einführung 2 von 4" */
export function weiterText(k: KapitelSicht): string {
  const id = k.offen?.art === 'aufgabe' ? k.offen.aufgabe_id : null;
  const nr = k.uebungen.findIndex((u) => u.id === id);
  if (nr >= 0) return `Übung ${nr + 1} von ${k.uebungen.length}: ${k.uebungen[nr].titel}`;
  const stueck = k.projekt.find((u) => u.id === id);
  if (stueck) return `Kapitelprojekt: ${stueck.titel}`;
  return `Einführung ${k.abschnitte_fertig} von ${k.abschnitte}`;
}
