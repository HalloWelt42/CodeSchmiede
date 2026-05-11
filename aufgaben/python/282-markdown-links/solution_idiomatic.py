import re


def markdown_links(text: str) -> list[list[str]]:
    return [list(t) for t in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)]
