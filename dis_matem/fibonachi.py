first = 1
print (first)
second = 1
print (second)
next = first + second
while next < 100:
    print (next)
    first = second
    second = next
    next = first +second

