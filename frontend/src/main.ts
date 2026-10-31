import { mount } from 'svelte';
import 'katex/dist/katex.min.css';
import './styles/fonts.css';
// Rahmen am Telefon (Kopf, Fußleiste, sichere Ränder, Seitenrand, Eingaben ohne Zoom): die eine Wahrheit im Appkern
import 'appkern-oberflaeche/rahmen.css';
import './styles/global.css';
import './styles/editor.css';
import './styles/kurs.css';
import './styles/steuerung.css';
import App from './App.svelte';

const ziel = document.getElementById('app');
if (!ziel) {
  throw new Error('Container #app fehlt im index.html');
}

const app = mount(App, { target: ziel });

export default app;
