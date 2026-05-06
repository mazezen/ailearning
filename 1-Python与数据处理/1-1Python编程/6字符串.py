#!/usr/bin/python3

var1 = "Hello World!"
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print("已更新的字符串 : ", var1[:6] + "Runoob!")

print("\a")
print("Hello \v World!")
print("Hello \t World!")
print("google runoob taobao\r123456")
print("Hello \f World!")
print("\110\145\154\154\157\40\127\157\162\154\144\41")
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")


# import time

# for i in range(101):
#     bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='', flush=True)
#     time.sleep(0.05)
# print()

# 字符串运算符
a = "Hello"
b = "Python"

print("a + b 的结果是: ", a + b)
print("a * a 的结果是: ", a * 2)
print("a[1] 的结果是: ", a[1])
print("a[1:4] 输出结果是: ", a[1:4])

if ('H' in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

print(r'\n')
print(R'\n')

print("我叫 %s, 今年 %d 岁!" % ('python', 20))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

name = 'Runoob'
print(f'Hello {name}')
print(f'{1+2}')

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

x = 1
print(f'{x+1}')
print(f'{x+1=}')

str1 = "[hello]"
print(str1.capitalize())
print(str1.center(40, '*'))
print(str1.count('l', 0, 4))

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

print(str1.endswith(']'))
print(str1.find(']'))
# print(str1.index(']1')) 

print(str1.isalnum())

print("12121".isdigit())
print("abc".islower())
print("121b".isnumeric())

print("This Is String Example...Wow!".istitle())
print("This is strng example...wow!".istitle())
print("Abc".isupper())

seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print("-".join(seq))
print(",".join(seq))
print(len("abc"))
print("abc".ljust(10, "*"))
print("ABC".lower())
print("abc".upper())
print(" abc".lstrip())
print("abc ".rstrip())
print(max("abc"))
print(min("abc"))
print("abc".replace("a", "1"))
print("abc12".rfind('c'))
print("abc".split())

str = "this is string example....wow!!!"
print (str.split())        # 默认以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符

print(str.title())


str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))


str = "runoob2016"
print (str.isdecimal())

str = "23443434"
print (str.isdecimal())
