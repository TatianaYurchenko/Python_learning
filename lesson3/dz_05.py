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
def type_of_input(a):
    print(a.__class__)
    return a
type_of_input(1.5)