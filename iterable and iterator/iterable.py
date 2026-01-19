#Iterators are those objects which can be iterated / looped through.
#Iterables are those objects which can be converted to iterators.

#list, tuple, string, dictionary, set are all iterables.
a = [1,2,3,4,5]  #list is an iterable
b = (1,2,3,4,5)  #tuple is an iterable
c = "Nishan"     #string is an iterable
d = {1: "one", 2: "two", 3: "three"}  #dictionary is an iterable
e = {1,2,3,4,5}  #set is an iterable

value = [1,2,3]
iter_a = value.__iter__()
iter_a = iter(value)  #converting iterable to iterator
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))