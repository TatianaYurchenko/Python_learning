import time, datetime
''' описание Определение декоратора 
Это ф-ция которая принимает другую ф-цию и возвращает ф-цию. декорараторы нужны чтобы у ф-ции 
добавилось новое поведение# для того чтобы расширить ф-л ф-ции необходимо в качестве переменной присваивания 
выбрать имя ф-ции ф-л которой мы хотим расширить'''
def decator(func):
    def inner():
        print('start')
        func()
        print('finish')
    return inner
def say():
    print('hello')
decator(say)
# выбрать имя ф-ции ф-л которой мы хотим расширить
say = decator(say)
say()
#  следующий шаг добавить к ф-ции say аргументы. Для этого надо добавить аргумент в
#  ф-цию say и в ф-цию inner внутри декоратора

# создадим два декоратора и применим их к ф-ции say
def heder(func):
    #  при описании декоратора все аргументы которые принимаются на вход лучше передавать в виде *args и **kwargs
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('/<h1>')
    return inner

def table(func):
    #  при описании декоратора все аргументы которые принимаются на вход лучше передавать в виде *args и **kwargs
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('/<table>')
    return inner
# результат
# декораторы навешиваются на ф-цию путем указания дероратора перед ф-цией
@table
@heder
def say(name, age):
    print('hello', name, age)


say('vasia', 30)




# def decorator_function(func):
#     def wrapper():
#         print('Wrapper function')
#         print(f'Wrapper function: {func.__name__}')
#         print('Wrapper function in process')
#         print(func())
#         print('exiting wrapper')
#     return wrapper
# @decorator_function
# def hello():
#     return f'  is wrapper'
#
# hello()
#
# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Wrapper function: {func.__name__}')
#         # посмотрим параметры ф-ии wrapper
#         print(f' with arguments: {args}')
#         print('Wrapper function in process')
#         print(func(*args))
#         print('exiting wrapper')
#     return wrapper
# @decorator_function
# def hello(item):
#     return f' {item} is wrapper'
# hello('candy')

# прикладное применение. Сколько времени выполняется ф-я

# def my_decorator(func):
#     def wrapper(arg):
#         start_time = time.perf_counter()
#         print(f'Start function at: {start_time}')
#         st = func(arg)
#         end_time = time.perf_counter()
#         print(f'End function at: {end_time}')
#         print(f'Total time execution of func: {end_time - start_time} seconds')
#         return st + ' I am decorator'
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     time.sleep(2)
#     return f'Hello! {name}'

# print(say_hello('Andrey'))

# # засекаем время начала работы скрипта
# # или куска кода
# t_start = time.perf_counter()
# # здесь код, время/производительность
# # которого необходимо замерить
# time.sleep(1)
# # засекаем время окончания работы скрипта
# # или куска кода
# all_time = time.perf_counter() - t_start
# print(all_time)
# # 1.0023632319971512

# x = datetime.datetime.now()
# time.sleep(1)
# y = datetime.datetime.now()
# b = y-x
print(f'текущее время {time.perf_counter()}')


# встроенные декораторы
# использование перебора по всем параметрам
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     pass