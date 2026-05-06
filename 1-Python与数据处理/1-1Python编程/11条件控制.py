#!/usr/bin/python3

var1 = 100
if (var1):
    print("1-if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2-if 表达式条件为 true")
    print(var2)

print("Good bye!")


# age = int(input("请输入狗年龄: "))
# print("")
# if age <= 0:
#     print("无效的年龄")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 2:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人的年龄: ", human)

# input("点击 enter 键退出")


# number = 7
# guess = -1
# print("数字精彩游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字: "))
#     if guess == number:
#         print("猜对了")
#     elif guess < number:
#         print("猜小了")
#     elif guess > number:
#         print("猜大了")

num = int(input("请输入一个整数: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("可以同时整除 2 和 3")
    else:
        print("可以整除2 不能整除 3")
else:
    if num % 3 == 0:
        print("可以整除3 不能整除2")
    else:
        print("2 和 3 都不能整除")

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(400))
print(http_error(200))
print(http_error(404))
print(http_error(418))

def check_permission(status):
    match status:
        case 200:
            return "Ok - Success"
        case 301 | 302:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 |  502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknown status - 未知状态码"

for code in [200, 301, 403, 500, 418]:
    print(f'状态码 {code}: {check_permission(code)}')


