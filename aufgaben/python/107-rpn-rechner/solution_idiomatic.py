def rpn_auswerten(ausdruck: str) -> int | None:
    if not ausdruck.strip():
        return None
    stack: list[int] = []
    for token in ausdruck.split():
        if token in "+-*/":
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                if b == 0:
                    return None
                stack.append(a // b)
        else:
            try:
                stack.append(int(token))
            except ValueError:
                return None
    return stack[0] if len(stack) == 1 else None
