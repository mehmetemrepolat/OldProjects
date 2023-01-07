import random
import sys

plt = True
tem = []

bolunen = int(sys.argv[1])

bolen = int(sys.argv[2])

while plt:
    temp = int(bolunen)

    sayman = 0

    while int(bolen) <= int(temp):
        temp -= bolen
        sayman += 1

        pass

    print("Bolüm: ", sayman)
    print("Kalan", temp)

    print("----------------------------------------------")
    print("                 İkinci aşama                 ")
    print("----------------------------------------------")

    sayman2 = 0

    for a in range(0, bolen+2):
        for x in range(0, bolen+2):
            sayman2 = a + bolen * x
            if not sayman2 >= bolunen:
                tem.append(sayman2)
        if not a>=bolen:
            print(f"Kalan Sınıfı {a}: {tem}")
        tem.clear()

    template = input("Devam etmek için yeni bolunen ve bolen giriniz:").split(" ")
    bolunen = int(template[0])
    bolen = int(template[1])
    if bolen == 0:
        plt = False



