name = input("write your name:")
print ("Hello,", name )

x = input("numer:")
if(int(x) > 100):
    print("Twój numer naley do grupy BIG")
elif(50 < int(x)):
    print("Twój numer naley do grupy MEDIUM")
else:
    print("Twój numer naley do grupy SMALL")

fruits = ["apple","orange","strawberry"]
fruit=input("Jaki jest Twój ulubiony owoc?")
if(fruit == fruits[0] or fruit == fruits[1] or fruit == fruits[2]):
    print("Mamy ten sam ulubiony owoc")
else:
    print("To nie jest mój ulubiony owoc")

age = input("Ile masz lat?")
y = int(age) *365 
print("Masz "+ str(y),"dni")

number1 = input("Podaj pierwsza wartość")
number2 = input("Podaj drugą wartość")
if(number1 == number2 ):
    print("Są równe")
else:
    print("Nie są równe")

liczba = input("Podaj wartość")
if(int(liczba) % 2 ==0 ):
    print("Liczba jest parzysta")
else:
    print("Liczba nie jest parzysta")


