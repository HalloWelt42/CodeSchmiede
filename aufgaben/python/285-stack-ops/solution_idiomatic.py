class Stack:
    def __init__(self) -> None:
        self.daten: list = []

    def push(self, wert) -> None:
        self.daten.append(wert)

    def pop(self) -> None:
        if self.daten:
            self.daten.pop()


def stack_lauf(operationen: list) -> list:
    s = Stack()
    for op in operationen:
        if op[0] == "push":
            s.push(op[1])
        else:
            s.pop()
    return s.daten
