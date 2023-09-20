def f(x):
    return x**2
# lambda арг_1б арг_2, ...: выражение
r = lambda x: x**2
print(r(8))
#  применение
def linear(k,b):
    return lambda x: x*k+b
graf1 = linear(2,5)
print(graf1(3))