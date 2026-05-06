#!/usr/bin/python3

with open('13推导式.py', 'r') as file:
    content = file.read()
    print(content)

# 同时打开多个文件
with open("13推导式.py", 'r') as infile, open("output.txt", 'w') as outfile:
    content = infile.read()
    outfile.write(content)


# 数据库连接
# import sqlite3
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("select * from users")
#     results = cursor.fetchall()


# 线程锁
import threading
lock = threading.Lock()

with lock:
    print("这段代码是线程安全的")


# 临时修改系统状态
import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 42 # 临时设置高精度


class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        import time
        self.end = time.time()
        print(f'耗时: {self.end - self.start:.2f}秒')

with Timer() as t:
    sum(range(1000000))


from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("这是一个标题")
