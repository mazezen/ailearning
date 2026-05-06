#!/usr/bin/python3

tup1 = ('Google', 'Runoob', 1997, 2000)
print(type(tup1))
print(tup1)

print(tup1[0])
print(tup1[-1])
# print(tup1[10])  # tupe index out of range
print(tup1[:2])

# tup1[0] = 'google1'  # 'tuple' object does not support item assignment
# print(tup1)

# del(tup1[0])  # 'tuple' object doesn't support item deletion
# print(tup1)

del(tup1)
# print(tup1)  # name 'tup1' is not defined. Did you mean: 'tuple'?

tup1 = (1, 2, 3)
tup2 = (2, 3, 4)
print(len(tup1))
print(tup1 + tup2)

tup1 += tup2
print(tup1)

# tup1 -= tup2 # TypeError: unsupported operand type(s) for -=: 'tuple' and 'tuple'
# print(tup1)

print(tup1*4)
print(3 in tup1)

for x in tup1:
    print(x, end=" ")
