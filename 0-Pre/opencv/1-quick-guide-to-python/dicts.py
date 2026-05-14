'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/dicts.py
Description: 
'''

#!/usr/bin/python3

# my_dict = {"country" : "France", "worldcups": "2"}
# print(type(my_dict))
# print(my_dict)
# print(my_dict['country'])

people = {}

people = {'Bob': 32, 'Mary': 25}
print(people)

# Add in a Dictionary
people['Salary'] = 30
print(people)

# Updateing a Dictionary
people['Salary'] = 32
print(people)

# Delete in a Dictionary
people.pop('Bob')
# people.pop('Bob') # KeyError: 'Bob'
print(people)

# Retrieving in a Dictionary
bob_age = people['Salary']
print(bob_age)

if 'Bob' in people:
    print('Bob in')
else:
    print('Bob not in')
