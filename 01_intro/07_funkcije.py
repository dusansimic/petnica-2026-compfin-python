def proizvod_u_klasu(proizvod):
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

    return klasifikacija[proizvod]


spisak_pica = ["sok", "kola", "pivo", "vino", "rakija", "voda", "čaj", "kafa"]

for pice in spisak_pica:
    print("Napitak:", pice, "| Vrsta:", proizvod_u_klasu(pice))
