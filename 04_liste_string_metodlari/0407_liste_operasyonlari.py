# region yer_degistirme
"""
listem = [1, 2, 3, 4, 5]
temp = listem[2]
listem[2] = listem[3]
listem[3] = temp
listem[2], listem[3] = listem[3], listem[2]
print(listem)
"""
#endregion

#region slice
#iterable, stringlerinde indexlerine ulaşacağımızı gösterir.
"""
liste =["a1", "a2", "a3"]
ad="ecodation"
print(ad[0])

print("www.trendyol.com"[-3:])
"""
#örnek
"""
url=input("lütfen site adı giriniz:")
if not url[-3:]=="com" or not url[0:3]=="www":
    print("Lütfen url formatına dikkat ediniz.")
else:
    print(f"internet sitesi  {url}")
    """
#endregion
