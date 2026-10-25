/*
 * Zugang zur App: uneingerichtet, abgemeldet oder bereit. Die Anmeldung
 * gilt mit dem Konto der Kellerwolke (Passwort oder gekoppeltes Gerät);
 * Name und Passwort gehen nur durch, gespeichert wird allein das Token
 * der Kellerwolke (sitzung.ts).
 */

import { sitzung } from '../api/sitzung';
import { zugangApi, type AppInfo, type Konto } from '../api/ZugangApi';

export type ZugangsStand = 'laden' | 'fehler' | 'einrichtung' | 'anmelden' | 'bereit';

/** Am Telefon vom Home-Bildschirm gestartet (eigener Speicher je Web-App) */
export function alsWebApp(): boolean {
  return window.matchMedia('(display-mode: standalone)').matches
    || (navigator as Navigator & { standalone?: boolean }).standalone === true;
}

class ZugangStore {
  stand = $state<ZugangsStand>('laden');
  info = $state<AppInfo | null>(null);
  konto = $state<Konto | null>(null);
  fehler = $state<string | null>(null);

  async init(): Promise<() => void> {
    const aus = sitzung.beiWechsel((token) => {
      if (!token && this.stand === 'bereit' && this.info?.anmeldung_pflicht) {
        this.konto = null;
        this.stand = 'anmelden';
      } else if (token && this.stand === 'anmelden') {
        void this.pruefen();
      }
    });
    await this.pruefen();
    return aus;
  }

  async pruefen(): Promise<void> {
    try {
      this.info = await zugangApi.info();
      this.fehler = null;
    } catch (e) {
      this.fehler = (e as Error).message;
      this.stand = 'fehler';
      return;
    }
    if (!this.info.anmeldung_pflicht) {
      this.stand = 'bereit';
    } else if (this.info.einrichtung_noetig) {
      this.stand = 'einrichtung';
    } else if (!sitzung.token) {
      this.stand = 'anmelden';
    } else {
      try {
        const s = await zugangApi.stand();
        this.konto = s.konto;
        this.stand = s.angemeldet ? 'bereit' : 'anmelden';
        if (!s.angemeldet) sitzung.setzen('');
      } catch (e) {
        // Kellerwolke gerade weg und die Anmeldung nie bestätigt: Grund zeigen, nicht abmelden
        this.fehler = (e as Error).message;
        this.stand = 'anmelden';
      }
    }
  }

  async einrichten(adresse: string, schluessel: string, code: string): Promise<void> {
    this.info = await zugangApi.einrichten(adresse, schluessel, code);
    this.stand = 'anmelden';
  }

  async anmelden(kennung: string, passwort: string): Promise<void> {
    const a = await zugangApi.anmelden(kennung, passwort);
    this.annehmen(a.token, a.konto);
  }

  async koppeln(code: string, geraetename: string): Promise<void> {
    const a = await zugangApi.koppeln(code, geraetename, alsWebApp() ? 'webapp' : 'browser');
    this.annehmen(a.token, a.konto);
  }

  private annehmen(token: string, konto: Konto): void {
    this.konto = konto;
    this.fehler = null;
    sitzung.setzen(token);
    this.stand = 'bereit';
  }

  async abmelden(): Promise<void> {
    try {
      await zugangApi.abmelden();
    } finally {
      this.konto = null;
      sitzung.setzen('');
      this.stand = 'anmelden';
    }
  }
}

export const zugang = new ZugangStore();
