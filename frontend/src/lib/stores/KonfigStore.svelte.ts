/*
 * Lädt die zentrale Konfiguration einmal beim App-Start. Komponenten
 * lesen daraus dynamisch Schwierigkeitsstufen, Sprachen und Aufgabentypen
 * -- damit sind die Listen nicht mehr im Code hardcodiert.
 */

import { adminApi } from '../api/AdminApi';
import type {
  AufgabentypKonfig,
  Konfiguration,
  SchwierigkeitsStufe,
  SprachKonfig,
} from '../types/Konfig';

class KonfigStore {
  daten = $state<Konfiguration>({
    schwierigkeiten: [],
    sprachen: [],
    aufgabentypen: [],
  });
  geladen = $state(false);
  fehler = $state<string | null>(null);

  async init(): Promise<void> {
    try {
      this.daten = await adminApi.konfig();
      this.geladen = true;
    } catch (e) {
      this.fehler = (e as Error).message;
    }
  }

  schwierigkeit(id: string): SchwierigkeitsStufe | undefined {
    return this.daten.schwierigkeiten.find((s) => s.id === id);
  }

  sprache(id: string): SprachKonfig | undefined {
    return this.daten.sprachen.find((s) => s.id === id);
  }

  aufgabentyp(id: string): AufgabentypKonfig | undefined {
    return this.daten.aufgabentypen.find((t) => t.id === id);
  }

  schwierigkeitTitel(id: string): string {
    return this.schwierigkeit(id)?.titel ?? id;
  }

  schwierigkeitFarbe(id: string): string {
    return this.schwierigkeit(id)?.farbe ?? 'accent';
  }
}

export const konfig = new KonfigStore();
