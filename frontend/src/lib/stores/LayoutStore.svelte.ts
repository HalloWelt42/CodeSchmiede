/*
 * LayoutStore -- aktuell nur das Ein-/Ausklappen der Sidebar.
 * Persistiert in localStorage, damit der Stand zwischen Sitzungen bleibt.
 */

const SCHLUESSEL = 'codeschmiede.sidebar_offen';

class LayoutStore {
  sidebarOffen = $state(true);

  init(): void {
    const wert = localStorage.getItem(SCHLUESSEL);
    if (wert !== null) {
      this.sidebarOffen = wert === '1';
    }
  }

  toggleSidebar(): void {
    this.sidebarOffen = !this.sidebarOffen;
    localStorage.setItem(SCHLUESSEL, this.sidebarOffen ? '1' : '0');
  }
}

export const layout = new LayoutStore();
