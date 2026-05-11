class Zaehler:
    def __init__(self) -> None:
        self.wert = 0

    def anwenden(self, op: str) -> int:
        if op == "inc":
            self.wert += 1
        elif op == "dec":
            self.wert -= 1
        elif op == "reset":
            self.wert = 0
        elif op == "double":
            self.wert *= 2
        return self.wert


def zaehler_lauf(operationen: list[str]) -> list[int]:
    z = Zaehler()
    return [z.anwenden(op) for op in operationen]
