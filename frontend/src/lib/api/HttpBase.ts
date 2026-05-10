/*
 * Schmaler fetch-Wrapper mit JSON-Parsing und einheitlicher
 * Fehlerbehandlung. Im Dev-Modus laeuft alles über den Vite-Proxy
 * (/api -> http://127.0.0.1:8200).
 */

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
    const antwort = await fetch(url, {
      headers: { 'Content-Type': 'application/json', ...(optionen.headers ?? {}) },
      ...optionen,
    });

    if (!antwort.ok) {
      let body: unknown = null;
      try {
        body = await antwort.json();
      } catch {
        // ignorieren -- nicht alle Fehler liefern JSON
      }
      throw new ApiFehler(antwort.status, `${antwort.status} ${antwort.statusText}`, body);
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
