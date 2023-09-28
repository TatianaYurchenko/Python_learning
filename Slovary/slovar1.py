stock = {
    'name': 'John',
    'last_name': 'Smith',
    'age': 32,
    'position': 'qa'
}

def print_key_values(**kwargs):
    for key in kwargs:
        print(kwargs[key])

def print_key_values_1(**kwargs):
    for key in kwargs:
        print(kwargs[key])

print_key_values(name='John', last_name='Smith', age=35)
# # exercise 1
# a = 0
# inventory = {
#     'gold': 300,
#     "pouch": {'flint', 'twine', 'gestoune'},
#     'backpack': {'xylofone', 'dagger', 'bedroll', 'breaf loaf'}
# }
# print(inventory)
# inventory['pocket'] = {}
# print(inventory)
# inventory['pocket'] = {'seashell', 'strange berry', 'lint'}
# print(inventory)
# print(sorted(inventory['backpack'], reverse=True))
# inventory['gold'] = inventory['gold'] + 50
# print(inventory)
# inventory['backpack'].remove('dagger')
# print(inventory)
# print('словарь {}'.format(inventory['backpack']))
# exercise 2
# prices = {
#     'Banana': 4,
#     'apple': 2,
#     'orange': 1.5,
#     'pear': 3
# }
# stock = {
#     'Banana': 6,
#     'apple': 0,
#     'orange': 32,
#     'pear': 15
# }
# total = 0
# a = 0
# for key, value in prices.items():
#     print(),
#     print(key),
#     print(value),
#     print(stock[key]),
#     total = stock[key] * prices[key]
#     a = total + a
#     print('Total: {}'.format(total))
# print()
# print('Sum: {}'.format(a))

# exercise 3
prices = {
    'Banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock = {
    'Banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
print(sum(stock.values()))
# или
res = 0
for x in stock:
    res += stock[x]

print(stock['orange'])




#
# grocerles = ['Banana', 'apple', 'orange', 'pear']
# def computer_bill(food):
#     total = 0
#     a = 0
#     for i in food:
#         total = stock[i] * prices[i]
#         print(stock[i])
#         print(prices[i])
#         a = a + total
#         print(total)
#         return total
#
# print(computer_bill(grocerles))
