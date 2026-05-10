import { pfadeApi } from '../api/PfadeApi';
import type { Pfad } from '../types/Aufgabe';

class PfadeStore {
  liste = $state<Pfad[]>([]);
  laden = $state(false);
  fehler = $state<string | null>(null);

  async ladeListe(): Promise<void> {
    this.laden = true;
    this.fehler = null;
    try {
      this.liste = await pfadeApi.liste();
    } catch (e) {
      this.fehler = (e as Error).message;
    } finally {
      this.laden = false;
    }
  }
}

export const pfadeStore = new PfadeStore();
