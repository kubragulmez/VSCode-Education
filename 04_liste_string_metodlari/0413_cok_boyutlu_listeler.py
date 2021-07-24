#tanımlama

#1 2 3 4
#5 6 7 8
#2x4 matris
"""
a=[[1,2,3,4],[5,6,7,8]]
print(a)
"""
#erisim
"""
a=[[1,2,3,4],[5,6,7,8]]
print(a)
print(a[1]) #satıra erişmek için
print(a[0][2]) #hücreye erişmek için
"""
"""
#for ile erisim
a=[[1,2,3,4],[5,6,7,8]]
for i in range(len(a)):
    for j in range(len(a[i])): #listeye yeni bir liste eklendiğine dinamik olması için len kullandık
        print(f"{a[i][j]}", end=" ")
    print()
    """
