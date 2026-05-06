#!/usr/bin/python3

# 隐式类型转换
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print("num_int 数据类型: ", type(num_int))
print("num_flo 数据类型: ", type(num_flo))
print("num_new 值为: ", type(num_new))
print("num_new 数据类型: ", type(num_new))


# 显式类型转换
# int()
x = int(1)   # 1
y = int(2.8) # 2
z = int(3)   # 3
print(x, y, z)

# float()
x = float(1)     # 1.0
y = float(2.9)   # 2.9
z = float("3")   # 3.0
d = float("4.2") # 4.2
print(x, y, z, d)

# str()
x = str("s1")   # 's1'
y = str(2)      # '2'
z = str(3.0)    # '3.0'
print(x, y, z)

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))
