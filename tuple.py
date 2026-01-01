tup = (45, 23, 67, 89, 12)
print(tup)
print(type(tup))
tup.count(23) # counts how many times 23 appears in the tuple
tup.index(67) # returns the index of the first occurrence of 67 in the tuple

tupA = (2,"nishan", 4.99, True)
num, name, rating, is_active = tupA
print(num)
print(name)
print(rating)
print(is_active)
mix=(23, "Rai", [1,2,3], (4,5,6))
# tuples are immutable
# tupA[0] = 100 # this will raise an error
mix[2][0] = 100 # this is allowed because we are modifying the list inside the tuple)
print(mix)
tup = (50,70,90)
x = tup[0]
y = tup[2]
print(x +y)