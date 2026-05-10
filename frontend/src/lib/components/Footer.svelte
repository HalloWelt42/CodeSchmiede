<script lang="ts">
  const version = __APP_VERSION__;
</script>

<footer>
  <span class="links">
    <i class="fa-solid fa-hammer" aria-hidden="true"></i>
    Codeschmiede v{version}
  </span>
  <span class="rechts">Lokal, ohne Tracking, ohne Werbung</span>
</footer>

<style>
  footer {
    height: var(--footer-h);
    flex-shrink: 0;
    padding: 0 var(--sp-4);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--bg-card);
    border-top: 1px solid var(--border);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }
  .links {
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .links i {
    color: var(--accent);
  }
  .rechts {
    color: var(--fg-mute);
  }
</style>
