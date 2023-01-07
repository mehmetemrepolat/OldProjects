import random

kütüphane = ["W1x1W", "0w0x0w0", "00x00", "q0x0q", "11x11", "01x10", "10x01", "ε"]
pallindrome = ["x"]


class pallindrome1():
    kütüphane = ["W1x1W", "0w0x0w0", "00x00", "q0x0q", "11x11", "01x10", "10x01", "ε"]
    pallindrome = ["x"]

    def pallindromeUret(self):
        pallindrome = ["x"]
        randomUzunluk = random.randint(1, 4)

        for z in range(randomUzunluk):

            xxx = kütüphane[int(random.randint(0, 7))]
            nokta = pallindrome.index("x")

            uzunluk = len(list(xxx))

            for x in range(uzunluk):
                if xxx == 'ε':
                    pallindrome.insert(nokta + 1, xxx[x])
                    pallindrome.pop(nokta)
                    print("pallindrome:", pallindrome)
                    return
                pallindrome.insert(nokta + 1, xxx[x])
            pallindrome.pop(nokta)
        print("pallindrome:", pallindrome)

    def yazdır(self):
        pallindrome = ["x"]
        for z in range(random.randint(1, 4)):
            randomQ = kütüphane[int(random.randint(0, 6))]
            uzunluk = len(list(randomQ))
            nokta = pallindrome.index("x")
            for x in range(uzunluk):
                pallindrome.insert(nokta + 1, randomQ[x])
            pallindrome.pop(nokta)
        print(pallindrome)


def uzunluk(pallindrome, pallindrome1):
    if len(pallindrome) == len(pallindrome1):
        print("Girilen pallindromelar aynı uzunlukta")

    else:
        print("Girilen pallindromelar aynı uzunlukta değil")


def test(palindromA):
    if palindromA == palindromA[::-1]:
        print("Girilen kelime Palindromdur")
    elif palindromA != palindromA[::-1]:
        print("Girilen kelime Palindrom değildir")


def unlemliUret():
    kütüphane = ["W1x1W", "0w0x0w0", "00x00", "q0x0q", "11x11", "01x10", "10x01", "ε"]
    pallindrome = ["x"]
    randomUzunluk = random.randint(1, 4)

    for z in range(randomUzunluk):

        xxx = kütüphane[int(random.randint(0, 7))]
        nokta = pallindrome.index("x")

        uzunluk = len(list(xxx))

        for x in range(uzunluk):
            if xxx == 'ε':
                pallindrome.insert(nokta + 1, xxx[x])
                pallindrome.pop(nokta)
                print(pallindrome)
                return
            pallindrome.insert(nokta + 1, xxx[x])
        pallindrome.pop(nokta)
    pallindrome.insert(0, '!')
    pallindrome.append('!')

    unlemliKelime = ""
    for c in range(len(pallindrome)):
        unlemliKelime += pallindrome[c]

    print(unlemliKelime)
    print(len(pallindrome), " Uzunluklu kelime:", unlemliKelime)


object2 = pallindrome1()
object2.pallindromeUret()
unlemliUret()
test("000x000")