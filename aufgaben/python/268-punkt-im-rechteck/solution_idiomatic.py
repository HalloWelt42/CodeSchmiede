def im_rechteck(punkt: list, rect: list) -> bool:
    x, y = punkt
    xmin, ymin, xmax, ymax = rect
    return xmin <= x <= xmax and ymin <= y <= ymax
