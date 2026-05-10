def balanciert(text: str) -> bool:
    paare = {")": "(", "]": "[", "}": "{"}
    oeffner = set("([{")
    stack: list[str] = []
    for c in text:
        if c in oeffner:
            stack.append(c)
        elif c in paare:
            if not stack or stack[-1] != paare[c]:
                return False
            stack.pop()
    return not stack
