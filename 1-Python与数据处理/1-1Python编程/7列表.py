#!/usr/bin/python3

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list)
print(list[0])
print(list[-1])
# print(list[10]) # index out of range
print(list[:3])
print(list[1:-2])

list.append('baidu')
print(list)

list[0] = 'google'
print(list)

del(list[-1])
print(list)

import operator

a = ['a', 'c', 'b']
n = [1, 2, 3]
x = [a, n]
print(x)

a = [1, 2]
b = [1, 2]
print(operator.eq(a, b))

print(len(a))
print(max(a))
print(min(a))



