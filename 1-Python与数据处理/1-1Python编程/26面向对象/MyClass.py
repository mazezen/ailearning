#!/usr/bin/python3

class MyClass:
    """
    一个简单的类实现
    
    这是类的构造方法 __init__ 
    """
    def __init__(self, value):
        print("实例化类的时候 会先调用")
        print(self)
        print(self.__class__)

        self.value = value


    i = 1234

    def f(self):
        return "hello world!"
    
    def display_value(self):
        print(self.value)
    



mc = MyClass(20)
print("MyClass 类的属性 i 为: ", mc.i)
print("MyClass 类的方法 f 为: ", mc.f())
mc.display_value()
