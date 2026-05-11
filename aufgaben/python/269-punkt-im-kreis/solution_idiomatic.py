def im_kreis(punkt: list, mittelpunkt: list, r: float) -> bool:
    dx = punkt[0] - mittelpunkt[0]
    dy = punkt[1] - mittelpunkt[1]
    return dx * dx + dy * dy <= r * r
