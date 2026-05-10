from itertools import permutations as it_perm


def permutationen(text: str) -> list[str]:
    return sorted({"".join(p) for p in it_perm(text)})
