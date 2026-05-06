#!/usr/bin/python3

list = [1, 2, 3, 4]
it = iter(list)
# print(next(it))

# for x in it:
#     print(x, end=" ")

# import sys

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
myClass = MyNumbers()
myiter = iter(myClass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for x in myiter:
    print(x)


def countDown(n):
    while n > 0:
        yield n
        n -= 1

generator = countDown(5)
# print(next(generator))
# print(next(generator))
# print(next(generator))

for value in generator:
    print(value)

