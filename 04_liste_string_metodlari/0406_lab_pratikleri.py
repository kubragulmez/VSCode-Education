"""
ogrenciListesi=[]
while True:
    ogrenci=input("Listeye eklenecek öğrenci, çıkmak için -1:")
    if ogrenci=="-1":
        break
    ogrenciListesi.append(ogrenci)
for i in ogrenciListesi:
    print(i)
"""
"""

ogrenciListesi=[]
print("""
        #[1]  EKLE
        #[2]  SİL
        #[3]  LİSTELE
        #[4]  ÇIK

""")
while True:
    secim=int(input("Lütfen seçiminizi yapınız:"))
    if secim==1:
        ogrenci=input("Listeye eklenecek öğrenci:")
        ogrenciListesi.append(ogrenci)
    elif secim==2:
        ogrenci=input("Listeden silinecek öğrenci:")
        ogrenciListesi.remove(ogrenci)
    elif secim==3:
        for i in ogrenciListesi:
            print(i)
    elif secim==4:
        break
    else:
        print("Hatalı seçim")
"""        
"""
notOrtalamalari=[]
while True:
    ogrenciAdSoyad=input("Lütfen ad, soyad giriniz, çıkmak için -1:")
    if ogrenciAdSoyad== "-1":
        break
    n1=int(input("Lütfen 1. notu giriniz:"))
    n2=int(input("Lütfen 2. notu giriniz:"))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("Lütfen [0-100] arası değer giriniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
for i in notOrtalamalari:
    print(i)
minimum, maksimum= 99999999,0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not {minimum}   en yüksek not{maksimum}")
"""
"""
notOrtalamalari=[]
while True:
    ogrenciAdSoyad=input("Lütfen ad, soyad giriniz, çıkmak için -1:")
    if ogrenciAdSoyad== "-1":
        break
    n1=int(input("Lütfen 1. notu giriniz:"))
    n2=int(input("Lütfen 2. notu giriniz:"))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("Lütfen [0-100] arası değer giriniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
genelOrtalama= sum(notOrtalamalari)/len(notOrtalamalari)
for i in notOrtalamalari:
    print(i)
minimum, maksimum= 99999999,0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not {minimum}   en yüksek not{maksimum}")

for i in notOrtalamalari:
    if i<genelOrtalama:
        print(f"dönem tekrar yapacak öğrencinin notu {i}")
"""
"""
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
sayi=int(input("Lütfen sayıyı giriniz:"))
print(f"{onlar[sayi//10]} {birler[sayi%10]}")
"""