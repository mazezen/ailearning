#!/usr/bin/python3

# 列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
new_dict = {key: len(key) for key in listdemo}
print(new_dict)

# 集合推导式
setnew = {i**2 for i in (1, 2, 3)}
print(setnew)

a = (x for x in range(1, 10))
print(a)
print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组
