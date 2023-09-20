# def main_func(name):
#     def inner_func():
#         print('hello', name)
#     return inner_func
# присваивание r = main_func('misha')
# в переменную с так же можно сохранить результат вызова этой ф-ции
# вызов r()
# ''' идея замыкания в том, что каждый раз когда мы вызываем main_func мы создаем свою область видимости
# и в ней будут хранится свои значения'''

# def adder(value):
#     def inner(a):
#         return value+a
#     return inner
#
# присваивание задается переменная value a2 = adder(2)
# вызов ф-ии задается переменная а a2(5)
# print(a2(5))

#  Ф-ция будет считать сколько раз мы вызываем нашу ф-ю
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# q = counter()
# print(q())
# q()
# print(q())

def counter():
    count = 0
    def inner():
        # nonlocal необходимо для того чтобы эту переменную изменять в другой области видимости
        nonlocal count
        count += 1
        return count
    return inner
q = counter()
print(q())
#  каждый экземпляр вызова ф-ции (например q = counter()) будет хранить свою область видимости и значение переменной count

