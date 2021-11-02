liczba1 = input("Podaj pierwszą liczbę")
liczba2 = input("Podaj drugą liczbę")
suma = int(liczba1) + int(liczba2)
print("Suma Twoich liczb to:", str(suma))

liczba3 = input("Podaj pierwszą liczbę")
liczba4 = input("Podaj drugą liczbę")
if(int(liczba3) < int(liczba4)):
    suma2 = int(liczba3) + int(liczba4)
    print("Działanie to sumowanie,wynik to:", str(suma2))
elif(int(liczba3) == int(liczba4)):
    suma2 = int(liczba3) * int(liczba3)
    print("Działanie to mnozenie,wynik to:", str(suma2))
elif(int(liczba3) > int(liczba4)):
    suma2 = int(liczba3) - int(liczba4)
    print("Działanie to odejmowanie,wynik to:", str(suma2))