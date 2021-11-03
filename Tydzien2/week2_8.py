numbers = [x for x in range(101)]
new_numbers = [number for number in numbers if number % 3 ==0 or number for number in numbers if number % 5 ==0]
print(new_numbers)