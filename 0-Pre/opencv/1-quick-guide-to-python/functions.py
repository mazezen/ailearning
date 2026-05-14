'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/functions.py
Description: 
'''

#!/usr/bin/python3

def print_first_function():
    print("my first function")
print_first_function()

def return_function1():
    return "return function"
print(return_function1())

def return_function() -> str:
    return "return string functon"
print(return_function())


# return tuple
def return_multiple_values():
    return 10, 2
print(return_multiple_values())
# unpack tuple
a, b = return_multiple_values()
print(a, b)


# one argument
def my_number(num: int) -> str:
    return "My number is: " + str(num)
print(my_number(num=10))

# more arguments
def add1(first_num: int, second_num: int) -> int:
    return first_num + second_num
print(add1(10, 20))


# default value
def add(first_numer: int, second_num: int = 30) -> int:
    return first_numer + second_num

print(add(10))


# Any numbers of arguments: *args
def any_numbers(*args):
    print(type(args))
    for arg in args:
        print(arg)
any_numbers(1, 2, 332)


# Any number of keyword/named arguments: **kwargs
def any_kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key + " = ", value)

any_kwargs(a=1, b=2, c=3)


def list_arguments(numbers: list):
    for item in numbers:
        print(item)
list_arguments([30, 230, 323])
