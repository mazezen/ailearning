#!/usr/bin/python3

# 类定义
class People:

    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性, 私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speek(self):
        print("%s 说: 我 %d 岁" % (self.name, self.age))

# p = People('python', 10, 30)
# p.speek()


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        super().__init__(name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speek(self):
        print("%s 说: 我 %d 岁了, 我在读 %d 年级" % (self.name, self.age, self.grade))

# s1 = Student('python', 10, 30, 5)
# s1.speek()


# 多继承
class Speaker:
    topic = ''
    name = ''
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speek(self):
        print("我叫 %s, 我是一个演说家, 我演讲的主题是 %s"%(self.name,self.topic))


class Sample(Speaker, Student):
    a = ''
    def __init__(self, name, age, weight, grade, topic):
        Speaker.__init__(self, name, topic)
        Student.__init__(self, name, age, weight, grade)
        


test = Sample("TIM", 25, 80, 4, 'Python')
test.speek()
