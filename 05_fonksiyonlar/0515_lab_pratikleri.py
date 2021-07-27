"""
def sonuc():
    s1 = int(input("Lütfen ilk sayıyı giriniz:"))
    s2 = int(input("Lütfen ikinci sayıyı giriniz:"))
    if s1 > s2:
        return s1-s2
    elif s1 < s2:
        return s1+s2
    else:
        return s1, s2


print(sonuc())
"""
"""
def birlestir(ad,soyad):
    return f"{ad.title()} {soyad.title()}"

print(birlestir(input("1. ifade: "), input("2. ifade: ")))
"""

"""
. yazıTura()
. random değere göre → 'yazı' - 'tura' return edeceğiz
. while True içinde sonsuz döngü için de yazı için 'y', tura için 't', çıkmak için 'ç'
. 5 kez kazanan oyunu bitirir.
. her döngü de skor ekrana yazılacak
"""
"""
def yaziTura():
    import random
    if random.randint(1,2)==1:
        return "yazı"
    else:
        return "tura"

def skorYaz(o,p):
    print(f"Oyuncu Skor {o}  Pc skor {p}")

def skorTest(o,p):
    if o>=5:
        return "Kazanan Oyuncu!!!"
    elif p>=5:
        return "Kazanan Bilgisayar!!!"
    else:
        return

oyuncuSkor, pcSkor= 0,0
while True:
    skorYaz(oyuncuSkor, pcSkor)
    yt=input("Yazı için 'y' tura için 't', çıkmak için 'ç'...")
    if yt.lower=="ç":
        break
    if yt=="y":
        if yaziTura()=="yazı":
            oyuncuSkor +=1
        else:
            pcSkor+=1
    elif yt=="t":
        if yaziTura()=="tura":
            oyuncuSkor +=1
        else:
            pcSkor+=1
    else:
        print("hatalı seçim")
        continue
    if not skorTest(oyuncuSkor,pcSkor)==None:
        print(skorTest(oyuncuSkor,pcSkor))
        break
"""
"""
. degerAl()
. kullanıcıdan sayı alacak, int olup olmadığını kontrol edecek
. int ise çeviri yapacak, değil ise -1 geriye return edecek
. us()
. degerAl() fonksiyonundan dönen değer -1 değil ise işlem
. 5. kuvvetini alsın
"""
"""
def degerAl():
    sayi=input("sayı giriniz:")
    if sayi.isdigit():
        return int(sayi)
    else:
        return -1

def us(taban):
    if taban==-1:
        print("hatalı giriş")
    else:
        print(taban**5)

kullaniciBilgisi=degerAl()
us(kullaniciBilgisi)
"""
