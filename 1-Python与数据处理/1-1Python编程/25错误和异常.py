#!/use/bin/python3


# print(10 / 0)     # ZeroDivisionError: division by zero

# print(4 + spam*3)   # NameError: name 'spam' is not defined

# print('2' + 2)   # TypeError: can only concatenate str (not "int") to str


# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字, 请再次尝试输入!")



import sys

# try:
#     f = open("myfile.txt")
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error: ", sys.exc_info()[0])
#     raise


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()), "lines")
        f.close()


# x = 10
# if x > 5:
#     raise Exception('x 不能 大于 5. x 的值为: {}'.format(x))


# 用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
