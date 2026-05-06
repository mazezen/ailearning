#!/usr/bin/python3

tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict)
print(tinydict["name"])
print(tinydict.keys())
print(tinydict.values())
print(len(tinydict))

tinydict["name"] = "runoob1"
print(tinydict)

emptyDict = {}
print(emptyDict)
print(type(emptyDict))

# del emptyDict
# print(emptyDict)

emptyDict.clear()

print(str(tinydict))

copyDict = tinydict.copy()
print(copyDict)

print(id(tinydict))
print(id(copyDict))

seq = ('name', 'age', 'sex')
d1 = dict.fromkeys(seq)
print(d1)
d2 = dict.fromkeys(seq, 20)
print(d2)

print(d2.get("age", 100))
print("name" in d1)

print(d1.items())
print(d2.pop("name"))
print(d2.popitem())
