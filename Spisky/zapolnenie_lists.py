# [выражение for val in коллекция]
# [выражение for val in коллекция if условие]   b = [elem for elem in a if elem%2==0]
import random
a = [random.randint(-10,10) for i in range(10)]
# a = [i*5 for i in 'hello']
print(a)
b = [abs(elem) for elem in a]
print(b)
