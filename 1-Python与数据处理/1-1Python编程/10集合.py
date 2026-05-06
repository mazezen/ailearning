#!/usr/bin/python3

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add('Facebook')
print(thisset)

thisset.update({1, 2})
print(thisset)

thisset.update([1, 3], [5, 6])
print(thisset)

thisset.remove("Google")
print(thisset)

thisset.discard("Google")
print(thisset)

thisset.pop()
print(thisset)

print(len(thisset))

print(5 in thisset)
