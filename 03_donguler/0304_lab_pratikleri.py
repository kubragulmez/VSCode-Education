"""
i = 1
s = 0
while i < 100:
    if s % 10 == 0:
        print()
    print(i, end=" ")
    s += 1
    i += 2
"""
"""
i = 1
toplam =0
while i < 100:
    toplam +=i
    i += 2
print(toplam)
"""
"""
i=1
sayi = int(input("Lütfen sayi giriniz"))
while i<=10:
    print(f"{sayi} x {i} = {sayi*i}")
    i+=1
"""
"""
kelime = input("açıl .... açıl !! Lütfen boşluğu doldurun:")
while kelime != "susam":
    print("hahhaah ne oldu bilemedin ama :-D")
    kelime = input("açıl .... açıl !! Lütfen boşluğu doldurun:")

print("Başardın!")
"""
"""
adet, toplam = 0, 0
sayi = int(input("Lütfen sayı giriniz, çıkmak için 0:"))
while sayi:
    toplam += sayi
    adet += 1
    sayi = int(input("Lütfen sayı giriniz, çıkmak için 0 :"))

print(f"Girdiğiniz sayıların ortalaması {toplam/adet} ")
"""
"""
i=1
rakam = int(input("Lütfen [1-9] arası rakam giriniz: "))
while i<6:
    print(f"{rakam*i}", end=" ")
    i+=1
"""
"""
i=1
sonuc=1
while i<6:
    sonuc *=i
    print(f"{i} \t {sonuc}")
    i+=1
"""
"""
i = 100
while i < 1000:
    kalan = i % 10
    birler = kalan//1
    kalan = i % 100
    onlar = kalan//10
    kalan = i % 1000
    yuzler = kalan//100
    haneleriToplami = birler+onlar+yuzler
    if haneleriToplami == 3:
        print(f"{i} (3 haneli, haneleri toplamı 3)")
    i += 1
"""
"""
import random
uretilenSayi = random.randint(1,99)
print(uretilenSayi)
i=0
enKucukFark=999999999999
while i<3:
    tahmin=int(input("Lütfen [1-99] arası tahmininizi giriniz:"))
    fark= uretilenSayi - tahmin
    if fark<0:
        fark*=-1
    if fark<enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i+=1
print(enYakinTahmin)
"""