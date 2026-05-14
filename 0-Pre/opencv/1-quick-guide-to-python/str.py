'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/str.py
Description: 
'''

#!/usr/bin/python3

my_city = "New York"
print(type(my_city))

# Single quotes hava exactly the same use as double quotes
my_city = 'New York'
print(type(my_city))

# Setting the variable type explicitly
my_city = str('New York')
print(type(my_city))

# Concetation
word1 = 'New'
word2 = ' York'
print(word1 + word2)


# len() returns the length of a string
print(len('NewYork'))

# replace() method replaces a part of string with another.
print("New York".replace('Yor', 'aaa', -1))

# upper() method will return characters as uppercase.
print("New York".upper())

# lower() method will return characters as lowercase.
print('New York'.lower())


# Concatenation
first_name = "mazen"
last_name = "ze"
print(first_name + last_name)

age = 'I have ' + str(30) + ' years old'
print(age)

# Comparion Operators
print('Euqal: ', 5 == 2)                    # False
print('Not equal: ', 5 != 2)                # True
print('Greather than: ', 5 > 2)             # True
print('Less than: ', 5 < 2)                 # False
print('Greater than or equal to: ', 5 >= 2) # True
print('Less than or equal to: ', 5 <= 2)    # False
