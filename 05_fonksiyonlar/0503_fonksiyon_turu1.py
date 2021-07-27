# region fonksiyon_turu_1_parametre_almayan_deger_dondurmeyen
"""
Fonksiyon tanımlama anında argüman almaz, değer döndürmez
def kullaniciGiris():
    kAd = input("Kullanıcı Adınız : ")
    print(f"hoşgeldiniz {kAd}")
kullaniciGiris()
"""
# endregion

# region ornek
def topla():
    s1=input("lütfen ilk sayıyı giriniz:")
    s2=input("lütfen ikinci sayıyı giriniz:")
    if s1.isdigit and s2.isdigit:
        s1, s2=int(s1), int(s2)
        print(f"{s1}+{s2}={s1+s2}") 
    else:
        print("Lütfen sayı giriniz")

topla()
# endregion