# what is set in python
# set is a collection which is unordered, unindexed. No duplicate members.
set1 = {45, 23, 67, 89, 12}
print(set1)
print(type(set1))
45 in set1  # True
43 in set1  # False
set3 = {}
print(type(set3))  # <class 'dict'>
set2 = set()
print(type(set2))  # <class 'set'>
a = set("aeiou")
b = set("aeioubcdfg")
