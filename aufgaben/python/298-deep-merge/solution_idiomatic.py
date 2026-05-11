def deep_merge(a: dict, b: dict) -> dict:
    out = dict(a)
    for key, b_val in b.items():
        if key in out and isinstance(out[key], dict) and isinstance(b_val, dict):
            out[key] = deep_merge(out[key], b_val)
        else:
            out[key] = b_val
    return out
