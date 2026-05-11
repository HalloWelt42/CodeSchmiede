import re


def emails(text: str) -> list[str]:
    return re.findall(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}", text)
