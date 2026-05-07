#!/usr/bin/python3

f = lambda: "Hello world!"
print(f())

x = lambda x: x + 10
print(x(5))

f1 = lambda a, b : a * b
print(f1(10, 5))

f2 = lambda a, b, c : a + b + c
print(f2(10, 20, 30))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
