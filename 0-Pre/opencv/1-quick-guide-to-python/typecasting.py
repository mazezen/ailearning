'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/typecasting.py
Description: 
'''

#!/usr/bin/python3

# Explicit conversion
# str() To cast a variable to a string.

my_str = str('132')
print(my_str)

# int to str
print(str(10))

# float to str
print(str(32.0))

# int() To cast a variable to an integer.
print(int('123'))
print(int(32.10))
# print(int(12+3j)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(int('abnc')) # ValueError: invalid literal for int() with case 10: "abnc"
# print(int('')) # ValueError: invalid literal for int() with base 10: ''

# float() To cast a variable to a float.
print(float('32'))
print(type(float('32')))
print(float(32))
print(float(0))


# Implicit conversion
my_int = 32
my_float = 3.2
print(my_int + my_float)


# when add an int and a str. python will not be able to
# make this implicti conversion, and the explicit type 
# conversion is necessary
my_int = 32
my_str = '32'
# print(my_str+my_int) # TypeError": can only concatenate str (not 'int') to str
print(int(my_str) + my_int)

# the same error is thrown when trying to add flot and str type without
# making an explicit conversion.
my_float = 3.2
my_str = '32'
# explicit conversion works
print(float(my_str) + my_float)

# implicit conversion throws an error
# print(my_str + my_float) # TypeError: can only concatenate str (not "float") to str

# User Input
# The captured value is always string. Just remember that you might need to convert it using typecasting
name = input("what'your name?\n")
print(name)
print(type(name))

age = input("How old are you?\n")
print(age)
print(type(age))
