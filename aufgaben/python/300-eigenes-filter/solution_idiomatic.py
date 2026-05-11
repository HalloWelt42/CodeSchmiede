_PREDS = {
    "positive": lambda x: x > 0,
    "negative": lambda x: x < 0,
    "even": lambda x: x % 2 == 0,
    "odd": lambda x: x % 2 != 0,
    "nonzero": lambda x: x != 0,
}


def filter_pred(liste: list, pred: str) -> list:
    if pred not in _PREDS:
        return list(liste)
    fn = _PREDS[pred]
    return [x for x in liste if fn(x)]
