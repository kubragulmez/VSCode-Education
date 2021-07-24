"""
toplam =0
while True:
    a=int(input("Lütfen sayı giriniz, çıkmak için -1 /t:"))
    if a==-1:
        break
    if a%2 ==0:
        print("Lütfen tek sayı giriniz.")
        continue
    toplam +=a
print(f"Girdiğiniz sayıların toplamı {toplam}")
"""
while True:
    secim = int(input("""
        [1] km mil
        [2] mil km
        [3] çık
        """))
    if secim == 1:
        km = float(input("Lütfen km bilgisi giriniz\t:"))
        mil = km*0.62137
        print(f"Girilen {km} değerinin mil hesabı {round(mil,2)}")
    elif secim == 2:
        mil = float(input("Lütfen mil bilgisi giriniz\t:"))
        km = mil/0.62137
        print(f"Girilen {mil} değerinin km hesabı {round(km,2)}")
    elif secim == 3:
        break
    else:
        print("Hatalı seçim yaptınız")
