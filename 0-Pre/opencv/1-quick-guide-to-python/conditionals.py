'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/conditionals.py
Description: 
'''

#!/usr/bin/python3

# The if statement
bob_age = 32
sarah_age = 29
if bob_age > sarah_age:
    print("Bob is old than sarah")

# The if else and elif statement
if bob_age < sarah_age:
    print("bob is younger than sarah")
else:
    print("bob is old than sarah")

if bob_age > sarah_age:
    print("bob is old than sarah")
elif bob_age < sarah_age:
    print("bob is younger than sarah")
else:
    print("bob and sarah hava the same age")



# Nested conditionals
bob_age = 32
sarah = 28
mary_age = 25

if bob_age > sarah_age:
    print("Bob is old than Sarah")
    if bob_age >  mary_age:
        print("Bob is the oldest")

if bob_age > sarah_age and bob_age > mary_age:
    print("Bob is the oldest")


# Ternary Operators
a = 25
b = 50
x = 0
y = 1
result = x if a < b else y
print(result) 

