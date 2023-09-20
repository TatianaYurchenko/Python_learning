#  map то же что цикл. эта ф-ция делает что либо с каждым элементом списка
a = input('введите два числа через пробел ')
b = list(map(str, a.split()))
print(b)
# map  lambda
result = list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7]))
print(result)