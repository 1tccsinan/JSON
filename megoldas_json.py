import json
with open("./adatok/diakok_adatai.json","r",encoding="utf-8") as fm1:
    adatok=json.load(fm1)

print(type(adatok))

for i,diak in enumerate(adatok['diakok']):
    print(diak['név'])

with open("./adatok/diakok_adatai.json","w",encoding="utf-8") as fm2:
    json.dump(adatok, fm2, indent=2)