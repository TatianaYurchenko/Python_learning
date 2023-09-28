a, *b , c = [True, 7, 'hello', 9, '54', 67,4,3]
print(a,b,c)

# s=[4,10]
# print(list(range(*s)))

# # распавковка в аргументавх ф-ции
# def eva(a,b,c,d):
#     print(a,b,c,d)
# a =('hello', 9, '54',[1,2,4])
# eva(*a)
#
# # передача произвольного количества объектов
# def f(*args):
#     print(args, type(args))
# f(1,2,3,4,5,6,7,7,8,8,9)
# # словари
# def fun(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# fun(a=1,b=2,c=3, name=89)
# # комбинирование
# def fun_1(*args, **kwargs):
#     print(args,kwargs)
# fun_1(5,4,3,2,a=1,b=2,c=3, name=89)

# x = [(1,2,3), (3,4,5), (3,5,6)]
# for i, *j in x:
#     print(f'{i}{j}')

# def concat(*args, sep=' '):
#     # sep = (f' {sep} ')
#     # b = (args)
#     b = sep.join(args)
#     return b
# print(concat('hello', 'python', 'and', 'stepik'))

#  **kwargs работает только со словарями
# def keywords(**kwargs):
#     return kwargs
# print(keywords(name = 'Alice', last_name = 'Petrova'))
