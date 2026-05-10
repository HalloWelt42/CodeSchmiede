import { HttpBase } from './HttpBase';
import type { VerwaltungsEintrag } from '../types/Admin';
import type { Konfiguration } from '../types/Konfig';

export class AdminApi extends HttpBase {
  constructor() {
    super('/api/admin');
  }

  aufgaben(): Promise<VerwaltungsEintrag[]> {
    return this.get<VerwaltungsEintrag[]>('/aufgaben');
  }

  konfig(): Promise<Konfiguration> {
    return this.get<Konfiguration>('/konfig');
  }
}

export const adminApi = new AdminApi();
