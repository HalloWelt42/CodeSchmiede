/* Gemeinsames der Steuerungsspiele (backend/src/codeschmiede/steuerung/teilschritte.py). */

export interface TeilschrittStand {
  titel: string;
  text: string;
  erfuellt: boolean;
  /** false, wenn der Schritt versteckte Abläufe braucht, die ein Probelauf nicht hat */
  geprueft: boolean;
  befunde: string[];
}
