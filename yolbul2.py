import time
import sys
# alternatif deneme diye alternatif yolun olup olmadığını kontrol edecek metot lazım

def Counter():
    aCounter = 0
    if(n1Satır[baslangicx - 1][baslangicy] == '1'): #Yukarı Kontrol
        aCounter += 1
    if(n1Satır[baslangicx][baslangicy - 1] == '1'): #Sol Kontrol
        aCounter +=1
    if(n1Satır[baslangicx + 1][baslangicy] == '1'):  # Aşağı Kontrol
        aCounter += 1
    if(n1Satır[baslangicx][baslangicy + 1] == '1'):  # Sağ Kontrol
        aCounter +=1

    return aCounter

dosya = open(sys.argv[1], "r")
dizi2 = dosya.readlines()


nSatir = []
n1Satır = []

for satır in dizi2:
    nSatir.append(satır.strip())


for iP in range(0, len(nSatir)):
    n2Satır = list(nSatir[iP])
    n1Satır.append(n2Satır)


print(n1Satır)

baslangic = []
bitis = []

for xq in range(len(n1Satır)):
    for yq in range(len(n1Satır[0])):
        if n1Satır[xq][yq] == "F":
            # print(f"Bitiş Noktası bulma başarılı:{xq},{yq}")
            bitis = n1Satır[xq][yq]
            dosya.close()
            break
for x in range(len(n1Satır)):
    for y in range(len(n1Satır[0])):
        if n1Satır[x][y] == "S":
            # print(f"Başlangıç Noktası bulma başarılı:{x},{y}")
            # Başlangıç indexini değişkene tanımlayacak
            baslangic = n1Satır[x][y]
            baslangicx = x
            baslangicy = y
            dosya.close()
            break

PacMan = []
PacMan.append(n1Satır[x][y])
PacMan.append(n1Satır[xq][yq])
# print("Başlangıç:", PacMan[0])
print("Bitiş:", PacMan[1])
print("-------")

aCounter = 0 #Alternatif yol sayacı

Start = x
Finish = y
Pac = []
yedekYol = []
n1Satır[baslangicx][baslangicy]
# Yukarı doğru hareketlendirmeye başlayalım


while(n1Satır[baslangicx][baslangicy] != 'F'):


    if n1Satır[baslangicx-1][baslangicy] == '1' or n1Satır[baslangicx-1][baslangicy] == 'F' and n1Satır[baslangicx-1][baslangicy] > 1:#labirent yukarı doğru açıksa ilerle
        PacMan.append(n1Satır[baslangicx-1][baslangicy])
        # x ve y ye değişkenler atamamız gerkiyor
        print("Yukarı hareket edildi")
        if(aCounter > 1):
            yedekYol.append(n1Satır[baslangicx][baslangicy])
        Pac.append([baslangicx-1, baslangicy])
        baslangicx -= 1
        #n1Satır[baslangicx+1][baslangicy] = '0'
        if(n1Satır[baslangicx][baslangicy] == 'F'):
            print("Çıkış Bulundu, programdan Çıkılıyor")
            break
    # n1Satır[baslangicx][baslangicy] = yedek[u][v]
        pass

    elif n1Satır[baslangicx][baslangicy-1] == '1' or n1Satır[baslangicx][baslangicy-1] == 'F':#Sola Doğru hareket
        PacMan.append(n1Satır[baslangicx][baslangicy - 1])

        print("Sola hareket edildi")
        if(aCounter > 1):
            yedekYol.append(n1Satır[baslangicx][baslangicy])
        Pac.append([baslangicx, baslangicy - 1])
        baslangicy -= 1


        # print(n1Satır[baslangicx][baslangicy - 1])
        # n1Satır[baslangicx][baslangicy] = [baslangicx][baslangicy-1]
        # print(n1Satır[baslangicx][baslangicy])
        # n1Satır[baslangicx][baslangicy+1] = '0'
        if(n1Satır[baslangicx][baslangicy] == 'F'):
            print("Çıkış Bulundu, programdan Çıkılıyor")
            break
        else:
            pass
        pass

    elif n1Satır[baslangicx+1][baslangicy] == '1' or n1Satır[baslangicx+1][baslangicy] == 'F' : # Aşağı Doğru hareket
        PacMan.append(n1Satır[baslangicx+1][baslangicy])
        print("Aşağı hareket edildi")
        if(aCounter > 1):
            yedekYol.append(n1Satır[baslangicx][baslangicy])
        Pac.append([baslangicx+1, baslangicy])
        baslangicx += 1
        #n1Satır[baslangicx-1][baslangicy] = '0'
        if(n1Satır[baslangicx][baslangicy] == 'F'):
            print("Çıkış Bulundu, programdan Çıkılıyor")
            break
        else:
            pass
        pass

    elif n1Satır[baslangicx][baslangicy+1] == '1' or n1Satır[baslangicx][baslangicy+1] == 'F': # Sağa Doğru hareket
        PacMan.append(n1Satır[baslangicx][baslangicy+1])
        print("Sağa hareket edildi")
        if(aCounter > 1):
            yedekYol.append(n1Satır[baslangicx][baslangicy])
        Pac.append([baslangicx, baslangicy +1])
        baslangicy += 1
        # if(aCounter > 1):
        # yedekYol.append(n1Satır[baslangicx][baslangicy])
        # Pac.append([baslangicx, baslangicy+1])
        # x += 1
        # n1Satır[baslangicx][baslangicy-1] = '0'
        if (n1Satır[baslangicx][baslangicy] == 'F'):
            print("Çıkış Bulundu, programdan Çıkılıyor")
            break
        pass

    for k0 in range(0, len(n1Satır)):
        for k1 in range(0, len(n1Satır[0])):
            if [k0, k1] in Pac:
                n1Satır[k0][k1] = 'P'
                break
        pass

print("--------------")
print(Pac)
#while

dosya1 = open("cikti.txt", "w")


for w1 in range(0, len(n1Satır)):
    for j in range(0, len(n1Satır[0])):
        if [w1, j] in Pac:
            n1Satır[w1][j] = 1
        else:
            n1Satır[w1][j]= 0

print(n1Satır)

dosya=open(sys.argv[2], "w")
for i in range(0, len(n1Satır)):
    tut=str("")
    for k in range(0, len(n1Satır[0])):
        tut+=str(n1Satır[i][k])
    dosya.write(tut+"\n")
dosya.close()