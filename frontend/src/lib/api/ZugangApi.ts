import { HttpBase } from './HttpBase';

/** Öffentliche Angaben der App (/api/v1/app). */
export interface AppInfo {
  name: string;
  fassung: string;
  oberflaeche: string | null;
  anmeldung_pflicht: boolean;
  einrichtung_noetig: boolean;
  /** solange die Einrichtung nötig ist: wo der Einrichtungscode liegt (nie der Code) */
  einrichtungscode: string | null;
  kellerwolke: string;
  app_name: string | null;
  besitzer: string | null;
}

export interface Konto {
  id: string;
  name: string;
  geraet: boolean;
}

export interface Angemeldet {
  token: string;
  konto: Konto;
}

export type GeraeteArt = 'webapp' | 'browser';

export class ZugangApi extends HttpBase {
  constructor() {
    super('/api/v1');
  }

  info(): Promise<AppInfo> {
    return this.request<AppInfo>('/app', { method: 'GET', cache: 'no-store' });
  }

  einrichten(kellerwolke_adresse: string, kellerwolke_schluessel: string, einrichtungscode: string): Promise<AppInfo> {
    return this.post<AppInfo>('/einrichtung', { kellerwolke_adresse, kellerwolke_schluessel, einrichtungscode });
  }

  stand(): Promise<{ angemeldet: boolean; konto: Konto | null }> {
    return this.get('/anmeldung');
  }

  anmelden(kennung: string, passwort: string): Promise<Angemeldet> {
    return this.post<Angemeldet>('/anmeldung', { kennung, passwort });
  }

  koppeln(code: string, name: string, art: GeraeteArt): Promise<Angemeldet> {
    return this.post<Angemeldet>('/anmeldung/koppeln', { code, name, art });
  }

  abmelden(): Promise<null> {
    return this.post<null>('/anmeldung/abmelden', {});
  }
}

export const zugangApi = new ZugangApi();
