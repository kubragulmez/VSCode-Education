"""
favoriAylar= []
while True:
    fav=input("Favori ayınızı giriniz, çıkamk için -1:")
    if fav=="-1":
        break
    if fav in favoriAylar:
        print("Daha önce eklendi.")
        continue
    favoriAylar.append(fav)
print(favoriAylar)
"""
"""
ortakElemanlar=[]
liste1=[1,2,6,7,8,5]
liste2=[4,3,7,6,9]
for i in liste1:
    if i in liste2:
        ortakElemanlar.append(i)
print(ortakElemanlar)
"""
"""
stok1=[1,2,3,4,5]
stok2=[4,5,7,8,9]
tekilListe=stok1.copy()
for item in stok2:
    if item not in tekilListe:
        tekilListe.append(item)
print(tekilListe)
"""