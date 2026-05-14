'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/files.py
Description: 
'''

#!/usr/bin/python3

# people_file = open("people.txt", 'x')
# print(people_file)

# people_file = open("people.txt", 'w')
# print(people_file)

# people_file = open('people.txt', 'a')


# people_file = open('people_file.txt', 'w')
# people_file.write('Bob\n')
# people_file.write('Mary\n')
# people_file.write('Sarah\n')

# people_file = open('people_file.txt', 'a')
# people_file.write('Bob\n')
# people_file.write("mary\n")


# read the whole file at once
# people_file = open('people_file.txt', 'r')
# print(people_file.read())

# read the file pass readline
people_file = open('people_file.txt', 'r')
# print(people_file.readline())
# print(people_file.readline())
# print(people_file.readline())
for person in people_file:
    print(person)


# check if a file exists
# delete file

import os
if os.path.exists('people_file.txt'):
    os.remove('people_file.txt')
else:
    print('The is no such file!')

# Copy a file
from shutil import copyfile
copyfile('my_file.txt', 'another_file.txt')


# rename or move a file
from shutil import move
move('my_file.txt', 'another_file.txt')
