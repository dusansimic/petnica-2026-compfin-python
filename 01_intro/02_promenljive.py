broj1 = 5
broj2 = 3.14

print(broj1, broj2)

logicka_vrednost = True
print(logicka_vrednost)

string = "Neki tekst"
print(string)

print("broj1:", broj1, "| tip:", type(broj1))
print("broj2:", broj2, "| tip:", type(broj2))
print("logicka_vrednost:", logicka_vrednost, "| tip:", type(logicka_vrednost))
print("string:", string, "| tip:", type(string))

print("Ime tipa:", type(broj1).__name__)

print("Da li je broj1 ceo broj?", isinstance(broj1, int))
print("Da li je broj2 ceo broj?", isinstance(broj2, int))
