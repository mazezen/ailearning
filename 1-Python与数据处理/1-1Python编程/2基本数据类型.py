#!/usr/bin/python3

counter = 100      # 整型变量
miles = 1000.0     # 浮点型变量
name = "runoob"    # 字符串型变量

print(counter, miles, name)

# 多个变量同时赋值
a, b, c, d, e = 1, 2, 'runoob', True, 4+3j
print(a, b, c, d, e)
print("type a = ", type(a), "type b = " , type(b), "type c = " , type(c), "type d = ", type(d), "type e = ", type(e))


# isinstance
class A:
    pass

class B(A):
    pass
print(isinstance(A(), A))  # True
print(type(A()) == A)      # True
print(isinstance(B(), A))  # True
print(type(B()) == A)      # False

# issubclass bool 是 int的子类, True and False 可以和数字相加
print(issubclass(bool, int)) # True
print(True == 1)
print(False == 0)
print(True + 1)   # 2
print(False + 1)  # 1
print(1 is True)  # False
print(0 is False) # False

# 数值运算
print(5 + 4)
print(4.3 - 2) 
print(3 * 7)
print(2 / 4)
print(2 // 4) # 整除 向下取整
print(17 % 3)
print(2 ** 3)


# 布尔类型的值和类型
a1 = True
b1 = False
print(type(a1), type(b1))

# 布尔类型的整数表现
print(int(True))  # 1
print(int(False)) # 0

# 使用 bool() 函数进行转换
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1,2,4]))   # True

# 布尔逻辑运算
print(True and False) # False
print(True or False)  # True
print(not True)  # False


# 布尔比较运算
print(5 > 3)   # True
print(2 == 2)  # True
print(7 < 4)   # False

# 布尔值在流程控制中的作用
if True:
    print("This will aways print")

if not False:
    print("This will aways print")

x = 10
if x:
    print("x是非零值, 在布尔上下文中为 True")


# List
my_list = ['abcd', 3, 786, 2.23, "runoob", 70.2]  
tinylist = [123, "runoob"]

print(my_list)       # 打印整个 my_list
print(my_list[0])    # 打印第一个元素
print(my_list[1:3])  # 打印索引 1 和 2 的元素（不含索引 3）
print(my_list[2:])   # 打印索引 2 之后的元素
print(my_list * 2)   # 重复打印 my_list 两次 
print(my_list + tinylist) # 拼接两个列表


import sys
def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    inputWords = ' '.join(inputWords)

    return inputWords

print(reverseWords('I like runoob'))


# Tuple

my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(my_tuple)       # 输出完整元组
print(my_tuple[0])    # 输出第一个元素
print(my_tuple[1:3])  # 输出索引 1 和 2 的元素
print(my_tuple[2:])   # 输出从索引 2 开始的所有元素
print(my_tuple * 2)   # 输出两次 my_tuple
print(my_tuple + tinytuple) # 拼接两个元组


# Set
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
print(sites)

if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

a2 = set('abracadabra')
b2 = set('alacazam')

print(a2) # a 中的唯一字符
print(a2 - b2)  # a 和 b 的差集（在 a 中但不在 b 中）
print(a2 | b2)  # a 和 b 的并集（在 a 或 b 中）
print(a2 & b2)  # a 和 b 的交集（同时在 a 和 b 中）
print(a2 ^ b2)  # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）


# Dictionary
my_dict = {}
my_dict['one'] = 'AI学习'
my_dict['two'] = 'Python学习'
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(my_dict)
print(my_dict['two'])
print(my_dict.keys())
print(my_dict.values())


# bytes类型
xb = b"hello"
print(xb)
print(type(xb))
print(xb[0])  # 104（'h' 的 ASCII 值，bytes 元素是整数）
if xb[0] == ord("h"):  # ord() 函数将字符转换为对应的整数值
    print("第一个元素是 'h'")

