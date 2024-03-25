laukums=[["-","-","-",]
         ["-","-","-",]
         ["-","-","-"]]
print(laukums)


def hor():
    horizon = ""
    while horizon not in ["3","1","2"]:
        horizon = input("Izvēlies skaitli - 1, 2, 3: ")
    return int(horizon)

print(laukums)
laukums= laukums.upper