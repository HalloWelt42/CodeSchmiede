import { HttpBase } from './HttpBase';

export interface VorschauTabelle {
  name: string;
  spalten: string[];
  zeilen: unknown[][];
  gesamt_zeilen: number;
}

export class SqlApi extends HttpBase {
  constructor() {
    super('/api/sql');
  }

  /** Die ersten Zeilen jeder Tabelle eines Datensatzes, für die Tabellenansicht neben dem Editor. */
  async vorschau(datensatz: string, zeilen = 5): Promise<VorschauTabelle[]> {
    const antwort = await this.get<{ tabellen: VorschauTabelle[] }>(
      `/datasets/${encodeURIComponent(datensatz)}/vorschau?limit=${zeilen}`,
    );
    return antwort.tabellen;
  }
}

export const sqlApi = new SqlApi();
