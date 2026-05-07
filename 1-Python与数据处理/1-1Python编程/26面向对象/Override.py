#!/usr/bin/python3

class Parent:
    def myMethod(self):
        print("调用父类的方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类的方法")

c = Child()
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod() # 用子类对象调用父类已被覆盖的方法
