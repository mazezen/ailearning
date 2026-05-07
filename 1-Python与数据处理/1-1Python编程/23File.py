#!/use/bin/python3

# file.close()
fo = open('foo.txt', 'a')
print("文件名: ", fo.name)
fo.close()

# file.flush()
fo = open('foo.txt', 'a')
print("文件名: ", fo.name)

fo.flush()
fo.close()

# file.fileno()
fo = open('foo.txt', 'a')
print("文件名: ", fo.name)

fid = fo.fileno()
print("文件描述符为: ", fid)
fo.close()

# file.isatty()
fo = open('foo.txt', 'a')
ret = fo.isatty()
print("返回值: ", ret)
fo.close()

# file.read()
fo = open('foo.txt', 'r+')
print("文件名: ", fo.name)

line = fo.read(10)
print ("读取的字符串: %s" % (line))

fo.close()

# file.readline()
fo = open('foo.txt', 'r+')
line = fo.readline()
print ("读取第一行 %s" % (line))

line = fo.readline(5)
print ("读取的字符串为: %s" % (line))
fo.close()

# file.readlines()
fo = open('foo.txt', 'r+')
lines = fo.readlines()
print(lines)
fo.close()

# file.seek()
fo = open("foo.txt", 'r+')
line = fo.readline()
print("读取到的数据为: %s" % (line))

# 重新设置文件读取指针到开头
fo.seek(0,0)
line = fo.readline()
print("读取到的数据为: %s" % (line))

fo.close()

# file.tell()
fo = open("foo.txt", 'r+')
line = fo.readline()
print("读取到的数据为: %s" % (line))
print("文件指针的位置: ", fo.tell())
fo.close()


# file.write()
with open('foo.txt', 'r+') as fo:
    print("文件名: ", fo.name)

    # 在文件末尾写入一行
    fo.seek(0, 2)
    fo.write("6:www.runoob.com\n")

    fo.seek(0)
    for index, line in enumerate(fo):
        print("文件行号: %d - %s" % (index, line.strip()))


# file.writelines()
with open('foo.txt', 'a') as fo:
    seq = ["python.org\n", "python3"]
    fo.writelines(seq)
