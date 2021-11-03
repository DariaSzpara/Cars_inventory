znak = input("Podaj znak z puli(+,-,*,/)")
liczba1 = input("Podaj pierwszą liczbę ")
liczba2 = input("Podaj drugą liczbę ")
if (znak == "+"):
    wynik = int(liczba1) + int(liczba2)
    print("Wynik to:", str(wynik))
elif (znak == "-"):
    wynik = int(liczba1) - int(liczba2)
    print("Wynik to:", str(wynik))
elif (znak == "*"):
    wynik = int(liczba1) * int(liczba2)
    print("Wynik to:", str(wynik))
elif (znak == "/"):
    wynik = int(liczba1) / int(liczba2)
    print("Wynik to:", str(wynik))
