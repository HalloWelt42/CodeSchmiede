fische = {"Pit": 4, "Pia": 7, "Paul": 9, "Polly": 2}
bester, meiste = "", 0
for name, n in fische.items():
    if n > meiste:
        bester, meiste = name, n
print(f"{bester} mit {meiste} Fischen")
