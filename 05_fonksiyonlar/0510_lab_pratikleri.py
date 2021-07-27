"""
def carp(a,b, c=1, d=1):
    print(a*b*c*d)

carp(4,2)
carp(4,2)
carp(4,2,3)
carp(4,2,6,3)
"""
"""
def carp(a,b,c, ayrac="x"):
    print(f"{a} {ayrac} {b} {ayrac} {c} ={a*b*c}")

carp(4,7,3, ayrac="*")
"""
"""
def mutlakDeger(a=-1):
    if str(a).lstrip("-").isdigit():
        a=int(a)
        if a<0:
            a *= -1
        print(f"mutlak değer  {a}") 
    else:
        print("Lütfen sayısal değer giriniz")

mutlakDeger("dghgh")
"""
def kayıtOl(tc,ad="isimsiz",email="@"):
    print("Kayıt başarılı")
    print(f"{tc} {ad} {email}")

kayıtOl(24345545,"ahmet","asdfg@gmail.com")

