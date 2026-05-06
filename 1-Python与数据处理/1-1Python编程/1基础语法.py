import keyword

print(keyword.kwlist)
print(r'this is a line with \n')

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x = "a"
y = "b"

# 换行输出
print(x)
print(y)

# 不换行输出
print(x, end=" ")
print(y, end=" ")

str = '123456789'

print(str)              # 输出字符串
print(str[0:-1])        # 输出第一个到倒数第二个的所有字符
print(str[0])           # 输出字符串第一个字符
print(str[2:5])         # 输出字符串第三个到第六个字符(不包含第六个字符)
print(str[2:])          # 输出从第三个开始后的所有字符
print(str[1:5:2])       # 输出从第二个开始到第五个结束且每隔一个的所有字符 (步长为2)
print(str*2)            # 输出字符串两次
print(str + '你好')      # 拼接字符串
