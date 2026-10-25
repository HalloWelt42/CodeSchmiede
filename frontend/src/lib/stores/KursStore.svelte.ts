/*
 * Kursübersicht aller Sprachen, einmal geladen und nach Fortschritt neu geholt (Abschnitt fertig, Kurztest,
 * gelöste Übung). Gewählte Sprache bleibt im Browser gemerkt.
 */
import { kursApi, type KapitelSicht, type KursSicht } from '../api/KursApi';

const MERKER = 'cs-kurs-sprache';

class KursStore {
  kurse = $state<KursSicht[]>([]);
  geladen = $state(false);
  fehler = $state<string | null>(null);
  sprache = $state<string>(lesen() ?? 'python');
  private laeuft: Promise<void> | null = null;

  laden(neu = false): Promise<void> {
    if (this.laeuft && !neu) return this.laeuft;
    this.laeuft = kursApi.uebersicht().then(
      (k) => {
        this.kurse = k;
        this.geladen = true;
        this.fehler = null;
        if (!k.some((x) => x.sprache === this.sprache) && k[0]) this.sprache = k[0].sprache;
      },
      (e: unknown) => {
        this.fehler = e instanceof Error ? e.message : String(e);
      },
    );
    return this.laeuft;
  }

  waehleSprache(sprache: string): void {
    this.sprache = sprache;
    try {
      localStorage.setItem(MERKER, sprache);
    } catch {
      // ohne Speicher bleibt die Wahl bis zum Neuladen
    }
  }

  get kurs(): KursSicht | null {
    return this.kurse.find((k) => k.sprache === this.sprache) ?? null;
  }

  alleKapitel(kurs: KursSicht | null = this.kurs): KapitelSicht[] {
    return kurs?.bloecke.flatMap((b) => b.kapitel) ?? [];
  }

  kapitel(einfuehrung: string): KapitelSicht | null {
    for (const k of this.kurse) {
      const treffer = this.alleKapitel(k).find((x) => x.einfuehrung === einfuehrung);
      if (treffer) return treffer;
    }
    return null;
  }

  /** Wo es weitergeht: das aktuelle Kapitel der gewählten Sprache */
  get weiter(): KapitelSicht | null {
    return this.alleKapitel().find((k) => k.stand === 'aktuell') ?? null;
  }

  sprachTitel(sprache: string): string {
    return this.kurse.find((k) => k.sprache === sprache)?.titel ?? sprache;
  }
}

function lesen(): string | null {
  try {
    return localStorage.getItem(MERKER);
  } catch {
    return null;
  }
}

export const kursStore = new KursStore();
