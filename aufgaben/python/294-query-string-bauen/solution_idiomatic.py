def query_build(d: dict) -> str:
    return "&".join(f"{k}={v}" for k, v in sorted(d.items()))
