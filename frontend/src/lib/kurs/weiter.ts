/*
 * "Nächste Aufgabe" und "zurück" einer geöffneten Aufgabe, einzige Stelle für alle Aufgabenansichten.
 * Gehört die Aufgabe zu einem Kurskapitel, entscheidet die Kursdatei (Server, kurs/weiter.py): nächste Übung, dann
 * Kapitelprojekt, dann nächstes Kapitel, am Ende die Kursübersicht. Nur Aufgaben außerhalb jedes Kurses nehmen den
 * allgemeinen Vorschlag (Pfad, dann Schwierigkeit).
 */
import { kursApi, type KursWeiter } from '../api/KursApi';
import { progressApi } from '../api/ProgressApi';
import { route } from '../stores/RouteStore.svelte';

function folgeKurs(schritt: KursWeiter): boolean {
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
    if (folgeKurs(await kursApi.weiter(aufgabeId, kapitel))) return;
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
