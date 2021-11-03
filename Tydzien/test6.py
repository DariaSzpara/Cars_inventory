a = float(input("Podaj pierwszy bok prostokąta (w cm)"))
b = float(input("Podaj drugi bok prostokąta (w cm)"))
pole = a*b
print("Pole prostokąta wynosi:", str(pole),"cm^2") 
if(pole < 20000):
    print("Jest mały")
else:
    print("Jest duzy")