# sort метод списка (менет первоначальный список) тvs sorted- встроеннная ф-ия )не меняет список
a = [5, 4, 9]
c = 'stroka'
a.sort()
print(a)
c = sorted(c)
print(c)
''' 
обе сортировки принимают два необязательных аргумента
Key  принимает ф-цию(определяет по какому ключу будет выполнятся сортировка, reverse = принимает значения True или False
    c = sorted(c, key = function, reverse=False/True (false = в порядке возр, true = по убыванию)
    a.sort(key = function, reverse=False/True)
'''
