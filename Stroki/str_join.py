name, city, state = ['John', 'Smith'], 'Phoenix', 'Arizona'
name = ' '.join(name)
print(name)

lst = ['a', 'b', [1, 2, 3], 'd']
i = lst[2]
print(*i, sep=',')
print(*i, sep='\n')
