"""
Mit re.sub -- so wuerden viele Linter / Naming-Helfer es machen.
"""

import re


def camel_zu_snake(text: str) -> str:
    return re.sub(r"(?<!^)([A-Z])", r"_\1", text).lower()
