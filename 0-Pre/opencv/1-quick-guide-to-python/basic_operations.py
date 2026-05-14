'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/basic_operations.py
Description: 
'''

def add(first_num: int, second_num: int) -> int:
    return first_num + second_num

def subtract(first_num: int, second_num: int) -> int:
    return first_num - second_num

def multiply(first_num: int, second_num: int) -> int:
    return first_num * second_num

def divide(first_num: int, second_num: int) -> float:
    return first_num / second_num

if __name__ == '__main__':
    print(add(10, 2)) 
    print(subtract(10,2))
    print(multiply(10,2))
    print(divide(10,2))
