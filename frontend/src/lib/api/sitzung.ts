/*
 * Sitzung der Kellerwolke für diese App: Token im Browser dieses Geräts
 * (localStorage), mitgeschickt als Kopf X-Kellerwolke-Sitzung. Weist der
 * Server die Anmeldung ab (401 mit `WWW-Authenticate: Kellerwolke-Sitzung`),
 * ist sie vorbei; ein anderer 401 beendet sie nie. Tabs derselben App
 * folgen einander über das storage-Ereignis.
 */

const SCHLUESSEL = 'codeschmiede.sitzung';
export const KOPF = 'X-Kellerwolke-Sitzung';

type Hoerer = (token: string) => void;
const hoerer = new Set<Hoerer>();

function lesen(): string {
  try {
    return localStorage.getItem(SCHLUESSEL) ?? '';
  } catch {
    return '';
  }
}

let token = lesen();

export const sitzung = {
  get token(): string {
    return token;
  },

  setzen(neu: string): void {
    token = neu;
    try {
      if (neu) localStorage.setItem(SCHLUESSEL, neu);
      else localStorage.removeItem(SCHLUESSEL);
    } catch {
      // privater Modus: gilt nur bis zum Neuladen
    }
    hoerer.forEach((h) => h(neu));
  },

  /** Ruft `h` bei jedem Wechsel, auch aus anderen Tabs; gibt das Abmelden zurück. */
  beiWechsel(h: Hoerer): () => void {
    hoerer.add(h);
    return () => hoerer.delete(h);
  },

  /** Antwort des Servers prüfen: nur seine eigene Abweisung beendet die Sitzung. */
  pruefen(antwort: Response): void {
    if (antwort.status === 401 && antwort.headers.get('WWW-Authenticate') === 'Kellerwolke-Sitzung' && token) {
      this.setzen('');
    }
  },
};

window.addEventListener('storage', (e) => {
  if (e.key !== SCHLUESSEL) return;
  token = e.newValue ?? '';
  hoerer.forEach((h) => h(token));
});
