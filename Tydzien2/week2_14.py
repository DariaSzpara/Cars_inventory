old_dict = {'Ala': 18, 'Anna': 20, 'Kasia': 15, 'Karolina': 10}
b=[old_dict.values]
c={}
a = [old_dict.values]
x = len(old_dict)
i =int(0)
while i < x:
    d = a[i]
    b[i]=d*d
    c [i]={a[i], b[i]}
    i = i+1
day_dict = {key: value for key, value in c}
print(day_dict)