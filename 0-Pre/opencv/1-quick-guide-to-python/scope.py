'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/scope.py
Description: 
'''
#!/usr/bin/python3

name = 'Bob' # Global SCOPE
def print_name():
    print('my name is ' + name)
print_name()

def local_name():
    name = "mary" # LOCAL SCOPE
    print('my name is ' + name)
local_name()
