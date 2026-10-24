// Hilfen für die Seitenskripte, vor dem Inhalt geladen.
window.STUFE = (id) => (DATEN.schwierigkeiten.find((s) => s.id === id) || { titel: id }).titel;
window.STATUS = { '233-zwei-tausch': 'geloest', '235-erste-n': 'arbeit', 's004-buecher-titel': 'geloest' };
window.STATUS_ICON = (s) => (s === 'geloest' ? 'fa-circle-check' : s === 'arbeit' ? 'fa-pen-to-square' : 'fa-circle');
window.SPRACHE = (id) => (DATEN.sprachen.find((s) => s.id === id) || { titel: id }).titel;
