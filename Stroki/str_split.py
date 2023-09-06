# def string_to_array(s):
#     a = s.split(";")
#     return a
# print(string_to_array("I; fg;gjhg;"))

some_str = "вася бежал по полю и умер"
lst = []
for i in range(len(some_str)):
    if some_str[i] == "а":
        lst.append(i)
print(lst)

# a = input('введите два числа через пробел ')
# a = a.split()
# c = 0
# for i in a:
#     i = int(i)
#     if i % 7 == 0:
#         c += 1
# if c == 2:
#     print('true')
# else:
#     print('false')

