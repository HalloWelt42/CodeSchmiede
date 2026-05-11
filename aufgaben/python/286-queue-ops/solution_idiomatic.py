from collections import deque


class Queue:
    def __init__(self) -> None:
        self.daten: deque = deque()

    def enqueue(self, wert) -> None:
        self.daten.append(wert)

    def dequeue(self) -> None:
        if self.daten:
            self.daten.popleft()


def queue_lauf(operationen: list) -> list:
    q = Queue()
    for op in operationen:
        if op[0] == "enqueue":
            q.enqueue(op[1])
        else:
            q.dequeue()
    return list(q.daten)
