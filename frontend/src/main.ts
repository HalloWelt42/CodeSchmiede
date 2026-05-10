import { mount } from 'svelte';
import './styles/fonts.css';
import './styles/global.css';
import App from './App.svelte';

const ziel = document.getElementById('app');
if (!ziel) {
  throw new Error('Container #app fehlt im index.html');
}

const app = mount(App, { target: ziel });

export default app;
