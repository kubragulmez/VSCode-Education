# region escape
"""
print("Ecodation\teğitim\tkurumları")
print("ecodation\neğitim\nkurumları")
print("merhaba \"ecodation\"")
print("Hayatta","En","Hakiki", end=">")
print("Mürşit", "İlimdir")
print("\"Ege\'nin\"", "\"İncisi\"", "\"İzmir!\"", sep="&")
print("Dünya\'nın", "En", "Güzel", "Şehri", "İstanbul\'dur", sep="*", end=".")
"""
# endregion
# region veri tipleri
"""
print(87)  #integer
print("elma") #string
print(65.98) #float
print(True) #boolean
print(type("ecodation")) 
"""
# endregion

# region aritmetik_operatorler
"""
print(12+3)
print(17-9)
print(15*7)
print(56/9)
print(45//2) #tam bölme
print(98%7) #mod alma
print(4**.5) #üs alma
print(10*(4*5)/(3**4))
print(3-5+7*9-(8%3))
print((1-5)**(9%4)+(96//7)*(48/5))
"""
# endregion

# region degiskenler
"""
Değişken İsimlendirme Kuralları
1- harf veya alt çizgi ile başlamalıdır
2- rakam ile başlayamaz
3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
5- case sensitive
6- anahtar kelimeler if, pass, while, def bunlar kullanılamaz
7- türkçe karakter kullanmamaya özen gösterelim
okulNumarasi= 234
ad= "Kübra"
soyad="Gülmez"
sinav_notu=89
print(okulNumarasi,ad,soyad, sinav_notu)
"""
# concat
"""
program_dili = "Python"
os = "7"
ver = "3.9.2"
print("Windows versiyonu " + os + " " + program_dili,  "versiyonu"  + " "+  ver)
"""
# swap
"""
a, b = 15, 25
temp = a
a=b
b=temp
a,b=b,a
print("a değeri", a, "b değeri", b)
"""
# steak_heap
"""
a, b = 1, 2
a=b
b=1
print(a)
"""
# atama_operatoru
"""
kg = 67
boy = 1.65
vki = kg / boy**2
print(round(vki,2))
"""
"""
sayi=5
toplam = 0
toplam = toplam + sayi
sayi = 10
sayi = sayi +1
toplam = toplam + sayi 
print(toplam, sayi)
"""
"""
skor =0
can=3
skor += 1
can -=1
print("anlık skorunuz", skor)
print("kalan canınız", can)
"""
# endregion

# region input
"""
ad = input("Lütfen adınızı giriniz\t :")
soyad = input("Lütfen soyadınızı giriniz\t:")
ders= input("En sevdiğiniz ders? \t:")
print("Adınız", ad, "Soyadınız", soyad, "En sevdiğiniz ders",ders)
"""
"""
dogum_tarihi=int(input("Lütfen doğum tarihinizi giriniz:"))
yas=2021 - dogum_tarihi
print(dogum_tarihi, "doğum tarihli öğrencimizin yaşı", yas)
"""
"""
print("+"*50)
okulTuru = "Anadolu"
seviye = 12
print(okulTuru + " " + str(seviye))
"""
"""
s1 = int(input("Lütfen ilk sayıyı giriniz:"))
s2 = int(input("Lütfen 2. sayıyı giriniz:"))
print(f"Girdiğiniz sayıların toplamı {s1+s2}")
print(f"{s1} + {s2} = {s1+s2} ")
"""
"""
print("Leylek Uygulamasına Hoş Geldiniz \n Sürüş Ücreti -- 0.59/dk")
s= int(input("Sürüş için geçen süre (saat)\t :"))
d= int(input("Sürüş için geçen süre (dakika)\t :"))
toplamDakika=s*60
toplamDakika += d
toplamTutar= 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"Sürüşün toplam süresi {s}: {d} - {toplamDakika} dakikada bitmiştir. ")
print(f"Kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")
"""
#endregion