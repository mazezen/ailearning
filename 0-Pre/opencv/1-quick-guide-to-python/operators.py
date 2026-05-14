'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/operators.py
Description: 
'''

#!/usr/bin/python3

print('Addition: ', 5 + 2)        # 7
print('Subtraction: ', 5 - 2)     # 3
print('Multiplication: ', 5 * 2)  # 10
print('Division: ', 5 / 2)        # 2.5
print('Floor Division: ', 5 // 2) # 2
print('Exponentiation: ', 5 ** 2) # 25
print('Modules: ', 5 % 2)         # 1


# Aassignment Operators
x = 7
print(x)

x += 2
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)

x = 10
x //= 3 # floor division and assignment
print(x)

x **= 2 # exponentiation and assignment 
print(x)


# Logical Operators
x = 5
y = 2
print(x == 5 and x > y)
print(x == 5 or y > 3)
print(not(x == 5))


# Membership Operators
# in: returns True is the object is present 
# not in: returns True if the object is not present
number_list = [1, 2, 3, 4, 5]
print(1 in number_list)
print(5 in number_list)
print(6 not in number_list)
print(2 not in number_list)
