"""
s = int(input("Bir sayı giriniz \t:"))
for i in range(1, s+1):
    if s % i == 0:
        print(i, end=" ")
"""
"""
say = 0
son = int(input("son değeri giriniz\t:"))
for i in range(2, son+1):
    for j in range(1, i):
        if i % j == 0:
            say += 1
    if say < 1:
        print(i, end=" ")
    say = 0
"""
"""
obeb =0
s1=int(input("lütfen 1. sayıyı gırınız:"))
s2=int(input("lütfen 2. sayıyı gırınız:"))
for i in range(1, min(s1,s2)+1):
    if s1%i==0:
        if s2%i==0:
            obeb=i
print(obeb)
"""
"""
sayac=0
sayi=int(input("Lütfen sayı giriniz:"))
for i in range(1,sayi+1):
    if sayi%i==0:
        sayac+=1
if sayi%sayac==0:
    print("TAU'DUR")
else:
    print("TAU DEĞİLDİR")
"""
"""
toplam=0
sayi=int(input("lütfen sayı girniz:"))
for i in range(1, int(sayi/2)+1):
    if sayi%i==0:
        toplam+=i
if toplam==sayi:
    print("Mükemmel sayıdır")
else:
    print("mükemmel sayı değildir")
"""