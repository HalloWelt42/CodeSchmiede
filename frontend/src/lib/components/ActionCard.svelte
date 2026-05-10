<script lang="ts">
  interface Props {
    icon: string;
    titel: string;
    wert: string;
    hinweis: string;
    cta: string;
    onClick: () => void;
  }

  let { icon, titel, wert, hinweis, cta, onClick }: Props = $props();
</script>

<button class="card" onclick={onClick}>
  <header>
    <i class="fa-solid {icon}" aria-hidden="true"></i>
    <span class="titel">{titel}</span>
  </header>

  <div class="wert num">{wert}</div>

  <p class="hinweis">{hinweis}</p>

  <span class="cta">
    {cta}
    <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
  </span>
</button>

<style>
  .card {
    text-align: left;
    padding: var(--sp-4);
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--fg);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
    cursor: pointer;
    transition: border-color 0.15s, transform 0.15s, background 0.15s;
    border-radius: var(--radius);
  }
  .card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    background: var(--bg-card);
  }
  header {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  header i {
    color: var(--accent);
    font-size: var(--fs-sm);
  }
  .wert {
    font-size: var(--fs-xxl);
    color: var(--fg);
    line-height: 1;
    margin-top: var(--sp-2);
  }
  .hinweis {
    margin: 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
    line-height: 1.5;
    flex: 1;
  }
  .cta {
    margin-top: var(--sp-3);
    color: var(--accent);
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-1);
  }
</style>
