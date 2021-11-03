liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = liczby
x = len(liczby)
i =int(0)
while i < x:
    newlist[i] = (liczby[i]*liczby[i])
    i = i+1
print (newlist)