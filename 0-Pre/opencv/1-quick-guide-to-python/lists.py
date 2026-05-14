'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/lists.py
Description: 
'''

#!/usr/bin/pyton3

my_list = ['bmw', 'ferrari', 'maclaren']
print(my_list)
print(type(my_list))


# Initialization
# Empty List
people = []

people = ['Bob', 'Mary']
people.append('Sarah')
print(people)

people.insert(0, 'Sarah1')
print(people)
people.insert(-1, 'Sarah2') # ['Sarah1', 'Bob', 'Mary', 'Sarah2', 'Sarah']
print(people)

people[0] = 'Sarah4.'
print(people)

people.remove('Sarah4.')
print(people)
# people.remove('Sarah4.')  # ValueError: list.remove(x): x not in list

# people.clear()
# print(people)

print(people[1])

# Check if a given item aleady exists in a List
if 'Bob' in people:
    print('Bob is in people List')
else:
    print('Bob is not in people List')
