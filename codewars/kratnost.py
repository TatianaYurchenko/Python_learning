# a = 2
# b = 12
# c = []
# for i in range(1, b + 1):
#     if i % a == 0:
#         c.append(i)
# print(c)

def kratnost_chisel(a, b):
    c = []
    for i in range(1, b + 1):
        if i % a == 0:
           c.append(i)
    print(c)
    return c
kratnost_chisel(2,12)
