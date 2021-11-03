old_dict = {'Ala': 18, 'Anna': 20, 'Kasia': 15, 'Karolina': 10}
day_dict = {key: value*365 for key, value in old_dict.items()}
print(day_dict)