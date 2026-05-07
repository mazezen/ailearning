#!/use/bin/python3

s = "Hello, Runoob"
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 300
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)

hello = "hello, runoob\n"
print(repr(hello))

print(repr((x, y, ('Google', 'Runoob'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


table = {'google': 1, "runoob": 2, "taobao": 3}
for name, number in table.items():
    print('{0:10}  ==> {1:10d}'.format(name, number))


# 读和写文件
with open("foo.txt", "w") as file:
    file.write("Python 是一个非常好的语言. \n是的, 的确非常好!!\n")

with open("foo.txt", 'r') as file:
    str = file.read()
    print(str)

with open('foo1.txt', 'rb+') as file:
    print(file.write(b"0123456789abcdef"))
    print(file.seek(5))
    print(file.read(1))
    print(file.seek(-3, 2))
    print(file.read(1))

