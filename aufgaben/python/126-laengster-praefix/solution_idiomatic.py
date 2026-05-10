def gemeinsamer_praefix(strings: list[str]) -> str:
    out: list[str] = []
    for spalte in zip(*strings):
        if len(set(spalte)) == 1:
            out.append(spalte[0])
        else:
            break
    return "".join(out)
