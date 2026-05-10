_ALLERGIEN = [
    "eier", "erdnuesse", "schalentiere", "erdbeeren",
    "tomaten", "schokolade", "pollen", "katzen",
]


def allergien(score: int) -> list[str]:
    return [a for i, a in enumerate(_ALLERGIEN) if score & (1 << i)]
