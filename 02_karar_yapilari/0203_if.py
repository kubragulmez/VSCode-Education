"""
havaDurumu ="yağmurlu"
if havaDurumu == "yağmurlu":
    print("Şemsiyeni al lütfen")

"""
"""
sayi = int(input("lütfen bir sayı giriniz:"))
if sayi<0 :
    print(f"{sayi} sayısı negatif")
"""
"""
ad = input("Lütfen kullanıcı adını giriniz:")
if ad =="user":
    print(f"{ad} yetkisiyle admin paneline girilmez")
"""
"""
_1nciSinavNotu = int(input("Lütfen 1. Sınav Notunuzu Giriniz:"))
_2nciSinavNotu = int(input("Lütfen 2. Sınav Notunuzu Giriniz:"))
_3nciSinavNotu = int(input("Lütfen 3. Sınav Notunuzu Giriniz:"))
ortalama = (_1nciSinavNotu+_2nciSinavNotu+_3nciSinavNotu)/3
if ortalama>=50:
    print(f"GEÇTİNİZ ortalama notunuz {ortalama}")
"""
"""
sayi1=int(input("Lütfen 1. Sayıyı Giriniz:"))
sayi2=int(input("Lütfen 2. sayıyı giriniz:"))
if sayi1>sayi2:
    print(f"{sayi1} büyüktür {sayi2}")
if sayi2>sayi1:
    print(f"{sayi2} büyüktür {sayi1}")
"""
"""
bakiye=5000
bankaKodu1=101
bankaKodu2=102
transfer=float(input("ne kadar transfer edilecek:"))
kesinti = 0
if bankaKodu1 != bankaKodu2:
    kesinti=transfer*0.05
print(f"Güncel bakiyeniz {bakiye-transfer-kesinti}dir")
"""
"""
biletFiyati=float(input("Lütfen bilet fiyatını giriniz:"))
bavulAgirligi=20
if bavulAgirligi>15:
    fark = bavulAgirligi-15
    biletFiyati += fark*5
print(f"Güncel bilet fiyatı {biletFiyati*1.18}")
"""

"""
kargo_bedeli = 7.5
fiyat = float(input("Lütfen fiyat bilgisi giriniz: ")) 
toplam_fiyat = fiyat + kargo_bedeli
if fiyat >= 250:
    toplam_fiyat = fiyat
print(f"Ödenecek tutar {toplam_fiyat} ")


"""





