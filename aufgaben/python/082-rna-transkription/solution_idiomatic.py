def zu_rna(dna: str) -> str:
    return dna.translate(str.maketrans("GCTA", "CGAU"))
