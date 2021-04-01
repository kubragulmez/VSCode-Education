# region giris
# loop
# loop ne zaman kullanılır?
# sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlardır
"""
print("24 saatte kargoda")
print("24 saatte kargoda")
print("24 saatte kargoda")
i = 0
while i<5:
    i +=1
    print("24 saatte kargoda")
"""
# endregion

# region ornek
"""
sayac = 5
while sayac:
    sayac -= 1
    print(sayac)
"""

#infinite loop

"""
eb = -99999999999
sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
while sayi != -1:
    if sayi>eb:
        eb = sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
print(f"girdiğiniz sayılardan en büyüğü → {eb}")
"""
"""
tekSayiAdedi, ciftSayiAdedi = 0,0
sayi=int(input("Lütfen bir sayı girin, çıkmak için 0'a basın:"))
while sayi!=0:
    if sayi %2 == 0:
        ciftSayiAdedi += 1
    else:
        tekSayiAdedi +=1

    sayi=int(input("Lütfen bir sayı girin, çıkmak için 0'a basın:"))
print(f"Tek sayıların adedi {tekSayiAdedi}")
print(f"Çift sayıların adedi {ciftSayiAdedi}")
"""
"""
tekSayilarinToplami, ciftSayilarinToplami = 0,0
sayi=int(input("Lütfen bir sayı girin, çıkmak için 0'a basın:"))
while sayi!=0:
    if sayi %2 == 0:
        ciftSayilarinToplami += sayi
    else:
        tekSayilarinToplami += sayi

    sayi=int(input("Lütfen bir sayı girin, çıkmak için 0'a basın:"))
print(f"Tek sayıların toplamı {tekSayilarinToplami}")
print(f"Çift sayıların toplamı {ciftSayilarinToplami}")
"""



