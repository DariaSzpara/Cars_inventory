import functools
numery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
sum = functools.reduce((lambda x, y: x + y), numery)
print(sum)
