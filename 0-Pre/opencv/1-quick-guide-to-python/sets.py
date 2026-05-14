'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/sets.py
Description: 
'''

#!/usr/bin/pyton3

# items in a set are not mutable. You have to either add or delete an item.

my_sets = {'bmw', 'ferrai', 'maclaren'}
print(my_sets)
print(type(my_sets))

# Adding in a Set
my_sets.add('BYD')
print(my_sets)

# add multiple items at once
my_sets.update(['Carol', 'Susan'])
print(my_sets)

# delete
my_sets.remove('Carol')
print(my_sets)

my_sets.clear()
print(my_sets)

people = {"Bob", 'mary'}

if 'Bob' in people:
    print('Bob exists!')
else:
    print('Bob is not exists!')
