#!/usr/bin/python3

import inspect

def add(a, b):
    '''返回两个数之和'''
    return a + b
print(add(1, 10))
print(add.__doc__)  # 通过__doc__属性访问注释
# help(add) # 使用 help 查看文档
print(inspect.getdoc(add))


def calculate(a, b, operation='add'):
    """
    执行数学运算

    参数:
        a: 第一个数字
        b: 第二个数字
        operation: 操作类型，可选 "add", "subtract", "multiply"

    返回:
        计算结果
    """ 
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    else:
        raise ValueError("不支持的操作")
    
# 查看完整的文档
# help(calculate)
print(calculate.__doc__)
print(inspect.getdoc(calculate))

