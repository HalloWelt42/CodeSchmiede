import random
import string


def roboter_name(seed: int) -> str:
    rng = random.Random(seed)
    buchstaben = "".join(rng.choice(string.ascii_uppercase) for _ in range(2))
    ziffern = "".join(str(rng.randint(0, 9)) for _ in range(3))
    return buchstaben + ziffern
