klasifikacija = {
    "sok": "bezalkoholno piće",
    "kola": "bezalkoholno piće",
    "pivo": "alkoholno piće",
    "vino": "alkoholno piće",
    "rakija": "alkoholno piće",
    "voda": "bezalkoholno piće",
    "čaj": "topli napitak",
    "kafa": "topli napitak",
}

print(klasifikacija)

klasifikacija["topla čokolada"] = "topli napitak"

for napitak, vrsta in klasifikacija.items():
    print("Napitak:", napitak, "| Vrsta:", vrsta)

for napitak in klasifikacija.keys():
    print("Napitak:", napitak, "| Vrsta:", klasifikacija[napitak])
