/*
 * Aufbaukurs: Übersicht, Einführungen, Antworten, Beispiele mit Aufzeichnung, Kurztest und Merkblatt.
 * Lösungen und Erklärungen kommen nie mit der Einführung, sondern erst mit dem Urteil auf eine Antwort
 * (backend/.../kurs/sicht.py ist die Wahrheit dieser Typen).
 */
import { HttpBase } from './HttpBase';

export type Kapitelstand = 'fertig' | 'uebersprungen' | 'aktuell' | 'offen' | 'zu';
export type Frageart = 'auswahl' | 'luecke' | 'ordnen' | 'fehlerstelle';

export interface BildVerweis {
  schluessel: string;
  url: string | null;
  motiv: string;
}

export interface FrageSicht {
  id: string;
  frageart: Frageart;
  text: string;
  code: string | null;
  optionen: string[] | null;
  mehrere: boolean;
  als_code: boolean;
  luecken: number | null;
  zeilen: string[] | null;
  beantwortet: boolean;
  richtig: boolean;
}

export interface VorhersageSicht {
  art: 'auswahl' | 'eintippen';
  optionen: string[] | null;
  beantwortet: boolean;
  richtig: boolean;
}

export type TeilSicht =
  | { art: 'text'; markdown: string }
  | { art: 'alltag'; text: string; zeichnung: string | null }
  | { art: 'merke'; text: string }
  | { art: 'falle'; titel: string; text: string }
  | { art: 'augenzwinkern'; text: string }
  | { art: 'zeichnung'; url: string; unterschrift: string }
  | { art: 'diagramm'; url: string | null; titel: string }
  | { art: 'beispiel'; id: string; code: string; vorhersage: VorhersageSicht | null; ablauf: boolean }
  | { art: 'frage'; frage: FrageSicht };

export type BeispielTeil = Extract<TeilSicht, { art: 'beispiel' }>;

export interface AbschnittSicht {
  nummer: number;
  titel: string;
  teile: TeilSicht[];
  fertig: boolean;
}

export interface UebungSicht {
  id: string;
  titel: string;
  geloest: boolean;
}

export interface KapitelSicht {
  nr: number;
  einfuehrung: string;
  titel: string;
  kurz: string;
  lernziele: string[];
  karte: string;
  bild: BildVerweis | null;
  stand: Kapitelstand;
  abschnitte: number;
  abschnitte_fertig: number;
  uebungen: UebungSicht[];
  projekt: UebungSicht[];
  uebungen_offen: boolean;
  kurztest: boolean;
  vertiefung: UebungSicht[];
}

export interface KursSicht {
  sprache: string;
  titel: string;
  bloecke: { titel: string; kapitel: KapitelSicht[] }[];
}

export interface EinfuehrungSicht {
  id: string;
  sprache: string;
  titel: string;
  kurz: string;
  lernziele: string[];
  karte: string;
  kapitel: number | null;
  abschnitte: AbschnittSicht[];
}

export interface KurztestSicht {
  einfuehrung: string;
  titel: string;
  fragen: FrageSicht[];
  uebung: UebungSicht;
  bestanden: boolean;
}

export interface MerkblattSicht {
  einfuehrung: string;
  sprache: string;
  titel: string;
  kapitel: number | null;
  lernziele: string[];
  merke: string[];
  beispiele: { code: string; ausgabe: string | null }[];
  fallen: { titel: string; text: string }[];
  begriffe: string[];
  bild: BildVerweis | null;
}

export interface Antwort {
  element: string;
  wahl?: number[];
  luecken?: string[];
  reihenfolge?: number[];
  zeile?: number;
  eingetippt?: string;
}

export interface Urteil {
  richtig: boolean;
  erklaerung: string;
  abschnitt_bereit: boolean;
}

/** Ein Wert im Speicherbild; gleiche `kennung` heißt: dasselbe Objekt (Pfeil). */
export interface Wert {
  art: 'zahl' | 'text' | 'wahrheit' | 'nichts' | 'liste' | 'tupel' | 'menge' | 'woerterbuch' | 'funktion' | 'klasse' | 'objekt' | 'sonst';
  darstellung: string;
  kennung: number | null;
  elemente: Wert[] | null;
  paare: [Wert, Wert][] | null;
  attribute: Record<string, Wert> | null;
  gekuerzt: boolean;
}

export interface Rahmen {
  name: string;
  variablen: Record<string, Wert>;
}

export interface Schritt {
  zeile: number;
  rahmen: Rahmen[];
  ausgabe: string;
  rueckgabe: Wert | null;
}

export interface Aufzeichnung {
  schritte: Schritt[];
  ausgabe: string;
  fehler: string | null;
  fehlerzeile: number | null;
  gekuerzt: boolean;
  zeitueberschreitung: boolean;
  laufzeit_ms: number;
}

class KursApi extends HttpBase {
  uebersicht() {
    return this.get<KursSicht[]>('/api/kurs');
  }
  einfuehrung(id: string) {
    return this.get<EinfuehrungSicht>(`/api/kurs/einfuehrung/${encodeURIComponent(id)}`);
  }
  antworten(id: string, antwort: Antwort) {
    return this.post<Urteil>(`/api/kurs/einfuehrung/${encodeURIComponent(id)}/antwort`, antwort);
  }
  abschnittFertig(id: string, nummer: number) {
    return this.post<EinfuehrungSicht>(`/api/kurs/einfuehrung/${encodeURIComponent(id)}/abschnitt/${nummer}/fertig`, {});
  }
  ausfuehren(id: string, beispiel: string, code?: string) {
    return this.post<Aufzeichnung>(`/api/kurs/einfuehrung/${encodeURIComponent(id)}/beispiel/${encodeURIComponent(beispiel)}/ausfuehren`, code === undefined ? {} : { code });
  }
  kurztest(id: string) {
    return this.get<KurztestSicht>(`/api/kurs/kurztest/${encodeURIComponent(id)}`);
  }
  kurztestAntworten(id: string, antwort: Antwort) {
    return this.post<Urteil>(`/api/kurs/kurztest/${encodeURIComponent(id)}/antwort`, antwort);
  }
  merkblatt(id: string) {
    return this.get<MerkblattSicht>(`/api/kurs/merkblatt/${encodeURIComponent(id)}`);
  }
}

export const kursApi = new KursApi();
