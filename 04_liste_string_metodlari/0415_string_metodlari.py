kotuKelimeler=["yuh", "tüh"]
yorum="Bu labtobu gectigimiz aylarda aldım. Aldıgıma pisman oldum satıcıya yuh diyorum."
kelimeler=[i.rstrip(".") for i in yorum.split(" ")]
for item in kotuKelimeler:
    if item in kelimeler:
        yorum= yorum.replace(item, "...")
print(yorum)