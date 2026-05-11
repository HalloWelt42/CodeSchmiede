import { HttpBase } from './HttpBase';
import type { VerwaltungsEintrag } from '../types/Admin';
import type { Konfiguration } from '../types/Konfig';

export interface MusterloesungEintrag {
  variante: string;
  code: string;
}

export interface VarianteErgebnis {
  variante: string;
  bestanden: boolean;
  sichtbar_pass: number;
  sichtbar_total: number;
  versteckt_pass: number;
  versteckt_fail: number;
  laufzeit_ms: number;
  fehler_text: string | null;
}

export interface ValidierungsErgebnis {
  varianten: VarianteErgebnis[];
}

export interface AufgabeSchreibAnfrage {
  frontmatter: Record<string, unknown>;
  beschreibung_md: string;
}

export interface AufgabeVersion {
  revision: number;
  hash: string;
  gueltig_ab: string;
}

export interface PfadEintrag {
  id: string;
  titel: string;
  beschreibung: string;
  reihenfolge: string[];
  aufgaben_anzahl: number;
}

export interface PfadSchreibAnfrage {
  id: string;
  titel: string;
  beschreibung: string;
  reihenfolge: string[];
}

export class AdminApi extends HttpBase {
  constructor() {
    super('/api/admin');
  }

  aufgaben(): Promise<VerwaltungsEintrag[]> {
    return this.get<VerwaltungsEintrag[]>('/aufgaben');
  }

  /**
   * Slim-Variante fuer die Verwaltungs-Liste: tests/beschreibung/starter
   * werden als leere Strings/Listen geliefert, nur die Anzahlen stimmen.
   * Pro Eintrag deutlich kleiner -- gut bei 300+ Aufgaben. Detail dann
   * via aufgabe(id) on-demand nachladen.
   */
  aufgabenSlim(): Promise<VerwaltungsEintrag[]> {
    return this.get<VerwaltungsEintrag[]>('/aufgaben?slim=true');
  }

  aufgabe(id: string): Promise<VerwaltungsEintrag> {
    return this.get<VerwaltungsEintrag>(`/aufgaben/${id}`);
  }

  aufgabeAnlegen(daten: AufgabeSchreibAnfrage): Promise<VerwaltungsEintrag> {
    return this.post<VerwaltungsEintrag>('/aufgaben', daten);
  }

  aufgabeAendern(id: string, daten: AufgabeSchreibAnfrage): Promise<VerwaltungsEintrag> {
    return this.put<VerwaltungsEintrag>(`/aufgaben/${id}`, daten);
  }

  aufgabeLoeschen(id: string): Promise<null> {
    return this.delete<null>(`/aufgaben/${id}`);
  }

  konfig(): Promise<Konfiguration> {
    return this.get<Konfiguration>('/konfig');
  }

  musterloesungen(id: string): Promise<MusterloesungEintrag[]> {
    return this.get<MusterloesungEintrag[]>(`/aufgaben/${id}/musterloesungen`);
  }

  musterloesungSpeichern(
    id: string,
    variante: string,
    code: string,
  ): Promise<MusterloesungEintrag> {
    return this.put<MusterloesungEintrag>(
      `/aufgaben/${id}/musterloesungen/${variante}`,
      { code },
    );
  }

  musterloesungLoeschen(id: string, variante: string): Promise<null> {
    return this.delete<null>(`/aufgaben/${id}/musterloesungen/${variante}`);
  }

  validieren(id: string): Promise<ValidierungsErgebnis> {
    return this.post<ValidierungsErgebnis>(`/aufgaben/${id}/validieren`, {});
  }

  pfade(): Promise<PfadEintrag[]> {
    return this.get<PfadEintrag[]>('/pfade');
  }

  pfadAnlegen(daten: PfadSchreibAnfrage): Promise<PfadEintrag> {
    return this.post<PfadEintrag>('/pfade', daten);
  }

  pfadAendern(id: string, daten: PfadSchreibAnfrage): Promise<PfadEintrag> {
    return this.put<PfadEintrag>(`/pfade/${id}`, daten);
  }

  pfadLoeschen(id: string): Promise<null> {
    return this.delete<null>(`/pfade/${id}`);
  }

  versionen(id: string): Promise<AufgabeVersion[]> {
    return this.get<AufgabeVersion[]>(`/aufgaben/${id}/versionen`);
  }
}

export const adminApi = new AdminApi();
