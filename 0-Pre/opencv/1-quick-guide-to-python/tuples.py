'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/tuples.py
Description: 
'''

#!/usr/bin/python3

my_tuples = ('bmw', 'ferrari', 'maclaren')
print(my_tuples)
print(type(my_tuples))

people = ('bob', 'mary')
print(people)
# people[2] = 'Sarah' # TypeError: 'tuple' object does not support item assignment


# Update in a tuple
# people[1] = "mary2" # TypeError: 'tuple' object does not support item assignment
# But there is a trick: you can convert into a list, change the item. and then
# convert it back to a tuple
people = ('bob', 'mary')
people_list = list(people)
# print(people)
# print(people_list)
people_list[1] = 'mary2'
people_list.append('Sarah')
people = tuple(people_list)
print(people)
print(type(people))

# Retriving in a Tuple
print(people[1]) # mary2

# Check if a givan item already exists in a Tuple
if 'bob' in people:
    print('bob exists!')
else:
    print('bob not exists!')

if 'BOB' in people:
    print('BOB exists!')
else:
    print('BOB not exists!')
