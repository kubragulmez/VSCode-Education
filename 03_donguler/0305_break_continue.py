# region break_continue_neden_kullanilir
"""
break  döngüyü sonlandırır
continue tepeye geri döner
"""
# endregion

# region break
"""
i=1
print("a")
while i<11:
    if i==5:
        print("b")
        break
    print(f"{i}. döngü")
    i+=1
print("c")

"""
"""
eb, say = 0, 0
while True:
    sayi = int(input("Lütfen sayi giriniz, çıkmak için -1 \t:"))
    if sayi == -1:
        break
    say += 1
    if sayi > eb:
        eb = sayi
if say:
    print(f"Girdiğiniz listedeki en büyük sayı {eb} ")
else:
    print("Sayı girmediniz")

"""
# endregion

# region continue
"""
i = 1
while i < 11:
    if i == 5:
        i += 1
        continue
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
# endregion
# region break_continue_mix
"""
i=1
print("a")
while i<100:
    if i%7==0:
        i+=1
        continue
    elif i%15==0:
        break
    print(f"{i}. döngüdeyim")
    i+=1
print("b")
"""
# endregion
