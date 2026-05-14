'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/example.py
Description: 
'''

numbers = [1, 2, 3, 4, 5]
new_list = []
for number in numbers:
    new_list.append(number**2)
print(new_list)


new_list = [n**3 for n in numbers]
print(new_list)


new_list = []
for n in numbers:
    if (n > 3):
        new_list.append(n**3)
print(new_list)

new_list = []
new_list = [n**3 for n in numbers if n > 3]
print(new_list)


new_list = []
def cube(number: int) -> int:
    return number**3
new_list = [cube(n) for n in numbers if n > 3]
print(new_list)
