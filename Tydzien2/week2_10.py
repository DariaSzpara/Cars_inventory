old_dict = {'Ala': 18, 'Anna': 20, 'Kasia': 15, 'Karolina': 10}
day_dict = {key: value*365 for key, value in old_dict.items()}
a =list(old_dict)
b =list(day_dict)
c =list(old_dict.values())
d =list(day_dict.values())
x = len(old_dict)
i =int(0)
while i < x:
    if list(day_dict.values())[i] <= 6570:
        print(a[i], c[i])
    else:
        print(b[i], d[i])
    i = i+1