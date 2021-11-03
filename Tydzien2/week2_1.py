liczby = []
i = 1
while i < 11:
    f = input("Wprowadz zmienna")
    liczby.append(f)
    i = i + 1
liczby = list(dict.fromkeys(liczby))
print(liczby)