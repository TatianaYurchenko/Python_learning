# def compare_two_numbers(a, b):
#     if a > b:
#         return True
#     else:
#         return False
# print(compare_two_numbers(6, 9))
#___________________

# def compare_two_numbers(a, b):
#     if a >= 0 and b >= 0:
#         if a >= b:
#             return True
#         else:
#             return False
#     else:
#         return("can conpare only positive numbers!")
# print(compare_two_numbers(0, 0))

# def compare_positive(x, y):
#     if x < 0 or y < 0:
#         return "Can compare only positive numbers!"
#     else:
#         return x > y
# print(compare_positive(8, 9))

# ____________
#
# def sum_two_numbers(a , b):
#     d = a + b
#     return d
# print(f'Сумма двух чисел = {sum_two_numbers(4 , 5)}')
# _____________

# def sum_two_numbers(a , b):
#     d = a - b
#     return d
# print(f'result:{sum_two_numbers(4 , 5)}')


# def subtract_two_numbers(a, b):
#     return a - b
# print(subtract_two_numbers(8, 9))
# __________

# def print_vertical(a):
#     for i in a:
#         print(i)
#     return a
# print_vertical("test me please")
# __________________

# def sum_two_numbers(a , b):
#     d = a + b
#     return d
# print(f'Результат сложения двух строк = "{sum_two_numbers("add" , "apples")}"')
#
# ____________________

# Написать функцию которая распечатывает тип введенных данных
# def type_of_input(a):
#     print(a.__class__)
#     return a
# type_of_input(1.5)
s = 0
lst = ['ha', 'ananas', 2, None, 78, True, 36]
for i in lst:
    if isinstance(i, int):
        s += i
print(s)
# с i никаких манипуляций не делаем, если оно соответствует нашим условиям, то мы его оставляем
list3 = sum([i for i in lst if isinstance(i, int)])
print(list3)

list_1 = [i for i in lst if isinstance(i, str) and 'a' in i]
print(*list_1, sep=',')

# list6 = [n*n for n in list1 if n % 2]