#tek satırda for yazmak
"""
liste=[]
for i in range(1,9):
    liste.append(i)
print(liste)

liste= [i for i in range(1,9)]
print(liste)
"""
"""
row = [ "piyon" for i in range(1,8)]
print(row)
"""
""""""
haftaninGunleri=["","Pzartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
liste=[f"Haftanın {i}. Günü {haftaninGunleri[i]}" for i in range(1,8)]
print(liste)