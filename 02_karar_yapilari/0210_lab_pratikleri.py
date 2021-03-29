"""
a = int(input("Lütfen kenar bilgisi giriniz:"))
b = int(input("Lütfen kenar bilgisi giriniz:"))

if a==b:
    print(f"Karenin alanı {a*b} ")
else:
    print(f"Dikdörtgenin alanı {a*b}")
"""
"""
kısa_kenar = int(input("Lütfen kısa kenarı giriniz:"))
uzun_kenar = int(input("Lütfen uzun kenarı giriniz:"))
cevre = (kısa_kenar+uzun_kenar)*2
if kısa_kenar < uzun_kenar:
    print(f"Dikdörtgenin çevresi {cevre}")
else:
    print("Kısa kenar uzun olamaz")
"""
"""
a = int(input("Lütfen 1. sayıyı giriniz:"))
b = int(input("Lütfen 2. sayıyı giriniz:"))

if a % b == 0:
    print(f"{a} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına tam bölünmez")
"""
"""
kullanıcıAdi = input("Lütfen kullanıcı adınızı giriniz:")
parola = int(input("Lütfen parolayı giriniz:"))

if kullanıcıAdi== "admin" and parola == 123:
    print("Giriş başarılı")
else:
    print("Giriş başarısız")

"""
"""

not1, not2=int(input("Lütfen 1. sınav notunu giriniz:")), int(input("Lütfen 2. sınav notunu giriniz:"))
ort = (not1+not2) / 2
if not1 >100:
    print("100'den büyük bir not giremezsiniz.")
elif not2 >100:
    print("100'den büyük bir not giremezsiniz.")

else:

    if ort>=85:
        print(f"Yıl sonu notunuz {ort}, başarı durumu Pekiyi")
    elif ort>=70:
        print(f"Yıl sonu notunuz {ort}, başarı durumu İyi")
    elif ort>=55:
        print(f"Yıl sonu notunuz {ort}, başarı durumu Orta")
    elif ort>=45:
        print(f"Yıl sonu notunuz {ort}, başarı durumu Geçer")
    else:
        print(f"Yıl sonu notunuz {ort}, başarı durumu Kaldı")
    
"""
"""
sayi1=int(input("Lütfen 1. sayıyı giriniz:"))
sayi2=int(input("Lütfen 2. sayıyı giriniz:"))
if sayi1<sayi2:
    print(f"{sayi1} sayısı {sayi2} sayısından küçüktür.")
elif sayi1>sayi2:
    print(f"{sayi1} sayısı {sayi2} sayısından büyüktür.")
else :
    print(f"{sayi1} sayısı {sayi2} sayısından eşittir.")

"""

"""
s1 = int(input("l. s1. giriniz : "))
s2 = int(input("l. s2. giriniz : "))
s3 = int(input("l. s3. giriniz : "))
if s1<s2:
    s1, s2 = s2, s1
if s1<s3:
    s1, s3 = s3, s1
if s2<s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")

"""


