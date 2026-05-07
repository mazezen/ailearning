#!/usr/bin/python3

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
print(a)
a.append(333)
print(a)

print(a.index(333))
a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

# 创建一个空栈 栈 LIFO
stack = []

# 压入栈
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# 弹出栈
top_element = stack.pop()
print(top_element)
print(stack)

# 查看栈顶元素
top_element = stack[-1]
print(top_element)

# 检查是否为空
is_empty = len(stack) == 0
print(is_empty)

# 获取栈的大小
print(len(stack))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3

print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2


# 使用 collections.deque 实现队列
from collections import deque

# 创建一个空队列
queue = deque()

# 向队尾添加元素
queue.append("a")
queue.append("b")
queue.append("c")

print("队列状态: ", queue)

# 从队首移除元素
first_element = queue.popleft()
print(first_element)
print(queue)

# 查看队首元素不移除
front_element = queue[0]
print("队首元素: ", front_element)

# 查看队首元素是否为空
print("队列是否为空: ", len(queue) == 0)

# 获取队列大小
print("队列中元素数量: ", len(queue))


# 使用 LIST 实现 队列
class Queue1:
    def __init__(self):
        self.queue1 = []

    def size(self):
        return len(self.queue1)
    
    def is_empty(self):
        return len(self.queue1) == 0
    
    def enqueue(self, element):
        self.queue1.append(element)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue1.pop(0)
        else:
            raise IndexError("queue is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.queue1[0]
        else:
            raise IndexError("queue is empty")

# 使用示例
queue1 = Queue1()
queue1.enqueue('a')
queue1.enqueue('b')
queue1.enqueue('c')

print("队首元素:", queue1.peek())    # 输出: 队首元素: a
print("队列大小:", queue1.size())    # 输出: 队列大小: 3

print("移除的元素:", queue1.dequeue())  # 输出: 移除的元素: a
print("队列是否为空:", queue1.is_empty())  # 输出: 队列是否为空: False
print("队列大小:", queue1.size())    # 输出: 队列大小: 2
