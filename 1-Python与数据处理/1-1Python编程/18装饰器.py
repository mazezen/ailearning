#!/usr/bin/python3


# def my_decorator(func):
#     def wrapper():
#         print("函数执行前")
#         func()
#         print("函数执行后")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("执行前")
#         func(*args, **kwargs)
#         print("执行后")

#     return wrapper

# @my_decorator
# def greet(name):
#     print(f"Hello, {name}")

# greet("Alice")

# def repeat(num_items):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_items):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print("hello!")

# say_hello()    

def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print("调用前")
            self.wrapped.display()
            print("调用后")

    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("原方法")

obj = MyClass()
obj.display()


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)


def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def sayHello():
    print("Hello!")
sayHello()
