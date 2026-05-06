#!/usr/bin/python3

def printh():
    print("Hello world!")
printh()

def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(19, 20))


def area(width, height):
    return width * height
print(area(10, 10))


def change(a):
    print(id(a))
    a = 10
    print(id(a))
a = 10
print(id(a))
change(10)

def changeName(myList):
    myList.append([1, 2, 3, 4])
    print("函数内的取值: ", myList)
    return

mylist = [10, 20, 30]
changeName(myList=mylist)
print("函数外的取值: ", mylist)


def printinfo(arg1, *vartuple):
    print(arg1)
    # print(vartuple)
    for var in vartuple:
        print(var)
    return
printinfo(70, 600, 100)

def printinfo(arg1, **vardict):
    print(arg1)
    print(vardict)

    return

printinfo(60, a = 2, b = 3)


sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
