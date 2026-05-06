#!/usr/bin/pytho3

sum = 0
counter = 100
while counter >= 1:
    sum = sum + counter
    counter -= 1
print(sum)

x = 10
while x < 20:
    print("x = ", x)
    x += 1
else:
    print("x >= 20")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

word = 'runoob'
for letter in word:
    print(letter, end=" ")
print("")

for number in range(1, 4):
    print(number, end=" ")

for x in range(6):
    print(f'x = {x}')
else:
    print("Finally finished!")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == 'Runoob':
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据")
print("完成循环!")

for i in range(len(sites)):
    print(i, sites[i])

print(list(range(5)))
