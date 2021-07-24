"""
sayilar=[11,3,5,6,7,4,23]
n=0
for i in sayilar:
    if i==3:
        break
    n+=1
print(f"Aradığınız {n} indisli eleman bulundu")
"""
"""
ogrenciListesi=["ali","ayşe","özge","ahmet","sibel"]
while True:
    ogrenciAdi=input("Aradığınız öğrenci giriniz, çıkmak için ç :")
    if ogrenciAdi=="ç":
        break
    for i in ogrenciListesi:
        if i==ogrenciAdi:
            print(f"Aradığınız {ogrenciAdi} isimli öğrenci bulundu.")
            break
    else:
        print("Aradığınız öğrenci bulunamadı.")
"""
"""
ogrenciListesi=["ali","ayşe","özge","ahmet","sibel"]
while True:
    ogrenciAdi=input("Aradığınız öğrenci giriniz, çıkmak için ç :")
    if ogrenciAdi=="ç":
        break
    for i in range(len(ogrenciListesi)):
        if ogrenciListesi[i]==ogrenciAdi:
            print(f"Aradığınız {ogrenciAdi} isimli öğrenci listenin {i+1}. sırasındadır.")
            break
    else:
        print(f"Aradığınız {ogrenciAdi} isimli öğrenci yoktur.")
"""