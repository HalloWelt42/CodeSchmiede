"""Lauf eines CSS-Beispiels: Markup und CSS für die Bühne im Browser.

CSS braucht keine Sandbox, gerendert wird im Browser auf derselben Bühne wie bei den CSS-Aufgaben. Der Lauf geht
trotzdem über den Server, damit dort wie bei den anderen Sprachen gilt: erst vorhersagen, dann ausführen.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class CssLauf(BaseModel):
    art: Literal["css"] = "css"
    html: str
    css: str
