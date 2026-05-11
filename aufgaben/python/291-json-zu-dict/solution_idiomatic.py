import json


def json_parse(s: str):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return None
