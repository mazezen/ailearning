'''
Author: mazezen
Date: 2026-05-13
LastEditors: mazezen
LastEditTime: 2026-05-13
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/for_loops.py
Description: 
'''

#!/usr/bin/python3

cars = ['BWM', 'Ferrari', 'Mclaren']
for car in cars:
    print(car)


for number in range(5):
    print(number) # 0, 1, 2, 3, 4

numbers = [0, 1, 2, 3, 4]
for number in numbers:
    print(number)


for number in range(0, 10):
    print(number)

for number in range(0, 10, 2):
    print(number)
else:
    print("range end!")

for car in cars:
    print(car)
    if car == 'BWM':
        break


for car in cars:
    if car == 'Ferrari':
        continue
    print(car)


car_models = [ 
['BMW I8', 'BMW X3', 
'BMW X1'], 
['Ferrari 812', 'Ferrari F8', 
'Ferrari GTC4'], 
['McLaren 570S', 'McLaren 570GT', 
'McLaren 720S']
]

for brand in car_models:
    print(brand)
    for item in brand:
        print(item, end=' ')


# Loop over a Tuple
people = ('Bob', 'Mary')
for p in people:
    print(p)


# Loop over a set
people = {'bob', 'amr'}
for person in people:
    print(person)

# Loop over a Dictionary
# To print the keys and print the age
people = {"bob": 32, "mary": 45}
for person in people:
    print(person)
    print(people[person])
