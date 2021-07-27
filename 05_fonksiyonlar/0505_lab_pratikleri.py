# region ornek_1
"""
def hataKodu100():
    print("Sadece sayısal değer giriniz")

def hataKodu200():
    print("Sadece pozitif değer giriniz")

yas=input("lütfen yaşanızı giriniz:")
if yas.lstrip("-").isdigit():
    yas=int(yas)
    if yas<0:
        hataKodu200()
    else:
        print(f"yaşınız {yas}")
else:
    hataKodu100()
"""
# endregion

# region ornek_2
"""
def hataKodu100():
    print("Sadece sayısal değer giriniz")

def hataKodu200():
    print("Sadece pozitif değer giriniz")

def alan(yaricap):
    alan=(3.14)*yaricap**2
    print(f"yarıçapı {yaricap} olan dairenin alanı {alan}")

yaricap=input("lütfen yarıçap giriniz:")
if yaricap.lstrip("-").isdigit():
    yaricap=float(yaricap)
    if yaricap<0:
        hataKodu200()
    else:
        alan(yaricap)
else:
    hataKodu100()
"""
# endregion

# region ornek_3

def selamlasma(ad):
    import datetime
    saat=datetime.datetime.now().hour
    if saat<12:
        print(f"günaydın {ad}")
    else:
        print(f"merhaba {ad}")

selamlasma(input("Lütfen adınızı giriniz:"))
# endregion     