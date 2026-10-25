def bis_zur_wand():
    while not wand_vorne() and not am_ziel():
        if kristall():
            nimm()
        gehe()

bis_zur_wand()
links()
bis_zur_wand()
rechts()
bis_zur_wand()
links()
bis_zur_wand()
