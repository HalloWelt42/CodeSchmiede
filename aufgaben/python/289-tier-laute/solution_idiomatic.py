class Tier:
    def laut(self) -> str:
        return "?"


class Hund(Tier):
    def laut(self) -> str:
        return "Wuff"


class Katze(Tier):
    def laut(self) -> str:
        return "Miau"


class Kuh(Tier):
    def laut(self) -> str:
        return "Muh"


class Hahn(Tier):
    def laut(self) -> str:
        return "Kikeriki"


_KLASSEN = {"Hund": Hund, "Katze": Katze, "Kuh": Kuh, "Hahn": Hahn}


def tier_konzert(tiere: list[str]) -> list[str]:
    return [_KLASSEN.get(name, Tier)().laut() for name in tiere]
