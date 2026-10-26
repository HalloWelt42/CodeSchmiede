/*
 * Spielmechanik: Stufe, Serie, Tagesauftrag, Meisterschaft und Erfolge.
 * Alles leitet der Server aus Abgaben und Fortschritt ab (docs/SPIELE.md);
 * die Belohnung einer Abgabe kommt mit der Abgabe.
 */
import type { AmpelAnsicht, AmpelLaeufe } from '../types/Ampel';
import type { AufzugAnsicht, AufzugLaeufe } from '../types/Aufzug';
import type { SchaltungAnsicht, SchaltungLaeufe } from '../types/Schaltung';
import type { TuringAnsicht, TuringLaeufe } from '../types/Turing';
import { HttpBase } from './HttpBase';

export type Rang = 'bronze' | 'silber' | 'gold';
export type ErfolgsGruppe = 'meilensteine' | 'serie' | 'technik' | 'spiele';

export interface StufenStand {
  stufe: number;
  titel: string;
  punkte: number;
  /** Punkte, ab denen die Stufe gilt, und ab denen die nächste gilt */
  ab: number;
  bis: number;
  naechster_titel: string | null;
  naechster_titel_ab_stufe: number | null;
}

export interface SerienStand {
  aktuell: number;
  laengste: number;
  heute_geuebt: boolean;
  schilde: number;
  schilde_max: number;
  /** Tage bis zum nächsten Schutzschild; null, wenn alle da sind */
  naechster_schild_in: number | null;
}

export interface AuftragsZiel {
  id: string;
  text: string;
  erledigt: boolean;
}

export interface Tagesauftrag {
  datum: string;
  ziele: AuftragsZiel[];
  erledigt: boolean;
  bonus: number;
  gutgeschrieben: boolean;
}

export interface BereichStand {
  id: string;
  titel: string;
  punkte: number;
  moeglich: number;
  anteil: number;
  rang: Rang | null;
}

export interface ErfolgStand {
  id: string;
  gruppe: ErfolgsGruppe;
  titel: string;
  beschreibung: string;
  icon: string;
  rang: Rang | null;
  wert: number;
  ziel: number;
  erreicht: boolean;
}

export interface ErfolgsListe {
  eintraege: ErfolgStand[];
  erreicht: number;
  gesamt: number;
}

export interface Spielstand {
  punkte: number;
  stufe: StufenStand;
  serie: SerienStand;
  auftrag: Tagesauftrag;
  meisterschaft: BereichStand[];
}

export interface LevelStand {
  id: string;
  titel: string;
  nummer: number;
  geloest: boolean;
  sterne: number | null;
  /** Pfad, zu dem das Level gehört (im Krimi der Fall), und die Nummer darin */
  gruppe: string | null;
  nummer_in_gruppe: number | null;
  gruppe_groesse: number | null;
}

export interface SpielUebersicht {
  id: string;
  titel: string;
  icon: string;
  beschreibung: string;
  aufgabentyp: string;
  /** "stufen": Levels nacheinander; "auswahl": gleichrangige Kategorien */
  levels_als: 'stufen' | 'auswahl';
  /** wie ein Level heißt, etwa "Kapitel" */
  level_wort: string;
  levels: LevelStand[];
  geschafft: number;
  sterne: number;
  sterne_moeglich: number;
  punkte: number;
  moeglich: number;
  /** Abgaben heute in diesem Spiel (Runden, Versuche) */
  versuche_heute: number;
  /** erstes nicht gelöstes Level */
  naechstes: LevelStand | null;
}

export interface Bestwert {
  art: 'zeichen' | 'laufzeit' | 'sterne';
  neu: number;
  vorher: number;
}

export interface Belohnung {
  /** Zuwachs der Aufgabe; der beste Versuch zählt */
  punkte: number;
  punkte_versuch: number;
  punkte_moeglich: number;
  hinweise: number;
  aufgegeben: boolean;
  wiederholung: boolean;
  erster_versuch: boolean;
  sterne: number | null;
  stufe_vorher: number;
  stufe: StufenStand;
  neue_erfolge: ErfolgStand[];
  bestwerte: Bestwert[];
  auftrag_bonus: number;
  auftrag: Tagesauftrag;
}

export interface RoboterSchritt {
  befehl: 'gehe' | 'links' | 'rechts' | 'nimm';
  zeile: number;
  x: number;
  y: number;
  /** 0 Osten, 1 Norden, 2 Westen, 3 Süden */
  richtung: number;
}

/** Ein vom Server nachgespielter Lauf in einer Welt */
export interface RoboterLauf {
  schritte: RoboterSchritt[];
  am_ziel: boolean;
  kristalle_offen: number;
  fehler: string | null;
  geschafft: boolean;
}

export interface RoboterLaeufe {
  /** null: das Programm lief nicht bis zum Ende */
  laeufe: RoboterLauf[] | null;
  stdout: string;
  stderr: string;
  laufzeit_ms: number;
  timeout: boolean;
}

export interface Ergebnistabelle {
  spalten: string[];
  zeilen: unknown[][];
}

export interface KrimiErgebnis {
  tabelle: Ergebnistabelle | null;
  fehler: string | null;
  laufzeit_ms: number;
}

export interface Notiz {
  kapitel: number;
  titel: string;
  text: string;
}

export interface SprintFrage {
  code: string;
  optionen: string[];
}

export interface SprintRunde {
  id: string;
  aufgabe_id: string;
  sekunden: number;
  fragen: SprintFrage[];
}

export interface SprintRueckmeldung {
  richtig: boolean;
  /** Stelle der richtigen Antwort in der gezeigten Reihenfolge */
  richtige_wahl: number;
}

export interface SprintAuswertung {
  code: string;
  optionen: string[];
  gewaehlt: number | null;
  richtig: number;
  warum: string;
}

export interface SprintAbschluss {
  bestanden: boolean;
  sterne: number;
  treffer: number;
  fragen: number;
  laengste_kette: number;
  sekunden: number;
  auswertung: SprintAuswertung[];
  belohnung: Belohnung | null;
}

export class SpielApi extends HttpBase {
  constructor() {
    super('/api/spiel');
  }

  stand(): Promise<Spielstand> {
    return this.get<Spielstand>('/stand');
  }
  erfolge(): Promise<ErfolgsListe> {
    return this.get<ErfolgsListe>('/erfolge');
  }
  spiele(): Promise<SpielUebersicht[]> {
    return this.get<SpielUebersicht[]>('/spiele');
  }
  roboterLauf(aufgabeId: string, code: string): Promise<RoboterLaeufe> {
    return this.post<RoboterLaeufe>(`/roboter/${aufgabeId}/lauf`, { code });
  }
  ampelAnlage(aufgabeId: string): Promise<AmpelAnsicht> {
    return this.get<AmpelAnsicht>(`/ampel/${aufgabeId}/anlage`);
  }
  ampelLauf(aufgabeId: string, code: string): Promise<AmpelLaeufe> {
    return this.post<AmpelLaeufe>(`/ampel/${aufgabeId}/lauf`, { code });
  }
  aufzugHaus(aufgabeId: string): Promise<AufzugAnsicht> {
    return this.get<AufzugAnsicht>(`/aufzug/${aufgabeId}/haus`);
  }
  aufzugLauf(aufgabeId: string, code: string): Promise<AufzugLaeufe> {
    return this.post<AufzugLaeufe>(`/aufzug/${aufgabeId}/lauf`, { code });
  }
  turingMaschine(aufgabeId: string): Promise<TuringAnsicht> {
    return this.get<TuringAnsicht>(`/turing/${aufgabeId}/maschine`);
  }
  turingLauf(aufgabeId: string, code: string): Promise<TuringLaeufe> {
    return this.post<TuringLaeufe>(`/turing/${aufgabeId}/lauf`, { code });
  }
  schaltungPlan(aufgabeId: string): Promise<SchaltungAnsicht> {
    return this.get<SchaltungAnsicht>(`/schaltung/${aufgabeId}/plan`);
  }
  schaltungLauf(aufgabeId: string, code: string): Promise<SchaltungLaeufe> {
    return this.post<SchaltungLaeufe>(`/schaltung/${aufgabeId}/lauf`, { code });
  }
  krimiAusfuehren(aufgabeId: string, code: string): Promise<KrimiErgebnis> {
    return this.post<KrimiErgebnis>(`/krimi/${aufgabeId}/ausfuehren`, { code });
  }
  krimiPinnwand(aufgabeId: string): Promise<Notiz[]> {
    return this.get<Notiz[]>(`/krimi/${aufgabeId}/pinnwand`);
  }
  sprintRunde(aufgabeId: string): Promise<SprintRunde> {
    return this.post<SprintRunde>(`/sprint/${aufgabeId}/runde`, {});
  }
  sprintAntwort(rundeId: string, frage: number, wahl: number): Promise<SprintRueckmeldung> {
    return this.post<SprintRueckmeldung>(`/sprint/runde/${rundeId}/antwort`, { frage, wahl });
  }
  sprintAbschluss(rundeId: string): Promise<SprintAbschluss> {
    return this.post<SprintAbschluss>(`/sprint/runde/${rundeId}/abschluss`, {});
  }
}

export const spielApi = new SpielApi();
