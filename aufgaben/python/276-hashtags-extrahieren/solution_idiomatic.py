import re


def hashtags(text: str) -> list[str]:
    return re.findall(r"#(\w+)", text)
