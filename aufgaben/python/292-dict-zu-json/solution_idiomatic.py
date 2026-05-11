import json


def json_dump(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))
