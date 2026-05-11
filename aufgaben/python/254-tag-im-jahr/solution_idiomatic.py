from datetime import date


def tag_im_jahr(jahr: int, monat: int, tag: int) -> int:
    try:
        return date(jahr, monat, tag).timetuple().tm_yday
    except ValueError:
        return 0
