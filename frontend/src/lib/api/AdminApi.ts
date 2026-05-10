import { HttpBase } from './HttpBase';
import type { VerwaltungsEintrag } from '../types/Admin';

export class AdminApi extends HttpBase {
  constructor() {
    super('/api/admin');
  }

  aufgaben(): Promise<VerwaltungsEintrag[]> {
    return this.get<VerwaltungsEintrag[]>('/aufgaben');
  }
}

export const adminApi = new AdminApi();
