def regenwasser(hoehen: list[int]) -> int:
    if not hoehen:
        return 0
    links, rechts = 0, len(hoehen) - 1
    max_l = max_r = 0
    wasser = 0
    while links <= rechts:
        if hoehen[links] < hoehen[rechts]:
            if hoehen[links] >= max_l:
                max_l = hoehen[links]
            else:
                wasser += max_l - hoehen[links]
            links += 1
        else:
            if hoehen[rechts] >= max_r:
                max_r = hoehen[rechts]
            else:
                wasser += max_r - hoehen[rechts]
            rechts -= 1
    return wasser
