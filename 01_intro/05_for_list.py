lista = ["Prvi", "Drugi", "Treći"]

# Iteriranje po indeksima
for i in range(len(lista)):
    print("Element na indeksu", i, "je", lista[i])

# Iteriranje po elementima
for element in lista:
    print("Element:", element)

# Iteriranje po elementima sa indeksom
for i, element in enumerate(lista):
    print("Element na indeksu", i, "je", element)

# Numeracija koja počinje od 1
for redni_broj, element in enumerate(lista, start=1):
    print("Element broj", redni_broj, "je", element)
