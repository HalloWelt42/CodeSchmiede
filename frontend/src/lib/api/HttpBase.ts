/*
 * Schmaler fetch-Wrapper mit JSON-Parsing und einheitlicher
 * Fehlerbehandlung. Jede Anfrage trägt die Sitzung der Kellerwolke
 * (sitzung.ts). Im Dev-Modus läuft alles über den Vite-Proxy
 * (/api -> http://127.0.0.1:8200).
 */

import { KOPF, sitzung } from './sitzung';

export class ApiFehler extends Error {
  constructor(
    public status: number,
    nachricht: string,
    public body?: unknown,
  ) {
    super(nachricht);
  }
}

export class HttpBase {
  constructor(protected basis: string = '') {}

  protected async request<T>(pfad: string, optionen: RequestInit = {}): Promise<T> {
    const url = this.basis + pfad;
    const kopf: Record<string, string> = { 'Content-Type': 'application/json' };
    if (sitzung.token) kopf[KOPF] = sitzung.token;
    const antwort = await fetch(url, {
      ...optionen,
      headers: { ...kopf, ...(optionen.headers ?? {}) },
    });
    sitzung.pruefen(antwort);

    if (!antwort.ok) {
      let body: unknown = null;
      try {
        body = await antwort.json();
      } catch {
        // ignorieren -- nicht alle Fehler liefern JSON
      }
      // Der Server nennt den Grund im Feld `detail` (z.B. Sandbox nicht erreichbar).
      const detail = (body as { detail?: unknown } | null)?.detail;
      const nachricht = typeof detail === 'string' ? detail : `${antwort.status} ${antwort.statusText}`;
      throw new ApiFehler(antwort.status, nachricht, body);
    }

    if (antwort.status === 204) return null as T;
    return (await antwort.json()) as T;
  }

  protected get<T>(pfad: string): Promise<T> {
    return this.request<T>(pfad, { method: 'GET' });
  }

  protected post<T>(pfad: string, body: unknown): Promise<T> {
    return this.request<T>(pfad, { method: 'POST', body: JSON.stringify(body) });
  }

  protected put<T>(pfad: string, body: unknown): Promise<T> {
    return this.request<T>(pfad, { method: 'PUT', body: JSON.stringify(body) });
  }

  protected delete<T>(pfad: string): Promise<T> {
    return this.request<T>(pfad, { method: 'DELETE' });
  }
}
