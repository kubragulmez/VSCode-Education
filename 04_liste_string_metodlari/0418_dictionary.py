"""
programlamaDilleri={
    "programDili":"python",
    "versiyon" : 3.92,
    "interpreter" : True,
    "seviye" : "yüksek"

    }
for key, value in programlamaDilleri.items():
    print(key, value)
"""

"""
ipDetay={
    "ip":{
       "query":"92.44.82.0",
       "status":"success",
       "continent":"Asia",
       "continentCode":"AS",
       "country":"Turkey",
       "countryCode":"TR",
       "region":34,
       "regionName":"İstanbul",
       "district":"",
       "zip":"34110",
       "lat":41.0205,
       "lon":28.9753,
       "timezone":"EUROPE/ISTANBUL"
    },
    "dns":{
        "geo":"TURKEY -- Turkcell Internet"
        }
}
print(ipDetay["ip"]["zip"])
print(ipDetay["dns"])
"""
"""
sirket = {
    "departman":{
        "yazılım":["ali","mehmet"],
        "muhasebe":["pınar","neşe"]
    },
    "calisanSayisi":100,
    "ceo":"Ali Kemal",
    "telefonlar":{
        "istanbul":"021234235",
        "ankara":"031294312"
    },
    "sirketArabalari":["i20", "megan", "focus"],
    "sirketArabalari2":{
        "i20":True,
        "megan":False,
        "focus":True
    }

}
print(sirket["calisanSayisi"])
print(sirket["sirketArabalari"])
print(sirket["sirketArabalari2"]["megan"])
print(sirket["departman"]["yazılım"][1])
print(sirket["telefonlar"]["ankara"])
"""