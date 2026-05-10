def baue_baum(records: list[dict]) -> dict:
    if not records:
        return {}
    # Validierung
    n = len(records)
    ids = sorted(r["id"] for r in records)
    if ids != list(range(n)):
        return {}
    # Sortiere nach id, validiere parent < id (außer Wurzel)
    by_id = {r["id"]: r for r in records}
    if by_id[0]["parent"] != 0:
        return {}
    for i in range(1, n):
        if by_id[i]["parent"] >= i:
            return {}
    # Baue Knoten
    knoten: dict[int, dict] = {i: {"id": i, "kinder": []} for i in range(n)}
    for i in range(1, n):
        knoten[by_id[i]["parent"]]["kinder"].append(knoten[i])
    return knoten[0]
