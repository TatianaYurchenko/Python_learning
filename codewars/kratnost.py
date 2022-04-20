# a = 2
# b = 12
# c = []
# for i in range(1, b + 1):
#     if i % a == 0:
#         c.append(i)
# print(c)
#__________
# c = []
# def kratnost_chisel(a, b):
#
#     for i in range(1, b + 1):
#         if i % a == 0:
#            c.append(i)
#     # print(c)
#     return c
# print(kratnost_chisel(2,12))
#_____________

def find_multiples(i, l):
    return list(range(i, l+1, i))

print(find_multiples(2,10))