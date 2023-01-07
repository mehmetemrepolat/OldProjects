import random

harfler = ["0a0", "000a000", "00a00", "1a1", "11a11", "01a10", "10a01", "#"]
palindrom = ["a"]

class palindromUret1():
    harfler = ["0a0", "000a000", "00a00", "1a1", "11a11", "01a10", "10a01", "#"]
    palindrom = ["a"]

    def palindromUret(self):
        palindrom = ["a"]
        randomUzunluk = random.randint(1, 4)

        for z in range(randomUzunluk):

            rastgeleEleman = harfler[int(random.randint(0, 7))]
            gecis = palindrom.index("a")

            uzunluk = len(list(rastgeleEleman))

            for x in range(uzunluk):
                if rastgeleEleman == '#':
                    palindrom.insert(gecis + 1, rastgeleEleman[x])
                    palindrom.pop(gecis)
                    print(palindrom)
                    return
                palindrom.insert(gecis+1, rastgeleEleman[x])  # palindrom = ["a", "1", "a", "1"]
            palindrom.pop(gecis)
        print("Palindrom:", palindrom)

def yazdır():
    palindrom = ["a"]
    randomUzunluk = random.randint(1, 4)

    for z in range(randomUzunluk):

        rastgeleEleman = harfler[int(random.randint(0, 6))]

        uzunluk = len(list(rastgeleEleman))

        gecis = palindrom.index("a")

        for x in range(uzunluk):
            palindrom.insert(gecis+1, rastgeleEleman[x])

        palindrom.pop(gecis)

    asilKelime = ""

    for c in range(len(palindrom)):
        asilKelime += palindrom[c]

    print(asilKelime)



# 0001a1000


def uzunluk(palindrom11, palindrom22):


    if len(palindrom11) == len(palindrom22):

         palindrom1uzunluk = len(palindrom11)

         #palindrom1 kontrol
         palikontrol1 = 3
         palikontrol2 = 4

         adimSayisi = (((palindrom1uzunluk + 1) / 2) - 1)
         ilkAdim = 0
         sonAdim = palindrom1uzunluk-1
         while (ilkAdim != adimSayisi + 1):
             if (ilkAdim == adimSayisi):
                 if (palindrom11[ilkAdim] == palindrom11[sonAdim]):
                     palikontrol1 = 1
             if (palindrom11[ilkAdim] != palindrom11[sonAdim]):
                 print("1. Kelime palindrom değil!")
                 return
             elif (palindrom11[ilkAdim] == palindrom11[sonAdim]):
                 ilkAdim += 1;
                 sonAdim -= 1;
             else:
                 break

         #palindrom2 kontrol
         palindrom2uzunluk = len(palindrom22)

         adimSayisi = (((palindrom2uzunluk + 1) / 2) - 1)
         ilkAdim = 0
         sonAdim = palindrom2uzunluk - 1
         while ilkAdim != adimSayisi + 1:
             if ilkAdim == adimSayisi:
                 if palindrom22[ilkAdim] == palindrom22[sonAdim]:
                     palikontrol2 = 1
             if palindrom22[ilkAdim] != palindrom22[sonAdim]:
                 print("2. Kelime palindrom değil!")
                 return
             elif palindrom22[ilkAdim] == palindrom22[sonAdim]:
                 ilkAdim += 1;
                 sonAdim -= 1;
             else:
                 break


         if palikontrol1 == palikontrol2:
            print(palindrom11," ve ", palindrom22," kelimeleri aynı uzunlukta ve palindrom")
         else:
             print("Kelimeler palindrom ama aynı uzunlukta değil")

    else:
        print("Girilen kelimeler aynı uzunlukta değil")




class unlemliPalindrom1(palindromUret1):
    def palindromUret(self):
         palindrom = ["a"]
         randomUzunluk = random.randint(1, 4)

         for z in range(randomUzunluk):

             rastgeleEleman = harfler[
                 int(random.randint(0, 7))]
             gecis = palindrom.index("a")

             uzunluk = len(list(rastgeleEleman))

             for x in range(uzunluk):
                 if rastgeleEleman == '#':
                     palindrom.insert(gecis + 1, rastgeleEleman[x])
                     palindrom.pop(gecis)
                     print(palindrom)
                     return
                 palindrom.insert(gecis + 1, rastgeleEleman[x])  # palindrom = ["a", "1", "a", "1"]
             palindrom.pop(gecis)

         palindrom.insert(0, '!')
         palindrom.append('!')

         print("Palindrom:", palindrom)

print("------------------")
object2 = unlemliPalindrom1()
print("Ünlemli Palindrom Üretme:")
object2.palindromUret()
print("------------------")
print("Palindrom Üretme:")
object = palindromUret1()
object.palindromUret()

print("------------------")
print("Yazdırma:")
yazdır()

print("------------------")
print("Uzunluk test etme:")
uzunluk('001a100', '000a000')
print("------------------")


