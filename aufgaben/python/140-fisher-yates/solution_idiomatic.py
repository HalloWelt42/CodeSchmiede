import random


def shuffle_seed(a: list, seed: int) -> list:
    a = list(a)
    rng = random.Random(seed)
    for i in range(len(a) - 1, 0, -1):
        j = rng.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a
