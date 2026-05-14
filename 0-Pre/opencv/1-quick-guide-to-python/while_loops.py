'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/while_loops.py
Description: 
'''

#!/usr/bin/python3

number = 1
# while number < 5:
#     print("number: ", number, "squared is ", number**2)
#     number+=1
# else:
#     print("no number left!")


# while number <= 5:
#     print("number: ", number, "squared is ", number**2)
#     number = number + 1
#     if number == 4:
#         break
    

# skip
number = 0
while number <= 5:
    number += 1
    if number == 3:
        continue
    print("number: ", number, "squared is ", number**2)
