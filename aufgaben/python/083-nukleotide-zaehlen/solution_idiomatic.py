def nukleotide_zaehlen(dna: str) -> dict[str, int]:
    if set(dna) - set("ACGT"):
        return {}
    return {n: dna.count(n) for n in "ACGT"}
