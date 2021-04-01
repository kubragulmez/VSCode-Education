"""
toplam=0
sayi=1
while sayi<=10:
    toplam = toplam + sayi
    sayi=sayi+1
print(toplam)
"""
"""
x=1
while x<=100:
    if x%2==0:
        print(f"sayı çift: {x}")
    else:
        print(f"sayı tek:{x}")
    x+=1
print()
"""
"""
x=0
while x<5:
    x+=1
    if x==2:
        break
    print(x)
"""
"""
x=0
toplam=0
while x<=100:
    x+=1
    if x%2 != 0:
        toplam += x
print(f"Tek sayıların toplamı: {toplam}")
"""
"""
baslangic=int(input("Lütfen başlangıç değeri girinz:"))
bitis =int(input("Lütfen bitiş değeri girinz:"))
i = baslangic
while i<bitis:
    i+=1
    if i%2 ==1:
    print(i)
"""
"""
anahtar=1
while anahtar ==1:
    soru= input("Yapmak istediğimiz işlemin numarasını giriniz, çıkmak için q:")
    
    if soru == "q":
        print("çıkılıyor")
        anahtar= 0
    elif soru == "1":
        sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print(f" {sayi1} + {sayi2} = {sayi1+sayi2} ")
    elif soru == "2":
        sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print(f" {sayi1} - {sayi2} = {sayi1-sayi2} ")
    elif soru == "3":
        sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print(f" {sayi1} * {sayi2} = {sayi1*sayi2} ")
    elif soru == "4":
        sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print(f" {sayi1} / {sayi2} = {sayi1/sayi2} ")
    elif soru == "5":
        sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print(f" {sayi1} ** {sayi2} = {sayi1**sayi2} ")
    else:
        print("Yanlış giriş!")

"""
"""
count=0
while count<5:
    print(count, "5'ten küçüktür")
    count+=1
else:
    print(count, "5'ten büyüktür.")
"""
"""
p=1
a=1
b=10
toplam=0
while a<=b:
    toplam += a**p
    a+=1
print("p=",p,", 1^p + ... + 10^p = ", toplam)
"""
"""
p=1
while p<=6:
    a=1
    b=10
    toplam=0
    while a<=b:
        toplam += a**p
        a+=1
    print("p=",p,", 1^p + ... + 10^p = ", toplam)
    p+=1
"""
"""
i, j =0, 0

while i<=5:
    while j<i:
        j+=1
        print(" * ", end=" ")
    j=0
    i += 1
    print( )

"""   
"""
i, j =0, 0

while i<=5:
    while j<5:
        if (j<=i):
            print(" ", end=" ")
        else:
            print(" * ", end=" ")
        j+=1
    j=0
    i+=1
    print()
"""
"""
i, j =0, 0

while i<=5:
    while j<=5:
        if (j<=5-i):
            print(" ", end=" ")
        else:
            print(" * ", end=" ")
        j+=1
    j=0
    i+=1
    print()
"""
"""
i, j =0, 0
while i<=5:
    while j<=5:
        if i==0:
            print(" * ", end=" ")
        elif i==5:
            print(" * ", end=" ")
        elif j==0:
            print(" * ", end=" ")
        elif j==5:
            print(" * ", end=" ")
        else:
            print("  ", end=" ")
        j+=1
    j=0
    i+=1
    print()
"""
"""
i, j = 0, 5
while i<5:
    while j>0:
        print(" * ", end="")
        j-=1
    i+=1
    j=5-i
    print()
i, j= 0, 0
while i<5:
    while j<i :
        print(" * ", end="")
        j+=1
    i+=1
    j=0
    print()
"""
