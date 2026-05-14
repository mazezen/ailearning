'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/lambda.py
Description: 
'''

#!/usr/bin/python3

cubic = lambda number : number ** 3
print(cubic(2))

exponential = lambda multipiler, number, exponent : multipiler * number ** exponent
print(exponential(2, 2, 3))

print((lambda multiplier, number, exponent : multiplier * number ** exponent)(2, 2, 3))

numbers = [2, 5, 10]
cubics = list(map(lambda number : number**3, numbers))
print(cubics)

filterted_list = list(filter(lambda number : number > 5, numbers))
print(filterted_list)

