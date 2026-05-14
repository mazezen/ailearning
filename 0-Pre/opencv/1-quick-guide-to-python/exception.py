'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/exception.py
Description: 
'''

try:
    32/0
except:
    print("Dividing by zero!")

try:
    car_brands = ['ford', 'ferrari', 'bmw']
    print(car_brands[3])
except IndexError:
    print('There is no such index!')

try:
    raise IndexError("This index is not allowed")
except:
    print("Doing somethind with the execption!")
    raise

