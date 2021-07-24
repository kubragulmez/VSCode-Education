s1=input("Lütfen sayı giriniz: ")
s2=input("Lütfen sayı giriniz: ")
if s1.isdigit() and s2.isdigit:
    s1,s2= int(s1), int(s2)
    if s1%s2==0:
        print("tam bölünür")
    else:
        print("tam bölünmez")
else:
    print("Lütfen sayısal değer giriniz")