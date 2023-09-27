# def f(x):
#     return x**2
# lambda арг_1б арг_2, ...: выражение
r = lambda x: x**2
print(r(8))

#  применение
def linear(k,b):
    return lambda x: x*k+b
graf1 = linear(2,5)
print(graf1(3))
# дз
list_1 = ['hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
def filter_and_sum(lst):
    new_1 = []
    for x in lst:
        if isinstance(x,int):
            new_1.append(x)
    print(new_1)
    return sum(new_1)

print(filter_and_sum(list_1))
#  то же с лямбдой
print(sum(filter(lambda x: isinstance(x, int), list_1)))
# задача на фильтрацию слов в которых есть а
filtered = list(filter(lambda x: isinstance(x, str), list_1))
print(list(filter(lambda i: 'a' in i, filtered)))
#  # ф-ция FILTER Тут мы должны указать какое-то уловие которому соответствует текущий элемент
#  и если элемент соответствуует этой послндовательности то он добавляется в этот отфильтрованный список
#  предыдущий пример в одну строчку
filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
print(filtered)

from functools import reduce
# ф-ция REDUSE В итоге получаем одно значение в примере элементы списка последовательно складываются
rezult = reduce(lambda x, y: x+y, [2, 3, 4, 5, 6])
print(rezult)
# ф-ция MAP выражение в lambda применяется для каждого элемента в списке
result = list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7]))
print(result)

