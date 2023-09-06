# list1 = [1,2,3,4,5,6]
# list3 = [n*n for n in list1 if n % 2]
# print(list3)

# задача 3
a = input('введите два числа через пробел ')
b = list(map(int, a.split()))
c = round(sqrt(sum([x*x for x in b])))
print(f'гипотенуза треугольника с катетами {a} = {c}')